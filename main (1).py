def getNewBoard():
    # Creates blank board.
    global board
    board = []
    for i in range(8):
        board.append([' ']*8)
    return board

#board generation:
def drawBoard(board):
    #Printing the board.
    Horizontal = '  +---+---+---+---+---+---+---+---+'
    Vertical = '  |   |   |   |   |   |   |   |   |'

    print('    A   B   C   D   E   F   G   H')
    print(Horizontal)
    for y in range(8):
        print(Vertical)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(Vertical)
        print(Horizontal)

def resetBoard(board):
    # Fills in starting values.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    board[3][3] = board[4][4] = 'X'
    board[3][4] = board[4][3] = 'O'

def convertcolumn(columnletter):
  # Converts letter of column to number.
  global playcolumn
  uncapital = 'abcdefgh'
  if columnletter.lower() in uncapital:
    playcolumn = uncapital.find(columnletter.lower())
  else:
    playcolumn = -1
  return playcolumn

def onboard(playcolumn,playrow):
  # Determines if move is on the board.
  if 0 <= playrow <= 7 and 0 <= playcolumn <= 7:
    return True
  else:
    return False

def legalmove(playcolumn, playrow):
  # Asks if coordinate is empty and lies on the board.
  if onboard(playcolumn,playrow) != True:
    print('Invalid input, that square lies outside of the board boundaries.')
    return False
  if mainboard[playcolumn][playrow] != " ":
    print('Invalid input, that square is already occupied.')
    return False
  else:
    return True

def flippingtiles(playcolumn, playrow, board):
  #Returns coordinates list of tiles to be flipped.
  #If no tiles should be flipped returns empty list.
  
  global flippinglist
  xinitial,yinitial = playcolumn,playrow
  flippinglist = []
  if board[xinitial][yinitial] == "X":
    opponenttile = "O"
  elif board[xinitial][yinitial] == "O":
    opponenttile = "X"

  for xshift,yshift in [1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]:
    x,y = xinitial+xshift,yinitial+yshift
    if onboard(x,y) != True:
      continue
    while board[x][y] == opponenttile:
      x += xshift
      y += yshift
      if onboard(x,y) != True:
        break
    if onboard(x,y) != True:
      continue
    if board[x][y] == board[xinitial][yinitial]:
      while board[x-xshift][y-yshift] == opponenttile:
        x -= xshift
        y -= yshift
        flippinglist.append([x,y])
  return flippinglist

#testing function to determine if board is full
def endthegame(board):
  occupiedsquares = []
  for x in range (8):
    for y in range(8):
      if board[x][y] != " ":
        occupiedsquares.append([x,y])
  return occupiedsquares

def finalscoring(board):
  #Calculates points after game concludes.
  player1score = player2score = 0
  for x in range(8):
    for y in range(8):
      if board[x][y] == "X":
        player1score += 1
      elif board[x][y] == "O":
        player2score += 1
  print('Player X scored %d points' % player1score)
  print('Player O scored %d points' % player2score)
  if player1score > player2score:
    print('Player X was victorious. Player O should reconsider life choices.')
  elif player1score < player2score:
    print('Player O was victorious. Player X stinks.')
  else:
    print('There are no winners to be found here, the game was a tie!')

#Calls initial board state
mainboard = getNewBoard()
resetBoard(mainboard)
drawBoard(mainboard)

gameongoing = True
player1turn = True

### The game of Reversi
while gameongoing == True:
  if player1turn == True:
    print('Player X has the move')
  else:
    print('Player O has the move')
  playcoord = input('Place a stone, or Q to quit:\n')
  if playcoord in {'Q','q'}:
    print("Thanks for playing!")
    break
  playcolumn = playcoord[0:1]
  playrow = playcoord[1:]
  if playrow.isdigit() == False:
    print('Invalid input, the correct format is algebraic notation.')
    continue
  convertcolumn(playcolumn)
  playrow = int(playrow)-1
  if legalmove(playcolumn, playrow) == True:
    if player1turn == True:
      mainboard[playcolumn][playrow] = "X"
    else:
      mainboard[playcolumn][playrow] = "O"
    if flippingtiles(playcolumn, playrow, board) != []:
      for x,y in flippinglist:
        if player1turn == True:
          mainboard[x][y] = "X"
        else:
          mainboard[x][y] = "O"
      drawBoard(mainboard)
      if endthegame(board) == []:
        print('The board is full, thanks for playing!')
        ganeongoing = False
    else:
      print('This move does not flip any tiles, try again.')
      mainboard[playcolumn][playrow] = " "
      continue
  if player1turn == True:
    player1turn = False
  else:
    player1turn = True
finalscoring(mainboard)