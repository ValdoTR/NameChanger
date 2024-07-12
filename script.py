import os
import shutil
import sys

# Constants
INPUT_DIR = 'input'  # Input directory containing files
OUTPUT_DIR = 'output'  # Output directory to save renamed files

def rename_files_in_directory(input_dir, output_dir, string_to_replace, replacement_string):
    """
    Rename files in a directory and its subdirectories by replacing a specified string.

    Parameters:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
        string_to_replace (str): The string to be replaced in file names.
        replacement_string (str): The string to replace with in file names.
    
    Returns:
        int: Number of files renamed.
    """
    files_renamed = 0
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            # Construct full file path
            input_file_path = os.path.join(root, file)
            
            # Replace string in file name
            new_file_name = file.replace(string_to_replace, replacement_string)
            
            # Determine the relative path to maintain directory structure
            relative_path = os.path.relpath(root, input_dir)
            output_file_dir = os.path.join(output_dir, relative_path)
            output_file_path = os.path.join(output_file_dir, new_file_name)
            
            # Ensure the output directory exists
            if not os.path.exists(output_file_dir):
                os.makedirs(output_file_dir)
            
            # Copy the file to the new location with the new name
            shutil.copy2(input_file_path, output_file_path)

            # Check if the string to replace is in the file name
            if string_to_replace in file:
                print(f"Renamed '{input_file_path}' to '{output_file_path}'")
                files_renamed += 1

    return files_renamed


def main():
    """
    Main function to execute the file renaming process.
    """
    if len(sys.argv) != 3:
        print("Please run: python3 script.py [string_to_replace] [replacement_string]")
        sys.exit(1)
    
    string_to_replace = sys.argv[1]
    replacement_string = sys.argv[2]

    files_renamed = rename_files_in_directory(INPUT_DIR, OUTPUT_DIR, string_to_replace, replacement_string)
    
    if files_renamed > 0:
        print(f"\033[92m{files_renamed} files have been renamed.\033[0m")
    else:
        print(f"\033[93mNo files have been renamed.\033[0m")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\033[91mScript cancelled by user.\033[0m")
    except Exception as e:
        print(f"\033[91mAn error occurred: {e}\033[0m")