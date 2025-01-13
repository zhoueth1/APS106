rps = {
  'r': 's',
  'p': 'r',
  's': 'p'
}

p1_choice = input()
p2_choice = input()

if (rps[p1_choice] == p2_choice):
  print(p1_choice, 'wins')
else:
  if (rps[p2_choice] == p1_choice):
    print(p2_choice, 'wins')
  else:
    print('tie')
