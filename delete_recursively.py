import os, sys

def getDirectoryContents(dir_name='.'):
    return [ path for path in os.listdir(dir_name) if path[0] != '.' ]

def deleteRecursively(top_dir):
    os.chdir(top_dir)
    for item in getDirectoryContents():
        if os.path.isdir(item):
            deleteRecursively(item)
        else:
            os.system('svn remove ' + item)
    os.chdir('..')
    os.system('svn remove ' + top_dir)

deleteRecursively(sys.argv[1])Recursively(sys.argv[1])