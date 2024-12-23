#program to create a alarm clock with sound

import time
import datetime
import pygame

alarm_time = input("Enter hrs:mins:sec")
print (f"Alarm set for {alarm_time}")
sound_file = "alarm_clock/no_love.mp3"

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print (current_time)
    if current_time == alarm_time:
        print ("Time's up")
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)
    

    time.sleep(1)
    
        
        

 
