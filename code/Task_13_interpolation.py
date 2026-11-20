import numpy as np
from scipy.interpolate import interp1d

# Real-world case: Missing soil-moisture reading
# Time in hours (e.g., 0, 2, 4, 6, 8) and moisture % 
time = np.array([0, 2, 4, 6, 8])
moisture = np.array([30.5, 28.2, 25.0, 22.1, 19.5])

# Create linear interpolation function
f_linear = interp1d(time, moisture, kind='linear')

# Missing reading at hour 5
missing_time = 5
interpolated_val = f_linear(missing_time)

print(f"Interpolated soil-moisture at hour {missing_time}: {interpolated_val:.2f} %")