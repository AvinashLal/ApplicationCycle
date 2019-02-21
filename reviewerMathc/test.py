class A():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return ("num1:%s num2:%s") % \
                (self.a,self.b)

class B(A):
    def __init__(self, a, b, c):
        A.__init__(self, a, b)
        self.h = c
    def __str__(self):
        return ("%s hola") % (self.a)


b = B('a' ,'b', 'c')

c = A(1,2)

d = {'a':[1,2,3], 'b':[4,5,6]}

e = ', '.join('{}:{} \n'.format(key, val) for key, val in d.iteritems())

print(b)

