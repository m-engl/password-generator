import string

#==================================================
#==================CHARACTER SETS==================
#==================================================

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits
specialChars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 

weakSet = lowerCase + numbers
mediumSet = lowerCase + upperCase + numbers
strongSet = lowerCase + upperCase + numbers + specialChars

#==================================================
#================SPECIAL CHARS DICT================
#==================================================

specialsDict = {
'A' : ['4', '@'],
'B' : ['8','3'],
'C' : ['<', '{', '[', '('],
'D' : [')', '>', '|)'],
'E': ['3'],
'F': ['#'],
'G' : ['6', '9'],
'H': ['4', '#'],
'I': ['1', '|', '!'],
'J': ['7', '|', ']'],
'K': ['|<', '1<', '<'],
'L': ['1_', '[', '1', '|'],
'M': ['44', '^^'],
'N':['|\|' , '/\/', '/V'],
'O': ['0', '()', '[]'],
'P': ['|o', '|O'],
'Q': ['O_', '0_' '9'],
'R': ['2', '12', '|2'],
'S': ['5', '$'],
'T': ['7', '+'],
'U': ['\/'],
'V': ['\/'],
'W': ['\/\/', '\X/', 'vv', 'VV'],
'X': ['%','><', ')('],
'Y': ['4', '7', '/'],
'Z': ['2', '7']
}