from faisalqureshi_ch1 import FieldElement

print("****************************************************************")
print("\033[31m Solutions for Excercises of Chapter 2. \033[0m")
print("****************************************************************")

class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({}, {}) is not on the curve'.format(x, y))
    # end::source1[]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b
    
# ***********************************Solution for Excercise 2 of Ch2***************************************
    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)
# *********************************************************************************************************
   
    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(
                'Points {}, {} are not on the same curve'.format(self, other))
        # Case 0.0: self is the point at infinity, return other
        if self.x is None:
            return other
        # Case 0.1: other is the point at infinity, return self
        if other.x is None:
            return self
        
# ***********************************Solution for Excercise 3 of Ch2***************************************
        # Case 1: self.x == other.x, self.y != other.y
        # Result is point at infinity
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)
# *********************************************************************************************************

# ***********************************Solution for Excercise 5 of Ch2***************************************  
        # Case 2: self.x ≠ other.x
        # Formula (x3,y3)==(x1,y1)+(x2,y2)
        # s=(y2-y1)/(x2-x1)
        # x3=s**2-x1-x2
        # y3=s*(x1-x3)-y1
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
# ********************************************************************************************************    

# ***********************************Solution for Excercise 7 of Ch2***************************************       
         # Case 3: self == other
        # Formula (x3,y3)=(x1,y1)+(x1,y1)

        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)
# ********************************************************************************************************  
        # Case 4: if we are tangent to the vertical line,
        # we return the point at infinity
        # note instead of figuring out what 0 is for each type
        # we just use 0 * self.x
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)


print("Solution for Excercise 1 of Ch2")
def on_curve(x, y):
    return y**2 == x**3 + 5*x + 7
print(on_curve(2,4)) #False
print(on_curve(-1,-1)) #True
print(on_curve(18,77)) #True
print(on_curve(5,7)) #False

print("Solution for Excercise 4 of Ch2")
p1 = Point(2,5,5,7)
p2 = Point(-1,-1,5,7)
print(p1+p2) #Point(3.0,-7.0)_5_7

print("Solution for Excercise 6 of Ch2")
p3 = Point(-1,-1,5,7)
p4 = Point(-1,-1,5,7)
print(p3+p4) #Point(18.0,77.0)_5_7