#CSCI 1133 Homework 7
#Erik Lindeman
#Problem 7B

class Member:
    def __init__(self,instrument,player):
        self.instrument = instrument
        self.player = player

    def getInstrument(self):
        return self.instrument

    def getPlayer(self):
        return self.player

    def setInstrument(self,instrument):
        self.instrument = instrument

    def setPlayer(self,player):
        self.player = player

    def __str__(self):
        return str(self.player)+" plays "+str(self.instrument)

    def __eq__(self,rhand):
        splayer = str(self.player).lower()
        sinst = str(self.instrument).lower()
        rplayer = str(rhand.player).lower()
        rinst = str(rhand.instrument).lower()
        if(splayer == rplayer and sinst == rinst):
            return True
        else:
            return False

class Band:
    def __init__(self,name,Members):
        self.name = name
        self.members = Members
        self.yeet = "Farquaad"

    def getBandName(self):
        return self.name

    def getPlayers(self):
        memberlist = []
        for x in range(0,len(self.members)):
            memberlist.append(self.members[x].getPlayer())
        return(memberlist)

    def getInstruments(self):
        d = {}
        for x in range(0,len(self.members)):
            instrument = self.members[x].getInstrument()
            instrument = instrument.lower()
            if(instrument in d):
                d[instrument]+=1
            else:
                d[instrument]=1
        return d

    def addMember(self,member):
        self.members.append(member)

    def removeMember(self,member):
        while(member in self.members):
            self.members.remove(member)

    def __str__(self):
        string = "Members of "+str(self.name)+":\n"
        for x in range(0,len(self.members)):
            string+=str(self.members[x])
            string+="\n"
        return string

    def findPlayer(self,player):
        newlist = self.members
        finallist = []
        for x in range(0,len(newlist)):
            if(str(newlist[x].getPlayer()).lower() == player.lower()):
                finallist.append(newlist[x])
        if(len(finallist) >0):
            for x in range(0,len(finallist)):
                print(finallist[x])
        else:
            print("{0} does not have any players named {1}".format(str(self.name),player))

    def findInstrument(self,instrument):
        newlist = self.members
        finallist = []
        for x in range(0,len(newlist)):
            if(str(newlist[x].getInstrument()).lower() == instrument.lower()):
                finallist.append(newlist[x])
        if(len(finallist) >0):
            for x in range(0,len(finallist)):
                print(finallist[x])
        else:
            print("{0} does not have any {1} players".format(str(self.name),instrument))
