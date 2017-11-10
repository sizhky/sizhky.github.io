
import numpy as np

f = np.column_stack
softmax = lambda x: np.exp(x-np.max(x, axis=1, keepdims=1))/np.sum(np.exp(x-np.max(x, axis=1, keepdims=1)), axis=1, keepdims=1)
###########################################################
# Circular data
# s = np.linspace(0, 2*np.pi, 50)
# x1 = np.cos(s); y1 = np.sin(s)
# x2 = 2*np.cos(s); y2 = 2*np.sin(s)
# d = np.concatenate((f((x1, y1)), f((x2, y2))), axis=0)
# X = d
# Y = np.array([[0]*50 + [1]*50])
# c = ['blue']*50+['red']*50
# model = Sequential([
# 	Dense(3, input_dim=2, activation='tanh'),
# 	Dense(2, activation='softmax')])
###########################################################
# backup weights
# m = f([[-0.0716613 , -1.84718764,  1.6533047 ],
#         [ 1.92858601,  1.01029253,  1.04533195]])
# b = f([ 1.92342341, -2.13294697, -1.99075675])
# m2 = f([[ 1.84705186, -2.24195766],
#         [-1.2809763 ,  2.78510642],
#         [-1.82382023,  2.28618288]]),
# b2 = f([-3.22734857,  3.22734928])
###########################################################
# D = list(zip(*d))
# h = np.tanh(np.matmul(d, m)+b)
# H = list(zip(*h))
# softmax = lambda x: np.exp(x-np.max(x, axis=1, keepdims=1))/np.sum(np.exp(x-np.max(x, axis=1, keepdims=1)), axis=1, keepdims=1)
# h2 = np.matmul(h, m2)+b2
# H2 = list(zip(*h2))
# o = softmax(h2)
# O = list(zip(*o))



# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = (10, 10)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(f(D[0]),f(D[1]),f([0]*100),color=c)
# plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(f(H[0]),f(H[1]),f(H[2]),color=c)
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(f(H2[0]),f(H2[1]),f([0]*100),color=c)
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(f(O[0]),f(O[1]),f([0]*100),color=c)
# plt.show()
###########################################################

###########################################################
# xor data
n = 500
d = np.array(np.random.rand(n*2)-0.5).reshape(n,2)
X = d
Y = np.product(d, axis=1) > 0
c = ['blue', 'red']
c = [c[i] for i in Y]
###########################################################
from keras.layers import Dense
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
Y = to_categorical(Y)

model = Sequential([
	Dense(3, input_dim=2, activation='relu'),
	Dense(3, input_dim=2, activation='relu'),
	Dense(2, activation='softmax')])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.fit(X, Y, epochs=1000, verbose=0)
print(model.evaluate(X, Y))


l = model.get_weights()
f = np.array
m = l[0]
b = l[1]
m2 = l[2]
b2 = l[3]
m3 = l[4]
b3 = l[5]


D = list(zip(*d))
h = np.matmul(d, m)+b
h = h*(h>0)
H = list(zip(*h))
h2 = np.matmul(h, m2)+b2
h2 = h2*(h2>0)
H2 = list(zip(*h2))
h3 = np.matmul(h2, m3)+b3
H3 = list(zip(*h3))
o = softmax(h3)
O = list(zip(*o))



from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 10)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(f(D[0]),f(D[1]),f([0]*n),color=c)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(f(H[0]),f(H[1]),f(H[2]),color=c)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(f(H2[0]),f(H2[1]),f(H2[2]),color=c)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(f(H3[0]),f(H3[1]),f([0]*n),color=c)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(f(O[0]),f(O[1]),f([0]*n),color=c)
plt.show()

