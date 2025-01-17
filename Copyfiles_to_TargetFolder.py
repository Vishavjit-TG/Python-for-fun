import os
import shutil

def copy_files(file_paths, target_directory):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Loop through each file path and copy the file
    for file_path in file_paths:
        if os.path.isfile(file_path):
            try:
                # Extract the filename from the path
                file_name = os.path.basename(file_path)
                
                # Define the target file path
                target_path = os.path.join(target_directory, file_name)
                
                # Copy the file to the target directory
                shutil.copy(file_path, target_path)
                print(f"Successfully copied {file_name} to {target_directory}")
            except Exception as e:
                print(f"Error copying {file_path}: {e}")
        else:
            print(f"File does not exist: {file_path}")

# Example usage:
if __name__ == "__main__":
    # List of file paths you want to copy
    file_paths = [
		r"<File Path- C:\Windows...>",
    ]
    
    # Specify the target directory in format D:\Folder1\SubFolder
    target_directory = r"<Target_Directory>" 
    
    # Call the function to copy files
    copy_files(file_paths, target_directory)
