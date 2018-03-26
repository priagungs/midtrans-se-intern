class names:
    def __init__(self):
        self.element = []
    
    def find(self, keyword):
        count = 0
        for name in self.element:
            found = True
            for i in range(len(keyword)):
                if keyword[i] != name[i]:
                    found = False
            if found:
                count+=1
        return count
    
    def add(self, name):
        self.element.append(name)


dataNames = names()
n = int(input('input : '))
for i in range(n):
    inp = input().split()
    if(inp[0] == 'add'):
        dataNames.add(inp[1])
    elif(inp[0] == 'find'):
        print(dataNames.find(inp[1]))


