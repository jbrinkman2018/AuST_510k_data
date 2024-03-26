# Class that graphs the 510k data ENTERPRISE

# Jared Brinkman
# 3-26-24

import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, dataEntries):
        self.data = dataEntries
    
    def barGraph(self, categories, values):
        print("we are graphing")
        plt.bar(categories,values)
        plt.xlabel('xaxis')
        plt.ylabel('yaxis')
        plt.title('Example Plot')
        
        # Show the plot
        plt.show()