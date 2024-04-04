import re
import sys


def pixelsToRem( matchObj ):
    value = matchObj.group(0)
    valueInt = int(value.strip('px'))
    remValueInt = valueInt/16
    remValue = str(remValueInt) + 'rem'
    return remValue


arguments = sys.argv[1:]

if len( arguments ) < 1:
    print(f'Err: 1 argument expected. { len( arguments ) } given.')
else:
    file = arguments[0]

with open( file, 'r+' ) as fileOpen:
    string = fileOpen.read()
    fileOpen.seek(0)
    fileOpen.write( re.sub( '-*\d+px', pixelsToRem, string ))
    fileOpen.truncate()