import numpy as np
import pandas as pd

subject_number = "01"
#01
x_edge1 = 14
y_edge1 = 118
#07
x_edge7 = 7
y_edge7 = 113
#13
x_edge13 = 4
y_edge13 = 113

#01
x_stone1 = 175 - x_edge1
y_stone1 = 1080 - 451 - y_edge1
#07
x_stone7 = 175 - x_edge7
y_stone7 = 1080 - 451 - y_edge7
#13
x_stone13 = 163 - x_edge13
y_stone13 = 1080 - 465 - y_edge13

M1 = pd.read_csv(f"J:/The_Hard_Drive/Processed_Video/Tracked_Data/U{subject_number}M1_track.csv")
M7 = pd.read_csv(f'J:/The_Hard_Drive/Processed_Video/Tracked_Data/U{subject_number}M7_track.csv')
M13 = pd.read_csv(f'J:/The_Hard_Drive/Processed_Video/Tracked_Data/U{subject_number}M13_track.csv')

x1 = np.array(M1['x_position'] - x_edge1)
y1 = np.array(1080 - M1['y_position'] - y_edge1)

x7 = np.array(M7['x_position'] - x_edge7)
y7 = np.array(1080 - M7['y_position'] - y_edge7)

x13 = np.array(M13['x_position'] - x_edge13)
y13 = np.array(1080 - M13['y_position'] - y_edge13)

# When resolution is 720P
# #01
# x_stone1 = x_stone1 * 1.5
# y_stone1 = y_stone1 * 1.5
# x1 = x1 * 1.5
# y1 = y1 * 1.5
# #07
# x_stone7 = x_stone7 * 1.5
# y_stone7 = y_stone7 * 1.5
# x7 = x7 * 1.5
# y7 = y7 * 1.5
# #13
# x_stone13 = x_stone13 * 1.5
# y_stone13 = y_stone13 * 1.5
# x13 = x13 * 1.5
# y13 = y13 * 1.5
#
# # Calculate Best Distance
# best_distance1 = 0
# best_distance7 = 0
# best_distance13 = 0

# Best Distance for M1
for i in range(0, len(x1) - 1):
    dx = x_stone1 - x1[i]
    dy = y_stone1 - y1[i]
    distance1 = np.sqrt(dx ** 2 + dy ** 2)
    best_distance1 = distance1 + best_distance1

print("Total Best distance M1 :", round(best_distance1, 2))
# Best Distance for M7
for i in range(0, len(x7) - 1):
    dx = x_stone7 - x7[i]
    dy = y_stone7 - y7[i]
    distance7 = np.sqrt(dx ** 2 + dy ** 2)
    best_distance7 = distance7 + best_distance7

print("Total Best distance M7 :", round(best_distance7, 2))

# Best Distance for M13
for i in range(0, len(x13) - 1):
    dx = x_stone13 - x13[i]
    dy = y_stone13 - y13[i]
    distance13 = np.sqrt(dx ** 2 + dy ** 2)
    best_distance13 = distance13 + best_distance13

print("Total Best distance M13 :", round(best_distance13, 2))

# Calculate Total Distance
total_distance1 = 0
total_distance7 = 0
total_distance13 = 0

# Distance for M1
distance1 = 0
for i in range(0, len(x1) - 1):
    dx = x1[i + 1] - x1[i]
    dy = y1[i + 1] - y1[i]
    distance1 = np.sqrt(dx ** 2 + dy ** 2)
    total_distance1 = total_distance1 + distance1

print("Total distance M1 :", round(total_distance1, 2))

# Distance for M7
distance7 = 0
for i in range(0, len(x7) - 1):
    dx = x7[i + 1] - x7[i]
    dy = y7[i + 1] - y7[i]
    distance7 = np.sqrt(dx ** 2 + dy ** 2)
    total_distance7 = total_distance7 + distance7

print("Total distance M7 :", round(total_distance7, 2))

# Distance for M13
distance13 = 0
for i in range(0, len(x13) - 1):
    dx = x13[i + 1] - x13[i]
    dy = y13[i + 1] - y13[i]
    distance13 = np.sqrt(dx ** 2 + dy ** 2)
    total_distance13 = total_distance13 + distance13

print("Total distance M13 :", round(total_distance13, 2))

# Calculate Total Time
# Time for M1
time1 = len(x1) / 60
print("Total time M1 :", round(time1, 2))

# Time for M7
time7 = len(x7) / 60
print("Total time M7 :", round(time7, 2))

# Time for M13
time13 = len(x13) / 60
print("Total time M13 :", round(time13, 2))
