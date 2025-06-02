# ===================== Python Array =====================
import array as arr
import os

# creating an array with integer type
a = arr.array('i', [1, 2, 3, ])
# a = arr.array('i', [1, 2, 3, 'qwerty']) # TypeError: 'str' object cannot be interpreted as an integer
print(type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print(type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print(type(a), a)

# import array module
import array as arr

get_cwd = os.getcwd()

# open file object for writing
f = open(rf'{get_cwd}\Log\array_file.txt', 'wb')
# write array of integers to file object
arr1 = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array in the file :", arr1)
arr1.tofile(f)
# close file
f.close()
# open file for reading
f = open(rf'{get_cwd}\Log\array_file.txt', 'rb')
# initialize array with integer type
array_one = arr.array("i")
# initialize array with integer type
array_two = arr.array("i")
# read 3 items from file
array_one.fromfile(f, 3)
print("Appended array1 :", array_one)
# Moving the cursor to the first position
f.seek(0)
# read 6 items from file
array_two.fromfile(f, 6)
print("Appended array2 :", array_two)
# close file
f.close()

import array as arr

arr3 = arr.array('d', [19.6, 24.9, 54.8, 60.8, 49.50])
print("Array Elements Before Appending :", arr3)
y = 'abcdefgi'
print(y.encode(), type(y.encode()))
arr3.frombytes(y.encode())
print("Array Elements After Appending :", arr3)
