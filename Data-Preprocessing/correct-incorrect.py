import os
import shutil

def copy_files_by_correctness(incorrect_files_list, source_folder, correct_folder, incorrect_folder):
    # Create the correct and incorrect folders if they don't exist
    os.makedirs(correct_folder, exist_ok=True)
    os.makedirs(incorrect_folder, exist_ok=True)

    # Iterate through all files in the source folder
    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)

        # Check if the file is a regular file (not a directory) and ends with .xlsx
        if os.path.isfile(source_file_path) and filename.endswith('.xlsx'):
            # Determine the destination folder based on correctness
            if filename in incorrect_files_list:
                destination_folder = incorrect_folder
            else:
                destination_folder = correct_folder

            # Copy the file to the appropriate folder
            shutil.copy2(source_file_path, destination_folder)

if __name__ == "__main__":
    # List of incorrect file names
    incorrect_files_list = ["1.xlsx","9.xlsx","7.xlsx","3.xlsx","26.xlsx","13.xlsx","20.xlsx","14.xlsx","23.xlsx"
                            ,"36.xlsx","34.xlsx","40.xlsx","42.xlsx"]

    # Source folder containing all xlsx files
    source_folder = "C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\B21236\\eye-data\\excel\\all-emails\\"

    # Destination folders for correct and incorrect files
    correct_folder = "C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\B21236\\eye-data\\excel\\correct-answered\\"
    incorrect_folder = "C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\B21236\\eye-data\\excel\\incorrect-answered\\"

    # Copy files based on correctness
    copy_files_by_correctness(incorrect_files_list, source_folder, correct_folder, incorrect_folder)
