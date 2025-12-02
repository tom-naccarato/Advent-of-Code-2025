import os
from util import get_ranges

def is_repeating(id_str):
    """Check if id_str is made of a repeating substring (at least 2 repetitions)."""
    n = len(id_str)
    # Try all possible substring lengths from 1 to n//2
    for length in range(1, n // 2 + 1):
        if n % length == 0: # Length must divide n evenly to form repeating pattern
            substring = id_str[:length]
            # Check if repeating this substring creates the full id
            if substring * (n // length) == id_str:
                return True
    return False

def sum_invalid_ids_in_range(start_id:int, end_id:int):
    invalid_sum = 0
    for id in range(start_id, end_id + 1):
        id_str = str(id)
        if is_repeating(id_str):
            invalid_sum += id
    return invalid_sum
    
def main():
    invalid_sum = 0
    ranges = get_ranges(os.path.join(os.path.dirname(__file__), "input.txt"))
    for range in ranges:
        invalid_range_sum = sum_invalid_ids_in_range(range[0], range[1])
        print(f"Sum of invalid IDs in range {range[0]}-{range[1]}: {invalid_range_sum}")
        invalid_sum += invalid_range_sum # Add to total sum across all ranges
    print(f"Total sum of invalid IDs across all ranges: {invalid_sum}")
        
    
if __name__ == "__main__":
    main()
    
    