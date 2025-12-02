def get_ranges(file_path: str):
    # Get a tuple of ranges from the input file separated by commas
    with open(file_path, "r") as file:
        ranges = file.read().strip().split(",")
        # Get start and end of each range as integers (removes leading 0s) and return as a list of tuples
        return [tuple(map(int, r.split("-"))) for r in ranges]