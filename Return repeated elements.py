#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#Examples (Input -> Output):
#* "String"      -> "SSttrriinngg"
#* "Hello World" -> "HHeelllloo  WWoorrlldd"
#* "1234!_ "     -> "11223344!!__  "

def double_char(s):
    x = []
    for i in range(len(s)):
        x.append(s[i])
        x.append(s[i])
    print(''.join(x))
    return(''.join(x))
