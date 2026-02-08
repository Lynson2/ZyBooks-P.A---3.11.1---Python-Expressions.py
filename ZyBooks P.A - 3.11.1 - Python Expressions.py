G = 6.673e-11
M = 5.98e+24

d = float(input("Enter distance in meters from the Earth's center: "))
d **= 2
a = (G * M)/d

print(f"Gravity acceleration: {a:.2f}")
