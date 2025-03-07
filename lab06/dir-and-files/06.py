import os
def generate_text_files():
    for letter in range(65, 91):  # ASCII values for A-Z
        filename = f"{chr(letter)}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}\n")
    return "26 text files generated successfully"
generate_result = generate_text_files()
print(generate_result)
