def countRemoveChar(str1, str2):
    count = 0
    for c1 in str1:
        if(c1 not in str2):
            count+=1
    for c2 in str2:
        if(c2 not in str1):
            count+=1
    return count

string1 = 'abcde'
string2 = 'bczah'
print(countRemoveChar(string1, string2))