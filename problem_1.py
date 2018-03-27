import re

address1 = input('input address 1 : ').lower()
address2 = input('input address 2 : ').lower()
splittedAddr1 = re.split('\\.|\\. |,|, |-| - |/| ', address1)
splittedAddr2 = re.split('\\.|\\. |,|, |-| - |/| ', address2)
count1 = 0
count2 = 0
similarity = 0

# compare splittedaddr1 with address2
for word in splittedAddr1:
    if word in address2:
        count1+=1

# compare splittedaddr2 with address1
for word in splittedAddr2:
    if word in address1:
        count2+=1

if(count1 > count2):
    similarity = (count1/len(splittedAddr1))*100
else:
    similarity = (count2/len(splittedAddr2))*100

print('Similarity between address 1 and address 2 is {0:.2f}%'.format(similarity))