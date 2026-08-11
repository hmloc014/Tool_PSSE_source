import math
import numpy as np 
import matplotlib.pyplot as plt

sin_wave = np.array([math.sin(x) for x in np.arange(200)])
plt.plot(sin_wave[:50])