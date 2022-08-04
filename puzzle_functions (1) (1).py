""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = "up"
DOWN = "down"
FORWARD = "forward"
BACKWARD = "backward"

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = "player one"
P2 = "player two"
P1_WINS = "player one wins"
P2_WINS = "player two wins"
TIE = "tie game"

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = "puzzle1.txt"


# Helper functions.  Do not modify these, although you are welcome to
# call them!


def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split("\n")
    column = ""
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.

    >>> get_row_length('abcd\nefgh\nijkl\n')
    4
    """
    return len(puzzle.split("\n")[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.


def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """
    value = int
    # Complete this function.
    if player_one_turn is True:
        value = P1
    elif player_one_turn is False:
        value = P2
    return value


def get_winner(p1_score: int, p2_score: int) -> str:
    """ Return a str that correlates to the player with the highest score.
    >>> get_winner(10, 12)
    "player two wins"
    >>> get_winner(13, 1)
    "player one wins"
    """
    winner = int
    if p1_score > p2_score:
        winner = P1_WINS
    elif p2_score > p1_score:
        winner = P2_WINS
    elif p2_score == p1_score:
        winner = TIE
    return winner


def reverse(jumbled_row_col: str) -> str:
    """ Return a reveresed copy of the string jumnled_row_col.
    >>> reverse("tab")
    "bat"
    >>> reverse("flower")
    "rewolf"
    """
    return jumbled_row_col[-1::-1]


def get_row(puzzle: str, row_num: int) -> str:
    """ Return a string of letters that correlate to the the row_num in the
    puzzle, excluding newline characters.

    >>> get_row("hrty\nywod\ntalo\nyqpl", 1)
    "ywod"
    >>> get_row("black\nhqyos\nqupls\nuqplf\njajjk", 0)
    "black"
    """
    modified_puzzle = puzzle.strip().split("\n")
    return modified_puzzle[row_num]


def get_factor(direction: str) -> int:
    """ Return the multiplicative factor that correlates to the direction.
    >>> get_factor(UP)
    4
    >>> get_factor(DOWN)
    2
    >>> get_factor(FORWARD)
    1
    >>> get_factor(BACKWARD)
    3
    """
    mult_factor = int
    if direction == UP:
        mult_factor = UP_FACTOR
    if direction == DOWN:
        mult_factor = DOWN_FACTOR
    if direction == FORWARD:
        mult_factor = FORWARD_FACTOR
    if direction == BACKWARD:
        mult_factor = BACKWARD_FACTOR
    return mult_factor


def get_points(direction: str, num_words_left: int) -> int:
    """ Return the number of points earned if we were to find some word in the
    direction given with the num_words_left.
    >>> get_points(UP, 5)
    20
    >>> get_points(DOWN, 4)
    12
    >>> get_points(FORWARD, 1)
    21
    >>> get_points(BACKWARD, 2)
    24
    """
    points = int
    if THRESHOLD <= num_words_left:
        points = THRESHOLD * get_factor(direction)
    if 1 < num_words_left < THRESHOLD:
        points = (2 * THRESHOLD - num_words_left) * get_factor(direction)
    if num_words_left == 1:
        p = (2 * THRESHOLD - num_words_left) * get_factor(direction)
        points = p + BONUS
    return points


def check_guess(puzzle: str, direction: str, guessed_word: str,
                row_col_num: int, num_words_left: int) -> int:

    """ Return the number of points earned for the correct guess word if it
    satisfies all the given contraints/arguments. If the guess doesn't satisfy
    all of the arguments return 0.
    >>> check_guess('abcd\nefah\nijtl\nhuye', DOWN, 'cat', 2, 2)
    16
    >>> check_guess('abcd\ntabj\nttwz\njklm', DOWN, 'dat', 1, 6)
    0
    >>> check_guess('abcd\ntabj\nttwz\njklm', UP, 'toy', 1, 2)
    0
    """

    row_string = get_row(puzzle, row_col_num)
    rev_row_string = reverse(row_string)
    col_string = get_column(puzzle, row_col_num)
    rev_col_string = reverse(col_string)
    word_direct = []

    if contains(row_string, guessed_word) is True:
        word_direct.append(FORWARD)
    if contains(rev_row_string, guessed_word) is True:
        word_direct.append(BACKWARD)
    if contains(col_string, guessed_word) is True:
        word_direct.append(DOWN)
    if contains(rev_col_string, guessed_word) is True:
        word_direct.append(UP)
    if contains(word_direct, direction):
        points = get_points(direction, num_words_left)
    else:
        points = 0
    return points
