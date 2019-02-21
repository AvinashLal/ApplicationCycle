from reviewers.roster import Roster 
from courses.catalogue import Catalogue 
import numpy as np

class Review_cycle:
    def __init__(self, name, roster, catalogue):
        self.name = name
        self.roster = roster
        self.catalogue = catalogue
        self.graph = np.zeros(len(roster.all_reviewers), 
                        len(catalogue.all_reviewers))

    def match(roster, catalogue):
    #match courses to reviewers
        pass

    def assign(reviewer, course):
    #assign course
    #update object information
    #notification email
        pass



