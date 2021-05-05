#1- first task :
#print("Hello world")

# 2- second task:
# name = "Noelle"
# print("Hello", name,"!")
# print("Hello"+name+"!")


#3-Third task:
# name = 42
# print("Hello" , name , "!")
# print("Hello"+name+"!")
#secound print error solved:
# print("Hello"+f"{name}"+"!")

#4- Fourth task:
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print("I love to eat {} and {}.".format(fave_food1, fave_food2))
# print(f"I love to eat {fave_food1} and {fave_food2}.")

#other methods:
# c = "hello world"
# print(c.upper())

# c = "HI GUYS"
# print(c.lower())

# c = "Hello yellow"
# d = "yellow"
# print(c.count(d))

# c = "hello world"
# print(c.split(" "))

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# for k, v in capitals.items():
#     print(k,"=",v)

x = 3
while x > 0:
    print(x)
    x -= 1
    if x == 2:
        break 
else:
    print("Final")
    