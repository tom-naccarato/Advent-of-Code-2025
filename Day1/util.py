def left_rotate(current_number,n):
    # Modulo 100 to wrap around dial
    return (current_number - n) % 100

def right_rotate(current_number,n):
    # Modulo 100 to wrap around dial (100 is equivalent to 0)
    return (current_number + n) % 100