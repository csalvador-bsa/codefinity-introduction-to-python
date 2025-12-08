# Step 1: Initialize Lists
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# Step 2: Create Main List
deli_dept = [meat, cheese, condiment]

# Output initial state
print(f"Initial Deli List: {deli_dept}")

# Step 3: Restock Item
if meat[0] == "Ham" and meat[2] < 100:
    meat[2] = 100

# Step 4: Add Seasonal Meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# Step 5: Remove Condiment
deli_dept.remove(condiment)

# Step 6: Sort List Alphabetically by First Element
deli_dept.sort(key=lambda x: x[0])

# Output updated state
print(f"Updated Deli List: {deli_dept}")