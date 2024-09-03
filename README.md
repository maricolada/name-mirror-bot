# Name mirror is a Telegram bot creating by Marina Pozhidaeva
This bot was created as part of the Data Science program at Elbrus bootcamp. 
The bot allows the user to obtain information about the transcription of a name in Cyrillic into Latin in accordance with the rules of the Ministry of Foreign Affairs of the Russian Federation.

Instructions for running the bot using Docker:

1. Fork the repository and copy the fork **git clone** to your device.

2. Enter the telegram bot's valid **token number** into the Dockerfile in the code line:
   **ENV TOKEN='you_should_type_the_number_her'**

4. Enter the command to create a **docker image** from your own edited Dockerfile:
   **docker build . -t type_image_id_here**

6. Check if the correct docker image was created - enter the command **docker images**.

7. Run a container based on your docker image in detached mode using the command **docker run -d -p 80:80 type_image_id_here**

8. Check that your container has started successfully by entering the command **docker ps -a**

Enjoy!
