
import glob

def MergeFiles(FilesToBeMerged, NewFileName):
    allfiles = glob.glob(FilesToBeMerged)
    filenames = allfiles
    with open(newfilename, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


MergeFiles()
