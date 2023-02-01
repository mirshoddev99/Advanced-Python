from collections import deque

my_deq = deque()
my_deq.append(1)
my_deq.append(2)
my_deq.append(3)
print(my_deq)

# # appendLeft method
# my_deq.appendleft(4)
# print("AppendLeft ", my_deq)

# # popLeft method
# my_deq.popleft()
# print("popLeft ", my_deq)

# # extendLeft method
# my_deq.extendleft([6, 5, 4])
# print("ExtendLeft ", my_deq)

# # rotate method
# my_deq.rotate(3)
# print("Rotate 3 ", my_deq)

# # Negative Rotate method
# my_deq.rotate(-3)
# print("Rotate -3 ", my_deq)

my_num = "12345".split(" ")
my_deq = deque()
my_deq.append(my_num)
print(my_deq)