# Jackson - Advanced Visuals

import matplotlib.pyplot as plt

# THIS IS FOR PRINTING LINE GRAPHS, remove the # and run this file if you want to see what its like
# When you use this when they X out of the program it will continue running your code
# The first and second lists are the x and y points so you can create any graph that you want too
def plot(x_list, y_list, x_title, y_title, plot_title):
    plt.plot(x_list, y_list) # Creates Plot
    plt.xlabel(x_title) # Sets labels/title
    plt.ylabel(y_title)
    plt.title(plot_title)
    plt.show() #shows plot

#plot([1, 2, 3, 4, 5],[2, 4, 1, 3, 5],"x axis title","y axis title","title") # Test Graph


# This is for printing PIE CHARTS, you do the sizes of each slice, the labels, colors, and the title of the graph all in respective order
def pie(sizes, labels, colors, title):
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title(title) # Sets the title
    plt.show()

#pie([25, 30, 15, 10, 20],['A', 'B', 'C', 'D', 'E'],['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange'],"Test Title") # Test Graph
