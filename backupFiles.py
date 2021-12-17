import os
import shutil

source = input("Enter Your Folder Name: ")
destination = input("Enter The Destination For Backup: ")
source = source+'/'
destination = destination+'/'

list_of_files = os.listdir(source)

for file in list_of_files: 
    shutil.copy(source+file,destination)