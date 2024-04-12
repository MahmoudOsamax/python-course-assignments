#assign 1

name = "mahmoud"
age = "21"
country = "Egypt"
print(f'''" Hello '{name}', How You Doing \  """ Your Age Is '{age}'"+ And Your Country Is: {country}''')

#assign 2

print(f'''" Hello '{name}', How You Doing \ \n """ Your Age Is '{age}'"+\n And Your Country Is: {country}''')

# assign 3

user='Elzero'
print(user[1])
print(user[2])
print(user[-1])

# assign 4
print(user[1:4])
print(user[::2])
print(user[-2::-2])

# assign 5
name2 = "#@#@Elzero#@#@"
print(name2.strip("@#"))

# assign 6

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

# assign 7

name_one = "mahmoud"
name_two = "mahmoud_osama"

print(name_one.center(20,'@'))
print(name_two.center(20,'@'))

# assign 8

name3 = "MAhmouD"
name4 = "mahmOUD"

print(name3.swapcase())
print(name4.swapcase())

# assign 9

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

# assign 10

name5 = "Elzero"
print(name5.index("z"))

# assign 11

msg2 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3","Love",1))

# assign 12

print(msg2.replace("<3","Love"))

# assign 13
names = "Osama"
ages = 38
countrys = "Egypt"

print(f"My Name Is {names}, And My Age Is {ages}, And My Country Is {countrys}")