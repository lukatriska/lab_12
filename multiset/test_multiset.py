from multiset.multisetll import Multiset

data_set = Multiset()
data_file = open("data.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    data_set.add(line.strip())

data_set.traversal()
print("all items - END")
# print(data_set.empty())
# print(data_set._head.next.next.next.next.next.next.next)
# print(data_set.split_half(2))
# print('FINDING')
# data_set.remove_all()
print(data_set.unorderedSearch('1'))
# print(data_set.__contains__(3))
# print(data_set.unorderedSearch(1))

# print(data_set._head.next.next.next.next.next.next)
# print(data_set._head.next.next.next.next.next)
# print(data_set._head.next.next.next.next)
# print(data_set._head.next.next.next)
# print(data_set._head.next.next)
# print(data_set._head.next)
# print(data_set._head)


# value = input("Guess a value or type stop: ")
# empty = False



# while value != "stop" and not empty:
#     if value in data_set:
#         print("Yes, the set contains", value)
#         data_set.delete(value)
#     else:
#         print("No, the set does not contain", value)
#     if data_set.empty():
#         print("Sorry, there are no values left to guess.")
#         empty = True
#     else:
#         value = input("Guess a value or type stop: ")
