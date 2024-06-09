#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

import bt as bt

from bt.composites import Selection, Sequence, Priority
from bt.conditions import GeneralCleaning, SpotCleaning, DustySpot,BatteryLessThan30
from bt.decorators import UntilFail
from bt.tasks import FindHome, DoneGeneral, DoneSpot, AlwaysFail, GoHome, Dock, DoNothing, CleanSpot, CleanFloor


# Instantiate the tree according to the assignment. The following are just examples.

# Example 1:
# tree_root = btl.Timer(5, tasks.FindHome())

# Example 2:
# tree_root = composites.Selection(
#     [
#         BatteryLessThan30(),
#         FindHome()
#     ]
# )

# Example 3:
# tree_root = bt.Selection(
#     [
#         bt.BatteryLessThan30(),
#         btl.Timer(10, bt.FindHome())
#     ]
# )

# Example 4:
# tree_root = Sequence(
#     [
#         GeneralCleaning(),
#         btl.Timer(10, bt.FindHome())
#     ]
# )
# Example 5:
# tree_root = Priority(
#     [
#         SpotCleaning(),
#         btl.Timer(10, bt.FindHome())
#     ]
# )

# Constantruct the Battery less than 30 branch
battery_low_branch = Sequence([
        BatteryLessThan30(),
        FindHome(),
        GoHome(),
        Dock()
        ])

# Construct the Spot Cleaning branch
spot_cleaning_branch = Sequence([
            SpotCleaning(),
            btl.Timer(20, CleanSpot()),
            DoneSpot()
        ])

# Construct the General Cleaning branch
general_cleaning_branch = Sequence([GeneralCleaning(),
                                    Sequence([
                                        Priority([
                                            Sequence([
                                                DustySpot(),
                                                btl.Timer(35, CleanSpot()),
                                                AlwaysFail()
                                            ]),
                                            UntilFail(CleanFloor())
                                        ]),
                                        DoneGeneral()
                                        ])
                                    ])

# Construct the Cleaning branch
cleaning_branch = Selection([spot_cleaning_branch, 
                             general_cleaning_branch
                             ])



#the main behavior tree
tree_root = Priority([
    battery_low_branch,
    cleaning_branch,
    DoNothing()
])