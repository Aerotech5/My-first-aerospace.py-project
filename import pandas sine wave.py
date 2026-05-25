import pandas as pd

# Aircraft data
data = {
    "Aircraft":["Boeing 737","Airbus A320","Cassna 172"],
    "Speed_km_h":[850, 830, 226],
    "Fuel_l_per_hr":[2400, 2200, 36]
}
#Create DataFrame
df = pd.DataFrame(data)

# Calculate efficiency
df["Efficiency"] = df["Speed_km_h"] / df["Fuel_l_per_hr"]

#print results
print(df)