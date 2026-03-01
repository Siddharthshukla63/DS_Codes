import matplotlib.pyplot as plt 
import numpy as np 
#sample data 
x = np.array([1,2,3,4,5])
y =np.array([10,20,25,30,40])
#creating the line plot 
plt.plot(x,y,marker = 'o', color = 'b')
#adding title and labels 
plt.title("Simple Line Plot")       
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
#show grid
plt.grid()
#display the plot
plt.show()