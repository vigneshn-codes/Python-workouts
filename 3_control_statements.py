#control statements

#if statement

a = 10
if a > 5:
    print("a is greater than 5")
else:
    print("a is less than 5")

#if else statement

a = 10
if a > 5:
    print("a is greater than 5")
else:
    print("a is less than 5")

#if elif else statement

a = 10
if a > 5:
    print("a is greater than 5")
elif a < 5:
    print("a is less than 5")
else:
    print("a is equal to 5")

#nested if statement

a = 10
if a > 5:
    if a > 10:
        print("a is greater than 10")
    else:
        print("a is less than 10")
else:
    print("a is less than 5")

#for loop

for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

#while loop

i = 0
while i < 10:
    print(i)
    i += 1