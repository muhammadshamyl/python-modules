import re
if __name__=="__main__":
    sentence = "a man, a plan, a canal panama"
    sentence = sentence.replace(",","")
    sentence = sentence.replace(" ","")
    reverse = len(sentence)-1
    for item in range(len(sentence)):
        if sentence[item]!= sentence[reverse]:
            print("Sentence is not a palindrome.")
            break
        elif item == reverse:
            print("Sentence is a palindrome.")
        reverse-=1
