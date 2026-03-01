import matplotlib.pyplot as plt
#sample data
categories = [1, 2, 3, 4, 5]
values = [10, 24, 36, 40, 5]
#creating the bar graph     
plt.bar(categories, values, color ='maroon', width = 0.4)
#adding title and labels
plt.title("Simple Bar Graph")
plt.xlabel("Categories")    
plt.ylabel("Values")
#show grid 
plt.grid()  
#display the plot
plt.show()