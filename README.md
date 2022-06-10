# Full-DIR-File-Changer
This script will go through all files in a directory and allow you to edit each file line by line and add the new files to a new directory.

Files:
* [README.md](README.md)
* [dir-file-changer.py](dir-file-changer.py)


## Script output debug mode
```
$ python3 filechange.py
Debug is enabled and so only one file was displayed with changes made.  Nothig was saved.

###
###File will be printed here
###


###
Debug is enabled and so only one file was displayed with changes made.  Nothig was saved.
###
Number of files are marked to be changed: 4990
The working DIR is   : /path/to/workingdir/
The new DIR is       : /path/to/workingdir/newdir/
The new file will be : /path/to/workingdir/newdir/footer.php
```


## Script output debug mode off
```
$ python3 filechange.py
New file made: /path/to/workingdir/newdir/brandfooter.php
New file made: /path/to/workingdir/newdir/brandheader.php
New file made: /path/to/workingdir/newdir/closecontentwrapper.php
New file made: /path/to/workingdir/newdir/contentwrapper.php
New file made: /path/to/workingdir/newdir/crFunctions.php
