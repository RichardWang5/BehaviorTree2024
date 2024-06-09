#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import SPOT_CLEANING


class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "spot cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # If spot cleaning is active, return succeeded
        # else, return failed
        if blackboard.get_in_environment(SPOT_CLEANING, 0) == True:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
