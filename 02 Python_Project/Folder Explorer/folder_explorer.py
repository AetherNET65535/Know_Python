import os
import shutil

source_folder = r"C:\Users\Lenovo\Documents\02 Python_Project\Explorer\source"

target_folder = r"C:\Users\Lenovo\Documents\02 Python_Project\Explorer\target"

# make a dic to remember file name 
file_names = {}

# see see all files in source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_file_path = os.path.join(root, file)
        
        # let computer know want take what things
        target_file_path = os.path.join(target_folder, file)
        
        # add number if file existed
        base_name, extension = os.path.splitext(file)
        count = 1
        while os.path.exists(target_file_path):
            new_file_name = f"{base_name}_{count}{extension}"
            target_file_path = os.path.join(target_folder, new_file_name)
            count += 1
        
        # copy files to target folder
        shutil.copy(source_file_path, target_file_path)
        
        # remember file name that already copy
        file_names[file] = os.path.basename(target_file_path)

# let bro see files that already done
for source_name, target_name in file_names.items():
    print(f"Done: {source_name} -> {target_name}")

print("DONE BRO GO WILD AND HAVE FUN")
