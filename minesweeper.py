import random

# Minesweeper Layout
def mines_layout():
    global mine_values
    global n
 
    print()
    print("\t\t\tMinesweeper\n")
 
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
 
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)
 
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
         
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(mine_values[r][col]) + "  "
        print(st + "|") 
 
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
    print()

# setting up Mines
def set_mines():
 
    global numbers
    global mines_no
    global n
 
    # Track of number of mines already set up
    count = 0
    while count < mines_no:
 
        # Random number from all possible grid positions 
        val = random.randint(0, n*n-1)
 
        # Generating row and column from the number
        r = val // n
        col = val % n
 
        # Place the mine, if it doesn't already have one
        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col] = -1


if __name__ == "__main__":
 
    # Size of grid
    n = 8
    # Number of mines
    mines_no = 8
 
    # The actual values of the grid
    numbers = [[0 for y in range(n)] for x in range(n)] 
    # The apparent values of the grid
    mine_values = [[' ' for y in range(n)] for x in range(n)]
    # The positions that have been flagged
    flags = []