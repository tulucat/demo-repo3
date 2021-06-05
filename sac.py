# Yi Xin Tan
# 26May2021
# Applied Computing SAC

# display to get user input for name
print('What is your name?')
UserName = input()

# calculate name length
length = len(UserName)

# display name and name length
print(f'Hello, {UserName}!')
print(f'Username length: {length}')

# display to get favourite traffic light colour
print('What is your favourite traffic light colour?')
colour = input().title()

if colour == 'Red':
    # if favourite colour is 'Red'
    print('Red means stop!')
elif colour == 'Yellow':
    # if favourite colour is 'Yellow'
    print('Yellow means stop unless it is unsafe to do so.')
elif colour == 'Green':
    # if favourite colour is 'Green'
    print('Green means GO!')
else:
    # if no matching case, display invalid input
    print('Unknown traffic light colour')