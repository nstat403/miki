import os,sys

if __name__ == "__main__":

    #print("tedt")
    path=sys.argv[1]
    abspath=os.path.abspath(path)
    print(abspath)
