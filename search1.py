def find_python (string, python):
 """searches for the letters 'python' in the word."""
 for eachLetter in string:
    if eachLetter not in python:
        return False
 return True

def main():
 python = 'python'
 how_many = 0
 try:
 open ( "words.txt","U" ) 
#open the file
 except:
     print("No, no, file no here") #if file is not found
 for eachLine in fin:
    string = eachLine
    find_python(string, python)
if find_python(string, python) == True:
    how_many = how_many + 1
#increment count if word found
 print how_many#print out count
 fin.close()#close the file

if __name__ == '__main__':
main()
