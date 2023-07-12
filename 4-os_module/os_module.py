import os
from datetime import datetime

#what's inside the module
#print(dir(os))

print('os name:\t', os.name)

#current directory
print('current dir:\t', os.getcwdb())
#absolute path of a file
print('absolute path:\t', os.path.abspath('os_module.py'))
#dir name of a file
print('dir name:\t', os.path.dirname(os.path.abspath('os_module.py')))
# file exists or not
print('file exists?:\t', os.path.exists('os_module.py'))
# is directory or not
print('is dir or not:\t', os.path.isdir('C:\\Users\\1047y'))
# is file or not
print('is file or not:\t', os.path.isfile(os.path.abspath('os_module.py')))
# make a path from strings
print('making a path:\t', os.path.join('F:\\', 'a folder', 'another folder in it', 'a_file_inside.py'))
# split a path
print('split a path:\t', os.path.split('C:\\Users\\yusuf\\folder\\folder in it\\file.py'))

#create a folder or folder inside folder
#os.mkdir('new_directory')
#os.makedirs("newdirectory/theotherone")

#change directory
#os.chdir('C:\\')
#os.chdir('..')
#print(os.getcwd())

#list directory 
print('dir list:\t', os.listdir())
print('dir list in \'C:\\\\Users\':\t', os.listdir('C:\\Users'))

# since we don't have any files in C:\\ directory. There's not gonna show any files but that's the idea.
for file in os.listdir('C:\\'):
    if file.endswith('.py'):
        print('a python file in C:\\\\ dir:\t', file)


stat = os.stat('os_module.py')

print('stat of os_module.py file:\t', stat)

#the size is in byte format
size = stat.st_size
print('size of it:\t', size)

# the time is in timestamp format
time = stat.st_atime # last time visited
time = stat.st_mtime # last time modified
time = stat.st_ctime # created time
print('time of the file when created(in timestamp format):\t', time)
# so we convert it
time = datetime.fromtimestamp(time)
print('time converted:\t', time)

#renaming
#mkdir('newfolder')
#os.rename('newfolder', 'renamed_folder')

#removing 
#os.remove('newfile.py')
#os.removedirs('folder/insidefolder/insideinsidefolder')









