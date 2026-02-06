temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
first_reading = temperatures[0]
last_reading = temperatures[-1]

afternoon_peak = temperatures[3:6]
last_3_hours = temperatures[-3:]
print("First Reading (Index 0):", first_reading)
print("Last Reading (Index -1):", last_reading)
print("Afternoon Peak Readings (Index 3 to 5):", afternoon_peak)
print("Last 3 Hours Readings:", last_3_hours)
