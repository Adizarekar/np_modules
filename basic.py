import numpy as np

a = np.array([1,2,3,4,5])
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.shape)

a= np.array([[1,2],[3,4]],dtype="float64")
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.shape)

b=np.zeros((3,4))
print(b)

c = np.ones((3,4))
print(c)

d  = np.linspace(1,10,20)
print(d)

e = np.array([[1,2,3],[4,5,6]])
print(e)
print(e.shape)
f = e.reshape(3,2)
print(f)
print(f.shape)

g = e.ravel()
print(g)

print(e.min())
print(e.max())
print(e.sum())
print(e.sum(axis=0))
print(e.sum(axis=1))
print(np.sqrt(e))
print(np.std(e))



