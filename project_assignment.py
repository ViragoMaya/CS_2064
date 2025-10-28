from assignment import Assignment

class ProjectAssignment(Assignment):
    def __init__(self,
                 title: str, student_name: str, score: float, submitted_on_time: bool
                 ):
        super().__init__(title, student_name, score) # initialize attrubutes 
        self.submitted_on_time = submitted_on_time

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return NotImplemented
        return (
            super().__eq__(other) and #acess parents dunder = method. 
            self.submitted_on_time == other.submitted_on_time
        )
    
    def is_passed(self):
        return (self.score >= 75 and self.submitted_on_time) or self.score >= 85 # then it will pass but if one of teh thinsg is not true and their score is above 85 they get deducted but still pass. 