import random
import secrets


random_integer = random.randint(1,10)
print(random_integer)

random_int_excl = random.randrange(1,10)
print(random_int_excl)

random_float = random.random()
print(f"Between 0 to 1: {random_float}")

random_uniform_float = random.uniform(1,5)
print(random_uniform_float)

my_list = ['apple','banana','cherry']
random_choice = random.choice(my_list)
print(random_choice)
