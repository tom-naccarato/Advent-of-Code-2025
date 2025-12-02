import os

def get_ranges(file_path: str):
    # Get a tuple of ranges from the input file separated by commas
    with open(file_path, "r") as file:
        ranges = file.read().strip().split(",")
        # Get start and end of each range as integers (removes leading 0s) and return as a list of tuples
        return [tuple(map(int, r.split("-"))) for r in ranges]
    
def sum_invalid_ids_in_range(start_id:int, end_id:int):
    invalid_sum = 0
    for id in range(start_id, end_id + 1):
        # Convert id to string
        id_str = str(id)
        if len(id_str) % 2 != 0:
            continue  # Skip IDs with odd number of digits as cannot be invalid
        # Split id into two halves
        mid = len(id_str) // 2
        first_half = id_str[:mid]
        second_half = id_str[mid:]
        # Check if first and second halves are the same - if so, index is invalid
        if first_half == second_half:
            invalid_sum += id # Add invalid ID to sum
    return invalid_sum # Return the sum of invalid IDs in the range
        
        
        
def main():    
    ranges = get_ranges(os.path.join(os.path.dirname(__file__), "input.txt"))
    invalid_sum = 0
    # Sum invalid IDs for each range and accumulate to total sum
    for range in ranges:
        # Calculate sum of invalid IDs in the range and add to total sum
        invalid_sum += sum_invalid_ids_in_range(range[0], range[1])
    print(f"Sum of invalid IDs: {invalid_sum}")
        
                        
if __name__ == "__main__":
    main()