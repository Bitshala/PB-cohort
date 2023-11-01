print("****************************************************************")
print("\033[31m Solutions for Excercises of Chapter 1. \033[0m")
print("****************************************************************")

class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

# ***********************************Solution for Excercise 1 of Ch1***************************************
    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)
# ***************************************************************************************************

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num + other.num) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)

# ***********************************Solution for Excercise 3 of Ch1***************************************
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num - other.num) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)
# ***************************************************************************************************

# ***********************************Solution for Excercise 6 of Ch1***************************************
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num * other.num) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)
# ***************************************************************************************************

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
# ***********************************Solution for Excercise 9 of Ch1***************************************
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)
# ****************************************************************************************************
    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num=num, prime=self.prime)


print("Solution for Excercise 2 of Ch1")
prime = 57
print((44+33)%prime)
print((9-29)%prime)
print((17+42+49)%prime)
print((52-30-38)%prime)


print("Solution for Excercise 4 of Ch1")
prime = 97
print(95*45*31 % prime)
print(17*13*19*44 % prime)
print(12**7*77**49 % prime)

print("Solution for Excercise 5 of Ch1")
prime = 19
for k in (1,3,7,13,18):
    print([k*i % prime for i in range(prime)])

'''Inference deduced from Excersice 4: It demonstrate some of the key properties of finite fields, 
including their cyclic nature, the existence of subgroups, and the behavior of elements under multiplication and modulo operations.
 The code helps illustrate the arithmetic properties of finite fields and how elements within them interact.
'''

print("Solution for Excercise 7 of Ch1")
for prime in (7, 11, 17, 31):
     print([pow(i, prime-1, prime) for i in range(1, prime)])

print("Solution for excercise 8 of Ch1")
prime = 31
print(3*pow(24, prime-2, prime) % prime)
print(pow(17, prime-4, prime))
print(pow(4, prime-5, prime)*11 % prime)
