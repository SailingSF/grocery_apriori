# Apiori
"""
Created on Thu Mar 14 11:55:55 2019

@author: maxab
"""

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
# Converting dataset to list of lists for each transaction
transactions = []
for i in range(len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(len(dataset.columns))])

# Training Apriori
from apyori import apriori
rules = apriori(transactions, min_support = 0.004, min_confidence = 0.2, min_lift = 3.0, min_length = 2)

# Visualizing the results
results = list(rules)

clean_results = []
for i in range(0, len(results)):
    result_dict = dict()
    result_dict["RULE"] = list(results[i][0])
    result_dict["SUPPORT"] = results[i][1]
    result_dict["CONFIDENCE"] = results[i][2][0][2]
    result_dict["LIFT"] = results[i][2][0][3]
    
    clean_results.append(result_dict)