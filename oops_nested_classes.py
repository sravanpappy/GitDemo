###########Nested classes####

# class Human:
    # def __init__(self):
        # self.name="Sravan"
        # self.head=self.Head()
        
    # def display(self):
        # print("name:",self.name)
        # self.head.talk()
        # self.head.brain.think()
        
    # class Head:
        # def __init____(self):
            # self.brain=self.Brain()
            
        # def talk(self):
            # print("Thinking---")
            
        # class Brain:
            # def think (self):
                # print("Talkig.......")
               
# h=Human()
# h.display()

class person:   
    def __init__(self):
        self.name="Sravan"
        self.dob=self.DOB()
    
    def display(self):
        print("Name:",self.name)
        self.dob.display()
       
    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=12
            self.yyyy=2014
          
        def display(self):
            print("Date of birth {}/{}/{}".format(self.dd,self.mm,self.yyyy))
           
p=person()
p.display()           
        