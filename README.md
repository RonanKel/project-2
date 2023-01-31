
Author=Ronan Kelly
Date Last Modified=1/30/23

Project Description:

For this project I started by modifying the credentials.ini to my desired port, name and email. Then I changed the name in the Docker file. Then I made it to check the different request possibilities.
Weather it's 200, 404 or 403, it'll be handled. In order to do this I took the parseconfig() function from project-0. I used it to get the PORT number. Then I made it so that a 200 would send the file to the browser, 404 would say "File not found", and 403 would say this is forbidden.
