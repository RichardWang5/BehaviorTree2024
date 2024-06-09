#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import SPOT_CLEANING

class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        blackboard.set_in_environment(SPOT_CLEANING, False) # set spot cleaning to false
        self.print_message("Done Spot Cleaning")
        
        return self.report_succeeded(blackboard)
