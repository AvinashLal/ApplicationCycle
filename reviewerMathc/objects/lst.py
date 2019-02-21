class Lst:
    def __init__(self):
        self.all = []
        #sort elt by area of expertise into dictionary
        self.available = {}
        self.busy = {}

    def __str__(self):
        a = ", ".join(self.all)
        b = ', \n'.join('{}:{}'.format(key, val) for key, val in self.available.iteritems())
        c = ', \n'.join('{}:{}'.format(key, val) for key, val in self.busy.iteritems())
        return "all: %s \n available:%s \n busy:%s" % (a, b, c)
        pass 
        
    def find(self, elt_name):
        found = None
        for elt in self.all:
            if elt.return_name == elt_name:
                found = elt
        if found == None:
            print('elt does not exist')
        else:
            return found    

    def add_to(self, dicts, elt):
        for subject in elt.specialty:
            if subject in dicts.keys():
                dicts[subject].append(elt)
            else:
                dicts[subject] = [elt]

    def remove_from(self, dicts, elt):
        for subject, elts in dicts.items():
            if elt in elts:
                elts.remove(elt)

    def move_from_to(self, elt, frm, to):
        self.remove_from(frm, elt)
        self.add_to(to, elt)

    def new(self, elt):
        self.all.append(elt)
        self.add_to(self.available, elt) 

    def delete(self, elt):
        self.remove_from(self.available, elt)
        self.remove_from(self.busy, elt)
        self.all.remove(elt)
