@@ -0,0 +1,28 @@
"""
import numpy as np
matrix = np.identity(4, dtype=int)
print(matrix)
"""
import numpy as np
a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 3))
print(a)
print(b)
print("Addition:",a + b)
print("Multiplication:",a @ b)
"""
#(5×3) × (3×2)
import numpy as np
a = []
b = []
for i in range(5):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(3):
    row = list(map(int, input().split()))
    b.append(row)
a = np.array(a)
b = np.array(b)
c = a @ b
print(c)
"""
