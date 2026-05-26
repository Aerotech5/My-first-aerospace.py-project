import numpy as np

#Create matrices for aircraft inertia properties
# Moment of inertia tensor (Kg*m^2)
I_xx = 12000 # Roll inertia 
I_yy = 54000 # Pitch inertia
I_zz = 63000 # Yaw inertia

inertia_matrix = np.array([
    [I_xx, 0,      0],
    [0,     I_yy,   0],
    [0,      0,      I_zz]
])

print("Inertia Matrix:")
print(inertia_matrix)

# Create mass matrix
mass_matrix = np.array([
    [45000, 0, 0],
    [0, 45000, 0],
    [0, 0, 45000]
])

# Matrix addition 
combined = inertia_matrix + mass_matrix
print("combined Matrix:")
print(combined)

# Matrix multiplication
result = np.dot(inertia_matrix, mass_matrix)
print(result)

# Transpose 
print("Transpose of inertia Matrix:")
print(inertia_matrix.T)

# Element-wise operations
scaled = inertia_matrix * 2
print("Scaled Inertia Matrix (x2):")