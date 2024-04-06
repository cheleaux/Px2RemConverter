import re
import sys
from os import chdir
from os.path import abspath, isfile
from  pathlib import Path
import logging


def pixelsToRem( matchObj ):
    value = matchObj.group(0)
    valueInt = int(value.strip('px'))
    remValueInt = valueInt/16
    remValue = str(remValueInt) + 'rem'
    return remValue

arguments = sys.argv[1:]


# Sort user and bash inserted arguments
if len( arguments ) != 2 :
    raise TypeError(f'1 argument expected. { min( 0, len( arguments ) - 1 ) } given.')
else:
    filePath = arguments[0]
    workingDirectory = arguments[1]


# Change directory and resolve path if it's a relative path
chdir( workingDirectory )
file = abspath( filePath ) if './' in filePath or '/c/' in filePath or 'C:' in filePath else abspath( './' + filePath )


# Check that the file exists and is operable
if isfile( file ):
    fileName = Path( file ).stem
    extName = Path( file ).suffix
    print(f'Converting unit values in { fileName + extName } ...')
else:
    raise FileNotFoundError(f'{ file } is not a file, is a directory or does not exist')


# Open the file and write to it with newly converter unit values
print('running pixel-rem unit conversion...')
with open( file, 'r+' ) as fileOpen:
    try:
        string = fileOpen.read()
        fileOpen.seek(0)
        fileOpen.write( re.sub( r'-*\d+px', pixelsToRem, string ))
        fileOpen.truncate()
        print(f'{ fileName } has been successfully converted to a Rem unit file.')
    except( OSError, IOError ) as error:
        print('Conversion unsuccessful!')
        logger = logging.getLogger(__name__)
        logger.error( error )
        raise