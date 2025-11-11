# Name: Karnav Tomar
# Date: 9/11/2025
# Project: Daily Calorie Tracker

print("Welcome to Daily Calorie Tracker!")
print("This simple app helps you track your daily meals and calories.\n")

# ----- Task 2 -----
meals = []
calories = []

n = int(input("How many meals did you have today? "))

for i in range(n):
    meal = input(f"Enter meal {i+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)

# ----- Task 3 -----
total_cal = sum(calories)
avg_cal = total_cal / len(calories)

limit = float(input("\nEnter your daily calorie limit: "))

# ----- Task 4 -----
if total_cal > limit:
    print("\n⚠️ You have exceeded your daily calorie limit!")
else:
    print("\n✅ You are within your daily calorie limit!")

# ----- Task 5 -----
print("\n------ Calorie Summary ------")
print("Meal Name\tCalories")
print("-----------------------------")

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("-----------------------------")
print(f"Total:\t\t{total_cal}")
print(f"Average:\t{avg_cal:.2f}")

# ----- Task 6 (Bonus) -----
save = input("\nDo you want to save this report to file? (yes/no): ")

if save.lower() == "yes":
    with open("calorie_log.txt", "w") as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write("-----------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]}\t{calories[i]}\n")
        file.write("-----------------------------\n")
        file.write(f"Total: {total_cal}\n")
        file.write(f"Average: {avg_cal:.2f}\n")
        if total_cal > limit:
            file.write("Status: Limit Exceeded\n")
        else:
            file.write("Status: Within Limit\n")
    print("Report saved successfully!")
else:
    print("Report not saved.")
