import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
def f1(x):
    return x**2
def f2(x):
    return x**3
def f3(x):
    return x/2
def f4(x):
    if x < 0:
        return f1(x)
    else:
        return f3(x)

fig, axs = plt.subplots(2, 2)

xs = []
for i in range(-10, 11):
    xs.append(i)
f1_ys = []
for x in xs:
    f1_ys.append(f1(x))


axs[0, 0].plot(np.array(xs),np.array(f1_ys))
axs[0, 0].set_title('Axis [0, 0]')


f2_ys = []
for x in xs:
    f2_ys.append(f2(x))
axs[0, 1].plot(np.array(xs), np.array(f2_ys), 'tab:orange')
axs[0, 1].set_title('Axis [0, 1]')


f3_ys = []
for x in xs:
    f3_ys.append(f3(x))
axs[1, 0].plot(np.array(xs), np.array(f3_ys), 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')



f4_ys = []
for x in xs:
    f4_ys.append(f4(x))
axs[1, 1].plot(np.array(xs), np.array(f4_ys), 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.savefig("subplots.png")

plt.show()