import os
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        return "List written to file successfully"
    except Exception as e:
        return f"Error writing to file: {e}"
file_to_write = "./output.txt"
data_list = ["Apple", "Banana", "Cherry"]
write_result = write_list_to_file(file_to_write, data_list)
print(write_result)
