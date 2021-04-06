import requests
import vk
import pytz
from datetime import datetime
from dateutil import tz
from vkdataanalytics.settings import ACCESS_TOKEN, V, OWNER_ID
from .models import VKUser, Post, Comment


def _add_new_vkuser(api, user_id):
    if user_id < 0:
        try:
            group = api.groups.getById(group_ids=-user_id, v=V)
        except requests.exceptions.RequestException:
            print('ConnectionError')
        name = group[0]['name']
    else:
        try:
            user = api.users.get(user_ids=user_id, v=V)
        except requests.exceptions.RequestException:
            print('ConnectionError')
        name = f"{user[0]['first_name']} {user[0]['last_name']}"
    obj, _ = VKUser.objects.get_or_create(id=user_id, name=name)
    return obj


def fill_db_tables(days=14):
    session = vk.Session(access_token=ACCESS_TOKEN)
    vkapi = vk.API(session)
    offset = 0
    count = 100
    posts = {'items': [0] * count}
    while len(posts['items']) == count:
        try:
            posts = vkapi.wall.get(owner_id=OWNER_ID, offset=offset, count=count, v=V)
        except requests.exceptions.RequestException:
            print('ConnectionError')
            continue
        offset += count
        for i, post_json in enumerate(posts['items'], start=offset-count):
            date = datetime.fromtimestamp(post_json['date'], tz=tz.gettz('Europe/Moscow'))
            curr_date = datetime.now(pytz.timezone('Europe/Moscow'))
            print((curr_date - date).days)
            if (curr_date - date).days <= days:
                post_id = post_json['id']
                from_id = post_json['from_id']

                if not Post.objects.filter(id=post_id).exists():
                    vkuser = _add_new_vkuser(api=vkapi, user_id=from_id)
                    post = Post.objects.create(id=post_id, author=vkuser,
                                                     date=datetime.fromtimestamp(post_json['date'], tz=tz.gettz('Europe/Moscow')),
                                                     likes=post_json['likes']['count'])
                else:
                    post = Post.objects.get(id=post_id)
                    post.likes = post_json['likes']['count']

                try:
                    comments = vkapi.wall.getComments(owner_id=OWNER_ID, post_id=post_id, need_likes=True, v=V)
                except requests.exceptions.RequestException:
                    print('ConnectionError')
                    continue
                for comment_json in comments['items']:
                    comment_id = comment_json['id']
                    from_id_comm = comment_json['from_id']
                    if not Comment.objects.filter(id=comment_id).exists():
                        vkuser_comm = _add_new_vkuser(api=vkapi, user_id=from_id_comm)
                        Comment.objects.create(id=comment_id, post=post, author=vkuser_comm,
                                               date=datetime.fromtimestamp(comment_json['date'], tz=tz.gettz('Europe/Moscow')),
                                               likes=comment_json['likes']['count'])
                    else:
                        comment = Comment.objects.get(id=comment_id)
                        comment.likes = comment_json['likes']['count']
            else:
                break
        else:
            continue
        break
