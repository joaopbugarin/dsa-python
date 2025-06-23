"""
#studies
"""

# Basic Syntax in Python
########################################################
# %% Variables
# determined at runtime
# multiple variables can be assigned in one line
n, m, o = 10, "abc", 3.14
print(n, m, o)
# None is the null value in Python
X = None  # X has to be uppercase for None
print(X)

########################################################
# %% Ifs
NUM = 1
if NUM < 2:
    print("NUM is lesser than 2, NUM is:", NUM)
    NUM += 1
elif NUM == 2:
    print("NUM is equal to 2")
    NUM += 2
else:
    print("NUM is greater than 2")
print("NUM is now:", NUM)

#########################################################
# %% Loops
n = 0
while n < 5:
    print("n is:", n)
    n += 1
    if n == 5:
        print("--------------------")

for i in range(2, 10):
    print("i is:", i)
    if i == 9:
        print("--------------------")

########################################################
# %% Math
print(5 / 2)
print(5 // 2)  # floor division, result is 2
print(int(-3 / 2))  # integer division, result is -1
print(5 % 2)  # modulo operation, result is 1
print(5**2)  # exponentiation, result is 25

import math

print(math.sqrt(25))  # square root, result is 5.0
print(math.pow(2, 3))  # power, result is 8.0

########################################################
# %% Arrays -> called lists in Python
arr = [1, 2, 3, 4, 5]
print(arr)
arr.append(6)
print(arr)
arr.pop()
print(arr)

arr.insert(3, 10)
print(arr)
arr[3] = 20
print(arr)
print("last but 2 element:", arr[-2], "\n")

# Initiliaze an array of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))  # length of the array
arr[len(arr) - 1] = 10  # change last element
print(arr[-1], "\n")  # last element of the array

# Slicing
print("Slicing:")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[2:5])  # elements from index 2 to 4
print(arr[:5])  # elements from start to index 4
print(arr[5:])  # elements from index 5 to end
print(arr[-3:])  # last 3 elements
print(arr[::2])  # every second element
print(arr[::-1])  # reverse the array
print()

# Unpacking
a, b, c = [1, 2, 3]  # number of elements must match
print(a, b, c)

# Loop through array
nums = [1, 2, 3, 4, 5]

# using index
for i in range(len(nums)):
    print(nums[i], end=" ")

# without index
for i in nums:
    print(i, end=" ")
print()

# with index and value
for i, n in enumerate(nums):  # enumarate gives index and value
    print(f"Index: {i}, Value: {n}", end=" ")
print()

# Loop through multiple arrays simultaneously
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
for a, b in zip(arr1, arr2):  # zip combines the two arrays
    print(f"Array1: {a}, Array2: {b}", end=" ")
print()

# Reverse
arr = [1, 2, 3, 4, 5]
arr.reverse()  # reverse the array in place
print(arr)
print()

# Sorting
arr = [5, 2, 9, 1, 5, 6]
arr.sort()  # sort the array in place
print(arr)
arr.sort(reverse=True)  # sort in descending order
print(arr)
print()

# Custom sorting
arr.sort(key=lambda x: -x)  # sort in descending order using a lambda function

# Custom sort by length of string
arr = ["apple", "banana", "kiwi", "cherry"]
arr.sort(key=lambda x: len(x))  # sort by length of string
print(arr)
print()

# List Comprehensions
arr = [i for i in range(5)]
print(arr)  # [0, 1, 2, 3, 4]
##testing for future exercise:
expected_length = 5
key_to_fill = "s"
array_1 = ["x"]
array_2 = array_1 + [
    key_to_fill for i in range(expected_length - len(array_1))
]  # fill the rest with 's'
print("array_2 length:", len(array_2))  # should be 5
print("array_2:", array_2)  # should be ['x', 's', 's', 's', 's']
print()
# 2-d lists
arr = [[0] * 4 for i in range(5)]  # 4x5 matrix initialized with 0
print(arr)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print()

#############################################
# %% Strings
s = "abc"
print(s[0:2])
s += "def"  # concatenation
print(s)
print(int("123") + int("123"))  # string to int conversion (works with numbers only)
print(str(123) + "abc")  # int to string conversion (works with numbers only)
print()
strings = ["abc", "def", "ghi"]
print(" ## ".join(strings))  # join strings with " ## "


#################################################
# %% Queues
from collections import deque

queue = deque()  # create a queue
queue.append(1)  # add an element to the queue
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])
queue.popleft()  # remove the first element from the queue
print(queue)  # deque([2, 3])
queue.appendleft(0)  # add an element to the front of the queue
print(queue)  # deque([0, 2, 3])


#################################################
# %% Hashsets
hashset = set()  # create a hashset
hashset.add(1)  # add an element to the hashset
hashset.add(2)
hashset.add(3)
print(hashset)  # {1, 2, 3}
print()

print(set([3, 2, 1, 4, 5]))  # create a set from a list
print({i for i in range(5)})  # create a set using a set comprehension
print({3 for i in range(5)})  # sets have no duplicates, so this will only add 3 once


#################################################
# %% Hashmaps (aka dict)
myMap = {}  # create a hashmap
myMap["alice"] = 88  # add a key-value pair
myMap["bob"] = 95
print(myMap)  # {'alice': 88, 'bob': 95}
myMap["alice"] = 90  # update the value for key "alice" - no duplicates in keys
print(myMap)  # {'alice': 90, 'bob': 95}
print("alice" in myMap)  # check if key "alice" exists in the hashmap
print("charlie" in myMap)  # check if key "charlie" exists
myMap = {"alice": 88, "bob": 95, "charlie": 100}
print(myMap.get("alice"))  # get the value for key "alice"
print()

# Dictionary Comprehensions
myMap2 = {i: 2 * i for i in range(3)}
print(myMap2)  # {0: 0, 1: 2, 2: 4}
print()

# loop through hashmap
for key in myMap:  # loop through keys
    print(f"Key: {key}, Value: {myMap[key]}")  # prints key and value
print()

for val in myMap.values():  # loop through values
    print(f"Value: {val}")  # prints value
print()

for key, val in myMap.items():  # loop through key-value pairs
    print(f"Key: {key}, Value: {val}")  # prints key and
print()

######################################################
# %% Tuples
# Like arrays, but immutable
tup = (1, 2, 3)  # create a tuple
print(tup)  # (1, 2, 3)
print(tup[0])  # access the first element
# Can be used as keys in hashmaps
myMap = {tup: 3}
print(myMap)  # {(1, 2, 3): 3}

mySet = set()  # create a set
mySet.add(tup)  # add a tuple to the set
print((1, 2) in mySet)  # check if tuple (1, 2) is in the set
print((1, 2, 3) in mySet)  # check if tuple (1, 2, 3) is in the set
print()

#######################################################
# %% Heaps
import heapq

# under the hood are arrays, but they are used as heaps
minHeap = []  # create a heap
heapq.heappush(minHeap, 4)  # add an element to the heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
print("Min Heap element in ascending order:")
print(minHeap[0])  # get the smallest element (root) of the heap
print()
print("Min Heap elements in ascending order:")
while len(minHeap):
    print(heapq.heappop(minHeap))  # print in ascending order
print()

# Max heaps do not exist in Python, but can be simulated by negating the values
maxHeap = []  # create a max heap
heapq.heappush(maxHeap, -4)  # add an element to the heap
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
print("Max Heap element in ascending order (negated):")
print(-maxHeap[0])  # get the largest element (root) of the heap
print()
print("Max Heap elements in descending order:")
while len(maxHeap):
    print(-heapq.heappop(maxHeap))  # print in descending order
print()

# Building a heap from an array
arr = [5, 2, 9, 1, 5, 6]
heapq.heapify(arr)  # convert the array into a heap
print("Heapified array:", arr)  # the array is now a heap
print("Smallest element in the heap:", arr[0])  # get the smallest element
print()


###############################################################
# %% Functions
def myFunction(n, m):
    return n + m  # return the sum of n and m


print(myFunction(2, 3))  # call the function with arguments 2 and 3
print()


# Nested functions
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c  # inner function can access outer function's variables

    return inner()  # return the inner function without calling it


print(outer("a", "b"))  # call the outer function, but inner function is not called
print()


# Can modify objects but not reassign them
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # modifying the array is allowed, we are modifying the object in place
        for i, n in enumerate(arr):
            arr[i] *= 2

            # will only modify in the helper function scope
            # val *= 2 we can't reassign val here
            # will raise an error, because val is not defined in the helper function scope
            nonlocal val  # allows to modify the outer function's variable
            val *= 2  # now we can modify val

    helper()  # call the inner function
    print("Array after doubling:", arr)  # print the modified array
    print("Value after doubling:", val)  # print the modified value


nums = [1, 2]
val = 3
double(nums, val)  # call the function with the array and value


####################################################################
# %% Classes
class MyClass:
    # Constructor
    def __init__(self, numes):
        # Create member variable
        self.nums = numes  # self refers to the instance of the class
        self.size = len(numes)  # size of the array

        # methods
        def getLength(self):
            return self.size

        def getDoubleLength(self):
            return 2 * self.getLength()  # call the getLength method
