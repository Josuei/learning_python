train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

c = 3 * 10 ** 8
def get_energy(mass, c):
  return mass * c
bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  get_force = mass * acceleration
  force = get_force * distance
  return force
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")

#-----------------------------------------------------------------------------------------------

def contains(big_string, little_string):
  return little_string in big_string
print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))

def common_letters(string_one, string_two):
  elements = []
  for d in string_two:
    if d in string_one and elements.count(d) < 1:
      elements.append(d)
  return elements

print(common_letters("banana", "cream"))
print(common_letters('manhattan', 'san francisco'))

def common_letters2(string_one, string_two):
  elements = []
  for d in string_two:
    if d in string_one and d not in elements:
      elements.append(d)
  return elements

print(common_letters2("banana", "cream"))
print(common_letters2('manhattan', 'san francisco'))