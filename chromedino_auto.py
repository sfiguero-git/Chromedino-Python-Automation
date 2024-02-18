import pyautogui as pag #pip install pyautogui
import time  
import sys   

#@author Saul Figueroa.

print('''
       _                                  _ _                         _        
      | |                                | (_)                       | |       
   ___| |__  _ __ ___  _ __ ___   ___  __| |_ _ __   ___   __ _ _   _| |_ ___  
  / __| '_ \| '__/ _ \| '_ ` _ \ / _ \/ _` | | '_ \ / _ \ / _` | | | | __/ _ \ 
 | (__| | | | | | (_) | | | | | |  __/ (_| | | | | | (_) | (_| | |_| | || (_) |
  \___|_| |_|_|  \___/|_| |_| |_|\___|\__,_|_|_| |_|\___/ \__,_|\__,_|\__\___/                 
                                                     |______| 

                                                               ~Saul was here...                 
      ''')
            
print('The script is running...\n')
print('Press CTRL+C to stop!')
image = 'images/dino.png'
confidenceVal = 0.90      #For image location.

#For reducing the size of the region for image identification:
regionLimitatorX = 1001
regionLimitatorY = 251     

while(1): #The program runs until we press CTRL+C.   
    try: #pip install opencv-python
        coordinate = pag.locateCenterOnScreen(image, confidence = confidenceVal, region=(0,0, 1920-regionLimitatorX, 1080-regionLimitatorY))  
        if coordinate == None:
            time.sleep(0.046) 
            pag.press('space') 
    
    except KeyboardInterrupt: #CTRL+C
        print('\nBye!\n')
        sys.exit()
	    
