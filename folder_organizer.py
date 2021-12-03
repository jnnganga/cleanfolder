import os
import shutil

def execute_move_file(path):
    # folder for files without extension
    no_extension = "unknowntype"

    # Folder to cleanup
    folder_path = rf"{path}"
    try:
        # Get a list of files in cleanup folder above
        files = [ f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f)) ]

        # Get unique file extensions, to be used as folder names
        extensions =set([file.split(".")[-1] for file in files if len(file.split("."))>1])

        # Create Folders if they don't exist
        [os.makedirs(os.path.join(folder_path,path))
        for path in extensions if not os.path.exists(os.path.join(folder_path,path))]

        # Move files in to folders
        [shutil.move(os.path.join(folder_path,file),os.path.join(folder_path,file.split(".")[-1]+"/"+file)) 
        for file in files if len(file.split("."))>1
        and os.path.exists(os.path.join(folder_path,file.split(".")[-1]))]

        # if there are files without extension and "no extension" folder does not exist, create it.
        if bool(["True"  for x in [len(each.split(".")) for each in files] if x == 1]) and not os.path.exists(os.path.join(folder_path,no_extension)):
            os.makedirs(os.path.join(folder_path,no_extension))

        # move files without extension
        [shutil.move(os.path.join(folder_path,file),os.path.join(folder_path,no_extension+"\\"+file)) 
        for file in files if len(file.split("."))==1 and os.path.exists(os.path.join(folder_path,no_extension))]
        return "All done !"
    except Exception as e :
        print(f'Oops !, run in to trouble {e}')

# print(extensions)
