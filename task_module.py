import test_module_1 as t1
import test_module_2 as t2
import random


t1.say_hello()
t2.say_hello()

dog = t1.Dog
cat = t2.Cat

rand = random.randint(1, 10)

print(dog)
print(cat)
print(rand)

