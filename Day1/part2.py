import os
from util import left_rotate, right_rotate

def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
        password = 0
        current_number = 50  # Dial starts at 50
        for line in file:
            # Read direction and number of steps
            direction = line[0]
            n = int(line[1:].strip())
            
            # Calculate full rotations
            full_rotations = n // 100 # Floor division to get complete 100-step rotations
            
            # Get the remainder when n is divided by 100 as effective steps
            n = n % 100
            
            if direction == 'L':
                new_number = left_rotate(current_number, n)
                if n > current_number:  # We crossed 0
                    password += 1
                current_number = new_number
            else:  # direction == 'R'
                new_number = right_rotate(current_number, n)
                if current_number + n >= 100:  # We crossed 0
                    password += 1
                current_number = new_number

            # Add full rotations (each full rotation crosses 0 once)
            password += full_rotations
            
        return print(f"The password is: {password}")
    
if __name__ == "__main__":
    main()
                
            
        