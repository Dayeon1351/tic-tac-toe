from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player
      button["bg"] = "skyblue"

      if player == "X" :
            player = "*"
            button["bg"] = "skyblue"
      else :
            player = "X"
            button["bg"] = "pink"

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()
