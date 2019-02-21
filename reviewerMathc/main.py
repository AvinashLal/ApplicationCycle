import random 

from objects.reviewers.reviewer import Reviewer
from objects.reviewers.roster import Roster
from objects.courses.course import Course 
from objects.courses.course import Catalogue 
from objects.lst import Lst 


#CONSTANTS
REV = 10 
COUR = 100 
MAX_STR = 2 
SUB = 5
SUBJECT = ['A','B','C','D','E']
GRD = ['K-5', '6-8','8-12']

#STORAGE
test_roster = Roster()
test_catalogue = Catalogue()

#generate Reviewers
for i in range(0, REV):
    name = 'name' + str(i)
    email = 'email' + str(i) + '@gmail.com'
    grade = GRD[random.randint(0,2)]
    x = Reviewer(name, grade, email)
    x.set_strength(random.randint(1, MAX_STR))

    specialty_num = random.randint(1,SUB+1)
    for j in range(1, specialty_num + 1):
        x.add_specialty(SUBJECT[j])
    #add reviewer to roster
    test_roster.new(x)
    
#generate Courses
for i in range(0,COUR):
    name = 'course' + str(i)
    number =  i
    subject = SUBJECT[random.randint(0,len(SUBJECT+1))]
    grade =  GRD[random.randint(0,2)]
    y = Course(name, number, subject, grade)
    #add Courses to Catalogue
    test_catalogue.new(y)

# assign courses from catalogue to Reivewers
#iterate over sorted available reviewers
for subject, reviewerlist in test_roster.available.iteritems():
    if test_catalogue.availble[subject]:
        
    #assing course and reviewer to one another 

