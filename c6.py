import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
y = [1,3,2,5,4]

fig, ax = plt.subplots(2,2, figsize=(10,8))

ax[0,0].plot(x,y)
ax[0,0].set_title("Line")

ax[0,1].bar(x,y)
ax[0,1].set_title("Bar")

ax[1,0].pie([15,40,45], labels=["A","B","C"], autopct="%1.1f%%")
ax[1,0].set_title("Pie")

ax[1,1].scatter(np.random.rand(30), np.random.rand(30))
ax[1,1].set_title("Scatter")

plt.tight_layout()
plt.show()