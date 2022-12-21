# function to display word with longest length
def longestWord():
    longest_len = -1
    longest_word = ""
    j = 0
    while j < len_st:
        l = 0
        word = ""
        while(str1[j] != " "):
            word+=str1[j]
            l += 1
            j += 1
            if j>=len_st:
                break
        if longest_len < l:
            longest_len = l
            longest_word = word
        j += 1
    print("Longest word: ", longest_word)

# --------------------------------------------------------------------
# function to calculate frequency of a character
def freqChar():
    char_count = 0
    for i in str1:
        if i == char:
            char_count += 1
    print(f"Count of the character '{char}' is = {char_count}")

# --------------------------------------------------------------------
# function to check wehter the given string is pallindrome or not
def isPalindrome():
    s = ""
    for i in range(len_st-1, -1, -1):
        s += str1[i]
    if s == str1:
        print("Given String is a Pallindrome")
    else:
        print("Given String is Not a Pallindrome")

# --------------------------------------------------------------------
# function to display first index of appearance of a sub-string
def calcIndexSubstr():
    len_substr = 0
    finalIndex = 0
    # calculating length of sub-string
    for t in substr:
        len_substr += 1
        
    for p in range(len_st):
        tempStr = ""
        index = p
        for q in range(len_substr):
            tempStr += str1[index]
            index += 1
        if (tempStr == substr):
            finalIndex = p
            break
    print("Index of First occurence of substring : ", finalIndex)

# --------------------------------------------------------------------
# function to count occurance of each word
def countWord():
    new_w = []
    wd = []
    w = []
    x = 0

    while x<len_st:
        k = ""
        while(str1[x] != " "):
            k+=str1[x]
            x += 1
            if x>=len_st:
                break
        if k not in new_w:
            new_w.append(k)
        w.append(k)
        x+=1

    for i in new_w:
        word_count = 0
        for j in w:
            if i == j:
                word_count += 1
        wd.append(word_count)
    y = 0
    
    print("Word Counts: ")
    for k in new_w:
        print(f"{k} -> {wd[y]}") 
        y += 1

# --------------------------------------------------------------------
# input data
str1 = input("Enter a string: ")
char = input("Enter Character to be searched: ")
substr = input("Enter Substring to be searched: ")

# calculating length of main string
len_st = 0
for i in str1:
    len_st+=1

# calling functions
longestWord()
freqChar()
isPalindrome()
calcIndexSubstr()
countWord()
