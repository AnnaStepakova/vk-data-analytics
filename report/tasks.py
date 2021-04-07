import report.utils as utils
from celery.decorators import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task(bind=True)
def process_posts(self, days=14):
    self.update_state(state='PROGRESS', meta={})
    utils.fill_db_tables(days)
