# Jackson - Advanced Visuals

import matplotlib.pyplot as plt

# THIS IS FOR PRINTING LINE GRAPHS, remove the # and run this file if you want to see what its like
# When you use this when they X out of the program it will continue running your code
# plot([1, 2, 3, 4, 5],[2, 4, 1, 3, 5],"x axis title","y axis title","title") 
def plot(x_list, y_list, x_title, y_title, plot_title):
    plt.plot(x_list, y_list) # Creates Plot
    plt.xlabel(x_title) # Sets labels/title
    plt.ylabel(y_title)
    plt.title(plot_title)
    plt.show() #shows plot

