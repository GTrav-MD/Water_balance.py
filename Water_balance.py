# Calculate liquid intake
hydration_os = 1000
hydration_ev = 500
Glucose_solution_infusion = False
if Glucose_solution_infusion:
    H2O_met = 0
else:
    H2O_met = 300
food_intake = False
if food_intake:
    hydration_from_food = 100
else:
    hydration_from_food = 0
intake = hydration_os + hydration_ev + hydration_from_food + H2O_met
print("In")
print(intake)
# Calculate liquid loss
Diuresis = 2200
Bowel_movement = False
if Bowel_movement:
    Water_through_feces = 200
else:
    Water_through_feces = 0
Respiratory_rate = 18
if Respiratory_rate >= 20:
    Lung_perspiration = 800
else:
    Lung_perspiration = 600
Normal_sweating = True
if Normal_sweating:
    Skin_water_loss = 450
else:
    Skin_water_loss = 650
loss = Diuresis + Water_through_feces + Lung_perspiration + Skin_water_loss
print("Out")
print(loss)
# Calculate water balance
Water_balance = intake - loss
if Water_balance >= 0:
    print("POSITIVE water balance")
    print(Water_balance)
else:
    print("NEGATIVE water balance")
    print(Water_balance)
