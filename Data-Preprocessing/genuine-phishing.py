import os
import shutil

def filter_and_copy_files(source_dir, dest_dir, filenames):
    # Ensure destination directory exists
    os.makedirs(dest_dir, exist_ok=True)
    # print("inside")

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    # print(files)

    # Iterate through each file
    for filename in files:
        # Check if the file name (without extension) is in the list of filenames
        if os.path.splitext(filename)[0] in filenames:
            # print(filename)
            # Construct full paths
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            # Copy the file to the destination directory
            shutil.copyfile(source_path, dest_path)
            print(f"File '{filename}' copied to '{dest_dir}'")




if __name__ == "__main__":
    source_directory = "C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\B21236\\eye-data\\excel\\all-emails"
    # destination_directory = "C:\\Users\\DELL\\Desktop\\Data-Collection\\Analysis\\Genuine-Phishing\\GPT3\\B21236\\genuine"
    destination_directory = "C:\\Users\\DELL\\Desktop\\Data-Collection\\Analysis\\Genuine-Phishing\\GPT3\\B21236\\phishing"
    # filenames_to_copy = ['7','5','9','1','3','13','15','11','14','23','12','25','26','27','24','36','34','40','42','38'] # genuine
    filenames_to_copy = ['2','6','4','8','10','33','30','20','19','29','31','32','21','18','17','35','39','43','37','41'] # phishing

    filter_and_copy_files(source_directory, destination_directory, filenames_to_copy)
