def countvowel(str):
    L = [c in 'aieou' for c in str]
    return sum(L)

def rotate (S, n):
    if 'a' <= S <= 'z':
        neword = ord(S) + n
        if neword <= ord('z'):
            return chr(neword)
        else:
            return chr(neword - ord('z') + ord('a') - 1)
    elif 'A' <= S <= 'Z':
        neword = ord(S) + n
        if neword <= ord ('Z'):
            return chr(neword)
        else:
            return chr(neword - ord('Z') + ord('A') -1)     
    else:
        return S
        
def encipher ( c, n ):
    result = ""
    for S in c:
        result += rotate( S , n)
    return result

def decipher ( S ):
    L = [encipher(S,n) for n in range (26)]
    scoredList = [[probScore(a),a] for a in L]  #takes sum of the letter probabilities in string
    best = max(scoredList) #takes the highest score of all possibilities
    return best[1] #prints highest score

def score(L):
    newL = [[countvowel(s),s] for s in L]
    return newL

def probScore(S):
    probs = [letProb(c) for c in S]
    return sum(probs)

def letProb(c):
    """ if c is the space character or an alphabetic 
    character, return its monogram probability (for english), 
    otherwise return 1.0 We ignore capitalization. 
    Adapted from 
    http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en
    _stat.html 
    """ 
    if c == ' ': return 0.1904 
    if c == 'e' or c == 'E': return 0.1017 
    if c == 't' or c == 'T': return 0.0737 
    if c == 'a' or c == 'A': return 0.0661 
    if c == 'o' or c == 'O': return 0.0610 
    if c == 'i' or c == 'I': return 0.0562 
    if c == 'n' or c == 'N': return 0.0557 
    if c == 'h' or c == 'H': return 0.0542 
    if c == 's' or c == 'S': return 0.0508 
    if c == 'r' or c == 'R': return 0.0458 
    if c == 'd' or c == 'D': return 0.0369 
    if c == 'l' or c == 'L': return 0.0325 
    if c == 'u' or c == 'U': return 0.0228 
    if c == 'm' or c == 'M': return 0.0205 
    if c == 'c' or c == 'C': return 0.0192 
    if c == 'w' or c == 'W': return 0.0190 
    if c == 'f' or c == 'F': return 0.0175 
    if c == 'y' or c == 'Y': return 0.0165 
    if c == 'g' or c == 'G': return 0.0161 
    if c == 'p' or c == 'P': return 0.0131 
    if c == 'b' or c == 'B': return 0.0115 
    if c == 'v' or c == 'V': return 0.0088 
    if c == 'k' or c == 'K': return 0.0066 
    if c == 'x' or c == 'X': return 0.0014 
    if c == 'j' or c == 'J': return 0.0008 
    if c == 'q' or c == 'Q': return 0.0008 
    if c == 'z' or c == 'Z': return 0.0005 
    return 1. 
    
