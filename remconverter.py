import re
import sys
from os.path import abspath, isfile
from  pathlib import Path


def pixelsToRem( matchObj ):
    value = matchObj.group(0)
    valueInt = int(value.strip('px'))
    remValueInt = valueInt/16
    remValue = str(remValueInt) + 'rem'
    return remValue


arguments = sys.argv[1:]

print( arguments )

# Sort user and bash inserted arguments
if len( arguments ) != 2 :
    print(f'TypeError: 1 argument expected. { min( 0, len( arguments ) - 1 ) } given.')
else:
    filePath = arguments[0]
    workingDirectory = arguments[1]
    file = filePath if filePath.count('/') > 1 else ( workingDirectory + filePath )

# Check that the file exists and is operable
if isfile( file ):
    fileName = Path( file ).stem
    print(f'Conversion unit values in { fileName }...')
else:
    print(f'Error: { file } does is not a file or does not exist')
    exit()

# Open the file and write to it with newly converter unit values
print('running pixel-rem unit conversion...')
with open( file, 'r+' ) as fileOpen:
    try:
        string = fileOpen.read()
        fileOpen.seek(0)
        fileOpen.write( re.sub( r'-*\d+px', pixelsToRem, string ))
        fileOpen.truncate()
        print(f'{ fileName } has been successfully converted to a Rem unit file.')
    except( OSError, IOError ):
        print('There was an error writing to the file')
        print( OSError ) if OSError else print( IOError )