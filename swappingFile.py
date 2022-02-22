def swapFiles():
   f1Name = input("Enter name of first file: ")
   f2Name = input("Enter name of second file: ")
   f1Read = open(f1Name, "r")
   f1 = f1Read.read()
   f2Read = open(f2Name, "r")
   f2 = f2Read.read()
   temp = f1
   with open(f1Name, "w") as a:
      a.write(f2)
   with open(f2Name, "w") as b:
      b.write(temp)
swapFiles()
