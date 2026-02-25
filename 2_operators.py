#arithmetic operators

a = 10
b = 5

print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a % b) #modulus
print(a ** b) #exponentiation
print(a // b) #floor division


#comparison operators

a = 10
b = 5

print(a == b) #equal to
print(a != b) #not equal to
print(a > b) #greater than
print(a < b) #less than
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to

#logical operators

a = True
b = False

print(a and b) #and
print(a or b) #or
print(not a) #not

#assignment operators

a = 10
b = 5

a += b #a = a + b
print(a)

a -= b #a = a - b
print(a)

a *= b #a = a * b
print(a)

a /= b #a = a / b
print(a)

a %= b #a = a % b
print(a)

a **= b #a = a ** b
print(a)

a //= b #a = a // b
print(a)

#membership operators

a = "Hello, World!"
print("Hello" in a) #True
print("Hello" not in a) #False

#identity operators

a = 10
b = 10
print(a is b) #True
print(a is not b) #False