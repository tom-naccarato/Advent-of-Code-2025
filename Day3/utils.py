def parse_input(file_path:str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()