import unittest

class TestExam(unittest.TestCase): #test exam class defined #unittest.TestCase is parent clas
    def test_equal(self):
        def setUp(self): 
            self.exam = ExamAssignment("Project 3", "Sue Flay", 95, 75) #defualt val
        def test_equal_same(self):
            self.assertTrue(self.exam == self.exam) #same obj in mem location - true
        # second if condition: comparing it with other data type #what case?
        def test_equal_different_type(self):
            self.assertFalse(self.exam == "Sue flay ") # dif data type - not implemented - false
        #same type dif objs, same data - true -- thre conditions for third case -- ttt - ttf - tf -ff 
        def tests_equal_same_tttt(self): #title name and score shodul be same #created new obj. same totle same name grades and same time limit so ehrn == sign used shoud return tru 
            temp = ExamAssignment("Project 3", "Sue Flay", 95.0, 75) 
            self.assertTrue(self.exam == temp) # same data - true
        def tests_equal_same_ttft(self):
            temp = ExamAssignment("Project 3", "Sue Flay", 95.1, 75) # not testing 75 bc 
            self.assertTrue(self.exam == temp)
        # def tests_equal_same_tf(self):
        #     temp = ExamAssignment("Project 3", "Sue Flay", 95.1, 75) 
        #     self.assertTrue(self.exam == temp)
        # def tests_equal_same_tf(self):
        #     temp = ExamAssignment("Project 3", "Sue Flay", 95.1, 75) 
        #     self.assertTrue(self.exam == temp) 

if __name__ == "__main__":
    unittest.main()

    #test with two dif objects 



