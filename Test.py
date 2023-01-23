import ctypes

libc = ctypes.CDLL('/text.a')

libc.example_function.argtypes = [ctypes.c_int]
libc.example_function.restype = ctypes.c_int

result = libc.example_function(5)

print(result)