# NTU-Canteen-Operating-Services
A mini project coded in python and pygame to help identify the queue time of the North Spine Canteen of NTU

# PREREQUISITES

Python version 3.7
Pygame version 1.9.6

# INTRODUCTION

The program intends to deliver information about canteen food options to the
user. This information includes the following: Operating hours of food stalls,
menu of the individual food stalls, the estimated waiting time based on the 
length of the queue. The user can select two different timings about which he
would like to view this information, viewing either for current time and date,
or a customised time and date set by the user.

# LAUNCH

Language used: Python version 3.7
Libraries and modules used: Pygame version 1.9.6, datetime, re, time
Files included with the program: Canteen_Operating_Services.py, Search_Screen.py,
				 Waiting_Time.py

Main file to run program: Canteen_Operating_Services

NOTE: Double clicking to run the file will work.

**If you are using an IDE, ensure the working directory is set to that of the
folder, as per your computer's absolute path to the directory in which the
images and the .py files are**

# DETAILED DESCRIPTION#

Upon selection of the option to view today's menus:

The user will see a list of food stalls he can choose from.

Upon choosing one, the menu shown will be the current food options offered by 
the stall. For example, if it is early in the morning, then all breakfast 
options will be displayed.

There will be an option to then either view the operating hours of the store or
to calculate the waiting time, given the queue length.

There are back buttons at each of the screens for the user to revert to the
previous page.

**Note: If the program is run after 10pm, no stores will be shown under the
the option to view menu for current time and date, since no stores would be
open then**

Upon selection of the option to view stores by other dates:

The screen will display two text fields - one for the date, in standard format
(DD/MM/YYYY), and one for the time in 24 hour format (0000 to 2359). The user
then confirms his selection by pressing the confirm button. If the format
requirements are not met, or if a date that does not exist is chosen (eg. 20/20
/2020), an error message will be displayed, informing the user of the error
and the program will not proceed further until the user changes his inputs to
meet format and validity requirements.

After a valid date and time have been entered and the confirm option is chosen,
the program retrieves the menu for the stalls at the given date and time. The 
user is able to choose which stall's menu he would like to view.

There will be an option to then either view the operating hours of the store or
to calculate the waiting time, given the queue length.

There are back buttons at each of the screens for the user to revert to the
previous page.

# AUTHOR

Tang Kai Wen, Alvin


# ACKNOWLEDGEMENTS
The Python Standard Documentation and
Google.
