import Change_angle

initial_velocity = float(input('Enter Initial Velocity : '))

time_taken = float(input('Enter time taken : '))

# x is displacement in horizontal direction
# y is displacement in vertical direction
 
x = float(initial_velocity * time_taken)

g = 9.80665

first_term = (x * Change_angle.tangent)
second_term = ((g * pow(x, 2)) / (2 * pow(initial_velocity, 2) * pow(Change_angle.cosine, 2)))

y = first_term - second_term

print(y)