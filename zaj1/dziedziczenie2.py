class A(object):
    def funkcja(self):
        print "A"

class B(A):
    def funkcja(self):
        print "B"
        super(B, self).funkcja()

B().funkcja()
