"""
Experiment 1 - NumPy syntax learning experiment.

Demonstrates the NumPy topics covered in the course material (Numpy.pptx):

    1.  NumPy overview
    2.  Array creation      (np.array, zeros, ones, empty, arange, linspace)
    3.  ndarray attributes  (shape, size, dtype, ndim)
    4.  Slicing
    5.  Multidimensional arrays
    6.  ufunc / arithmetic operations
    7.  Comparison operations
    8.  Broadcasting
    9.  Random numbers
    10. Statistics          (sum, mean, variance, standard deviation)
    11. Sorting and statistical functions
    12. vstack, hstack, column_stack, split

Run this file with:
    python numpy_experiment.py
"""

import numpy as np


# ---------------------------------------------------------------------------
# Small helper function: prints a clear header before every section so the
# console output is easy to read and to screenshot for the report.
# ---------------------------------------------------------------------------
def section(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 1. NumPy overview
# ---------------------------------------------------------------------------
def demo_01_overview():
    section("1. NumPy overview")

    # NumPy (Numeric Python) is an open source library for numerical
    # computing. Its two basic objects are:
    #   - ndarray : an n-dimensional array that stores ONE data type
    #   - ufunc   : a "universal function" that operates on whole arrays
    print("NumPy version:", np.__version__)

    # Standard Python lists can hold any object, which wastes memory and
    # CPU time. NumPy arrays store a single type, so they are much faster.
    python_list = [1, 2, 3, 4]          # normal Python list
    numpy_array = np.array([1, 2, 3, 4])  # NumPy ndarray

    print("Python list:", python_list, "-> type:", type(python_list))
    print("NumPy array:", numpy_array, "-> type:", type(numpy_array))


# ---------------------------------------------------------------------------
# 2. Array creation
# ---------------------------------------------------------------------------
def demo_02_array_creation():
    section("2. Array creation")

    # np.array() creates an array from a Python list
    data1 = np.array([1, 2, 3])                 # 1-dimensional array
    print("data1 =", data1)

    data2 = np.array([[1, 2, 3], [4, 5, 6]])    # 2-dimensional array
    print("data2 =")
    print(data2)

    # np.zeros() creates an array filled with 0.0
    print("np.zeros((3, 4)) =")
    print(np.zeros((3, 4)))

    # np.ones() creates an array filled with 1.0
    print("np.ones((2, 3)) =")
    print(np.ones((2, 3)))

    # np.empty() only allocates memory; the values inside are not
    # meaningful yet (often zeros or numbers close to zero).
    print("np.empty((2, 2)) =")
    print(np.empty((2, 2)))

    # np.arange(start, stop, step) works like range() but returns an array
    print("np.arange(1, 20, 5) =", np.arange(1, 20, 5))

    # np.linspace(start, stop, num) creates num evenly spaced values
    # from start to stop (stop is INCLUDED by default)
    print("np.linspace(0, 1, 10) =")
    print(np.linspace(0, 1, 10))


# ---------------------------------------------------------------------------
# 3. ndarray attributes: shape, size, dtype, ndim
# ---------------------------------------------------------------------------
def demo_03_ndarray_attributes():
    section("3. ndarray attributes: shape, size, dtype, ndim")

    # The same example as in the course slides:
    # a 3 rows x 4 columns array holding 0..11
    data = np.arange(12).reshape(3, 4)
    print("data =")
    print(data)

    print("data.shape =", data.shape)   # (3, 4)  -> 3 rows, 4 columns
    print("data.size  =", data.size)    # 12      -> total number of elements
    print("data.dtype =", data.dtype)   # int     -> type of the elements
    print("data.ndim  =", data.ndim)    # 2       -> number of dimensions

    # The element type can also be chosen when creating the array
    floats = np.array([1, 2, 3, 4], dtype=float)
    print("floats =", floats, "-> dtype:", floats.dtype)


# ---------------------------------------------------------------------------
# 4. Slicing
# ---------------------------------------------------------------------------
def demo_04_slicing():
    section("4. Slicing")

    a = np.arange(10)
    print("a =", a)

    print("a[5]      =", a[5])        # single element
    print("a[3:5]    =", a[3:5])      # elements from index 3 up to 5 (5 not included)
    print("a[:5]     =", a[:5])       # from the start up to index 5
    print("a[:-1]    =", a[:-1])      # everything except the last element
    print("a[1:-1:2] =", a[1:-1:2])   # start 1, stop before last, step 2
    print("a[::-1]   =", a[::-1])     # reversed array (step -1)

    # Slices can also be used to MODIFY elements of the array
    a[2:4] = 100, 101
    print("after a[2:4] = 100, 101 -> a =", a)

    # IMPORTANT: a slice is a VIEW of the original array.
    # Changing the slice also changes the original array!
    b = a[3:7]
    b[0] = -10
    print("after b[0] = -10 -> b =", b)
    print("the original a also changed: a =", a)


# ---------------------------------------------------------------------------
# 5. Multidimensional arrays
# ---------------------------------------------------------------------------
def demo_05_multidimensional():
    section("5. Multidimensional arrays")

    # Build the 6x6 array used in the course slides.
    # reshape(-1, 1) turns [0,10,20,30,40,50] into one value per ROW (6,1),
    # then broadcasting (see section 8) adds [0,1,2,3,4,5] to every row.
    a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
    print("a =")
    print(a)

    # For 2D arrays we use a[row, column].
    # Axis 0 goes down the rows, axis 1 goes across the columns.
    print("a[0, 3:5]  =", a[0, 3:5])    # row 0, columns 3 and 4
    print("a[4:, 4:]  =")               # rows 4 and 5, columns 4 and 5
    print(a[4:, 4:])
    print("a[2::2, ::2] =")              # rows 2,4 (step 2), columns 0,2,4 (step 2)
    print(a[2::2, ::2])


# ---------------------------------------------------------------------------
# 6. ufunc and arithmetic operations
# ---------------------------------------------------------------------------
def demo_06_ufunc_arithmetic():
    section("6. ufunc and arithmetic operations")

    # ufunc = "universal function": a function applied to EVERY element
    # of an array. They are implemented in C, so they are very fast.

    x = np.linspace(0, 2 * np.pi, 5)    # 5 values from 0 to 2*pi
    print("x      =", x)
    print("np.sin(x) =", np.sin(x))     # np.sin works on the whole array

    # Arithmetic operators (+ - * / **) have ufunc equivalents.
    a = np.arange(0, 4)                 # [0, 1, 2, 3]
    b = np.arange(1, 5)                 # [1, 2, 3, 4]
    print("a =", a)
    print("b =", b)

    print("np.add(a, b)      =", np.add(a, b), "  (same as a + b)")
    print("np.subtract(a, b) =", np.subtract(a, b), "  (same as a - b)")
    print("np.multiply(a, b) =", np.multiply(a, b), "  (same as a * b)")
    print("np.divide(a, b)   =", np.divide(a, b), "  (same as a / b)")
    print("np.power(a, b)    =", np.power(a, b), "  (same as a ** b)")


# ---------------------------------------------------------------------------
# 7. Comparison operations
# ---------------------------------------------------------------------------
def demo_07_comparison():
    section("7. Comparison operations")

    # Comparing two arrays with ==, <, > ... returns a BOOLEAN array:
    # every element is the result of comparing the corresponding elements.
    a = np.array([1, 2, 3])
    b = np.array([3, 2, 1])

    print("a =", a)
    print("b =", b)
    print("a < b  ->", a < b)
    print("a == b ->", a == b)
    print("a > b  ->", a > b)

    # A boolean array can be used to filter (select) elements
    data = np.arange(10)
    print("data =", data)
    print("data[data > 5] =", data[data > 5])   # keep only values bigger than 5


# ---------------------------------------------------------------------------
# 8. Broadcasting
# ---------------------------------------------------------------------------
def demo_08_broadcasting():
    section("8. Broadcasting")

    # When two arrays have different shapes, NumPy "broadcasts" the smaller
    # one so the operation can still be done element by element.
    # Rule: each dimension is stretched up to the larger size of the two.

    a = np.arange(0, 60, 10).reshape(-1, 1)   # shape (6, 1) - a column
    b = np.arange(0, 5)                        # shape (5,)   - a row

    print("a (shape %s) =" % (a.shape,))
    print(a)
    print("b (shape %s) = %s" % (b.shape, b))

    c = a + b          # b is broadcast against every row of a -> shape (6, 5)
    print("c = a + b  (shape %s) =" % (c.shape,))
    print(c)


# ---------------------------------------------------------------------------
# 9. Random numbers
# ---------------------------------------------------------------------------
def demo_09_random():
    section("9. Random numbers")

    # np.random.seed() makes the "random" numbers reproducible:
    # with the same seed we always get the same numbers
    # (important so an experiment can be repeated exactly).
    np.random.seed(42)

    # rand() gives floats between 0 and 1
    print("np.random.rand(4, 3) =")
    print(np.random.rand(4, 3))

    # randint(low, high, size) gives random integers from low up to high-1
    a = np.random.randint(0, 10, size=(4, 5))
    print("np.random.randint(0, 10, size=(4, 5)) =")
    print(a)

    return a   # reused in the statistics section


# ---------------------------------------------------------------------------
# 10. Statistics: sum, mean, variance, standard deviation
# ---------------------------------------------------------------------------
def demo_10_statistics(a):
    section("10. Statistics: sum, mean, variance, standard deviation")

    print("a =")
    print(a)

    # Statistics of the WHOLE array
    print("np.sum(a)  =", np.sum(a))    # sum of all elements
    print("np.mean(a) =", np.mean(a))   # average of all elements
    print("np.var(a)  =", np.var(a))    # variance (how spread out the data is)
    print("np.std(a)  =", np.std(a))    # standard deviation (sqrt of variance)

    print()

    # The axis parameter chooses the direction of the calculation:
    #   axis=0 -> calculate down each COLUMN (result has one value per column)
    #   axis=1 -> calculate across each ROW   (result has one value per row)
    print("np.sum(a, axis=0)  =", np.sum(a, axis=0))   # sum of each column
    print("np.sum(a, axis=1)  =", np.sum(a, axis=1))   # sum of each row
    print("np.mean(a, axis=1) =", np.mean(a, axis=1))  # average of each row


# ---------------------------------------------------------------------------
# 11. Sorting and statistical functions
# ---------------------------------------------------------------------------
def demo_11_sorting(a):
    section("11. Sorting and statistical functions")

    print("a =")
    print(a)

    # np.sort() returns a NEW sorted array (the original is not changed)
    print("np.sort(a) =")               # default: sort every row
    print(np.sort(a))

    print("np.sort(a, axis=0) =")       # axis=0: sort every column
    print(np.sort(a, axis=0))

    # Other simple statistical functions
    print("np.min(a)    =", np.min(a))      # smallest value
    print("np.max(a)    =", np.max(a))      # largest value
    print("np.ptp(a)    =", np.ptp(a))      # range = max - min
    print("np.median(a) =", np.median(a))   # median (middle value)

    # np.unique() returns the sorted, distinct values of an array
    values = np.array([6, 3, 4, 6, 2, 7, 4, 4, 6, 1])
    print("values =", values)
    print("np.unique(values) =", np.unique(values))


# ---------------------------------------------------------------------------
# 12. vstack, hstack, column_stack, split
# ---------------------------------------------------------------------------
def demo_12_stacking_split():
    section("12. vstack, hstack, column_stack, split")

    a = np.arange(3)           # [0, 1, 2]
    b = np.arange(10, 13)      # [10, 11, 12]
    print("a =", a)
    print("b =", b)

    # vstack: stack arrays VERTICALLY (as rows, one under the other)
    v = np.vstack((a, b))
    print("np.vstack((a, b)) =")
    print(v)

    # hstack: stack arrays HORIZONTALLY (one after another)
    h = np.hstack((a, b))
    print("np.hstack((a, b)) =", h)

    # column_stack: join 1D arrays as COLUMNS of a 2D array
    c = np.column_stack((a, b))
    print("np.column_stack((a, b)) =")
    print(c)

    # split() cuts one array into several parts.
    # np.split(a, 2) -> split into 2 equal parts
    data = np.array([6, 3, 7, 4, 6, 9, 2, 6, 7, 4, 3, 7])
    print("data =", data)
    print("np.split(data, 2) ->")
    print(np.split(data, 2))

    # np.split(data, positions) -> split BEFORE each given index
    print("np.split(data, [3, 6]) ->")
    print(np.split(data, [3, 6]))


# ---------------------------------------------------------------------------
# Main program: run all demo sections in order
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    demo_01_overview()
    demo_02_array_creation()
    demo_03_ndarray_attributes()
    demo_04_slicing()
    demo_05_multidimensional()
    demo_06_ufunc_arithmetic()
    demo_07_comparison()
    demo_08_broadcasting()
    random_array = demo_09_random()      # keep the array for sections 10-11
    demo_10_statistics(random_array)
    demo_11_sorting(random_array)
    demo_12_stacking_split()
    print()
    print("NumPy experiment finished.")
