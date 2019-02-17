###########################################################
##                                                       ##
##    Dictionary python script, find certain strings!    ##
##                                                       ##
###########################################################


# Read in text file.
# Have certain strings defined to look for
# Have an option to look for a new string
#if UInput == "y" or UInput == 'yes' or UInput == 'Y' or Uinput == 'Yes' or UInput == 'YES':
    #string = input("What string are you looking for? > ")
    #type(string)
DictList = ('isis, weapons, bombs, iraq, violence, death, kill')                # Terms to look for
print("These are the terms that are going to be searched for. \n[" + str(DictList) + "] \nDid you want to search for anything else? ")
select = input("> yes  or no: ")
if select == 'yes':
    NewList = input("Enter the new terms: (enter in this format (x, y, z))")
    FinalList = NewList + " " + DictList
else:
    FinalList = DictList

print ("Here's the list: [" + str(FinalList)  + ']')

filename = input("What's the name of the file? > ")                             # Grab the filename from the user
file_object = open(str(filename), "r")
file = file_object

FileContents = file.read()

i = 0

j = FileContents.count(FinalList)
type(FinalList)
length = len (FinalList)
for i in range(0, length):
    a = FinalList.index[i]
    for FinalList[i] in FileContents:
        result = FinalList[i] in FileContents
        if result == True:
            print (str(FinalList[i]) + " was found " + str(j) + " time(s)!")
        if result == False:
            print ("None of the search terms were found, sorry!")
