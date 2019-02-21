class Reviewer:
    def __init__(self, name, grade, email):
        self.name = name
        self.grade = grade
        self.email = email
        self.specialty = []
        self.strength = 1
        self.assigned_courses = []

    def __str__(self):
        spec = ",".join(self.specialty)
        assigned_cour = ",".join(self.assigned_courses)
        return "name:%s grade:%s email:%s specialty:%s strength:%s assigned:%s" % (self.name, self.grade, self.email, spec, str(self.strength), assigned_cour)    

    def set_strength(self, value):
        self.strength = value
        
    def is_busy(self):
        if len(self.assigned_courses) < self.strength:
            return False
        else:
            return True   

    def add_specialty(self, subject):
        self.specialty.append(subject)

    def assign(self, course):
        if not self.busy:
            self.assigned_courses.append(course)
        else:
            print("is busy")
    
    def complete(self, course):
        self.assigned_courses.remove(course)