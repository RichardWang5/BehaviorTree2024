
from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode


class UntilFail(Decorator):
    """
    Specific implementation of the decorator until fail
    """
    def __init__(self, child: TreeNode):
        """
        Default constructor
        
        :param child: Child node associated to the decorator
        """
        super().__init__(child)
    
    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior until it fails.
        
        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        result_child = self.child.run(blackboard)
        
        # if the result_child is failed, return success
        # else just return running
        if result_child == ResultEnum.FAILED:
            return self.report_succeeded(blackboard)
        
        return self.report_running(blackboard)


