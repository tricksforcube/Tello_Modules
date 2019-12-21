''' Tricks and Cube UI for Tello Say Hi to Your TEllo -- DSC happy Drone Flying :)'''

import tkinter as tki
import threading 
import time 
from tkinter import Toplevel, Scale,Frame
import tello_working

class Tello_updated:
    
    def __init__(self,tello):
        
        self.tello=tello # tello class object 
        
        self.root=tki.Tk() # main tkinter ui class call
        
        self.root.geometry("800x800")
        
        self.frame1=Frame(self.root, width=700, height=350, background="white")  # Partitioning the Root Frame into Four Frames for Adjusting the Controls
        self.frame1.grid(row=0, column=0)
        
        self.frame2=Frame(self.root, width=700, height=350, background="white")  # Partitioning the Root Frame into Four Frames for Adjusting the Controls
        self.frame2.grid(row=1, column=0)
        
        self.frame3=Frame(self.root, width=700, height=350, background="white")  # Partitioning the Root Frame into Four Frames for Adjusting the Controls
        self.frame3.grid(row=0, column=1)
        
        self.frame4=Frame(self.root, width=700, height=350, background="white")  # Partitioning the Root Frame into Four Frames for Adjusting the Controls
        self.frame4.grid(row=1, column=1)
        
        ''' Four Scale Bars are being used as slide conrtol for Tello Control 

Distance bar, Angle Bar, F_B bar , L_R bar

        '''
# Distance Bar : To move Tello in Up and Down directions

        self.distance_bar = Scale(self.frame1, from_=100, to=-100, tickinterval=0.01, digits=3, label='U-D(cm) ',

                                  resolution=0.02,length=250,width=50)
        self.distance_bar.set(0)

        self.distance_bar.pack(side="left")

        #Angle Bar : To move Tello in clock wise and anti-clock wise directions    
        
        self.angle_bar = Scale(self.frame3, from_=-180, to=180, tickinterval=0.01, digits=3, label='Angle(Degree)',

                                  resolution=0.02,length=250,width=50,orient = 'horizontal')

        self.angle_bar.set(0)

        self.angle_bar.pack(side="right")
        
		# lr_bar : TO Move the Tello in left and right directions
        
        self.lr_bar = Scale(self.frame3, from_=-150, to=150, tickinterval=0.01, digits=3, label='L-R(cm)',

                                  resolution=0.02,length=250,width=50,orient = 'horizontal')

        self.lr_bar.set(0)

        self.lr_bar.pack(side="right")
		
		# fb_bar : To Move the Tello in Forward and Reverse directions
        
        
        self.fb_bar = Scale(self.frame1, from_=150, to=-150, tickinterval=0.01, digits=3, label='F-R(cm) ',

                                  resolution=0.02,length=250,width=50)
        self.fb_bar.set(0)

        self.fb_bar.pack(side="left")

        
# Four Threads are being started to Control all the four bars for easy control of Tello Using the Scale Bar

        self.thread = threading.Thread(target=self.dist) # Thread for Distance bar

        self.thread.start()

        self.thread = threading.Thread(target=self.ang)   # Thread for Angle bar

        self.thread.start()
        
        
        self.thread = threading.Thread(target=self.fb)	# Thread for Forward Reverse bar

        self.thread.start()

        self.thread = threading.Thread(target=self.lr)  # Thread for Left Right bar

        self.thread.start()
        
        self.thread = threading.Thread(target=self.bat)
        
        self.thread.start()
        
        # Take off Button

        self.btn_takeoff = tki.Button(

            self.frame2, text="Takeoff", height=10,width=10, relief="ridge",command=self.telloTakeOff)

        self.btn_takeoff.pack(side="left",pady=10)     
        
# Land Button

        self.btn_land = tki.Button(

            self.frame2, text="Land", height=10,width=10, relief="ridge",command=self.telloLand)

        self.btn_land.pack(side="right",padx=10)
        
        
        
        

    # Tello UI Functions to Call the Main Tello Class Functions  for Tello Actions  
        
    
    def telloTakeOff(self):

        return self.tello.takeoff()                



    def telloLand(self):

        return self.tello.land()   
    
    
    
    def telloCW(self, degree):

        return self.tello.cw(degree)



    def telloCCW(self, degree):

        return self.tello.ccw(degree)
    
    
    
    
    def telloUp(self, dist):

        return self.tello.up(dist)



    def telloDown(self, dist):

        return self.tello.down(dist)
    
    
    def telloMF(self, distance):

        return self.tello.forward(distance)


    def telloMB(self, distance):

        return self.tello.back(distance)
    
    
    def telloML(self, distance):

        return self.tello.left(distance)



    def telloMR(self, distance):

        return self.tello.right(distance)
    
    def tello_battery(self):
        
        return self.tello.get_battery()
        
        
        
    def updateDistancebar(self):
        distance = self.distance_bar.get()
        self.distance_bar.set(0)
        print('reset distance to %.1f' % distance)
        print('\n')

            
    def updateanglebar(self):
        angle = self.angle_bar.get()
        self.angle_bar.set(0)
        print('reset angle to %.1f' % angle)  
        print('\n')    
            
            
            
    # Tello Distance Bar for moving Tello Up and Down        
    
    def dist(self):
    
    
        while True:
            time.sleep(5)
            dist=int(self.distance_bar.get())    # To get the current position of the Scale bar and to pass the value to tello up or down function for movement
                
            if(dist>0):# If dist is positive the UP action is triggered 
                print('up\n')
                print(self.distance_bar.get())
                self.telloUp(dist)
                time.sleep(3)
                self.distance_bar.set(0)# The scale bar is again set to 0 once the tello completes the action
                
            else:
                print('down\n')
                print(self.distance_bar.get())
                d1=abs(dist)
                self.telloDown(d1)
                time.sleep(3)
                self.distance_bar.set(0)  
    '''
 Tello is powerful but battery level is critical while flying so the below function will display the battery percentage during the drone flight
'''
                
    def bat(self):
        
        while True:
            
            battery_level=self.tello_battery()
            b_msg="Bat :" + str(battery_level) + "%"
            #time.sleep(2)
            messageVar = tki.Message(self.frame4, text = b_msg,width=85) 
            messageVar.pack() 
            time.sleep(2)
            messageVar.destroy()
            
    # Tello fb(Forward Back) Bar for moving Tello Forward  and Reverse                 
    
    def fb(self):
    
    
        while True:
            time.sleep(5)
            fb=int(self.fb_bar.get())
                
            if(fb>0):
                print('forward\n')
                print(self.fb_bar.get())
                self.telloMF(fb)
                time.sleep(3)
                self.fb_bar.set(0)
                
            else:
                print('reverse\n')
                print(self.fb_bar.get())
                fb1=abs(fb)
                self.telloMB(fb1)
                time.sleep(3)
                self.fb_bar.set(0)  
                
    
# Tello lr(left right) Bar for moving Tello left  and right 
                
    def lr(self):
    
    
        while True:
            time.sleep(5)
            lr=int(self.lr_bar.get())
                
            if(lr>0):
                print('Right\n')
                print(self.lr_bar.get())
                self.telloMR(lr)
                time.sleep(3)
                self.lr_bar.set(0)
                
            else:
                print('reverse\n')
                print(self.lr_bar.get())
                lr1=abs(lr)
                self.telloML(lr1)
                time.sleep(3)
                self.lr_bar.set(0)              
                    
    
# Tello angle Bar for moving Tello clockwsie  and anti clockwise directions   


    def ang(self):
        
        #print("in thread")
    
    
        while True:
            time.sleep(5)
            ang=int(self.angle_bar.get())
                
            if(ang>0):
                print('clockwise\n')
                print(self.angle_bar.get())
                self.telloCW(ang)
                time.sleep(3)
                self.angle_bar.set(0)
        
            else:
                print('anticlockwise\n')
                print(self.angle_bar.get())
                ag=abs(ang)
                self.telloCCW(ag)
                time.sleep(3)
                self.angle_bar.set(0)           
         
        
       

        
def main():
    
    drone = tello_working.Tello()  
    tu=Tello_updated(drone)
    tu.root.mainloop()
    
    
if __name__ == "__main__":

    main()    
