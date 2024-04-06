# Pixel To Rem Unit Converter

Primarliy for use on CSS files where majority of element properties are defined with a 'px' (pixels) unit value, or any document that requires all rem values.

## Using rem values ensures that:

- User preferences are preserved and respected
- Its possible to adjust the apparent font size across the board, proportionally.

## How to Use

Once youve cloned to repo place the pxToRemConverter directory into you `$HOME/bin` directory, or any directory that you have dedicatied to housing your custom executables and is in you `$PATH`.
If you haven't made such a directory, [learn how here](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7).

Makes sure to change to change the cd path in the bash file, ending in `.sh`, to the `$PATH` path where you put the pxToRemConverter directory. Other the script won't be able to find remconverter.py.

```
cd /c/Users/MyUser/bin/PxToRemConverter/
```


Then place the bash file into `$HOME/bin` outside of the pxToRemConverter directory.
You can now execute `pxToRem.sh` on any file.

```
pxToRem.sh /c/Users/MyUser/desktop/projects/someProject/styles.css
```

This script also supports relative paths: 

```
pxToRem.sh ./someProject/styles.css
```

or

```
pxToRem.sh styles.css
```
