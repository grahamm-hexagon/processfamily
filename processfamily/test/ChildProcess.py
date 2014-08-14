__author__ = 'matth'

from processfamily import ChildProcess, start_child_process
import logging
from processfamily.test.FunkyWebServer import FunkyWebServer

class ChildProcessForTests(ChildProcess):

    def init(self):
        self.server = FunkyWebServer()

    def run(self):
        self.server.run()

    def stop(self, timeout=None):
        self.server.stop()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_child_process(ChildProcessForTests())