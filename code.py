

class Video:
    def __init__ (self):
        self.GameName=""
        self.cost=0
    def __repr__(self):
        return self.GameName + " cost $" + str(self.cost)
    def __add__(self,other):
        tc = self.cost + other.cost
        return "The cost of " + self.GameName + " + " + other.GameName + " is equal to $" + str(tc)
    def __sub__(self,other):
        tc = self.cost - other.cost
        if tc > 0:
            return self.GameName + "is $" +str(tc)+  "less than " + other.GameName
        elif tc < 0:
            return other.GameName + " is $" + str(abs(tc)) + " more than " +self.GameName
        elif tc == 0:
            return "They have the same cost"
class Game(Video):
    def __init__(self,n,c):
        Video.__init__(self)
        self.GameName=n
        self.cost=c
g1=Game("good",20)
g3=Video()
g2=Game("bad",30)
print(g1)
print(g1+g2)
print(g1-g2)
print(g3)
