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

# Setting up the other grid values
def set_values():
 
    global numbers
    global n
 
    # Loop for counting each cell value
    for r in range(n):
        for col in range(n):
 
            # Skip, if it contains a mine
            if numbers[r][col] == -1:
                continue
 
            # Check up  
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check down    
            if r < n-1  and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check left
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r] = numbers[r] + 1
            # Check right
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-left    
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-right
            if r > 0 and col < n-1 and numbers[r-1][col+1]== -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-left  
            if r < n-1 and col > 0 and numbers[r+1][col-1]== -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-right
            if r < n-1 and col< n-1 and numbers[r+1][col+1]==-1:
                numbers[r][col] = numbers[r][col] + 1


if __name__ == "__main__":
 
    # Size of grid
    n = 8
    # Number of mines
    mines_no = 8
    
    # Set the mines
    set_mines()
    
    # Set the values
    set_values()
    
    # Display the instructions
    instructions()
    
    # Variable for maintaining Game Loop
    over = False
            
    # The GAME LOOP 
    while not over:
        print_mines_layout()
        # Input from the user
        inp = input("Enter row number followed by space and column number = ").split()



    # The actual values of the grid
    numbers = [[0 for y in range(n)] for x in range(n)] 
    # The apparent values of the grid
    mine_values = [[' ' for y in range(n)] for x in range(n)]
    # The positions that have been flagged
    flags = []