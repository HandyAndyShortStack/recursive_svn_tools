import os, sys

def getDirectoryContents(dir_name='.'):
    return [ path for path in os.listdir(dir_name) if path[0] != '.' ]

def addRecursively(top_dir):
    os.chdir(top_dir)
    for item in getDirectoryContents():
        if os.path.isdir(item):
            addRecursively(item)
        else:
            os.system('svn add ' + item)
    os.chdir('..')
    os.system('svn add ' + top_dir)

addRecursively(sys.argv[1])