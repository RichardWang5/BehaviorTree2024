#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl


class Dock(btl.Task):
    """
    Implementation of the Task "Dock".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the task "Dock".
        
        :param blackboard: the blackboard of the behavior tree
        :return: the result of the execution
        """
        self.print_message("Dock Succeeded")
        # Charge the battery to 100%
        blackboard.set_in_environment("BATTERY_LEVEL", 100)
        self.print_message("Battery Charged to 100%")
        
        return self.report_succeeded(blackboard)
