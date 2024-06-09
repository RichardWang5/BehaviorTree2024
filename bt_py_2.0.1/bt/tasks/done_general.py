#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import GENERAL_CLEANING


class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the task "Done General".
        """
        blackboard.set_in_environment(GENERAL_CLEANING, False) # set general cleaning to false
        self.print_message("Done General Cleaning")
        
        return self.report_succeeded(blackboard)
