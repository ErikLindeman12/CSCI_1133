#Final Project
#Erik Lindeman, LINDE799, 5424984
#CSCI 1133

import turtle

class County:
    def __init__(self,name,population):
        #setting up instance variables
        self.name = name
        self.population = population
        #Finding which population was the highest for scaling, checks each population to see if it's bigger than the current highest population
        self.highestPopulation = 0
        for x in range(0,len(self.population)):
            if(self.population[x]>self.highestPopulation):
                self.highestPopulation = self.population[x]
        #Sets equation of the line stuff to 0 so I can use "+=" later on
        self.m = 0
        self.b = 0
        #Setting up the County vs State specific things, ex. color and placement of title
        self.color = "red"
        self.extraDist = 0
        #Finds the equation for the line just so i don't have to later
        self.findEq()

    def findEq(self):
        #Finds the equation by using the equation given.  Uses a for loop so the code isn't as long
        for x in range(0,6):
            self.m += float(self.population[x])*(-1/7+x*2/35)
            self.b += float(self.population[x])*(11/21-x*3/21)
        #Rounds the equation to 4 Decimal Places to meet requirements
        self.m = round(self.m,4)
        self.b = round(self.b,4)

    def __lt__(self,rhand):
        #Just if the m of the right one is more than the left side, return true.
        if(self.m<rhand.m):
            return True
        else:
            return False

    def display(self,y_max=200):
        #Sets the x xcalar for later use (not really needed)
        xscalar = 110
        #Sets the scaling for the Y axis so the graph is spaced relative to the high population, rather than being a set scaling
        self.yscalar = (y_max+300)/self.highestPopulation
        #Basically just finds the highest population and rounds it to 1 sig fig so it can display the spacing increments on the graph.
        #If the turtle is at the origin (so bassically if this is the first time the turtle has run) set up the graph
        if(turtle.xcor() == 0 and turtle.ycor() == 0):
            #Setting up turtle settings
            turtle.color("black")
            turtle.hideturtle()
            turtle.speed(0)
            #Drwa the y axis
            turtle.penup()
            turtle.goto(-300,-300)
            turtle.pendown()
            turtle.goto(-300,y_max)
            #Draw the X axis
            turtle.penup()
            turtle.goto(250,-300)
            turtle.pendown()
            turtle.goto(-300,-300)
            turtle.penup()
            #Write titles for the Axes
            turtle.goto(-450,0)
            turtle.write("Population (people)")
            turtle.goto(0,-350)
            turtle.write("Date (years)")
            #Draw each increment on the X axis
            for x in range(1,6):
                turtle.penup()
                turtle.goto(-310+xscalar*x,-320)
                turtle.write("201{}".format(x))
                turtle.goto(-300+xscalar*x,-300)
                turtle.pendown()
                turtle.goto(-300+xscalar*x,-285)
            #Draw each increment on the Y axis
            for x in range(1,5):
                turtle.penup()
                turtle.goto(-300,-300+(300+y_max)/4*x)
                turtle.pendown()
                turtle.goto(turtle.xcor()+20,turtle.ycor())
                turtle.penup()
                turtle.goto(turtle.xcor()-70,turtle.ycor()-10)
                turtle.write(self.highestPopulation/4*x)
        #Change the color based on what it initialized as
        turtle.color(self.color)
        turtle.penup()
        for x in range(0,6):
            #Draww all 6 points, moving over 110 every time, and placing the y Axis spot relative to the Y scalar (so highest is on top)
            turtle.goto(x*xscalar-300,self.population[x]*self.yscalar-300)
            turtle.dot(6,self.color)
        #Draw the Line Based on the equation
        turtle.goto(-300,self.b*self.yscalar-300)
        turtle.pendown()
        turtle.goto(250,(self.b+5*self.m)*self.yscalar-300)
        turtle.penup()
        #Actually displays the Equation
        turtle.goto(turtle.xcor()+10,turtle.ycor())
        turtle.write("y={0}x+{1}".format(float(self.m),float(self.b)))
        #Displays the name either at the set height or a bit above it so the state and county doesn't overlap
        turtle.goto(-300,240+20*self.extraDist)
        turtle.write(self.name)

    def getName(self):
        #just makes it so the name can be obtained in other classes (this was written before I realized you could just do Object.variablename)
        return self.name


class State(County):
    def __init__(self,name,population,counties):
        #Initialize it with the county initialization (to not copy paste code basically)
        County.__init__(self,name,population)
        self.counties = counties
        #Overwrite the State/County specific variables to make it clear it's a state
        self.color = "blue"
        self.extraDist = 1

    def display(self):
        #Displays the State but with a specific y_max
        County.display(self,200)

    def greatestCounty(self):
        #Used for analysis, basically finds the largest county then returns it
        self.largestCounty = self.counties[0]
        for x in range(0,len(self.counties)):
            if(self.counties[x]>self.largestCounty):
                self.largestCounty = self.counties[x]
        return self.largestCounty

    def leastCounty(self):
        #Used for analysis, basically finds the Smallest county then returns it
        self.lowestCounty = self.counties[0]
        for x in range(0,len(self.counties)):
            if(self.counties[x]>self.lowestCounty):
                self.lowestCounty = self.counties[x]
        return self.lowestCounty

class Analysis:
    def __init__(self,state_list):
        #Sets up instance variables
        self.state_list = state_list

    def displayState(self,name):
        #Finds the state object based on the name, then displays it
        for x in range(0,len(self.state_list)):
            if(str(self.state_list[x].getName()) == name):
                self.state_list[x].display()

    def displayStateGreatestCounty(self,name):
        #Finds the state object based on the name
        for x in range(0,len(self.state_list)):
            if(str(self.state_list[x].getName()) == name):
                state = self.state_list[x]
        #Displays the state
        state.display()
        #Based on the y_scalar, it finds what to say as y_max so both the state and county are scaled the same
        y_max = float(state.yscalar)*float(state.greatestCounty().highestPopulation)-300
        #Finds the largest county then displays it with the y_max
        state.greatestCounty().display(y_max)

    def displayStateLeastCounty(self,name):
        #Finds the state object based on the name
        for x in range(0,len(self.state_list)):
            if(str(self.state_list[x].getName()) == name):
                state = self.state_list[x]
        #Displays the state
        state.display()
        #Based on the y_scalar, it finds what to say as y_max so both the state and county are scaled the same
        y_max = float(state.yscalar)*float(state.leastCounty().highestPopulation)-300
        #Finds the smallest county then displays it with the y_max
        state.leastCounty().display(y_max)

    def clear(self):
        #Sets up the desired clear function
        turtle.reset()

    def greatestState(self):
        #Finds the Greatest state, then returns its name
        self.greatest_state = self.state_list[0]
        for x in range(0,len(self.state_list)):
            if(self.state_list[x]>self.greatest_state):
                self.greatest_state = self.state_list[x]
        print(self.greatest_state.getName())

    def leastState(self):
        #Finds the loweest state, then returns its name
        self.least_state = self.state_list[0]
        for x in range(0,len(self.state_list)):
            if(self.state_list[x]<self.least_state):
                self.least_state = self.state_list[x]
        print(self.least_state.getName())

#Opens the CSV
censusdataobj = open("censusdata.csv",'r')
#Discards the first line (no actual data)
censusdataobj.readline()
#Sets the 2nd line to the data
data = censusdataobj.readline()
#So that it doesn't cause an error the first time (could use try catch I guess, but no real need)
begin = True
#Empty state list so I can append to it
stateList = []
#Does this while there is data to read
while not(data == ""):
    #Makes a list of all the data because CSV splits it by periods
    data = data.split(",")
    #If it's a state (or not a  county)
    if not("County" in data[0]):
        #If  it's not the loop, create a state variable in stateList
        if not(begin):
            stateList.append(State(currentState,statePopulation,countyList))
        else:
            #if it is the first loop, set begin o false
            begin = False
        #Set the current state name, and then find the population of the state in all 6 spots
        currentState = data[0]
        statePopulation = []
        for x in range(1,7):
            statePopulation.append(int(data[x]))
        #sets the countyList to empty so I can append to it
        countyList = []
    else:
        #Find the Name
        countyName = data[0]
        #prepare to find the population of each year
        countyPopulation = []
        for x in range(1,7):
            countyPopulation.append(int(data[x]))
        #make a new county in the countylist, to be added to the state variable once the next one comes
        countyList.append(County(countyName,countyPopulation))
    #read the next line (strategically at the end so if it's "", it doesn't error out or anything)
    data = censusdataobj.readline()
#Close the File
censusdataobj.close()
#setting up analysis object
analysis = Analysis(stateList)

#put testing code here, before turtle.done() so it doesn't close the window immediately
turtle.done()
