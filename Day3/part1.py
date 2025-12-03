import os

from utils import parse_input


def find_highest_number_in_line(nums):
    """Start at the right hand side and find the highest two digit number that can be made."""
    # Start at second last index and move to the left
    max_after = nums[-1]
    max_two_digit = int(nums[-2] + nums[-1])
    # Iterate backwards through the list a d form two digit numbers with the current digit and the max digit seen so far
    for i in range(len(nums) - 2, -1, -1):
        current_max = int(nums[i] + max_after)
        if current_max == 99:
            return current_max # Early exit if we find the highest possible two digit number
        if current_max > max_two_digit:
            max_two_digit = current_max # Update the highest two digit number found
        if nums[i] > max_after:
            max_after = nums[i] # Update the max digit seen so far
        
    return max_two_digit

def main():
    input_file = 'input.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_file)
    input_lines = parse_input(input_path)
    sum = 0
    for line in input_lines:
        line = line.strip()
        sum += find_highest_number_in_line(line)
    print(f'Sum of highest two digit numbers: {sum}')

if __name__ == '__main__':
    main()