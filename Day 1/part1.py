def left_rotate(current_number,n):
    # Modulo 100 to wrap around dial
    return (current_number - n) % 100

def right_rotate(current_number,n):
    # Modulo 100 to wrap around dial (100 is equivalent to 0)
    return (current_number + n) % 100

def main():
    # Dial starts at 50
    current_number = 50
    password = 0
    
    with open("Day 1/input.txt", "r") as file:
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