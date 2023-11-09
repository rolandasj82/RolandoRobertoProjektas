# Pabaik mano minti
u_input = input('Give me a sentence, and I will tell you the length of its first and last component >>> ')
# u_input=Let's learn with GitHub

new_list = u_input.split()
# Opt 1
fc = 0
lc = 0
i = 0
for comp in new_list:
    if i == 0:
        fc = len(comp)
    if i == len(new_list) - 1:
        lc = len(comp)
    i += 1
# Opt 2
firstcom = new_list[0]
lastcom = new_list[-1]

print(f'Option 1: The length of the first component is {len(firstcom)}, while of the the last is {len(lastcom)}')
# Option 1: The length of the first component is 5, while of the the last is 6
print(f'Option 2: The length of the first component is {fc}, while of the the last is {lc}')
# Option 2: The length of the first component is 5, while of the the last is 6
