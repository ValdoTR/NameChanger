import os
import shutil

# Constants
INPUT_DIR = 'input'  # Input directory containing files
OUTPUT_DIR = 'output'  # Output directory to save renamed files
STRING_TO_REPLACE = 'foo'  # String to be replaced
REPLACEMENT_STRING = 'bar'  # String to replace with

def rename_files_in_directory(input_dir, output_dir, string_to_replace, replacement_string):
    """
    Rename files in a directory and its subdirectories by replacing a specified string.

    Parameters:
        input_dir (str): Path to the input directory.
        output_dir (str): Path to the output directory.
        string_to_replace (str): The string to be replaced in file names.
        replacement_string (str): The string to replace with in file names.
    """
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
            
            print(f"Renamed {input_file_path} to {output_file_path}")

def main():
    """
    Main function to execute the file renaming process.
    """
    rename_files_in_directory(INPUT_DIR, OUTPUT_DIR, STRING_TO_REPLACE, REPLACEMENT_STRING)
    print("\033[92mFile renaming completed.\033[0m")

if __name__ == "__main__":
    main()
