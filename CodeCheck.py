'''
Esther He
February 3, 2020

CodeCheck.py takes in a valid input file and outputs the following:
Total # of lines:
Total # of comment lines:
Total # of single line comments:
Total # of comment lines within block comments:
Total # of block line comments:
Total # of TODO’s:

Note: a valid input file is defined as a file with a filename that does not start with '.', and contains an extension

1) When a file is checked in, scan the file to count the total number of lines.
2) Scan the file to identify comments and count the total lines of comments in the file.
3) After identifying the lines of comments, scan to segregate the total number of single line
comments and the total number of multi-line comments.
4) Any line of code that has a trailing comment should be counted both as lines of code
and also a comment line.
5) Finally, from all the comments in the file, identify and count the total number of TODOs.
6) Please note, that the file that is being checked in could be any valid program file. Files
checked in without an extension can be ignored. You can also ignore file names that
start with a ‘.’.

Assumptions:
1. Docstrings are ignored.
2. Block comments are consecutive lines that start with a '#'.
3. A single line comment is a line that starts with a '#', but does not belong to a block comment.
4. TODO lines are lines that start with '# TODO'. If a TODO line does not belong to a block comment, it is then counted as a single line comment.
5. Inline comments count as single line commnets, but are not counted towards bloack comments.
'''

class codeCheck:
    def __init__(self, FIN):
        # open input file to read, handle errors with try & except
        try:
            f = open(FIN, 'r')
        except:
            print("ERR: file", FIN, "is not present or can't be opened.")

        tempLines = f.readlines()       # read the lines in the file
        f.close()                       # close file

        accum = []                      # initialize temporary accumulator

        for line in tempLines:          # parse at each \n character and accumulate non '\n' lines
            accum += [(line.split('\n'))[0]]

        self.store = list(accum)        # save parsed code in class variable - store
        self.numLines = len(self.store) # save the total number of lines of code in class variable - numLines

        # initialize temporary variables
        tempComIdx = []                 # line number of comment lines
        tempNumTODOS = 0                # number of TODO's
        tempNumInlineCom = 0            # number of inline comments

        # iterate through each line of the parsed code
        for i in range(0, self.numLines - 1, 1):
            # check for the substring '# TODO' at index 0 to see if the line is a TODO line
            if ((self.store[i]).upper()).find('# TODO') != -1:
                tempNumTODOS += 1
                tempComIdx += [i]
            # if it's not a TODO line, check for the substring '  # ' at index 0 to see if it's a single line comment
            elif (self.store[i]).find('#') != -1:
                tempComIdx += [i]
            # if it's neither, check if the line contains the substring anywhere to see if it's an inline comment
            elif (self.store[i]).find('#') != -1:
                tempNumInlineCom += 1

        self.numCom = len(tempComIdx) + tempNumInlineCom  # find the total number of comment lines
        self.numTODOS = tempNumTODOS  # save the total number of TODO's

        # for k in tempComIdx:      # debug
        #    print(self.store[k])

        # initialize temporary variables
        tempBlockComIdx = []  # line number of block comment lines
        tempNumBlockCom_lines = 0  # number of lines within block comments
        tempNumBlockCom = 0  # number of block comments
        blockCom = False  # boolean for keeping track of the number of block comments

        j = 0
        while (j <= len(tempComIdx) - 2):  # iterate through the comment lines
            if (tempComIdx[j + 1] == tempComIdx[j] + 1):  # if the next comment line is consecutive to the current one
                tempNumBlockCom_lines += 1  # increment the number of lines within block comment by 1
                blockCom = True  # toggle blockCom boolean to True
                # print(self.store[j]) # debug
            else:
                if blockCom:  # this is the end of a block comment
                    tempNumBlockCom_lines += 1  # account for the first comment line in this block comment
                    blockCom = False  # toggle blockCom boolean to False
                    tempNumBlockCom += 1  # increment the number of block comments
            j += 1

        # account for the case where the last block comment extends to the last line
        if blockCom:
            tempNumBlockCom += 1
            tempNumBlockCom_lines += 1

        self.numBlockCom_lines = tempNumBlockCom_lines
        self.numBlockCom = tempNumBlockCom
        self.numSingleCom = self.numCom - self.numBlockCom_lines

    # 1. class function getNumLines() returns the total number of lines in the file
    def getNumLines(self):
        return self.numLines

    # 2. class function getNumCom() returns the total number of comment lines in the file
    def getNumCom(self):
        return self.numCom

    # 3. class function getNumSingleCom() returns the total number of single comment lines in the file
    def getNumSingleCom(self):
        return self.numSingleCom

    # 4. class function getNumBlockCom returns the total number of comment lines within the block comments in the file
    def getNumBlockCom(self):
        return self.numBlockCom

    # 5. class function getNumBlockCom_lines returns the total number block line comments
    def getNumBlockCom_lines(self):
        return self.numBlockCom_lines

    # 6.  class function getNumTODOS returns the total number of TODO's
    def getNumTODOS(self):
        return self.numTODOS

# main program
def main():
    FIN = str(input("Please enter the file name: "))  # acquire input file
    # handle illegal file names
    if FIN.find('.') == -1:  # file name does not contain an extension
        print("ERR: input file does not have an extension")
    elif FIN.find('.') == 0:  # file name starts with '.'
        print("ERR: input file name cannot start with '.'")
    else:
        x = codeCheck(FIN)
        print("Total # of lines: ", x.getNumLines())
        print("Total # of comment lines: ", x.getNumCom())
        print("Total # of single line comments: ", x.getNumSingleCom())
        print("Total # of comment lines within block comments: ", x.getNumBlockCom_lines())
        print("Total # of block line comments: ", x.getNumBlockCom())
        print("Total # of TODO’s: ", x.getNumTODOS())

main()
