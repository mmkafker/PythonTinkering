# Read and write from numpy arrays to binary file.

import numpy as np

testfile2 = open("a.cwr","rb")
val = np.frombuffer(testfile2.read(8),dtype=np.double) # Read one double
print(f"val = {val}")
testfile2.close()
