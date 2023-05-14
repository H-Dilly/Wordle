def get_attempt():
  #gets a string from user and converts it to lower case for easier use later
  
  while True:
    word = (input('What word did you enter: ')).lower()
    if len(word) != 5 or not word.isalpha():
      print('ERROR: INVALID ENTRY')
      continue
    else:
      break

  #adds each word in a string to letter in order
  letters = []
  for letter in word:
    letters.append(letter)

    # because word is five characters long, can use a range for later stitching
    positions = list(range(5))

    #gets color for each letter and adds to list for later stitching
  colors = []
  for letter in letters:
    while True:
        color = input(f'Enter square color {letter}: ')
        if color not in ('yellow', 'green', 'grey'):
            print('ERROR: INVALID COLOR')
        else:
           colors.append(color)
           break


    #all three lists are stitched together into one 2d list consisiting of [letter, position, color]
  attempt = list(zip(letters, positions, colors))
  return attempt



