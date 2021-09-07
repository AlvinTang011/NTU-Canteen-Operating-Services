import pygame
import datetime
import re

pygame.init()
 
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#Tricia's Function
def text_display(text, colour, size, x, y):
    font = pygame.font.SysFont(None, size)
    text = font.render(text, True, colour)
    screen.blit(text, (x, y))   #x and y are the pixel coordinates
 
 
'''takes in the date from the user and returns day of the week as an integer
where Monday is 1 and Sunday is 7. For All Day menu, it returns the integer of the
day added with 7,  (i.e. All Day return for Monday is 8 and for Tuesday is 9...)
to differentiate between breakfast and All Day menus on the same day'''

def date_sel(sel):
 
    year = int(sel[6:])
    mth = int(sel[3:5])
    day = int(sel[:2])
    date_index = datetime.date(year, mth, day).isoweekday()
 
    return date_index
 
 
'''displays the search box and breakfast and all day button, takes the date input from the user,
forces valid input from the user. Only a maximum of 9 characters can be typed since that's
all that is required for the date format we will be using.'''

def search_box(x, y, w = 140, h = 32):
    
    #colour definitions in RGB tuple
    black = (0, 0, 0)
    green = (0, 200, 0)
    bright_green = (0,255,0)
    white = (255, 255, 255)
    gray = (150, 150, 150)
    burly_wood1 = (255,211,155)
    burly_wood1_dark = (255, 190, 130)


    enter_button1_x = 330     #button x coordinate for confirm button
    enter_button1_y = 415     #button y coordinate for confirm button
    back_button_x = 330
    back_button_y = 465
 
    enter_button_w = 140      #button width for confirm button
    enter_button_h = 32       #button height for confirm button
 
    
    box = pygame.Rect(x, y, w, h)
    box1 = pygame.Rect(x, y + 100, w, h)
    inactive_colour = gray
    active_colour = black
    colour = inactive_colour
    colour1 = inactive_colour
    font = pygame.font.Font(None, h)
    active = False
    active1 = False
    text = ''
    time_text = ''
    count = 1
 
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #check if the quit button has been pressed
                pygame.quit()
                quit()
 
            if event.type == pygame.MOUSEBUTTONDOWN:    #check if mousebutton has been pressed
                if box.collidepoint(event.pos):     #check the coordinates of the cursor when pressed
                    active = not active
                    active1 = False
                elif box1.collidepoint(event.pos):
                    active1 = not active1
                    active = False
                else:
                    active = False
                    active1 = False
                colour = active_colour if active else inactive_colour   #to make the box colour interactive
                colour1 = active_colour if active1 else inactive_colour
 
            if event.type == pygame.KEYDOWN and active == True:    #check if a keyboard key has been pressed while box is selected
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]    #remove last character when backspace is pressed
                elif len(text) <= 9:    #limit the len of characters that can be typed
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        pass
                    else:
                        text += event.unicode   #unicode of the button pressed to choose character to display         
 
            if event.type == pygame.KEYDOWN and active1 == True:    #check if a keyboard key has been pressed while box is selected
                if event.key == pygame.K_BACKSPACE:
                    time_text = time_text[:-1]    #remove last character when backspace is pressed
                elif len(time_text) <= 3:    #limit the len of characters that can be typed
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        pass
                    else:
                        time_text += event.unicode   #unicode of the button pressed to choose character to display         
 
        #backImg = pygame.image.load('BackgroundEditFinal.png')
 
        text_surface = font.render(text, True, colour)   #render the text
        time_text_surface = font.render(time_text, True, colour1)
 
        screen.fill(white)
        #screen.blit(backImg, (0,0))
        text_display("Enter the date in DD/MM/YYYY format:", black, 30, 225, 200)
        text_display("Enter time of visit (eg. 0900 or 1800):", black, 30, 235, 300)
    
 
        screen.blit(text_surface, (box.x+5, box.y+5))    #blit the text onto the screen
        screen.blit(time_text_surface, (box1.x+5, box1.y+5))
        pygame.draw.rect(screen, colour, box, 2)    #blit the box onto the screen
        pygame.draw.rect(screen, colour1, box1, 2)    #blit box1 onto the screen
 
 
        #Drawing a rectangle to act as the button
        pygame.draw.rect(screen, bright_green, (enter_button1_x, enter_button1_y, enter_button_w, enter_button_h))
        pygame.draw.rect(screen, burly_wood1, (back_button_x, back_button_y, enter_button_w, enter_button_h))
 
        #Display text on top of the button
        text_display('Confirm', black, 22, (enter_button1_x +38), (enter_button1_y + 10))
        text_display('Back', black, 22, (back_button_x + 50), (back_button_y + 10))
 
 
        #To get the position of the cursor within the window screen
        mouse = pygame.mouse.get_pos()
        #To iterate through each of the x and y coordinates of the cursor
        for event in mouse:
            #To make the button interactive when the cursor hovers above
            if enter_button1_x <= mouse[0] <= (enter_button1_x + enter_button_w) and enter_button1_y <= mouse[1] <= (enter_button1_y + enter_button_h):
                pygame.draw.rect(screen, green, (enter_button1_x, enter_button1_y, enter_button_w, enter_button_h))
                text_display('Confirm', black, 22, (enter_button1_x +38), (enter_button1_y + 10))
                #To give the button a function when it is pressed
                for event1 in pygame.event.get():
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        test = re.match('^[0-9]{2}/[0-9]{2}/[0-9]{4}$', text)
 
                        if not test:
                            count += 1      #keep track of the input number, if invalid input given, then run the loop again
                            continue
                        else:
                            try:
                                date = date_sel(text)
                                datetime.datetime.strptime(time_text, "%H%M")

                                #take integer given by date_sel() and convert to day string to iterate and compare with dictionary
                                if date == 1:
                                    return ['Monday', time_text] 
                                if date == 2:
                                    return ['Tuesday', time_text] 
                                if date == 3:
                                    return ['Wednesday', time_text] 
                                if date == 4:
                                    return ['Thursday', time_text] 
                                if date == 5:
                                    return ['Friday', time_text] 
                                if date == 6:
                                    return ['Saturday', time_text] 
                                if date == 7:
                                    return ['Sunday', time_text] 
                                
 
                            except:
                                count += 1
                                continue
 
                
            if back_button_x <= mouse[0] <= (back_button_x + enter_button_w) and back_button_y <= mouse[1] <= (back_button_y + enter_button_h):
                pygame.draw.rect(screen, burly_wood1_dark, (back_button_x, back_button_y, enter_button_w, enter_button_h))
                text_display('Back', black, 22, (back_button_x + 50), (back_button_y + 10))
                for event1 in pygame.event.get():
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        return 'menu'     #run the main_menu loop if the user clicks the back button.
 
 
 
        #display an error message for an invalid entry after the first try
        if count > 1:
            text_display("Invalid value, try again. Enter in the (DD/MM/YYYY) format, and time in 24-hour format.", (200, 0, 0), 25, 55, 380)
            pygame.display.update()
 
        pygame.display.update()
        clock.tick()
 
