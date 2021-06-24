'''
path에 있는 파일의 인코딩을 전부 utf-8로 변경
'''

import os
from chardet import detect

# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

def change_encoding_type(srcfile,trgfile):
    from_codec = get_encoding_type(srcfile)

    # add try: except block for reliability
    try: 
        with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
            text = f.read() # for small files, for big use chunks
            e.write(text)

        os.remove(srcfile) # remove old encoding file
        os.rename(trgfile, srcfile) # rename new encoding
    except UnicodeDecodeError:
        print('Decode Error')
    except UnicodeEncodeError:
        print('Encode Error')

# get all of filename in path
path = "./"
files = os.listdir(path)

for file in files:
    change_encoding_type(file,file+".new")