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

# Show mines
def show_mines():
    global mine_values
    global numbers
    global n
 
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                mine_values[r][col] = 'M'


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

        # Standard Move
        if len(inp) == 2:
        
            # Try block to handle errant input
            try: 
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue
        
        # Flag Input
        elif len(inp) == 3:
            if inp[2] != 'F' and inp[2] != 'f':
                clear()
                print("Wrong Input!")
                instructions()
                continue
        
            # Try block to handle errant input  
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue
        
            # Sanity checks
            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("Wrong Input!")
                instructions()
                continue
            
            # Get row and column numbers
            r = val[0]-1
            col = val[1]-1

            # If cell already been flagged
            if [r, col] in flags:
                clear()
                print("Flag already set")
                continue
            
            # If cell already been displayed
            if mine_values[r][col] != ' ':
                clear()
                print("Value already known")
                continue
            
            # Check the number for flags    
            if len(flags) < mines_no:
                clear()
                print("Flag set")
            
                # Adding flag to the list
                flags.append([r, col])
                
                # Set the flag for display
                mine_values[r][col] = 'F'
                continue
            else:
                clear()
                print("Flags finished")
                continue

        # If landing on a mine --- GAME OVER    
        if numbers[r][col] == -1:
            mine_values[r][col] = 'M'
            show_mines()
            print_mines_layout()
            print("Landed on a mine. GAME OVER!!!!!")
            over = True
            continue
        