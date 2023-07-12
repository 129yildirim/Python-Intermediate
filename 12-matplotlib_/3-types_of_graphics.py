import matplotlib.pyplot as plt

#-------------stack---------------
"""
year = [2012, 2013, 2014, 2015, 2016]

player1 = [8, 15, 60, 48, 12]
player2 = [12, 13, 16, 32, 15]
player3 = [9, 20, 30, 12, 20]

plt.plot([], [], color="r", label="play1")
plt.plot([], [], color="g", label="play2")
plt.plot([], [], color="b", label="play3")

plt.stackplot(year, player1, player2, player3, colors=['r', 'g', 'b'])
plt.title('My title')
plt.legend()
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()
"""

#------------------pie--------------------
"""
types= ['Type1', 'Type2', 'Type3']
nums = [64, 32, 76]
colors = ['r', 'g', 'b']
#plt.pie(nums, labels=types, colors=colors)
#plt.pie(nums, labels=types, colors=colors, shadow=True)
#plt.pie(nums, labels=types, colors=colors, shadow=True, explode=(0.05, 0.05, 0.05))
plt.pie(nums, labels=types, colors=colors, shadow=True, explode=(0.05, 0.05, 0.05), autopct='%1.1f%%')

plt.show()
"""

#------------------bar----------------
"""
plt.bar([-0.25, 0.70, 1.55, 2, 3], [50, 30, 60, 10, 40], label="BMW")
plt.bar([-0.5, 0.5, 1.5, 2.5, 3.5], [70, 10, 50, 30, 30], label="Audi")

plt.legend()
plt.xlabel('Day')
plt.ylabel('Distance (km)')
plt.title('Vehicles Features')

plt.show()
"""
#------------------hist-------------
ages = [22, 28, 55, 60, 47, 21, 64, 71, 86, 12, 4, 8, 32, 34, 39, 36]
age_groups= [0, 10, 20, 30, 40, 50, 60, 70, 80]

plt.hist(ages, age_groups, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('num of ages')
plt.title('My Hist')

plt.show()