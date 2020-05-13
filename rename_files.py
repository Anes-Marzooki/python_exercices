import os
def rename_files():
    # Get the all the file names from a folder
    file_list = os.listdir("Folder_Dir")
    current = os.getcwd()
    print("Working dir "+current)
    os.chdir("Folder_Dir")
    print(file_list)
    # For each file, rename its name by removing the numbers in it
    for file_name in file_list:
      os.rename( file_name, file_name.translate(str.maketrans("","","0123456789")) )
      print(file_name)
    os.chdir(current)       
            
rename_files()
