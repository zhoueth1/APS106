beats = {
    'rock': 'scissors lizard',
    'paper': 'rock spock',
    'scissors': 'paper lizard',
    'lizard': 'spock paper',
    'spock': 'scissors rock'
}

player1 = input('Player 1: ')
player2 = input('Player 2: ')

if player1 == player2:
  print('Tie')
else:
  if player2 in beats[player1]:
    print('Player 1 wins')
  else:
    print('Player 2 wins')