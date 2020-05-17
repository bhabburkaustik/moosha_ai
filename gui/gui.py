import tkinter as tk 

from PIL import Image, ImageTk
import pyautogui


root= tk.Tk()

#set width and height

canvas=tk.Canvas(root,width=1920,height=1440)


#give this image path. image should be in png format.

#Example: "C:\\Users\\ASUS\\OneDrive\\Pictures\\image.png"

image=ImageTk.PhotoImage(Image.open("C:\\Users\\kaustik\\Downloads\\loader-ai-siri_2x.gif"))

#canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

name_var = 'name_var value'
name_label = tk.Label(root, text = 'Username', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# name using widget Entry 
name_entry = tk.Entry(root, 
                      textvariable = name_var,font=('calibre',10,'normal')) 
   
# creating a label for password 
passw_label = tk.Label(root, 
                       text = 'Password', 
                       font = ('calibre',10,'bold')) 
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Submit', 
                  command = submit) 
   
# placing the label and entry in 
# the required position using grid 
# method 
name_label.grid(row=0,column=0) 
name_entry.grid(row=0,column=1)  
sub_btn.grid(row=2,column=1) 
   
# performing an infinite loop  
# for the window to display 
root.mainloop() 
