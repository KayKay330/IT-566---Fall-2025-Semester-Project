

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from employee_training.application_base import ApplicationBase

class TestApp(ApplicationBase):
    def __init__(self):
        super().__init__("TestApp", "employee_training")

if __name__ == "__main__":
    app = TestApp()
    app._logger.log_debug("Testing debug message from base class.")
    app._logger.log_error("Testing error message from base class.")
