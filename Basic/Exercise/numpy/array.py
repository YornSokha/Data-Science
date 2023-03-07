import matplotlib.pyplot as plt 
import numpy as np
n = 50
x = np.random.rand(n)
plt.hist(x, color="blue")
plt.title("A Sample Histogram")
plt.show()
