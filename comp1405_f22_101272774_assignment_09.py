#Hirad Showghi Sarkhosh
#101272774

#OMG, LOL, BTW, OMW
#][, |3, $, |-|

def capitalize(_str):
    string_cap = ""
    for x in _str:
        if ord(x) >= 97:
            string_cap = string_cap + chr(ord(x)-32)
        elif ord(x) < 91:
            string_cap = string_cap + x
    print(string_cap)
    return(string_cap)
    
    
def acronyms(_acr):  
    acronyms={"ON MY WAY":"OMW","BY THE WAY": "BTW","OH MY GOD": "OMG","LAUGHING OUT LOUD": "LOL"}
    i=0
    string_acr=""
    while i<len(_acr):
        found=False
        for key in acronyms:
            keyLen=len(key)
            if (i+keyLen)<=len(_acr):
                if _acr[i:i+keyLen]==key:
                    i=i+(keyLen)
                    string_acr=string_acr+acronyms[key]
                    found=True
                    break
        if not found:
            string_acr+=_acr[i]
            i+=1
    print(string_acr)
    return(string_acr)
    
def homo(_hm):
    homoglyphs={"I":"][","H":"|-|","S":"$","B":"|3"}
    i=0
    string_homo=""
    while i<len(_hm):
        found=False
        for key in homoglyphs:
            keyLen=len(key)
            if (i+keyLen)<=len(_hm):
                if _hm[i:i+keyLen]==key:
                    i=i+(keyLen)
                    string_homo=string_homo+homoglyphs[key]
                    found=True
                    break
        if not found:
            string_homo+=_hm[i]
            i+=1
    print(string_homo)

def main():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    #do ur thing
    print("Enter a sentence:")
    inputString = input()
    for char in inputString:
        if char not in punctuations:
            no_punct = no_punct + char
    print(no_punct)
    
    capitalizedString = capitalize(no_punct)
    string_w_acronyms = acronyms(capitalizedString)
    end_string = homo(string_w_acronyms)
    
    

if __name__ == "__main__":
    main()



