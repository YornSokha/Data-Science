# # Import pandas package
# import pandas as pd

# # Create distinct dataframes for each column
# modelNumber_df = pd.DataFrame() 
# description_df = pd.DataFrame() 
# color_df = pd.DataFrame() 
# maxSpeed_df = pd.DataFrame() 

# # Add columns to respective dataframes
# modelNumber_df['Model Number'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10
# description_df['Description'] = ["SUV", "Sedan", "SUV", "Truck", "Convertible", "Coupe", "Minivan", "Sedan", "SUV", "Sedan"]*10
# color_df['Color'] = ['Red','Green','Blue','Yellow','Orange','White','Silver','Purple','Gray','Black']*10
# maxSpeed_df['Max Speed'] = list(range(20,200,20))*5

# # Merging all dataframes
# df = modelNumber_df.merge(description_df, left_index=True, right_index=True).merge(color_df, left_index=True, right_index=True).merge(maxSpeed_df, left_index=True, right_index=True)


# # View dataframe
# print(df.head())


import matplotlib.pyplot as plt 
  
# Creating Sample Data 
data = [2, 3, 5, 6, 8, 9, 10]
  
# Setting up the parameters for x-axis and y-axis 
bins = [0, 2, 4, 6, 8, 10] 
x = range(len(bins)-1) 
  
# Drawing the histogram from data 
plt.hist(data,bins,histtype='bar',rwidth=0.8, color =['C2']) 
    
# Setting the title, labels and ticks of the graph 
plt.title("Sample Histogram") 
plt.xlabel("Animal Age") 
plt.ylabel("Number of Animals") 
# plt.xticks(x, bins)
plt.xticks(x, bins, locs = [5]) 

  
# Displaying the plot 
plt.show() 
