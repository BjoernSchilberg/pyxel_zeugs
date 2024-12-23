import sys
import pyxel

# https://github.com/kitao/pyxel for information about the pyxel game library

# Window
WIDTH = 150
HEIGHT = 180
RED = 3
WHITE = 7
BLACK = 2
CELL_DIMENSIONS = 50


class Game:
    """A class to contain the game state, and useful methods for modifying it."""

    def __init__(self):
        # Game Settings
        # Makes X start first by default, will get changed to decide whos turn it is
        self.PlayerTurn = "X"

        # Creates our board layout to put values to. by default, the board is blank.
        self.grid = [[None, None, None], [None, None, None], [None, None, None]]
        self.winner = None  # Adds a winner variable for later

    def game_message(self):
        # Determine what to write
        if self.winner == None and self.checkforFull() == False:
            # If there isn't a winner and the board isn't full
            message = "{}'s turn".format(self.PlayerTurn)
            # make message equal to whoevers turn it is
        elif self.winner != None:
            message = "{} Wins!".format(self.winner)
            # Otherwise, display whoever wins instead
        elif self.winner == None and self.checkforFull() == True:
            # If there isn't a winner and the board is full
            message = "A tie!"  # Call for a tie
        return message

    def checkforFull(self):
        for row in self.grid:
            # For every row in grid (keeping in mind grid is just made up of 3 lists)
            if None in row:  # If there is None in any of the lists in grid
                finished = False  # The game hasn't finished yet
                break
            else:  # If there isn't...
                finished = True  # The game has finished
        return finished

    def gameFinished(self):
        """Job: To check for either a player win or a tie
        board is the game board surface."""

        # For extra info:
        # To draw a line,the following variables are needed (in order)
        # Surface, color, start position, end position, width

        grid = self.grid

        # Check for rows in which someone has won
        for row in range(0, 3):  # In any of the rows (i.e row 1, row 2, or row 3)
            # If the 1st, 2nd and 3rd values are the same and are not empty...
            if (grid[row][0] == grid[row][1] == grid[row][2]) and (
                grid[row][0] is not None
            ):
                self.winner = grid[row][0]
                # The winner is the symbol on the first value of the row (i.e column 1)
                # Draws a line through the row
                return ("row", row)  # Break out of the for loop

        # Check for columns in which someone has won
        for col in range(
            0, 3
        ):  # IN any of the columns (i.e column 1, column 2 or column 3
            # If the 1st, 2nd and 3rd values are the same and are not empty...
            if (grid[0][col] == grid[1][col] == grid[2][col]) and (
                grid[0][col] is not None
            ):
                self.winner = grid[0][col]
                # The winner is the symbol on the first value of the column (i.e row 1)
                # Draws a line through the column
                return ("column", col)  # Break out of the for loop

        # Check for diagonal wins
        # If the diagonal values starting from the top left are all the same and are not empty
        if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
            self.winner = grid[0][0]  # The winner is the symbol in the top left
            return ("diag1", None)  # Draw a line through the diagonal

        # If the diagonal values starting from the top right are all the same and are not empty
        if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
            self.winner = grid[0][2]  # The winner is the symbol in the top right
            return ("diag2", None)  # Draw a line through the diagonal

        # Check for ties
        # If the board is full and winner is not equal to X or O
        # It is a tie. Change the status
        return (None, None)

    def toggle_turn(self):
        """Turn the player turn to the opposite player."""
        if self.PlayerTurn == "X":
            self.PlayerTurn = "O"
        elif self.PlayerTurn == "O":
            self.PlayerTurn = "X"

    def is_populated(self, row, col):
        cell = self.grid[row][col]
        return cell != None


class App:
    """A class to initialise the game, take input, and display the board."""

    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)
        pyxel.mouse(True)

        self.finished = False
        self.game = Game()

        pyxel.run(self.update, self.display)

    #
    # Update methods
    #

    def update(self):
        """The main game loop."""

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and not self.finished:
            self.clickBoard()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.game = Game()
            self.finished = False

    @staticmethod
    def boardPosition(mouseX, mouseY):
        """Job: Find out which board space (i.e row, column) the user clicked in based on their mouse coordinates
        Here, mouseX is the X coordinate the user clicked and mouseY is the Y coordinate the user clicked
        Note: Lists are 0 based in terms of index. This means that if you call for the 0th item (i.e list[0]), you will
        get the first, as the index "starts" from 0."""

        point = (position // CELL_DIMENSIONS for position in (mouseY, mouseX))

        return point
        # Returns the tuple containing the row and column that the user clicked in

    def clickBoard(self):
        """Job: Find out where the user clicked and if the space isn't occupied, have a symbol drawn there
        board is the game board surface."""

        mouseX, mouseY = pyxel.mouse_x, pyxel.mouse_y
        # Makes mouseX and mouseY equal to the coordinates of the mouse
        row, col = self.boardPosition(mouseX, mouseY)
        # As a note, boardPosition, returns the row and column that the user clicked in

        # Check to see if the space is empty
        if self.game.is_populated(row, col):
            # If an X or an O is present in the box that was clicked
            return

        # Mark the square as occupied
        self.game.grid[row][col] = self.game.PlayerTurn

        # Toggle PlayerTurn to make it the other persons turn
        self.game.toggle_turn()

    #
    # Display methods
    #

    def display(self):
        self.display_board()
        self.drawStatus()
        self.display_cells()
        self.display_winning()  # Check to see if the game finished

    def display_board(self):
        """Job: Initialise the board and return the board as a variable."""

        # Creates a surface object with the window size
        pyxel.cls(WHITE)  # Converts the background to a WHITE color (I think)

        # Draw Grid Lines

        # Vertical lines
        pyxel.line(50, 0, 50, 150, BLACK)
        pyxel.line(100, 0, 100, 150, BLACK)

        # horizontal lines...
        pyxel.line(0, 50, 150, 50, BLACK)
        pyxel.line(0, 100, 150, 100, BLACK)

    def drawStatus(self):
        """Job: Shows status at the bottom of the board (i.e player turn, num of moves, etc)
        In this case, board is the initialised game board where the status will be drawn onto."""

        message = self.game.game_message()
        # Send the finished status onto the board

        pyxel.text(10, 160, message, BLACK)
        # Pastes the status onto the board at the coordinates 10, 300

    def display_cells(self):
        for row in range(3):
            for col in range(3):
                self.drawMove(row, col)

    def drawMove(self, row, col):
        """Job: Draw either an X or an O (Symbol) on the board in a specific boardRow and boardCol
        Board is the game board surface we are drawing on. boardRow and boardCol are the row and column in which
        we will draw the symbol in. Symbol is either an X or an O, based on who's turn it is.
        Note: Lists are 0 based in terms of index. This means that if you call for the 0th item (i.e list[0]), you will
        get the first, as the index "starts" from 0."""

        symbol = self.game.grid[row][col]
        if not symbol:
            return

        # Finds the center of the box we will draw in
        centerX = ((col) * CELL_DIMENSIONS) + (CELL_DIMENSIONS // 2)
        centerY = ((row) * CELL_DIMENSIONS) + (CELL_DIMENSIONS // 2)

        # Draws the appropriate symbol
        if symbol == "O":  # If the Symbol is O, draw a circle in the specified square
            pyxel.circb(centerX, centerY, 15, BLACK)

        elif symbol == "X":
            # If the Symbol is X, draw two lines (i.e an X) in the specified square
            pyxel.line(centerX - 11, centerY - 11, centerX + 11, centerY + 11, BLACK)
            pyxel.line(centerX + 11, centerY - 11, centerX - 11, centerY + 11, BLACK)

    def display_winning(self):
        win_state, value = self.game.gameFinished()
        if win_state:
            self.finished = True

        if win_state == "row":
            row = value
            pyxel.line(10, (row + 1) * 50 - 25, 140, (row + 1) * 50 - 25, RED)

        elif win_state == "column":
            col = value
            pyxel.line((col + 1) * 50 - 25, 10, (col + 1) * 50 - 25, 140, RED)

        elif win_state == "diag1":
            pyxel.line(25, 25, 125, 125, RED)

        elif win_state == "diag2":
            pyxel.line(125, 25, 25, 125, RED)


if __name__ == "__main__":
    App()
