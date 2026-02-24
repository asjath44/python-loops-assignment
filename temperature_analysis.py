# Name: Asjath Ahamed
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

max_temp = temperatures[0]
min_temp = temperatures[0]

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
    if temp < min_temp:
        min_temp = temp

print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp > 30:
        hot_days += 1

print("Number of Hot Days (>30°C):", hot_days)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days_before_alert = 0

for day in range(len(temperatures)):
    temp = temperatures[day]

    if temp >= 40:
        print("ALERT! Temperature reached", temp, "°C on Day", day + 1)
        break

    if temp > 30:
        hot_days_before_alert += 1

print("Hot days before alert (>30°C):", hot_days_before_alert)
