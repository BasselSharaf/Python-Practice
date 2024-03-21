names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1


# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)


# The best pythonic approach
best_list = [name for name in names if len(name) >= 6]


# range() function
# Returns a range object
nums = range(0,11) 
nums_list = list(nums) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums_list = [*range(0,15,2)] # [0, 2, 4, 6, 8, 10, 12, 14]


# enumerate() function
letters = ['a','b','c','d']
indexed_letters = enumerate(letters) 
indexed_letters_list = list(indexed_letters) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

indexed_letters2 = enumerate(letters, start=2) 
indexed_letters_list2 = list(indexed_letters2) # [(2, 'a'), (3, 'b'), (4, 'c'), (5, 'd')]

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)



# map() function

nums = [1.5, 2.3, 3.4, 4.6, 5.0]
rnd_nums = map(round, nums)
rnd_nums_list = list(rnd_nums) # [2, 2, 3, 5, 5]

# map() iwth lambda
nums = [1,2,3,4,5]
sqrd_nums = map(lambda x: x**2,nums)
sqrd_nums_list = list(sqrd_nums) # [1, 4, 9, 16, 25]
print(sqrd_nums_list)
