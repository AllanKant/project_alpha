class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.my_list = []
        self.my_lister()

    def my_lister(self):
        x = self.start
        while x<self.end:
            self.my_list.append(x)
            x+=1
        return self.my_list
    
    def __iter__(self):
        return iter(self.my_list)
        
    

for x in Counter(20, 30):
    print(x)