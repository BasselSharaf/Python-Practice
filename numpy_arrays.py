import numpy as np

# NumPy array are homogenious
nums_np_ints = np.array(range(5))
nums_np_ints.dtype #int32

nums_np_floats = np.array([[1,2.5,3],[4,6,7],[7,23,543]])
nums_np_floats.dtype # float64
nums_np_floats #[1.  2.5 3. ]



def welcome_guest(elm):
    return f'Welcome to Festivus {elm[0]}... You\'re {elm[1]} min late.'

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]


# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

