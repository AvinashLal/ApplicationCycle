class Course:
    def __init__(self, name, number, subject, grade):
        self.name = name
        self.number = number
        self.subject = subject
        self.grade = grade
        self.assigned = False
        self.reviewer = None
        self.reviewed = False

    def __str__(self):
        return ("name:%s \n number:%s \n subject:%s \n grade:%s \n assigned?:%s reviewer:%s reviewed?:%s") % (self.name, self.number, self.subject, self.grade, self.assigned,self.reviewer,self.reviewed) 
    
    def assign(self, reviewer):
        self.assign = True
        self.reviewer = reviewer
    
    def complete(self):
        self.reviewed = True
    
 