import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


# _ = input("line 13")
big_range = range(5)
# big_range = my_range(5)
# _ = input("line 15")

# print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range

big_list = []
# _ = input("line 22")
for val in big_range:
    # _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
for i in big_range:
    print("i is {}".format(i))

# variable generators are bad if you intend to use them in a for loop, but is fine for when you intend
# to use the next statement

for i in my_range(5):
    print("i is {}".format(i))

# range class behaves like an iterable however and resets each time that it is called
