import re
def anagramSearcher(string1,string2):
    lis = re.split(" ",string1)
    print(lis)
    temp_list = []
    compare_list = list(string2)
    anagram_counter = 0
    compare_list.sort()
    for item in lis:
        print(item)
        temp_list = list(item)
        temp_list.sort()
        if temp_list == compare_list:
            anagram_counter +=1
    print("Total Anagrams: ", anagram_counter)

if __name__=="__main__":
    string1 = "what is up with you, mi amigo? Tell me nap pan anp pu pna"
    string2 = "nap"
    anagramSearcher(string1,string2)