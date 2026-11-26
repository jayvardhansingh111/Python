# MRO - method resolution order  ------ Algorithm
# in hybrid inheritance the method resolution order based on MRO algo
# This algorithm is also known as C3 algorith
# it follows DLR( Depth First Left to Right )



class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())


# ------------------------------------------------------------------
#  Flow of child to parent classes -------



class A:
    def m1(self):
        print("class A m1 method.")
class B(A):
    def m1(self):
        print("class B m1 method.")
class C(A):
    def m1(self):
        print("class C m1 method.")
class D(B,C):
    def m1(self):
        print("class D m1 method.")

d=D()
d.m1()



class A:
    def m1(self):
        print("class A m1 method.")
class B(A):
    def m1(self):
        print("class B m1 method.")
class C(A):
    def m1(self):
        print("class C m1 method.")
class D(B,C):
   pass

d=D()
d.m1()




class A:
    def m1(self):
        print("class A m1 method.")
class B(A):
    def m1(self):
        print("class B m1 method.")
class C(A):
    def m1(self):
        print("class C m1 method.")
class D(C,B):
   pass

d=D()
d.m1()





class A:
    def m1(self):
        print("class A m1 method.")
class B(A):
    pass
class C(A):
    pass
class D(B,C):
   pass

d=D()
d.m1()






# --------------------------------------------------
#  C3 algorithm -----


class A: pass
class B: pass
class C: pass
class X(A,B): pass
class Y(B,C): pass
class P(X,Y,C): pass

print(A.mro())
print(B.mro())
print(X.mro())
print(Y.mro())
print(P.mro())





# -----------------------------------------------------------------


class A:
    def m1(self):
        print("parent class A m1 method")
class B:
    def m1(self):
        print("parent class B m1 method")
class C:
    def m1(self):
        print("parent class C m1 method")
class X(A,B):
    def m1(self):
        print("X child class of A,B m1 method")
class Y(B,C):
    def m1(self):
        print("Y child class of B,C m1 method")
class P(X,Y,C):
    def m1(self):
        print("P child class of X,Y,C m1 method")

p1=P()
p1.m1()  # P child class of X,Y,C m1 method






class A:
    def m1(self):
        print("parent class A m1 method")
class B:
    def m1(self):
        print("parent class B m1 method")
class C:
    def m1(self):
        print("parent class C m1 method")
class X(A,B):
    def m1(self):
        print("X child class of A,B m1 method")
class Y(B,C):
    def m1(self):
        print("Y child class of B,C m1 method")
class P(X,Y,C):pass

p1=P()
p1.m1()  # X child class of A,B m1 method






class A:
    def m1(self):
        print("parent class A m1 method")
class B:
    def m1(self):
        print("parent class B m1 method")
class C:
    def m1(self):
        print("parent class C m1 method")
class X(A,B):
    def m1(self):
        print("X child class of A,B m1 method")
class Y(B,C):pass
class P(X,Y,C):pass

p1=P()
p1.m1()  # X child class of A,B m1 method






class A:
    def m1(self):
        print("parent class A m1 method")
class B:
    def m1(self):
        print("parent class B m1 method")
class C:
    def m1(self):
        print("parent class C m1 method")
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass

p1=P()
p1.m1()  # parent class A m1 method






class A:
    def m1(self):
        print("parent class A m1 method")
class B:
    def m1(self):
        print("parent class A m1 method")
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass

p1=P()
p1.m1()  # parent class A m1 method






class A:
    def m1(self):
        print("parent class A m1 method")
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass

p1=P()
p1.m1()  # parent class A m1 method







# ----------------------------------------------------


class D: pass
class E: pass
class F: pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass

print(A.mro())  # A+B+C+D+E+F+O





