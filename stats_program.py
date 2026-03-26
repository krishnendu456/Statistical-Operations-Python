import statistics

# Input data
data = [10, 20, 30, 40, 50, 20, 30]

print("Data:", data)

# Mean
mean_value = statistics.mean(data)
print("Mean:", mean_value)

# Median
median_value = statistics.median(data)
print("Median:", median_value)

# Mode
try:
    mode_value = statistics.mode(data)
    print("Mode:", mode_value)
except statistics.StatisticsError:
    print("Mode: No unique mode found")

# Variance
variance_value = statistics.variance(data)
print("Variance:", variance_value)

# Standard Deviation
std_dev = statistics.stdev(data)
print("Standard Deviation:", std_dev)