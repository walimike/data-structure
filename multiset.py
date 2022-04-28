class Multiset:
    def __init__(self):
        self.set=[]

    def add(self, val):
        if val:
            self.set.append(val)
            return self.set

    def remove(self, val):
        for value in self.set:
            if value == val:
                self.set.remove(val)
        return self.set

    def __contains__(self, val):
        if val in self.set:
            return True
        return False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.set)

# m=Multiset()
# print(m.add(12))
# print(m.__contains__(12))
# print(m.__len__())
# print(m.remove(12))
# print(m.__contains__(12))
# print(m.__len__())
x=[1,2]
print