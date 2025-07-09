# Step 1: Store daily temperatures in a list (e.g., one week)
temperatures = [72, 85, 78, 90, 88, 76, 80]  # 7 days

# Step 2: Find the hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)
hottest_day = temperatures.index(hottest) + 1  # Day number (1-based)
coldest_day = temperatures.index(coldest) + 1

# Step 3: Calculate average and count days above average
average_temp = sum(temperatures) / len(temperatures)
days_above_average = [temp for temp in temperatures if temp > average_temp]

# Step 4: Demonstrate list slicing (e.g., weekdays vs weekend)
weekdays = temperatures[:5]
weekend = temperatures[5:]

# Step 5: Display results
print("Daily Temperatures:", temperatures)
print(f"Hottest day: Day {hottest_day} with {hottest}°F")
print(f"Coldest day: Day {coldest_day} with {coldest}°F")
print(f"Average temperature: {average_temp:.2f}°F")
print(f"Number of days above average: {len(days_above_average)}")

print("\nList Slicing:")
print("Weekdays (Mon–Fri):", weekdays)
print("Weekend (Sat–Sun):", weekend)
