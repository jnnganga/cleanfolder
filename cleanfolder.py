#!/usr/bin/python

import sys
import os
import folder_organizer as fo

print(f"             **********************************************************************************")
print(f"             *                                                                                *")
print(f"             *    This script organizes all files in a folder into subdirectories of          *")
print(f"             *    corresponding file types.                                                   *")
print(f"             *                                                                                *")
print(f"             *                                                                                *")
print(f"             *    [Warning]   Do not operate this script in a system or application folder,   *")
print(f"             *                the files will be move rendering the application unusable!      *")
print(f"             *                                                                                *")
print(f"             *                              MIT License                                       *")
print(f"             *                           Copyright (c) 2021                                   *")
print(f"             *                       https://github.com/jnnganga/                             *")
print(f"             *                                                                                *")
print(f"             **********************************************************************************")

# C:\Users\Nganga\OneDrive\Documents\GaoChao\projects\clean
count = 0
while count < 4:
    path = input(f'Enter the folder\'s full path or "c" to cancel:')
    if path == "c" or path == "q" :
        print("Operation has been canceled.\nGoodbye.")
        break
    try:
        if os.path.isdir(path):
            files = [ f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]
            total = len(files)
            if total == 0:
                print(f"\nAll clean, there are no files to be moved in this folder : {path}\n")
                continue
            print(f'\nThe files in this folder "{path}" will be moved to corresponding file-type sub folders.\n')

            print(f"A total of {total} will be moved.\nSome files to be moved include : \n")
            for f in files[:5]:
                print(f)
            run = input('Enter "y" to perform this operation or "c" to cancel [y]')

            if run == "y" or run == "Y":
                print("Excecuting...\n")
                print(fo.execute_move_file(path))
                c = 0
            else:
                print("Operation has been canceled.\nGoodbye.")
                break
        else:
            print(f"The folder '{path}' does not exist, please enter a valid path.\n")
            count += 1
            if count == 4:
                print("\nGoodbye.\n")
    except Exception as e:
        print(f"Someting went wrong : {e}")
        count += 1
        if count == 4:
            print("\nGoodbye.\n")