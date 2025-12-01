import os
from util import left_rotate, right_rotate

def main():
    # Dial starts at 50
    current_number = 50
    password = 0
    
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        for line in file:
            # Read direction and number of steps
            direction = line[0]
            n = int(line[1:].strip())
            
            if direction == 'L':
                current_number = left_rotate(current_number, n)
            else: # direction == 'R'
                current_number = right_rotate(current_number, n)
            
            # If the dial lands on 0, increment password
            if current_number == 0:
                password += 1
                
        return print(f"The password is: {password}")
                
                


if __name__ == "__main__":
    main()