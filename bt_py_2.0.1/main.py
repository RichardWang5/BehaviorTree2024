#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#
import random
import bt_library as btl

from bt.behavior_tree import tree_root
from bt.globals import *

# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(BATTERY_LEVEL, 31)
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, False)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")




# ask userinput for the initial battery level
while True:
    # try and except block to catch invalid input
    # ensure the input is an integer 
    try:
        # ask user for the initial battery level
        battery_level = int(input("Enter an initial battery level between 0 and 100: "))
        
        # check if the battery level is between 0 and 100
        # if so, set the battery level in the blackboard
        # otherwise, print the error message
        if 0 <= battery_level <= 100:
            current_blackboard.set_in_environment(BATTERY_LEVEL, battery_level)
            break
        else:
            print("Please enter a valid battery level between 0 and 100.")
            
    except ValueError:
        print("Please enter a valid integer for battery level.")


done = False
while not done:
    # Each cycle in this while-loop is equivalent to 1 second time
    
    # Step 1: Change the environment
    #   - Change the battery level
    #   - Simulate the response of the dusty spot sensor
    #   - Simulate user input commands
    # current_blackboard.set_in_environment(BATTERY_LEVEL, random.randint(0, 100))
    
    # if the spot cleaning and general cleaning are both false, ask user for cleaning tasks to perform
    # This ensures that running tasks are not interrupted
    if current_blackboard.get_in_environment(SPOT_CLEANING, 0) == False and \
        current_blackboard.get_in_environment(GENERAL_CLEANING, 0) == False:
        while True:
            # ask user for cleaning tasks to perform
            cleaning_task = input("Enter cleaning task to perform (spot cleaning (s) or general cleaning(g)): ")
            # ensure the input is a valid cleaning task
            cleaning_task = cleaning_task.lower().strip()
            # if the input is 's', set spot cleaning to true and general cleaning to false
            # else if the input is 'g', set general cleaning to true and spot cleaning to false
            # otherwise, print the error message and do nothing
            if cleaning_task == "s":
                current_blackboard.set_in_environment(SPOT_CLEANING, True)
                current_blackboard.set_in_environment(GENERAL_CLEANING, False)
                break
            elif cleaning_task == "g":
                current_blackboard.set_in_environment(SPOT_CLEANING, False)
                current_blackboard.set_in_environment(GENERAL_CLEANING, True)
                break
            else:
                print("Not a valid cleaning task. Idling...")
                break
    # randomize the dusty spot sensor behavior
    current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, random.choice([True, False]))

    # Step 2: Evaluating the tree
    
    result = tree_root.run(current_blackboard)

    # Step 3: Determine if your solution must terminate
    # if there is a task succeeded or failed, the solution terminates
    # otherwise, the solution continues
    if result != btl.ResultEnum.RUNNING and result != btl.ResultEnum.SUCCEEDED:
        done = True
    else: 
        done = False
    
