# Please download the attached ZIP file and extract its files in a folder. Then, write a script that counts and prints out the number of .py files in that folder.

import glob
 
file_list=glob.glob1("files","*.py")
print(len(file_list))

#output : 2