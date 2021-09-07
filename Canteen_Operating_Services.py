import time
import re
#import functions across files
import Waiting_Time
import Search_Screen
#load and launch pygame
import pygame
pygame.init()
 
#Set Screen Display Size[Width, Height] and Title
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Canteen Information')
 
#Defining clock
clock = pygame.time.Clock()
 
 
#Colour definitions in RGB tuple
black = (0, 0, 0)
green = (0, 200, 0)
white = (255,255,255)
bright_green = (0,255,0)
burly_wood1 = (255,211,155)
cadet_blue3 = (122,197,205)
 
 
#Button 1 position and size
button1_x = 195     #button x coordinate
button1_y = 400     #button y coordinate
button1_w = 420      #button width
button1_h = 50       #button height
 
#Button 2 position and size
button2_x = 195     #button 2 x coordinate
button2_y = 470     #button 2 y coordinate
button2_w = 420      #button 2 width
button2_h = 50       #button 2 height
 
#Tuple every stores days opening by breakfast and lunch_dinner to make the dictionary neater
KFC_Breakfast_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
KFC_Lunch_Dinner_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Subway_Breakfast_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Subway_Lunch_Dinner_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Mcdonalds_Breakfast_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Mcdonalds_Lunch_Dinner_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
SandwichGuys_Breakfast_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
SandwichGuys_Lunch_Dinner_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
LongJohnSilvers_Breakfast_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
LongJohnSilvers_Lunch_Dinner_Days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
 
#Dictionary for the Operating Shops in terms of ( (Days Open), (Duration Open for), (Title of menu image))
shops_operating = {
    'KFC' : [(KFC_Breakfast_Days,range(700,1100), 'Kfc_B1'), (KFC_Lunch_Dinner_Days,range(1100,2200), 'Kfc_L1')],
    'Subway' : [(Subway_Breakfast_Days,range(800,1100), 'Subway_B1'), (Subway_Lunch_Dinner_Days,range(1100,2200), 'Subway_L1')],
    'McDonalds' : [(Mcdonalds_Breakfast_Days,range(800,1100), 'Mcd_B1'), (Mcdonalds_Breakfast_Days,range(1100,2200), 'Mcd_L1')],
    'Sandwich Guys' : [(SandwichGuys_Breakfast_Days,range(800,1100), 'Tsg_B1'), (SandwichGuys_Lunch_Dinner_Days,range(1100,2200), 'Tsg_L1')],
    'Long John Silvers' : [(LongJohnSilvers_Breakfast_Days,range(800,1100), 'Ljs_B1'), (LongJohnSilvers_Lunch_Dinner_Days,range(1100,2200), 'Ljs_L1')]
}
 

#Defining Text Display
def text_display(text, colour, size, x, y):
    font = pygame.font.SysFont(None, size)
    text = font.render(text, True, colour)
    screen.blit(text, (x, y))       #x and y are the pixel coordinates
 

#Defining theTime()
def theTime(length,time_x,size):
    theTime=time.strftime("%A, %d %b %Y %H:%M:%S", time.localtime())
    pygame.draw.rect(screen, black, (0, 0, length, 35))
    text_display(theTime, white, size, time_x, 5)
    #screen is updated only at the clock section
    pygame.display.update(pygame.Rect(0, 0, length, 35))
    clock.tick(60)
 

#Defining the Back Button
def backButton(bb_x, bb_y):
    pygame.draw.rect(screen, burly_wood1, (bb_x, bb_y, 90, 50))
    text_display('Back', black, 40, (bb_x+10), (bb_y+10))
    pygame.display.update(pygame.Rect(bb_x, bb_y, 90, 50))
    mouse = pygame.mouse.get_pos()
    
    for event in mouse:
        #To make the button interactive
        if bb_x <= mouse[0] <= (bb_x + 90) and bb_y <= mouse[1] <= (bb_y + 50):
            #To give the button a function when it is pressed
            for event1 in pygame.event.get():
                if event1.type == pygame.MOUSEBUTTONDOWN:
                    return 1
 

#Defining Operating Hours List
def operating_hours(image_title):
    
 
    #Load Image for operating hours
    operating_image = pygame.image.load("%s2.png" %image_title)
    operating_image_r = pygame.transform.scale(operating_image, (620,936)).convert()
    
 
    #Keeps the window running while this is up
    operating = True
 
    while operating:
        #Set Screen Display Size[Width, Height] and Title
        screen = pygame.display.set_mode([620,936])
        pygame.display.set_caption('Operating Hours')
 
        #Quit when closed
        for event in pygame.event.get():   #User did something
            if event.type == pygame.QUIT:  #If user clicked close
                
                operating = False                #Flag that user is done and exits this loop
                
 
        #Make the image the background
        screen.blit(operating_image_r,(0,0))
        #Tells user to close the window to go back to view the menu list
        text_display("Close Window to view the Menu List", white, 40, 70, 20)
        pygame.display.update()
        clock.tick()
    #Goes to display menu
    menu(image_title)
 

#Defining Menu Page
def menu(image_title):
    #Set Screen Display Size[Width, Height] and Title
    screen = pygame.display.set_mode([750,964])
    pygame.display.set_caption('Menu Lists')
 
    screen.fill((0,0,0))
    #Load menu image as background
    menu_image = pygame.image.load("%s.png" %image_title)
    menu_image_r = pygame.transform.scale(menu_image, (750,964)).convert()
    screen.blit(menu_image_r,(0,-20))
 
    menu_list = True
 
    #Defining Button 3 which is Operating Hours
    button4_x = 60
    button4_y = 5 
    button4_w = 180
    button4_h = 30
    button5_x = button4_x+200
    button5_w = button4_w+65
 
    #Loop until the user clicks either button or close the application
    while menu_list:
    
        #Quit when closed
        for event in pygame.event.get():   #User did something
            if event.type == pygame.QUIT:  #If user clicked close
                
                menu_list = False                #Flag that user is done and exits this loop
 
 
        #Drawing a rectangle to act as the button
        pygame.draw.rect(screen, white, (button4_x, button4_y, button4_w, button4_h))       
        #Display text for Operating Hours
        text_display('Operating Hours', black, 30, (button4_x+5), (button4_y + 5))
        pygame.display.update(pygame.Rect(button4_x, button4_y, button4_w, button4_h))
 
        #To get the position of the cursor within the window screen
        mouse = pygame.mouse.get_pos()
 
        #To iterate through each of the x and y coordinates of the cursor
        for event in mouse:
            #To make the button interactive
            if button4_x <= mouse[0] <= (button4_x + button4_w) and button4_y <= mouse[1] <= (button4_y + button4_h):
                #To give the button a function when it is pressed
                for event4 in pygame.event.get():
                    if event4.type == pygame.MOUSEBUTTONDOWN:
                        operating_hours(image_title)
                        return   
                        
 
        #Drawing a rectangle to act as the button
        pygame.draw.rect(screen, white, (button5_x, button4_y, button5_w, button4_h))       
        #Display text for Calculate Waiting Time
        text_display('Calculate Waiting Time', black, 30, (button5_x + 10), (button4_y + 5))
        pygame.display.update(pygame.Rect(button5_x, button4_y, button5_w, button4_h))

        for event in mouse:
            #To make the button interactive
            if button5_x <= mouse[0] <= (button5_x + button5_w) and button4_y <= mouse[1] <= (button4_y + button4_h):
                #To give the button a function when it is pressed
                for event5 in pygame.event.get():
                    if event5.type == pygame.MOUSEBUTTONDOWN:
                        value = Waiting_Time.waiting_time(300, 235, 140, 32)
                        if value == 'menu':
                            return 2

        #Signal for back button
        bb = backButton(320,760)
        if bb == 1:
            return 1
        
        pygame.display.update()
        clock.tick()


#Defining Today's stores that are open
def main1():
    
    today_stores = True
 
    #Loop until the user clicks either button or close the application
    while today_stores:
        
 
        #Defining the "View Today's Stores" window's size and title
        screen = pygame.display.set_mode([400,570])
        pygame.display.set_caption('View Today\'s Stores')
        screen.fill((230,230,230))
        
        #Giving value to a signal that will be used to stop the loop when the window closes
        signal = 1
        #Quit when closed
        for event in pygame.event.get():   #User did something
            if event.type == pygame.QUIT:  #If user clicked close
                return 0                #Flag that user is done and exits this loop
 
         
 
        #Clock display on the top centered
        theTime(400,15,35)
 
        #Tells user to choose a store
        text_display("Choose a Store:", black, 35, 105, 70)
        #Values for button
        button3_x = 160
        button3_y = 140
        button3_w = 80
        button3_h = 50
        #Iteration of the dictionary into the tuple to compare with the current timing that was previously given in the main loop
        for keys, values in shops_operating.items():
            for name,time,image in values:
                if current_day in name and int(current_timing) in time:
                    
                    #Stops the loop when the window closes to prevent any new boxes to be generated
                    if signal == 0:
                        break
                    #Drawing a rectangle to act as the button
                    pygame.draw.rect(screen, burly_wood1, (button3_x, button3_y, button3_w, button3_h))       
                    #Display text for View Today Store
                    text_display('%s'%keys, black, 40, (button3_x+10), (button3_y + 12))
                    pygame.display.update(pygame.Rect(button3_x, button3_y, button3_w, button3_h))
 
                    #To get the position of the cursor within the window screen
                    mouse = pygame.mouse.get_pos()
 
                    #Get the name of menu
                    image_title = image
                    #To iterate through each of the x and y coordinates of the cursor
                    for event in mouse:
                        #To make the button interactive
                        if button3_x <= mouse[0] <= (button3_x + button3_w) and button3_y <= mouse[1] <= (button3_y + button3_h):
                            #To give the button a function when it is pressed
                            for event3 in pygame.event.get():
                                if event3.type == pygame.MOUSEBUTTONDOWN:
                                    #Loads the menu images
                                    menu(image_title)
                                    #Sends a signal to the program to stop the loop in the box generation list
                                    signal = 0
                                    #When back button is pressed on menu(image title)
                                    if menu(image_title) == 1:
                                        return 2
                                    #When the back button is pressed in the calculate waiting time
                                    elif menu(image_title) == 2:
                                        return 2
                                    #When the user closes the menu(image title) window
                                    else:
                                        return 0
                                    
                    #Adjust to the size of the text as the list increases
                    button3_x -= 22
                    button3_y += 70
                    button3_w += 50

        #Signal for back button
        bb = backButton(150,500)
        if bb == 1:
            return 1
                
        pygame.display.update()
        clock.tick()
 

#Defining the window for View Stores by other dates
def main2():
    #Instantiate the search module to get the user input in terms of date time
    user_datetime = Search_Screen.search_box(300, 235, 200, 30)
    
    #Returns a value 1 to allow it to loop back to the main_menu()
    if user_datetime == 'menu':
        return 2
    
    user_date = user_datetime[0]
    user_time = user_datetime[1]

    clock = pygame.time.Clock()
    
    
    desired_dates = True

    #Loop until the user clicks either button or close the application
    while desired_dates:

        #Defining the "View Store's that are opened at your time" window's size and title
        screen = pygame.display.set_mode([400,570])
        pygame.display.set_caption('View Store\'s that are opened at your time')
        screen.fill((230,230,230))
        
        #Giving value to a signal that will be used to stop the loop when the window closes
        signal = 1
        #Quit when closed
        for event in pygame.event.get():   #User did something
            if event.type == pygame.QUIT:  #If user clicked close
                #Tells the program to stop the loop in the box generation list
                signal = 0
                return 0                #Flag that user is done and exits this loop

        #Clock display on the top centered
        theTime(400,15,35)

        #Tells user to choose his desired store to check on the store
        text_display("Choose a Store:", black, 35, 105, 70)
        #Button 3 definition
        button3_x = 160
        button3_y = 140
        button3_w = 80
        button3_h = 50
        #Iteration of the dictionary into the tuple to compare with the desired timing that was inputted by user
        for keys, values in shops_operating.items():
            for name,time,image in values:
                if user_date in name and int(user_time) in time:
                    
                    #Stops the loop when the window closes to prevent any new boxes to be generated
                    if signal == 0:
                        break
                    #Drawing a rectangle to act as the button
                    pygame.draw.rect(screen, burly_wood1, (button3_x, button3_y, button3_w, button3_h))       
                    #Display text for View Today Store
                    text_display('%s'%keys, black, 40, (button3_x+10), (button3_y + 12))
                    pygame.display.update(pygame.Rect(button3_x, button3_y, button3_w, button3_h))

                    #To get the position of the cursor within the window screen
                    mouse = pygame.mouse.get_pos()

                    #Get the name of menu
                    image_title = image
                    #To iterate through each of the x and y coordinates of the cursor
                    for event in mouse:
                        #To make the button interactive
                        if button3_x <= mouse[0] <= (button3_x + button3_w) and button3_y <= mouse[1] <= (button3_y + button3_h):
                            #To give the button a function when it is pressed
                            for event3 in pygame.event.get():
                                if event3.type == pygame.MOUSEBUTTONDOWN:
                                    #Loads up menu
                                    menu(image_title)
                                    #Loops back to main2()
                                    if menu(image_title) == 1:
                                        continue
                                    #Loops back to main_menu()
                                    elif menu(image_title) == 2:
                                        continue
                                    #Breaks out of loop to quit
                                    else:
                                        signal = 0
                                        return 0
                                    
                    #Adjust the box size accordingly to fit the shop title
                    button3_x -= 22
                    button3_y += 70
                    button3_w += 50

        #Defining Home X and Y coordinates and Home button itself
        hm_x = 150
        hm_y = 500
        pygame.draw.rect(screen, burly_wood1, (hm_x, hm_y, 100, 50))
        text_display('Home', black, 40, (hm_x+10), (hm_y+10))
        pygame.display.update(pygame.Rect(hm_x, hm_y, 100, 50))
        mouse = pygame.mouse.get_pos()
        
        for event in mouse:
            #To make the button interactive
            if hm_x <= mouse[0] <= (hm_x + 90) and hm_y <= mouse[1] <= (hm_y + 50):
                #To return a value 2 when press, sending it back to home
                for event1 in pygame.event.get():
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        return 2
                


        pygame.display.update()
        clock.tick()


#Defining Main Menu
def main_menu():
 
    #Load NTU LOGO [CHANGE THE DIRECTORY TO WHERE YOUR NTU LOGO IS LOCATED OR JUST HASTAG STATEMENT 59-63 TO IGNORE NTU LOGO]
    ntu_logo = pygame.image.load("ntu_logo.png")    
    #Resize NTULOGO to width = 500 and height = 250
    ntu_logo_r = pygame.transform.scale(ntu_logo, (550,198))
    
    menu = True
 
    #Loop until the user clicks either button or close the application
    while menu:
 
        #Set Screen Display Size[Width, Height] and Title
        screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Canteen Information')
        #Screen Filled with White Color
        screen.fill((255,255,255)) 
        #Quit when closed
        for event in pygame.event.get():   #User did something
            if event.type == pygame.QUIT:  #If user clicked close
                return 0                #Flag that user is done and exits this loop
    
        #The current time displayed on top
        theTime(800,205,40)
    
        
        #Display NTU Logo on specific position
        screen.blit(ntu_logo_r, (135, 100))
 
    
        #BUTTON 1
        #Drawing a rectangle to act as the button for View Today Store
        pygame.draw.rect(screen, burly_wood1, (button1_x, button1_y, button1_w, button1_h))       
        #Display text for View Today Store
        text_display('           View today stores', black, 40, (button1_x), (button1_y + 12))
        pygame.display.update(pygame.Rect(button1_x, button1_y, button1_w, button1_h))
 
        #To get the position of the cursor within the window screen
        mouse = pygame.mouse.get_pos()
 
        #To iterate through each of the x and y coordinates of the cursor
        for event in mouse:
            #To make the button interactive when the cursor hovers above View today stores
            if button1_x <= mouse[0] <= (button1_x + button1_w) and button1_y <= mouse[1] <= (button1_y + button1_h):
                #To give the button a function when it is pressed
                for event1 in pygame.event.get():
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        
                        return 1     #Returns 1 so that main1() will be opened when main_menu() ends
                        
 
        #BUTTON 2
        #Drawing a rectangle to act as the button for View Stores by other dates
        pygame.draw.rect(screen, burly_wood1, (button2_x, button2_y, button2_w, button2_h))       
        #Display text on top of the button
        text_display('    View stores by other dates', black, 40, (button2_x), (button2_y + 12))
        pygame.display.update(pygame.Rect(button2_x, button2_y, button2_w, button2_h))
 
        #To iterate through each of the x and y coordinates of the cursor
        for event in mouse:
            #To make the button interactive when the cursor hovers above View stores by other dates
            if button2_x <= mouse[0] <= (button2_x + button2_w) and button2_y <= mouse[1] <= (button2_y + button2_h):
            #To give the button a function when it is pressed
                for event2 in pygame.event.get():
                    if event2.type == pygame.MOUSEBUTTONDOWN:
                        return 2     #Returns 2 so that main2() will be opened when main_menu() ends
 
        clock.tick()
        pygame.display.update()
        
 
#Overlay of function discussed together between Alvin, Majid and Tricia
#Runs the main program
run = True
while run:
    #Executres Main Menu
    x = main_menu()
    
    #Defined according to a flowchart format so that we can use a return value for the back button
    
    #Application quits
    if x == 0:
        break
    
    #Goes to first button
    elif x == 1:
        #Collate current timing for button 1 (View Today\'s Store)
        current_timing = time.strftime("%H%M", time.localtime())
        current_day = time.strftime("%A", time.localtime())
        
        #Defining in a flowchart view
        loop1 = True
        while loop1:
            y = main1()
            
            #Exit with y == 0
            if y == 0:
                break
            #Exit with y == 1
            elif y == 1:
                break
            elif y == 2:
                continue
        #Application quits
        if y == 0:
            break
        #Loops back to main_menu()
        elif y == 1:
            continue
    
    #Goes to second button  
    elif x == 2:
        #Defining in a flowchart view
        z = main2()
        
        #Breaks out to quit application
        if z == 0:
            break
        #Loops back to main_menu()
        elif z == 2:
            continue
 
pygame.quit()
