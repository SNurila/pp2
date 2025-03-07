import os
def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files
specified_path = "."  
dirs, files = list_directories_files(specified_path)
print("Directories:", dirs)
print("Files:", files)
