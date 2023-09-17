import os
import shutil

# setting source and target folder path
source_folder = r"C:\Users\Lenovo\Documents\02 Python_Project\Video Dog\source"
target_folder = r"C:\Users\Lenovo\Documents\02 Python_Project\Video Dog\target"

# see see all subfolders
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # see see files is vid or not
        if file.endswith((".mp4", ".WebM", ".avi", ".m4v", ".mov", ".wmv")):
            source_file_path = os.path.join(root, file)
            # go find files name
            target_files = os.listdir(target_folder)
            # check check have same name file or not
            if file in target_files:
                # if existed, make a new file name
                base_name, ext = os.path.splitext(file)
                new_file_name = f"{base_name}_copy{ext}"
                target_file_path = os.path.join(target_folder, new_file_name)
            else:
                # if no have same name, just use ori name
                target_file_path = os.path.join(target_folder, file)
            # copy video to target folder
            shutil.copy(source_file_path, target_folder)
