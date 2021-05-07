from matplotlib import pylot as plt
import seaborn as sns
import numpy as np
import pandas as pd 


# Barplot with Seaborn
sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value', ci='sd')

# KDE Plots (Kernel Density Estimator)
sns.kdeplot(dataset, shade=True)

# Box plots
sns.boxplot(data=df, x='label', y='value')

# Violin plots
sns.violinplot(data=df, x='label', y='value')

# Built-in themes
sns.set_style("dark") # Change background and grids
sns.set_style("ticks") # Add ticks
sns.despine(#left=True, bottom=True) # Usage of spines

# Presets figure styles for differents mediums
sns.set_context('paper/notebok/talk/poster', font_scale=.5, rc={'grid.linewidth':0.6})

# RC Paremeter (run command)
{'axes.labelsize': 17.6,
 'axes.titlesize': 19.200000000000003,
 'font.size': 19.200000000000003,
 'grid.linewidth': 1.6,
 'legend.fontsize': 16.0,
 'lines.linewidth': 2.8000000000000003,
 'lines.markeredgewidth': 0.0,
 'lines.markersize': 11.200000000000001,
 'patch.linewidth': 0.48,
 'xtick.labelsize': 16.0,
 'xtick.major.pad': 11.200000000000001,
 'xtick.major.width': 1.6,
 'xtick.minor.width': 0.8,
 'ytick.labelsize': 16.0,
 'ytick.major.pad': 11.200000000000001,
 'ytick.major.width': 1.6,
 'ytick.minor.width': 0.8}



# Save a palette to a variable:
palette = sns.color_palette("bright") # deep, muted, pastel, bright, dark, colorblind.  

# Use palplot and pass in the variable:
sns.palplot(palette)

# Set the palette using the name of a palette:
sns.set_palette("Paired") 

# Plot a chart:
sns.stripplot(x="day", y="total_bill", data=tips)

# Color brewer
custom_palette = sns.color_palette("Paired", 9)
sns.palplot(custom_palette)

qualitative_colors = sns.color_palette("Set3", 10)
sns.palplot(qualitative_colors)

sequential_colors = sns.color_palette("RdPu", 10)
sns.palplot(sequential_colors)

diverging_colors = sns.color_palette("RdBu", 10)
sns.palplot(diverging_colors)

https://seaborn.pydata.org/tutorial/color_palettes.html?highlight=color