#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl


class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Spot Cleaning ...")
        # This task would drain the battery by 1 each second
        battery_level = blackboard.get_in_environment("BATTERY_LEVEL", 0)
        battery_level -= 1
        blackboard.set_in_environment("BATTERY_LEVEL", battery_level)
        # report the current battery level
        self.print_message(f"Current Battery Level: {battery_level}")
        
        return self.report_succeeded(blackboard)
