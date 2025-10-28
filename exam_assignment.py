from assignment import Assignment # inherets from assignment # testing 

#dont test abstact class/assignment but DO test all the subclasses. testing exam assignment and project assignment

class ExamAssignment(Assignment):
    def __init__(self, title: str, student_name: str, score: float, time_limit=75): #initialize attributes of parent class and time limit
        super().__init__(title, student_name, score)
        self.time_limit = time_limit

    def __eq__(self, other): #equa method order swapped 
        if self is other:
            return True
        if type(self) is type(other):
            return (
                super().__eq__(other) and# tells to go to asisgnmemnt class and preform equal mothod on that class using this other and to add to it and for time limit to be equal -- this how you compare what u previosuly done 
                self.time_limit == other.time_limit #is it same type # need to test time limit!
            )
        return NotImplemented

    def is_passed(self):
        return (self.score >= 70 and self.time_limit <= 75) or self.score >= 90 #if over time limit btu scoure is above 90 you get to pass 