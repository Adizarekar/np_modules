import numpy as np

a = np.array([3,4,6,7,9])
print(a[0:2])

b= np.array([[2,3,4],[3,4,5],[4,5,6]])
print(b)
print(b[1,2])
print(b[-1])
print(b[-1,0:2])
print(b[:,0:2])

for row in b:
    print(row)

for cell in b.flat:
    print(cell)

a = np.arange(6).reshape(3,2)
print(a)
b = np.arange(6,12).reshape(3,2)
print(b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

a = np.arange(30).reshape(2,15)
print(a)

result = np.hsplit(a,3)
print(result[0])
print(result[1])
print(result[2])

result = np.vsplit(a,2)
print(result[0])
print(result[1])

a = np.arange(12).reshape(3,4)
print(a)
b = a>4
print(b)
print(a[b])
a[b] = -1
print(a)

