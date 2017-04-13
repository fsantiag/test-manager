import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manager.settings")
django.setup()


import queue
import time
from app.models import Run, Status
from executor import TestExecutor
from django.utils import timezone


STATUS = {
        "waiting": 1,
        "failed": 2,
        "success": 3,
        "running": 4
    }


class Scheduler(object):
    """
    A general purpose scheduler to determine when a test can execute according
    to the environment. It is also responsible for checking the tests states.
    """

    def __init__(self):
        # initialize variables
        self.running = False
        self.message_queue = queue.Queue()
        self.environments = {}
    # __init__()

    def start(self):
        """
        Scheduler main loop.
        """
        self.running = True

        while self.running:
            runs_waiting = Run.objects.filter(
                    status=STATUS["waiting"]).order_by("id").all()

            for run in runs_waiting:
                if self.environments.get(run.environment.id) is None:
                    self.environments[run.environment.id] = run
                    thread = TestExecutor(
                            run.id, run.test.name, self.message_queue)
                    thread.start()
                    run.status = Status.objects.get(id=STATUS["running"])
                    run.start = timezone.now()
                    run.save()
                time.sleep(1)

            self._verify_test_states()
    # start()

    def _verify_test_states(self):
        """
        Verify the test states and update accordingly
        """
        while not self.message_queue.empty():
            run_id, return_code = self.message_queue.get_nowait()
            run = Run.objects.get(id=run_id)
            run.end = timezone.now()
            if return_code != 0:
                run.status = Status.objects.get(id=STATUS["failed"])
                run.save()
            else:
                run.status = Status.objects.get(id=STATUS["success"])
                run.save()

            # delete key since test is not executing anymore
            del self.environments[run.environment.id]
    # _verify_test_states()


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.start()
