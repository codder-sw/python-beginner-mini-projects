# Importing time module so we can pause the program for some time
import time  

# Importing notification module from plyer for desktop notifications
from plyer import notification  

# Infinite loop — this keeps running forever unless you stop the program manually
while True:  
    # This prints a reminder in the terminal/console
    print("Please sip a water!!")  
    
    # This line shows a desktop notification on your PC/Mobile  
    notification.notify(
        title = "Please drink some water",   # Notification title
        message = "You need to drink some water"  # Notification body text
    )
    
    # Sleep function stops the loop for 1 hour (60 sec * 60 min = 1 hour)
    time.sleep(60*60)  
