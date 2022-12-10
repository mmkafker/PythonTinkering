# Read and write from numpy arrays to binary file.

import numpy as np

x = np.array([i**(-0.5) for i in range(1,10)])
y = np.array([i**2. for i in range(1,10)])

import struct
import numpy as np
testfile = open("write_test.cwr","wb")
testfile.write(x)
testfile.write(y)
testfile.close()


testfile2 = open("write_test.cwr","rb")
for k in range(len(x)+len(y)):
    testfile2.seek(8*k)
    val = np.frombuffer(testfile2.read(8),dtype=np.double) # Read one double
    print(f"k = {k}, element k = {val}")
testfile2.close()
