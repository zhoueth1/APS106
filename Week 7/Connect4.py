import random

def empty_space(board, column):
  for i in range(6):
    if board[column - 1][i] == ' ':
      return i


def make_move(board, current_color, column):
  """
  (list(list), str, int) -> Bool
  """
  column_count = 0
  for j in range(6):
    if board[column - 1][j] != ' ':
      column_count += 1

  if column_count >= 6:
    return False
    
  if empty_space(board, column) != None:
    board[column - 1][empty_space(board,column)] = current_color

  return True


def check_win(board, current_colour):
  """
  (list(list), str) -> Bool
  """
  for row in board:
    acc = 0
    for item in row:
      if item == current_color:
        acc += 1
      else:
        acc = 0

    return acc == 4
  
  for i in range(6):
    acc = 0
    for j in range(7):
      if board[j][i] == current_color:
        acc += 1
      else:
        acc = 0
    
    return acc == 4
  

  return False

def visualize(board):
  for i in range(5,-1,-1):
    print(
      i + 1, '|', board[0][i], 
      '|', board[1][i], 
      '|', board[2][i], 
      '|', board[3][i], 
      '|', board[4][i], 
      '|', board[5][i], 
      '|', board[6][i], '|'
      )


board = [[' ']*6 for i in range(7)]
current_color = 'X' if random.randint(1,2) else 'O'

print('Current color is:', current_color)
visualize(board)
make_move(board, current_color, int(input("What column? (1-7): ")))

while not check_win(board, current_color):
  #main game loop
  current_color = 'X' if current_color == 'O' else 'O'
  print('Current color is:', current_color)
  visualize(board)
  make_move(board, current_color, int(input("What column? (1-7): ")))

print(current_color, 'wins')

