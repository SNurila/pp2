import os
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return "File not found"
    
file_to_count = "./example.txt" 
line_count = count_lines_in_file(file_to_count)
print(f"Number of lines in '{file_to_count}':", line_count)
