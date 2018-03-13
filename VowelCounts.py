import collections

file_Name = input("Enter the file to check: ").rstrip()
infile = open(file_Name, "r")

vowels = set("AEIOUaeiou")

countA = 0
countE = 0
countI = 0
countO = 0
countU = 0

c = collections.Counter(infile.read())

countA = sum(c[z] for z in c if z=='a' or z=='A' in vowels)
countE = sum(c[z] for z in c if z=='e' or z=='E' in vowels)
countI = sum(c[z] for z in c if z=='i' or z=='I' in vowels)
countO = sum(c[z] for z in c if z=='o' or z=='O' in vowels)
countU = sum(c[z] for z in c if z=='u' or z=='U' in vowels)

print("A:",countA)
print("E:",countE)
print("I:",countI)
print("O:",countO)
print("U:",countU)

