import os
from utils import parse_input

def greedy_largest_12_digit_number(nums: str) -> int:
    """Use a monotonic stack to greedily build the largest 12-digit number."""
    removals_allowed = len(nums) - 12
    result_stack = []
    
    for digit in nums:
        # While we can remove digits and last digit in stack is less that current digit
        while removals_allowed > 0 and result_stack and result_stack[-1] < digit:
            result_stack.pop() # Remove the last digit from the stack
            removals_allowed -= 1 # Decrease the number of allowed removals
        result_stack.append(digit) # Add current digit to the stack
        
    # If there are still removals left, remove from the end of the stack
    while removals_allowed > 0:
        result_stack.pop()
        removals_allowed -= 1
        
    # Join the stack to form the final 12-digit number and convert to int
    largest_12_digit_number = int(''.join(result_stack[:12]))
    return largest_12_digit_number
    
        
def main():
    input_file = 'input.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_file)
    input_lines = parse_input(input_path)
    sum = 0 # Sum of all largest 12-digit numbers in each line
    for line in input_lines:
        line = line.strip()
        largest_number = greedy_largest_12_digit_number(line)
        sum += largest_number
    print(f'Sum of all largest 12-digit numbers: {sum}')

if __name__ == "__main__":
    main()