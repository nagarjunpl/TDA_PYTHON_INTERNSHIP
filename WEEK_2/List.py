# Lists

list = [1, 2, 4, 1, 10]

print(list) # print all items
print(list[0]) # print first item
print(list[0:3]) # print first 3 items
print(list[0:3:2]) # print first 3 items with step 2
print(list[::2]) # print all items with step 2

# List Methods

items = ["banana", "apple", "orange", "mango"]

print(items)
items.append("kiwi") # add item
items.insert(0, "pineapple") # insert item at index 0
items.remove("apple") # remove item
items.pop() # remove last item
items.pop(0) # remove first item
items.sort() # sort items
items.reverse() # reverse items

print(items)

items.clear() # remove all items
print(items)


# adding strings, numbers, booleans, lists, tuples, dictionaries, sets, and other lists to the list

list1 = ["bat", 20, True, 20.5, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: "one", 2: "two", 3: "three"}]

print(list1[4]) # list
print(list1[4][1]) # list
print(list1[5][1]) # tuple
print(list1[6]) # set
print(list1[7]) # dictionary
print(list1[7].values())
