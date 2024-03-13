from tkinter import *                 # Importing the tkinter module
from pytube import YouTube            # Importing the YouTube class from pytube module

root = Tk()                           # Creating a new tkinter window
root.geometry('500x300')              # Setting the size of the window to 500x300 pixels
root.resizable(0,0)                   # Preventing the window from being resized
root.title("DataFlair-youtube video downloader")  # Setting the title of the window

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()  # Creating and packing a label for the title

link = StringVar()                    # Creating a StringVar object for storing the link

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)  # Creating and placing a label for the link input
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)   # Creating and placing an Entry widget for the link input

# Defining the Downloader function to be called when the download button is clicked
def Downloader():
      url =YouTube(str(link.get()))  # Creating a YouTube object with the entered link
      video = url.streams.first()     # Getting the first available stream of the video
      video.download()               # Downloading the video
      Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)    # Creating and placing a label to indicate the download is complete

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)  # Creating and placing a download button that calls the Downloader function

root.mainloop()                       # Starting the tkinter event loop
