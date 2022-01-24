import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

subject_number = "05"
x_edge = 304
y_edge = 115

M1 = pd.read_csv(f"J:/The_Hard_Drive/Processed_Video/Tracked_Data/U{subject_number}M1_track.csv")
M7 = pd.read_csv(f'J:/The_Hard_Drive/Processed_Video/Tracked_Data/U{subject_number}M7_track.csv')
M13 = pd.read_csv(f'J:/The_Hard_Drive/Processed_Video/Tracked_Data/U{subject_number}M13_track.csv')

x1 = M1['x_position']
y1 = M1['y_position']

x7 = M7['x_position']
y7 = M7['y_position']

x13 = M13['x_position']
y13 = M13['y_position']

color_weight1 = np.arange(0, len(x1))
color_weight7 = np.arange(0, len(x7))
color_weight13 = np.arange(0, len(x13))

plt.xlim(0, 1600)
plt.ylim(0, 600)
plt.scatter(x1 - x_edge, 1080 - y1 - y_edge, c=color_weight1, cmap='winter', s=8)
plt.title(f'U{subject_number}M1')
plt.show()

plt.xlim(0, 1600)
plt.ylim(0, 600)
plt.scatter(x7 - x_edge, 1080 - y7 - y_edge, c=color_weight7, cmap='winter', s=8)
plt.title(f'U{subject_number}M7')
plt.show()

plt.xlim(0, 1600)
plt.ylim(0, 600)
plt.scatter(x13 - x_edge, 1080 - y13 - y_edge, c=color_weight13, cmap='winter', s=8)
plt.title(f'U{subject_number}M13')
plt.show()

plt.xlim(0, 1600)
plt.ylim(0, 600)
plt.scatter(x1 - x_edge, 1080 - y1 - y_edge, c=color_weight1, cmap='Blues', s=8)
plt.scatter(x7 - x_edge, 1080 - y7 - y_edge, c=color_weight7, cmap='Greens', s=8)
plt.scatter(x13 - x_edge, 1080 - y13 - y_edge, c=color_weight13, cmap='Reds', s=8)
plt.title(f'U{subject_number}')
plt.show()



