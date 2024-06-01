import numpy as np

one_dimensional_arr = np.array([10, 12])
print(f"one_dimensional_arr: {one_dimensional_arr}")

# Create and print a NumPy array
a = np.array([1, 2, 3])
print(f"a: {a}")

# Create sn array with 3 integers, starting from default integer 0.
b = np.arange(1, 5, 2)
print(f"b: {b}")

# Create an array that starts from integer 1, ends at 20, incremented by 3.
c = np.arange(1, 20, 3)
c_int = np.arange(1, 20, 3, dtype=int)
c_float = np.arange(1, 20, 3, dtype=float)
print(f"c: {c}")
print(f"c_int: {c_int}")
print(f"c_float: {c_float}")

# Create an array with evenly spaced. Start 0, end 100, Space 5
d = np.linspace(0, 100, 5)
print(f"d: {d}")

# Create an array with evenly spaced. Start 0, end 98, Space 5, dtype integer
line_spaces_int = np.linspace(0, 98, 9, dtype=int)
print(f"e: {line_spaces_int}")

# Character array
char_arr = np.array(['Welcome to Math for ML! Hello'])
print(f"char_arr: {char_arr}")
print(f"dtype of char_arr: {char_arr.dtype}")

# Return a new array of shape 3, filled with ones.
ones_arr = np.ones(3, dtype=int)
print(f"ones_array: {ones_arr}")

# Return a new array of shape 3, filled with zeros.
zeros_arr = np.zeros(3)
zeros_arr_int = np.zeros(3, dtype=int)
print(f"zeros_arr: {zeros_arr}")
print(f"zeros_arr_int: {zeros_arr_int}")

# Return a new empty array of shape 3, without initializing entries.
empty_arr = np.empty(3)
print(f"empty_arr: {empty_arr}")

# Return a new array of shape 3 with ramdome number between 0 and 1.
random_arr = np.random.rand(5)
print(f"random_arr: {random_arr}")

############################################################################################################
# Multidimensional Arrays
############################################################################################################

# Create a 2 dimensional array
two_dim_arr = np.array([[1,2,3], [4,5,6,]])
print(f"two_dim_arr: {two_dim_arr}")

# 1-D array
one_dim_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 3])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(
    one_dim_arr, # the array to be reshaped
    (3, 3) # dimension of the new array
)
print(f"multi_dim_arr: {multi_dim_arr}")

# Dimension of multi dimension array
print(f"multi_dim_arr_dimension: {multi_dim_arr.ndim}")

# Shape of multi dimension array
print(f"multi_dim_arr_shape: {multi_dim_arr.shape}")

# Size of the array multi_dim_arr. Returns total number of elements
print(f"multi_dim_arr_size: {multi_dim_arr.size}")

############################################################################################################
# Array MATH operations
############################################################################################################

arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

# Addition two 1-D array
print(f"Addition: {arr_1 + arr_2}")

# Subtraction two 1-D array
print(f"Subtraction: {arr_1 - arr_2}")

# Multiplication two 1-D array
print(f"Multiplication: {arr_1 * arr_2}")

# Multiplication of vector with a scalar (broadcasting)
vector = np.array([1, 2])
scalar = 1.5
print(f"vector * scalar : {vector * scalar}")

############################################################################################################
# Indexing and Slicing
############################################################################################################

# indexing 1-D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Select the third element of the array.
print(f"3rd element: {arr[2]}")

# Select the first element of the array.
print(f"1st element: {arr[0]}")

# indexing 2-D array
two_dim = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Select element 8 from two_dim array
print(f"Index of 8 - two brackets: {two_dim[2][1]}")
print(f"Index of 8 - one brackets: {two_dim[2, 1]}")

#Slicing
arr_to_sliced = np.array([4, 21, 22, 12])
# Slice the array to get [21, 22, 12]
print(f"sliced arr: {arr_to_sliced[1:4]}")

# Slice the array to get [4, 21, 22]
print(f"sliced arr: {arr_to_sliced[:3]}")

# Slice the array to get [22, 12]
print(f"sliced arr: {arr_to_sliced[2:]}")

# Slice the array to get [ 4 22]
print(f"sliced arr: {arr_to_sliced[::2]}")

# Note that a == a[:] == a[::]
#print(arr_to_sliced == arr_to_sliced[:] == arr_to_sliced[::])

# Slice the two_dim array to get first two rows
print(f"sliced_two_dim_array: {two_dim[0:2]}")

# Slice the two_dim array to last two rows.
print(f"sliced_last_two_rows: {two_dim[1:3]}")

# Get all rows and slice 2nd column
print(f"slice 2nd column: {two_dim[:, 1]}")

############################################################################################################
# Stacking
############################################################################################################
a1 = np.array([
    [1, 1],
    [2, 2]
])
a2 = np.array([
    [3, 3],
    [4, 4]
])

print(f"a1:\n{a1}")
print(f"a2:\n{a2}")

# Stack the arrays vertically
vert_stack = np.vstack((a1, a2))
print(f"vert_stack: {vert_stack}")

# Stack arrays horizontally
horz_stack = np.hstack((a1, a2))
print(f"horz_stack: {horz_stack}")

# Split the horizontal stacked array into 2 separate arrays of equal size
print(f"Split horizontally into two: {np.hsplit(horz_stack, 2)}")

# Split the horizontal stacked array into 4 separate arrays of equal size
print(f"Split horizontally into four: {np.hsplit(horz_stack, 4)}")

# Split the horizontally staked array after the first column
print(f"Split after 1st column: {np.hsplit(horz_stack,[1])}")

# Split the vertically stacked array into 2 separate arrays of equal size
print(f"vert_split_two: {np.vsplit(vert_stack, 2)}")

# Split the vertically stacked array into 4 separate arrays of equal size
print(f"vert_split_four: {np.vsplit(vert_stack, 4)}")

# Split the vertically stacked array after the first and third row
print(f"vert_split_first_third: {np.vsplit(vert_stack, [1, 3])}")
