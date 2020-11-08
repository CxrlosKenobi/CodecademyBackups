import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import iqr


example_array = np.array([24, 16, 30, 10, 12, 28, 38, 2, 4, 36]) # NumPy Array
csv_array = np.genfromtxt('sample.csv', delimiter=',') # Getting an array from a CSV file
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]]) # Two dimensional array with NumPy
seventy_nine = student_scores[1,0] # array[row,column]
sorted_temps = np.sort(temps) # Sorting the temp's array


example_average = np.average(example_array) # Calculates the Mean/Average of an array
example_median = np.median(example_array) # Calculates the Median of an array. Middle value of a dataset
example_mode = stats.mode(example_array) # Calculating the Mode of a dataset 
variance = np.var(dataset) # Calculates the variance of a dataset
standard_deviation = np.std(data) # Calculates the Standard Deviation of the data. Means how spread out the data is

min_age = np.amin(array)
max_age = np.amax(array)
np.histogram(exercise_ages, range = (20, 70), bins = 5)
plt.hist(exercise_ages, range = (20, 70), bins = 5, edgecolor='black')


thirtieth_percentile = np.percentile(array, 30) # 30th percentile 
seventieth_percentile = np.percentile(patrons, 70) # 70th percentile
songs_q1 = np.quantile(songs, 0.25) # First quartile of songs. It's the same that 25th percentile
songs_q2 = np.quantile(songs, 0.50) # Second quartile of songs. It's the same that the median
songs_q3 = np.quantile(songs, 0.75) # Third quartile of songs. It's the same thet 75th percentile

quartiles = np.quantile(songs, [0.25, 0.5, 0.75]) # Quartiles
deciles = np.quantile(songs, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]) # Deciles
interquartile_range = iqr(songs) # Getting the Interquartile Range. Means the difference between the 1st and 3rd quartile

'''
# Distributions on histogram
There are:

Unimodal Distribution | One peak
Bimodal Distribution | Two peaks
Multimodal Distribution | Many peaks
Uniform Distribution | No peaks at all, plain

symmetric dataset has equal amounts of data on both sides of the peak. Both sides should look about the same. 
skew-right dataset has a long tail on the right of the peak, but most of the data is on the left. 
skew-left dataset has a long tail on the left of the peak, but most of the data is on the right. 

'''
a = np.random.normal(number_of_trials, probability_of_each_event, size=numbers_to_generate)
a = np.random.normal(0, 1, size=100000)


tstat, pval = ttest_1samp(example_distribution, expected_mean)
tstat, pval = ttest_1samp(prices, 1000) # Example of  the upside



