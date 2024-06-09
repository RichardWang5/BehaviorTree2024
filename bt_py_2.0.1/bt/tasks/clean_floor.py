#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import random

class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        
        # set a randomized value as the failure probability
        # if the value is below 0.1, the task will fail
        # else just return running
        if random.random() < 0.1:
            self.print_message("Floor Cleaned, Task Done")
            return self.report_failed(blackboard)
        

        return self.report_running(blackboard)
