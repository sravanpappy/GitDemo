#########oops inheretence in part 2

# class Parent:
    # def __init__(self,name,age):
        # self.name=name
        # self.age=age
    # def disply(self):
        # print(self.name,self.age)
       
# class child(Parent):
    # def __init__(self,name,age):
        # self.name=name
        # self.age=age
        # self.lastname="Ganga"
    # def disply(self):
        # print(self.age,self.lastname,self.name)
       
# ob=child("Sravan",23)    
# ob.disply() 
def run_game():

    pygame.display.set_caption("Alien Invasion")
 # Set the background color.
    bg_color = (230, 230, 230)
 # Start the main loop for the game.
    while True:
 # Watch for keyboard and mouse events.
      
 # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
 # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()
    