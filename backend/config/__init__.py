"""
- Prompt user for tasks 
- One by one mark off tasks as completed  
- If the tasks are completed than a QR Code unlocking access to locked apps is given to the user    

//---- Session configuration <------------------------------------------------
- Apps they want to block                                                    |
- Tasks they want to complete                                                |
- Generates a random key which is converted into a qr code                   | 
|                                                                            |
V                                                                            |
//---- Simple to-do list                                                     |
- X out task if completed                                                    |
- If all tasks completed than go to the next page                            |
- If not run session and block registered apps                               |
|                                                                            |
V                                                                            |
//---- QR Code display:                                                      |
- Scannable qr code for unlocking app permissions is displayed on screen ____|
- Button input for going back to the session configuration screen
 
 
//---- 

"""  
