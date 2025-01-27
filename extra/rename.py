from os import listdir
from os.path import isdir, join, isfile
import os.path
import shutil
import os

skip_folders = ['new-format']
def readFolder(root):
    files = []
    for file in listdir(root):
        if isdir(join(root, file)):
            for file2 in readFolder(join(root, file)):
                if file2 not in skip_folders:
                    files.append(join(join(root, file),file2))
        elif isfile(join(root, file)):
            if file.endswith('.png'):
                files.append(join(root, file))
    return files

def rename(files,root):
    newfiles=files.copy()
    for i,v in enumerate(files):
        splitted = v.split('/')[root.count('/'):]
        tail = v[-(v[::-1].find('-')):].split('.')[0].split('x')[0]
        if tail == '50':
            tail = 'drawable-ldpi'
        elif tail == '75':
            tail = 'drawable-mdpi'
        elif tail == '100':
            tail = 'drawable-hdpi'
        elif tail == '125':
            tail = 'drawable-xhdpi'
        elif tail == '150':
            tail = 'drawable-xxhdpi'
        new_name = (splitted[-2] + '.png').lower().replace('-','_')
        folder = splitted[2].lower().replace('-','_')
        if new_name.split('.')[0] != folder:
            name =(folder+'_'+new_name)
        else:
            name = new_name
        newfiles[i] = join(root,'new-format/',tail,name)
        #print(files[i],newfiles[i])
    return files,newfiles


def copy_files(files, renamed):
    if len(files) != len(renamed):
        raise Exception
    for old, new in zip(files,renamed):
        old_splitted = new.split('/')
        temp = '/'
        while not temp.endswith('.png'):
            if not os.path.exists(temp):
                os.makedirs(temp)
            if temp =='/':
                temp = ''
            temp += '/' + old_splitted[0]
            old_splitted = old_splitted[1:]
        shutil.copyfile(old,new)



def main():
    root = os.path.dirname(os.path.abspath(__file__))
    files = readFolder(root)
    files,renamed = rename(files, root)
    copy_files(files,renamed)

if __name__ == '__main__':
    main()
