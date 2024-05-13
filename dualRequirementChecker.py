#dual requirement checker

fileSE = open("Sustainability Experience.txt","r") 
fileGAE = open("Global Awareness Experience.txt","r") 
fileDR = open("Dual Requirement.txt","w+") #Creates a file that will be used to store classes that fufills both requirements

lines_fileSE = fileSE.readlines()
lines_fileGAE = fileGAE.readlines()


for lineSE in lines_fileSE:
    for lineGAE in lines_fileGAE:
        if (lineGAE == lineSE):
            fileDR.write(lineGAE)
            print(lineGAE)
            break

