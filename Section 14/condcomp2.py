menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("A meal was skipped")
print(meals)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

meals_2 = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
print(meals_2)

x = 12
expression = "Twelve" if x == 12 else "unknown"     # Conditional Expression
print(expression)

for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

for x in range(1, 31):
    # Order is important here!
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)

fizzies = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
           for x in range(1, 31)]
print(fizzies)

for buzz in fizzies:
    print(buzz.center(12, '*'))     # only works with strings

# it's easier to mess with items in a list if every item in the list is of the same type (homogeneous)
