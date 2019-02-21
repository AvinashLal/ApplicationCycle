from objects.lst import Lst 
from reviewer import Reviewer

class Roster(Lst):
    def __init__(self):
        Lst.__init__(self) 

    def assign(self, reviewer_name, course):
        reviewer = self.find(reviewer_name)
        if not reviewer.is_busy:
            reviewer.assign(course)
            if reviewer.is_busy:
                self.move_from_to(reviewer, self.available,
                    self.busy)
        else:
            print('reviewer is busy')           

    def complete(self, reviewer_name, course):
        reviewer = self.find(reviewer_name)
        if course in reviewer.assigned_courses:
            reviewer.complete(course)
            self.move_from_to(reviewer, self.busy,
                self.availabler)
        else:
            print('reviewer was not assigned this course')