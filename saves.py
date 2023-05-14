#get_attempt for 5.10.23

# def get_attempt():
#   #gets a string from user and converts it to lower case for easier use later
#   word = (input('What word did you enter: ')).lower()

#   #adds each word in a string to letter in order
#   letters = []
#   for letter in word:
#     letters.append(letter)

#     # because word is five characters long, can use a range for later stitching
#     positions = list(range(1, 6))

#     #gets color for each letter and adds to list for later stitching
#   colors = []
#   for letter in letters:
#     color = input(f'Enter square color {letter}: ')
#     colors.append(color)

#     #all three lists are stitched together into one 2d list consisiting of [letter, position, color]
#   attempt = list(zip(letters, positions, colors))
#   return attempt

# print(get_attempt())