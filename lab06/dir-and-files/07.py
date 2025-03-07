import os
import shutil
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        return "File copied successfully"
    except FileNotFoundError:
        return "Source file not found"
    except Exception as e:
        return f"Error copying file: {e}"
source_file = "./example.txt"
destination_file = "./copy_example.txt"
copy_result = copy_file(source_file, destination_file)
print(copy_result)
