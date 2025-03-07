import os
def analyze_path(path):
    if os.path.exists(path):
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        return {"Directory": directory, "Filename": filename}
    else:
        return "Path does not exist"
path_to_analyze = "./example.txt"  # Change this to any desired path
path_info = analyze_path(path_to_analyze)
print("Path analysis:", path_info)