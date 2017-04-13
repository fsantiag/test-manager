import threading
import subprocess


class TestExecutor(threading.Thread):

    def __init__(self, run_id, test_name, queue):
        super().__init__()
        self.run_id = run_id
        self.test_name = test_name
        self.queue = queue

    def run(self):
        with open("runs/static/runs/autotests/runs/{}.txt".format(self.run_id), "w") as f:
            CMD = "python3 -m unittest -v autotests/tests/{}.py 2>&1".format(
                    self.test_name)
            return_code = subprocess.call(CMD, stdout=f, shell=True)
            self.queue.put((self.run_id, return_code))
