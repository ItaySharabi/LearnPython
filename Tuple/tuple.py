print("\n-----------------------------------------\n")
# Tuples are used to store multiple items in a single variable.
# The Tuple data-type is similar to a list, they both have indexes, but the difference is:
# *** You cannot change the values inside a tuple once you have created it!

my_tuple = ("Apple", "Banana", "Cherry")

# my_tuple[0] = "Mango"     # ERROR!

print(my_tuple[0])
















#
# print(f"print(my_tuple) -> {my_tuple}")
# print("\n-----------------------------------------\n")
#
# # Tuple items are indexed, the first item has index [0], the second item has index [1] and so on...
# # To access the tuple items use [] and specify the index you want to access:
#
# print(f"Access item at index 1: my_tuple[1] = {my_tuple[1]}")
# print(f"Access item at index -1(Last): my_tuple[-1] = {my_tuple[-1]}")
#
#
# print("\n-----------------------------------------\n")
#
# # Allow duplicate values:
# my_tuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(f"my_tuple with duplicate values:\t {my_tuple}")
#
# # Tuple is `iterable`, you can iterate over it's items:
# for x in my_tuple:
#     print(f"x = {x}")
