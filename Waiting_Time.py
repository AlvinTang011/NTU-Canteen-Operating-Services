import pygame
import datetime
import re
 
pygame.init()

screen = pygame.display.set_mode((750,964))
clock = pygame.time.Clock()

def text_display(text, colour, size, x, y):
    font = pygame.font.SysFont(None, size)
    text = font.render(text, True, colour)
    screen.blit(text, (x, y))   #x and y are the pixel coordinates
 

def find_time(user_int):
    try:
        ch = int(user_int)
 
    except ValueError:
        return 'error'
 
    else: 
        if (ch >= 1) & (ch < 100):  
    
            s = ch * 5
            return s
        
        else:
            return 'error'
 
 

def waiting_time(x, y, w = 140, h = 32):
    
    #colour definitions in RGB tuple
    black = (0, 0, 0)
    green = (0, 200, 0)
    bright_green = (0,255,0)
    white = (255, 255, 255)
    gray = (150, 150, 150)
    burly_wood1 = (255,211,155)
    burly_wood1_dark = (255, 190, 130)

    enter_button1_x = 300     #button x coordinate for confirm button
    enter_button1_y = 315     #button y coordinate for confirm button
    back_button_x = 300
    back_button_y = 365
 
    enter_button_w = 140      #button width for confirm button
    enter_button_h = 32       #button height for confirm button
 
    box = pygame.Rect(x, y, w, h)
    inactive_colour = gray
    active_colour = black
    colour = inactive_colour
    font = pygame.font.Font(None, h)
    active = False
    text = ''
    count = 1
    result_count = 1
 
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #check if the quit button has been pressed
                pygame.quit()
                quit()
 
            if event.type == pygame.MOUSEBUTTONDOWN:    #check if mousebutton has been pressed
                if box.collidepoint(event.pos):     #check the coordinates of the cursor when pressed
                    active = not active
                    
                else:
                    active = False
                    
                colour = active_colour if active else inactive_colour   #to make the box colour interactive
                
            if event.type == pygame.KEYDOWN and active == True:    #check if a keyboard key has been pressed while box is selected
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]    #remove last character when backspace is pressed
                elif len(text) <= 1:    #limit the len of characters that can be typed
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        pass
                    else:
                        text += event.unicode   #unicode of the button pressed to choose character to display         
 
        text_surface = font.render(text, True, colour)   #render the text
 
        screen.fill(white)
        #screen.blit(backImg, (0,0))
        text_display("Please enter the number of people in the queue(1-99): ", black, 30, 120, 180)
 
 
        screen.blit(text_surface, (box.x+5, box.y+5))    #blit the text onto the screen
        pygame.draw.rect(screen, colour, box, 2)    #blit the box onto the screen
 
 
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
                        if not text.isdigit():
                            count += 1
                            continue
                        else:
                            time_calc = str(find_time(text))
                            if time_calc == 'error':
                                count += 1
                            else:
                                result_count += 1
                
            if back_button_x <= mouse[0] <= (back_button_x + enter_button_w) and back_button_y <= mouse[1] <= (back_button_y + enter_button_h):
                pygame.draw.rect(screen, burly_wood1_dark, (back_button_x, back_button_y, enter_button_w, enter_button_h))
                text_display('Back', black, 22, (back_button_x + 50), (back_button_y + 10))
                for event1 in pygame.event.get():
                    if event1.type == pygame.MOUSEBUTTONDOWN:
                        return 'menu'     #run the main_menu loop if the user clicks the back button.
 
 
 
        #display an error message for an invalid entry after the first try
        if count > 1:
            text_display("Please enter numbers only", (200, 0, 0), 25, 260, 205)
        
        #display the waiting time and remove error message if input valid
        if result_count > 1:
            text_display("Approximate Waiting Time (mins):", (200, 0, 0), 25, 210, 280)
            text_display(time_calc , (200, 0, 0), 25, 500, 280)
 
        pygame.display.update()
        clock.tick()
