print("Program to copy contents of one file to another file by skipping line number 5\n\n\n")
file1 = open("sample1.txt", "w+")
file2 = open("sample2.txt", "w")
file1.write("""This is statement 1\nThis is statement 2\nThis is statement 3\nThis is statement 4\nThis is statement 5\nThis is statement 6\nThis is statement 7\n""")

file1.seek(0)
count = 1
for line in file1:
    if count != 5:
        file2.write(line)
    count +=1

file2.close()
file1.close()
print("Done. ")



