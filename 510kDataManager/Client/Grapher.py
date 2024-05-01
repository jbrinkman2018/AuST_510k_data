# Class that graphs the 510k data ENTERPRISE

# Jared Brinkman
# 3-26-24

import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, dataEntries):
        self.data = dataEntries
    
    def barhGraph(self, category, title, xlabel, ylabel):
        print("we are graphing")
        keys = list(category.keys())
        values = list(category.values())
        plt.barh(keys, values)
        plt.xticks(rotation='vertical', fontsize = 10)
        # plt.yticks(rotation = 45, fontsize = 10)
        plt.tight_layout()
  
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        
        # Show the plot
        plt.show()
    def barGraph(self, category, title, xlabel, ylabel):
        print("we are graphing")
        keys = list(category.keys())
        values = list(category.values())
        plt.bar(keys, values)
        plt.xticks(rotation='vertical', fontsize = 10)
        plt.tight_layout()
  
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        
        # Show the plot
        plt.show()