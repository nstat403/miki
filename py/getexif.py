#-*- cofing:utf-8 -*-

from PIL import Image
from PIL.ExifTags import TAGS
import sys,re



def getexif(fname):
    im=Image.open(fname)
    try:
        exif=im._getexif()
    except AttributeError:
        return {}
    exif_table={}
    for id,value in exif.items():
        tag=TAGS.get(id,id)
        exif_table[tag]=value

    return exif_table

def getdate_from_picture(fname):
    table=getexif(fname)
    return table.get("DateTimeOriginal")

if __name__ == "__main__":
    fname=sys.argv[1]
    date=getdate_from_picture(fname)
    date=re.sub(":","",date)
    date=re.sub(" ","_",date)   
    print(date)
    pass
