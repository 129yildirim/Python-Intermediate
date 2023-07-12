import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#---------1-----------
"""
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
#plt.plot(x, y, color="red", linewidth="5")
#plt.plot(x, y, "-g")
#plt.plot(x, y, "--g")
#plt.plot(x, y, "o--g")
plt.plot(x, y, "o--r")
plt.axis([0, 6, 0, 20])
plt.title('This Is My Title')
"""

#--------2-------------
"""
x = np.linspace(0, 2, 100)
#plt.plot(x, x, label="linear")
plt.plot(x, x, label="linear", color="red")
#plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**2, label="quadratic", color="green")
#plt.plot(x, x**3, label="cubic")
plt.plot(x, x**3, label="cubic", color="blue")

plt.xlabel('x label')
plt.ylabel('y label')

plt.legend()

plt.title("Simple Plot")

plt.show()
"""

#--------------3-------------
"""
x = np.linspace(0, 2, 100)

fig, axs = plt.subplots(3)

axs[0].plot(x, x, color="red")
axs[0].set_title('Linear')
axs[1].plot(x, x**2, color="green")
axs[1].set_title('Quadratic')
axs[2].plot(x, x**3, color="blue")
axs[2].set_title('Cubic')

plt.tight_layout()

plt.show()
"""
#-------------4-------------
"""
x = np.linspace(0, 2, 100)
fig, axs = plt.subplots(2, 2)
fig.suptitle('Graphic Title')

axs[0, 0].plot(x, x, color="red")
axs[0, 1].plot(x, x**2, color="orange")
axs[1, 0].plot(x, x**3, color="blue")
axs[1, 1].plot(x, x**3, color="green")

plt.show()
"""

df = pd.read_excel('excel_sample.xlsx')
df = df.groupby('Country')[['Age', 'Id']].mean()

df.plot(subplots=True)

plt.legend()
plt.show()

