import report.utils as utils
from celery.decorators import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task
def process_posts(days=14):
    utils.fill_db_tables(days)
