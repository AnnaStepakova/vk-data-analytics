import vk
from datetime import datetime
from dateutil import tz
from vkdataanalytics.settings import ACCESS_TOKEN, V, OWNER_ID
from .models import VKUser, Post, Comment


def _add_new_vkuser(api, user_id):
    if not VKUser.objects.filter(id=user_id).exists():
        if user_id < 0:
            group = api.groups.getById(group_ids=-user_id, v=V)
            VKUser.objects.create(id=user_id, name=group[0]['name'])
        else:
            user = api.users.get(user_ids=user_id, v=V)
            VKUser.objects.create(id=user_id, name=f"{user[0]['first_name']} {user[0]['last_name']}")


def fill_db_tables():
    session = vk.Session(access_token=ACCESS_TOKEN)
    vkapi = vk.API(session)
    posts = vkapi.wall.get(owner_id=OWNER_ID, v=V)
    for post in posts['items']:
        post_id = post['id']
        from_id = post['from_id']
        if not Post.objects.filter(id=post_id).exists():
            _add_new_vkuser(api=vkapi, user_id=from_id)
            vkuser = VKUser.objects.get(id=from_id)
            Post.objects.create(id=post_id, author=vkuser,
                                date=datetime.fromtimestamp(post['date'], tz=tz.gettz('Europe/Moscow')),
                                likes=post['likes']['count'])
        comments = vkapi.wall.getComments(owner_id=OWNER_ID, post_id=post_id, need_likes=True, v=V)
        for comment in comments['items']:
            comment_id = comment['id']
            from_id_comm = comment['from_id']
            if not Comment.objects.filter(id=comment_id).exists():
                _add_new_vkuser(api=vkapi, user_id=from_id_comm)
                vkuser_comm = VKUser.objects.get(id=from_id_comm)
                post = Post.objects.get(id=post_id)
                Comment.objects.create(id=comment_id, post=post, author=vkuser_comm,
                                       date=datetime.fromtimestamp(comment['date'], tz=tz.gettz('Europe/Moscow')),
                                       likes=comment['likes']['count'])
