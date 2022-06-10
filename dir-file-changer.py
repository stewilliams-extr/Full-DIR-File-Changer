import os

#This Script was made to change some 4 thousand PHP files to remove and change some lines in each file.

##Global Variables
 
#workingdir is where all your starting files are.
workingdir = ("/path/to/workingdir/")

#newdir is where you will place the files when done.
newdir = ("/path/to/workingdir/newdir/")

#filenamematch is for matching filenames in your dir so you dont edit unwanted files
#If empty It will check all files.
filenamematch = ("")

#If debug is = 1 only one file was displayed with changes made.  Nothig was saved. If 0 the script will run
debug = 1

#File changer
def file_changer(filename):
    newfile_str = ""
    with open(filename, 'r+', encoding = "ISO-8859-1") as file:
        for line in file.readlines():
            line = line.rstrip()
            #If's and elif for catching lines you want to change.  If you want to delete the line just use pass.
            
            #deleteing a line if it has loginCheck.php in it
            if "loginCheck.php" in line:
                pass

            #changeing the line with apple in it to say "New line for apple"
            elif "apple" in line:
                newfile_str += str("New line for apple") + "\n"

            #Else for printing inchanged lines
            else:
                newfile_str += str(line) + "\n"

        #setting the new file name and location
        newfile = (f'{newdir}{filename}')
        #Making New File with the changed lines
        if debug == 1:
            print ("Debug is enabled and so only one file was displayed with changes made.  Nothig was saved.")
            print ("")
            print (newfile_str)
            print ("")
            print ("###")
            print ("Debug is enabled and so only one file was displayed with changes made.  Nothig was saved.")
            print ("###")
            print (f'Number of files are marked to be changed: {len(file_list)}')
            print (f'The working DIR is   : {workingdir}')
            print (f'The new DIR is       : {newdir}')
            print (f'The new file will be : {newfile}')
        else:
            make_new = open(newfile, "w")
            make_new.writelines(newfile_str)
            print (f'New file made: {newfile}')
            make_new.close()
        file.close()

#Pulling the files from the workingdir and makeing them into a list.
file_list = []
for file in os.listdir(workingdir):
    if filenamematch in file:
        file_list.append(file)

for filename in file_list:
    file_changer(filename)
    #this will only check the first file for debug mode
    if debug == 1:
        break
