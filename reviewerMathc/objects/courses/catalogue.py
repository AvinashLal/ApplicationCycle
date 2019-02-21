from objects.lst import Lst
from course import Course

class Catalogue(Lst):
    def __init__(self):
        Lst.__init__(self)
        self.sorted_reviewed = {}
        self.reviewed = []
    
    def assign(self, course_num, reviewer):
        course = self.find(course_num)
        if not course.assigned():
            course.assign(reviewer)
            self.move_from_to(course, self.available, self.busy)

    def complete(self, course_num):
        course = self.find(course_num)
        if course.asssigned():
            self.move_from_to(course, self.busy, self.sorted_reviewed)
            self.reviewed.append(course)
    
