import random
def randInt(min=0, max=100):
    if min > 0 and  min <= 100 and not(min > max):
        max -= min 
    elif min > max or max < 0:
        return "min must be less or equal max"
    num = int(random.random()*max + min)
    return num

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))

