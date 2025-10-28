from abc import ABC, abstractmethod

class Assignment(ABC):
    def __init__(self, title: str, student_name: str, score: float):
        self.title = title
        self.student_name = student_name
        self.score = score
    
    def __str__(self):
        return f"{self.title}\n{self.student_name}/{self.score}"
    
    def __eq__(self, other): #concerented classes doent have to be dunder methods - they js gotta be common with all subclasses. 
        if self is other:
            return True
        if type(self) is not type(other): # check if same obj and data type 
            return NotImplemented
        return (
            self.title == other.title and
            self.student_name == other.student_name and
            abs(self.score - other.score) < 0.000001 # float , cant js use doubel equal sign so use math.isclose( -- or using abs cal and comapring it to a small value/ decimal place. 
        )# you get to decideid when creating objs what is equal and whats not -- stime limit  didnt natter for equal sign 
    
    @abstractmethod
    def is_passed(self):
        pass