import os
def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        try:
            os.remove(file_path)
            return "File deleted successfully"
        except Exception as e:
            return f"Error deleting file: {e}"
    else:
        return "File does not exist or cannot be deleted"
    
delete_file_path = "./example.txt"  
delete_result = delete_file(delete_file_path)
print(delete_result)
