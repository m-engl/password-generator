import random
import string
import charSet as cs
import customWord as cw

# EXAMPLE:
# INPUT: cat wants food badly
# OUTPUT: cAt$wantS*(foOd_baDLy or cat+wants=food@badly or cAT,wants]fOOD[baDlY

sequence = "cat wants food badly"  # change to input

def spaces_to_specials(sign):
    if sign == " ":
        sign = random.choice(cs.specialChars)
        return sign
    else:
        return sign


specialSequence = ''.join(spaces_to_specials(sign) for sign in sequence) #  cat]wants$food-badly
specialSequenceMixed = ''.join(cw.randomize_case(sign) for sign in specialSequence) #  cat]wANTS$fOod-BadlY
mixedSequence = ''.join(cw.randomize_case(sign) for sign in sequence) #  CAtwantsfOoDBAdlY

print(specialSequence)
print(specialSequenceMixed)
print(mixedSequence)