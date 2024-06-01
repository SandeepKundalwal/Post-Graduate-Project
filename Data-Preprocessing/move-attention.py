import os
import shutil

def move_files(source_folder, destination_folder, files):
    for file_name in files:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {file_name} to {destination_folder}")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")

def main():
    source_folder = 'C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\B21236\\eye-data\\excel\\all-emails\\'
    destination_folder = 'C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\B21236\\eye-data\\excel\\attention\\'
    file_names = ["16.xlsx", "22.xlsx", "28.xlsx"]  # Replace these with your file names

    move_files(source_folder, destination_folder, file_names)

if __name__ == "__main__":
    main()
