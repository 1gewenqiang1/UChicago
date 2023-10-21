# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:34:58 2023

@author: gewq8
"""

# Find this code on my GitHub: https://github.rpi.edu/gew/Wenqiang_Ge_DS-Supplement.git

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

state=input('Hello, which state do you wanna know about its urban coverage? ')
print('\nI will let you know about',state+"'s stcd and cd.\n")

# Ingest data from a CSV file
data = pd.read_csv('urbanization-index-2022.csv')

# Manage different data types
numeric_data = data.select_dtypes(include=['int64','float64'])
categorical_data = data.select_dtypes(include=['object'])

# Get the numbers of rows and columns of each dataset
def get_shape(data):
    df = pd.DataFrame(data)
    shape=df.shape 
    return(shape)
print('The numerical_data has',get_shape(numeric_data)[0],'rows and',
          get_shape(numeric_data)[1],'columns.\n'+
          '\nThe categorical_data has',get_shape(categorical_data)[0],'rows and',
          get_shape(categorical_data)[1],'columns.')

# Define a function for data analysis
def analyze_data(data):
    summary = data.describe()
    correlation_matrix = data.corr()
    return summary, correlation_matrix

# Wrangle data (drop rows with missing values)
data_cleaned = data.dropna()

#Write my own function to visualize
def plot_and_save(state):
    NY_stcd=list()
    NY_cd=list()
    for i in range(len(list(data['state']))):
        if list(data['state'])[i]==str(state):
            NY_cd.insert(i, list(data['cd'])[i])
            NY_stcd.insert(i, list(data['stcd'])[i])
            
    # Visualize data       
    plt.figure(figsize=(10, 8))
    plt.scatter(NY_stcd, NY_cd)
    plt.title('Scatter Plot of stcd vs cd in '+str(state))
    plt.xlabel('stcd')
    plt.ylabel('cd')
    plt.show()

plot_and_save(state)