# Assign an integer value to variable n from STDIN
n = int(input("#Please enter a value for n\n"))
# Assign the star and whitespace char to variables to avoid literal strings in code.
star = "*"
space = " "
def line(m, k):
    """Returns a line (the horicontal component) of a 'chessboard' as a string.
    It actually does the main work of the program: It determines what the current line shall look like and returns the corresponding string.
    Therefore, to construct a nxn chessboard, this function needs to be called inside a loop (so n times).
    It takes two arguments:
    - int m: The length of the line
      This variable needs to be a constant. If it changes from one call to another, no proper chessboard is constructed.
    - int k: A variable which allows to determine how many stars and how many spaces are supposed to be in the line.
      It needs to be incremented 
      - If k is even, then m stars and m-1 spaces are printed.
      - If k is uneven, then m spaces and m-1 stars are printed"""
    # The future return value is initialized as the empty string
    my_line = ""
    # Check if k is even
    if k%2 == 0:
        # Add star and space m-2 times to my_line, unless the loop has arrived at the last iteration step.
        # Then just add a star. This is necessary to obtain a proper chessboard, that is, a chessboard with straight edges.
        for i in range(m):
            if i < m-1:
                my_line += star+space
            else:
                my_line += star
    else:
        for i in range(m):
            if i < m-1:
                my_line += space+star
            else:
                my_line += space
    return my_line

def print_chessboard(m):
     """Call the function that returns proper chessboard lines n times. Use the
     counter variable of the for loop as the counter variable required by the
     function.
     This function has no return value, it is only for printing. 
     """
     for i in range(m):
         print(line(m,i))

print_chessboard(n)
