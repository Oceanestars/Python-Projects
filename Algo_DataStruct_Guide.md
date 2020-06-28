# Must Know Algorithms and Data Structure 
(Python edition)
# Cheat sheet:
- [Big O Cheat Sheet](https://github.com/RehanSaeed/.NET-Big-O-Algorithm-Complexity-Cheat-Sheet/blob/master/Cheat%20Sheet.pdf)
- [Algorithms](https://github.com/TheAlgorithms/Python)
- [Markdown features](https://guides.github.com/features/mastering-markdown/)

# Algorithm
### Linear Search

```python
def search(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1
```
- Time complexity = O(n)
- Space complexity = O(1)

### Binary Search

```python
# Recursive: Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
```
- Time complexity = O(n)
- Space complexity = O(n)


### Merge Sort

```python
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]

    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0 	# Initial index of first subarray
    j = 0 	# Initial index of second subarray
    k = l 	# Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l+(r-1))//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),

mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),
```
- Time Complexity:O(nlog(n))
- Space Complexity:O(n)

### QuickSort

```python
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )     	# index of smaller element
    pivot = arr[high] 	# pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

```

- Time Complexity: O(n^2)
- Space Complexity: O(log(n))

### Insertion Sort
```python
def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
```
- Time Complexity: O(n^2)
- Space Complexity: O(1)

### Bubble Sort

```python
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
```
- Time Complexity: O(n^2)
- Space Complexity: O(1)

### Heap Sort

```python
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1 	# left = 2*i + 1
    r = 2 * i + 2 	# right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
# This code is contributed by Mohit Kumra
```
- Time Complexity: O(nlog(n))
- Space Complexity: O(1)

## Dynamic Problems
Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial.

Here is where greedy algorithms differ from dynamic programming. In dynamic programming, we make a choice at each step, but the choice usually depends on the solutions to subproblems. Consequently, we typically solve dynamic-programming problems in a bottom-up manner, progressing from smaller subproblems to larger subproblems.

A problem exhibits optimal substructure if an optimal solution to the problem contains within it optimal solutions to subproblems.

__Overlapping Subproblems__:
Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed.
### Knapsack problem

```python
# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W
def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included  
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
                knapSack(W, wt, val, n-1))

# end of function knapSack

# To test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapSack(W, wt, val, n)

# This code is contributed by Nikhil Kumar Singh
```

### Subsequence problem

```python
edit
play_arrow

brightness_4
# Dynamic Programming implementation of LCS problem

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

```

## Greedy Problems
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal also leads to global solution are best fit for Greedy.

- Examples: Kruskal, Prim’s, Dijkastra, Max Flow


## Divide and Conquer Problems
This technique can be divided into the following three parts:
Divide: This involves dividing the problem into some sub problem.
Conquer: Sub problem by calling recursively until sub problem solved.
Combine: The Sub problem Solved so that we will get find problem solution.

- Example: Binary Search, Quicksort, Merge Sort

#  Data Structure

## Arrays

- append() - Adds an element at the end of the list
- clear() - Removes all the elements from the list
- copy() - Returns a copy of the list
- count() - Returns the number of elements with the specified value
- extend() - Add the elements of a list (or any iterable), to the end of the current list
- index() - Returns the index of the first element with the specified value
- insert() - Adds an element at the specified position
pop() - Removes the element at the specified position
- remove() - Removes the first item with the specified value
- reverse() - Reverses the order of the list
- sort() - Sorts the list

- Time complexity = O(1)(Access)
- Space complexity = O(n)


## Stacks

```python

class Stack:


   """ A stack is an abstract data type that serves as a collection of

   elements with two principal operations: push() and pop(). push() adds an

   element to the top of the stack, and pop() removes an element from the top

   of a stack. The order in which elements come off of a stack are

   Last In, First Out (LIFO).

   https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

   """

   def __init__(self, limit=10):

       self.stack = []

       self.limit = limit


   def __bool__(self):

       return bool(self.stack)


   def __str__(self):

       return str(self.stack)


   def push(self, data):

       """ Push an element to the top of the stack."""

       if len(self.stack) >= self.limit:

           raise StackOverflowError

       self.stack.append(data)


   def pop(self):

       """ Pop an element off of the top of the stack."""

       if self.stack:

           return self.stack.pop()

       else:

           raise IndexError("pop from an empty stack")


   def peek(self):

       """ Peek at the top-most element of the stack."""

       if self.stack:

           return self.stack[-1]


   def is_empty(self):

       """ Check if a stack is empty."""

       return not bool(self.stack)


   def size(self):

       """ Return the size of the stack."""

       return len(self.stack)


   def __contains__(self, item) -> bool:

       """Check if item is in stack"""

       return item in self.stack


class StackOverflowError(BaseException):

   pass


if __name__ == "__main__":

   stack = Stack()

   for i in range(10):

       stack.push(i)


   print("Stack demonstration:\n")

   print("Initial stack: " + str(stack))

   print("pop(): " + str(stack.pop()))

   print("After pop(), the stack is now: " + str(stack))

   print("peek(): " + str(stack.peek()))

   stack.push(100)

   print("After push(100), the stack is now: " + str(stack))

   print("is_empty(): " + str(stack.is_empty()))

   print("size(): " + str(stack.size()))

   num = 5

   if num in stack:

       print(f"{num} is in stack")


```
- Time complexity = O(n)
- Space complexity = O(n)

## Queues
```python
# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

```
- Time complexity = O(n)
- Space complexity = O(n)

## Linked Lists

```python
class Node:

   def __init__(self, data):

       self.data = data

       self.next = None


   def __repr__(self):

       return f"Node({self.data})"


class LinkedList:

   def __init__(self):

       self.head = None  # initialize head to None


   def insert_tail(self, data) -> None:

       if self.head is None:

           self.insert_head(data)  # if this is first node, call insert_head

       else:

           temp = self.head

           while temp.next:  # traverse to last node

               temp = temp.next

           temp.next = Node(data)  # create node & link to tail


   def insert_head(self, data) -> None:

       new_node = Node(data)  # create a new node

       if self.head:

           new_node.next = self.head  # link new_node to head

       self.head = new_node  # make NewNode as head


   def print_list(self) -> None:  # print every node data

       temp = self.head

       while temp:

           print(temp.data)

           temp = temp.next


   def delete_head(self):  # delete from head

       temp = self.head

       if self.head:

           self.head = self.head.next

           temp.next = None

       return temp


   def delete_tail(self):  # delete from tail

       temp = self.head

       if self.head:

           if self.head.next is None:  # if head is the only Node in the Linked List

               self.head = None

           else:

               while temp.next.next:  # find the 2nd last element

                   temp = temp.next

               # (2nd last element).next = None and temp = last element

               temp.next, temp = None, temp.next

       return temp


   def is_empty(self) -> bool:

       return self.head is None  # return True if head is none


   def reverse(self):

       prev = None

       current = self.head


       while current:

           # Store the current node's next node.

           next_node = current.next

           # Make the current node's next point backwards

           current.next = prev

           # Make the previous node be the current node

           prev = current

           # Make the current node the next node (to progress iteration)

           current = next_node

       # Return prev in order to put the head at the end

       self.head = prev


   def __repr__(self):  # String representation/visualization of a Linked Lists

       current = self.head

       string_repr = ""

       while current:

           string_repr += f"{current} --> "

           current = current.next

       # END represents end of the LinkedList

       return string_repr + "END"


   # Indexing Support. Used to get a node at particular position

   def __getitem__(self, index):

       current = self.head


       # If LinkedList is empty

       if current is None:

           raise IndexError("The Linked List is empty")


       # Move Forward 'index' times

       for _ in range(index):

           # If the LinkedList ends before reaching specified node

           if current.next is None:

               raise IndexError("Index out of range.")

           current = current.next

       return current


   # Used to change the data of a particular node

   def __setitem__(self, index, data):

       current = self.head

       # If list is empty

       if current is None:

           raise IndexError("The Linked List is empty")

       for i in range(index):

           if current.next is None:

               raise IndexError("Index out of range.")

           current = current.next

       current.data = data


   def __len__(self):

       """

       Return length of linked list i.e. number of nodes

       >>> linked_list = LinkedList()

       >>> len(linked_list)

       0

       >>> linked_list.insert_tail("head")

       >>> len(linked_list)

       1

       >>> linked_list.insert_head("head")

       >>> len(linked_list)

       2

       >>> _ = linked_list.delete_tail()

       >>> len(linked_list)

       1

       >>> _ = linked_list.delete_head()

       >>> len(linked_list)

       0

       """

       if not self.head:

           return 0


       count = 0

       cur_node = self.head

       while cur_node.next:

           count += 1

           cur_node = cur_node.next

       return count + 1


```

- Time complexity = O(n)
- Space complexity = O(n)

## Hash Tables
[Hashing](https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html)

## Trees
[Python BST - Insert/Inorder/Preorder/Postorder](https://youtu.be/YlgPi75hIBc)

Depth First Traversals:
(a) Inorder (Left, Root, Right) 
(b) Preorder (Root, Left, Right) 
(c) Postorder (Left, Right, Root) 

Breadth First or Level Order Traversal: Per level(top to bottom)

```python
class Node:
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insert(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True
				
	def find(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False
				
	def getHeight(self):
		if self.leftChild and self.rightChild:
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

	def preorder(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value))

	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print (str(self.value))
			if self.rightChild:
				self.rightChild.inorder()

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False
			
	def getHeight(self):
		if self.root:
			return self.root.getHeight()
		else:
			return -1
	
	def remove(self, data):
		# empty tree
		if self.root is None:
			return False
			
		# data is in root node	
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild
					
				self.root.value = delNode.value
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild
				else:
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None
						
			return True
		
		parent = None
		node = self.root
		
		# find node to remove
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild
		
		# case 1: data not found
		if node is None or node.value != data:
			return False
			
		# case 2: remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		# case 3: remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		# case 4: remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		# case 5: remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None

	def preorder(self):
		if self.root is not None:
			print("PreOrder")
			self.root.preorder()
		
	def postorder(self):
		if self.root is not None:
			print("PostOrder")
			self.root.postorder()
			
	def inorder(self):
		if self.root is not None:
			print("InOrder")
			self.root.inorder()

bst = Tree()
print(bst.insert(10))
#print(bst.insert(5))
bst.preorder()
print(bst.getHeight())
#bst.postorder()
#bst.inorder()
print(bst.remove(10))
bst.preorder()

```
## Tuple
You cannot change or remove items in a tuple.
```python
integer_list = map(int, input().split()) #Map is for typecasting here
  print(hash(tuple(integer_list)))
```
- cmp(tuple1, tuple2) - Compares elements of both tuples.

- len(tuple) - Gives the total length of the tuple.

- max(tuple) - Returns item from the tuple with max value.

- min(tuple) - Returns item from the tuple with min value.

- tuple(seq) - Converts a list into tuple.

## Dictionary

```python
temp = min(Weighted_average.keys()) # smallest key
Iterate through a Dictionary
for key, value in dict(Weighted_average).items():
            if  blabla:
                del Weighted_average[key]
	    Weighted_average.update({int(Weighted_average[key][0]): float(current_average)})
```

## Maps
 map(fun, iter)

```python
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

Output :
[5, 7, 9]
# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
Output :
[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
```




## Sets
Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
Define a set: S = {1,2,3}

- s.update(t) - s |= t - return set s with elements added from t
- s.intersection_update(t) - s &= t - return set s keeping only elements also found in t
- s.difference_update(t) - s -= t - return set s after removing elements found in t
- s.symmetric_difference_update(t) - s ^= t - return set s with elements from s or t but not both
- s.add(x) - add element x to set s
- s.remove(x) - remove x from set s; raises KeyError if not present
- s.discard(x) - removes x from set s if present
- s.pop() - remove and return an arbitrary element from s; raises KeyError if empty
- s.clear() - remove all elements from set s

## Graphs
### BFS

```python
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
```
- Time Complexity: O(n)
- Space Complexity: O(n)

### DFS

```python

# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited[v] = True
        print(v, end = ' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph)+1)

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

# Driver code

# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
```
- Time Complexity: O(n)
- Space Complexity: O(logn)
### Dijkstra

```python
# Library for INT_MAX
import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    def printSolution(self, dist):
        print "Vertex \tDistance from Source"
        for node in range(self.V):
            print node, "\t", dist[node]

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxint

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

g.dijkstra(0);

```
### Huffman’s

[Huffman’s code](https://www.programiz.com/dsa/huffman-coding)


### Recursion

Count substrings with same first and last characters
```python
# Python 3 program to count substrings with same
# first and last characters

# Function to count subtrings with same first and
# last characters
def countSubstrs(str, i, j, n):

    # base cases
    if (n == 1):
        return 1
    if (n <= 0):
        return 0

    res = (countSubstrs(str, i + 1, j, n - 1)
        + countSubstrs(str, i, j - 1, n - 1)
        - countSubstrs(str, i + 1, j - 1, n - 2))

    if (str[i] == str[j]):
        res += 1

    return res

# driver code
str = "abcab"
n = len(str)
print(countSubstrs(str, 0, n - 1, n))

```




# Time complexity:
## O(1) time
- Accessing Array Index (int a = ARR[5];)
- Inserting a node in Linked List
- Pushing and Popping on Stack
- Insertion and Removal from Queue
- Finding out the parent or left/right child of a node in a tree stored in Array
- Jumping to Next/Previous element in Doubly Linked List

## O(n) time
In a nutshell, all Brute Force Algorithms, or Noob ones which require linearity, are based on O(n) time complexity
- Traversing an array
- Traversing a linked list
- Linear Search
- Deletion of a specific element in a Linked List (Not sorted)
- Comparing two strings
- Checking for Palindrome
- Counting/Bucket Sort and here too you can find a million more such

## O(log n) time
- Binary Search
- Finding largest/smallest number in a binary search tree
- Certain Divide and Conquer Algorithms based on - Linear functionality
- Calculating Fibonacci Numbers - Best Method The basic premise here is NOT using the complete data, and reducing the problem size with every iteration

## O(n log n) time
The factor of 'log n' is introduced by bringing into consideration Divide and Conquer. Some of these algorithms are the best optimized ones and used frequently.
- Merge Sort
- Heap Sort
- Quick Sort
- Certain Divide and Conquer Algorithms based on optimizing O(n^2) algorithms

## O(n^2) time
These ones are supposed to be the less efficient algorithms if their O(nlogn) counterparts are present. The general application may be Brute Force here.
- Bubble Sort
- Insertion Sort
- Selection Sort
- Traversing a simple 2D array
