import os


def replaceCharacterInFilesInDirectory(find, replace, directory):
    for filename in os.listdir(directory):
        os.rename(os.path.join(directory, filename),
                  os.path.join(directory, filename.replace(find, replace)))
