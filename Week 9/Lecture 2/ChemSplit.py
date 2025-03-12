def molecule_formula(compound_formula):

  # List of beginning indices where type changes happen (ex. "C6" -> 0)
  # It begins at -1, as python splicing is kinda wacky and this is a hacky way to make it work
  split_beginning_indices = [-1] 

  # Looping through the string
  for i in range(1, len(compound_formula)):

    # If the previous character is a letter, and the next is a number
    if compound_formula[i-1].isalpha() and compound_formula[i].isnumeric():
      # Append previous character index to the list
      split_beginning_indices.append(i-1)

    # Else if the previous character is a number, and the next is a letter
    elif compound_formula[i-1].isnumeric() and compound_formula[i].isalpha():
      #Append previous character index to the list
      split_beginning_indices.append(i-1)
    
  # Append the last possible index of string to the end of the list
  split_beginning_indices.append(len(compound_formula) - 1)

  # print(split_beginning_indices)

  # Strings split into letters and numbers
  split_strings = [] # -> ['Element', 'Number', 'Element', 'Number']

  # Loop through the list of indices
  for i in range(1,len(split_beginning_indices)):

    # Append to list of letters and numbers the sliced string according to list of indices
    split_strings.append(
      compound_formula[
        split_beginning_indices[i-1] + 1: # The +1 here is why we started with -1 in the list
        split_beginning_indices[i] + 1
      ]
    )

  # Initiate return dictionary
  result = {}

  # Loop through the list of split strings, jump by 2 indices
  for i in range(1 ,len(split_strings), 2):
      
      # If the current element is not already in the dictionary
      if split_strings[i-1] not in result:
          result[split_strings[i-1]] = int(split_strings[i])

      # If the current element is already in the dictionary, add the number
      else:
          result[split_strings[i-1]] += int(split_strings[i])
  
  return result



print(molecule_formula('C622H2G6'))


