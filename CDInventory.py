#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MList, 2020-Feb-23, Modified File by replacing inner lists with dictiionaries
# MList, 2020-Feb-24 Added delete functionality
# Mlist, 2020-Feb-24 Made file loading mandatory to prevent duplicates
# Mlist, 2020-Feb-24 Added error message in case deleted CD does not exist
# Mlist, 2020-Feb-24 Cleaning up code and adding comments
# Mlist, 2020-Feb-24 Improving SoC
#------------------------------------------#

#---------- DATA ----------#

# Declare variabls
strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
lstRow = []  # Row list variable for storing text file infomration while reading
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
Flag = True # flag to identify no found match for delete functionality

#---------- PROCESSING ----------#

# Attempting to load current iventory upon startup. Loading inventory from existing CDInventory.txt file has been made non-optional to avoid writing duplicates when deleting/saving edits with append
try:
    with open(strFileName, 'r') as objFile:
            for line in objFile:
                lstRow = line.strip().split(',')
                dicRow = {'ID': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist': lstRow[2]}
                lstTbl.append(dicRow)
            print('\nGood news! There is already a CDinventory.txt file. \nThe existing file has been loaded and any saved changes will overrite the existing file.')
except IOError: 
    print('\nThere is currently no existing inventory file - A new Inventory File will be creating when saving.\n')

#---------- PRESENTATION (Input/Output) (I/O) ----------#

print('\nThe Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

# Exit the program if the user chooses so
    if strChoice == 'x':
        break

# Add data to the table (2d-list) each time the user wants to add data
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # Ask for CD input
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        # casting input into dictionary
        dicRow = {'ID': intID, 'CD Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    # Display the current data to the user each time the user wants to display the data
    elif strChoice == 'i':
        print('ID, CD Title, Artist')
        for row_dic in lstTbl:
            row_dic_values = row_dic.values()
            print(*row_dic_values, sep = ', ')

    # Delete functionality
    elif strChoice == 'd':
        # Ask for entry to delete. This will need to the value of the album because artist is not a unique identifier and their could be potential duplicate IDs.
        CD = input('Which CD would you like to delete?: ')
        # Counter starting at 0 for cycling through the individual dictionaries. Need to reset counter to 0 in case user alread used delete functionality
        counter = 0
        # Defining a flag as false in case no match will be identified to print an error message
        Flag = False
        # For each dictionary row in the 2D list
        for row in lstTbl:
            # Assinging values of dictionary row to a variable
            row_values = row.values()
            # Checking if input matches any values of dictionary row
            if CD in row_values:
                # If match has been indentified use counter variable as index location for delete function in the 2D list
                del lstTbl[counter]
                print ('The requested CD has been deleted. Do not forget to save your changes!')
                # Setting Flag to true so error message does not get printed
                Flag = True
                break
            else:
                # If the input does not match the values of the dictionary row increase the counter by 1 and move to the next dictionary row in the 2D list
                counter += 1
        # If no match has been found and deleted the flag will still be False and an error message will be printed
        if Flag is False:
            print ('The requested CD does not exist in the inventory txt file')

    # Save the data to a text file CDInventory.txt if the user chooses so
    elif strChoice == 's':
        write_string = ''
        for row_dic in lstTbl:
            row_dic_values = row_dic.values()
            for item in row_dic_values:
                write_string += str(item) + ','
            write_string = write_string [:-1] + '\n'
        objFile = open(strFileName, 'w')
        objFile.write(write_string)
        objFile.close()
    else:
        print('Please choose either a, i, d, s or x!')

