import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()  

print (messagebox.showinfo("Hi", "How are you?"))# you can remove print function if you want it will doesn't affect the program 


start = ""
while start.lower().strip() != "start":
    start = simpledialog.askstring("Input", "Write start to start the test")
    
    if start.lower().strip() != "start":
        messagebox.showerror("Error", "Error! Please try again")


answer = ""
while answer != "gaya bh1":
    answer = simpledialog.askstring("INPUT", "3. Which is the nearest blackhole to earth?")
    if answer is None:
        break
    answer = answer.lower().strip()
    if answer != "gaya bh1":
        messagebox.showerror("Error", "Please try again")
    else:
        messagebox.showinfo("", "CORRECT")


answerA = ""
question = (
"2.Rational numbers are in the form of:\n"
"A. p*q\n"
"B. p+q\n"
"C. p/q\n"
"D. p-q\n"
"CHOOSE THE CORRECT OPTION"
)

while answerA.lower().strip() != "c":
    answerA = simpledialog.askstring("Question no.2", question)
    if answerA is None:
        break
    if answerA.lower().strip() != "c":
        messagebox.showerror("Error", "Try again")
    else:
        messagebox.showinfo("", "CORRECT")


ans = ""
questionB = (
"3. The centre of a black hole\n"
"is known as (choose the correct option)\n"
"a} black horizon\n"
"b} event horizon\n"
"c} middle horizon\n"
"d} black point\n"
)

while ans.lower().strip() != "b":
    ans = simpledialog.askstring("Question no.3", questionB)
    if ans is None:
        break
    if ans.lower().strip() != "b":
        messagebox.showwarning("Error", "Please try again!!!")
    else:
        messagebox.showinfo("", "CORRECT")



from tkinter import simpledialog, messagebox

# Question 4
while True:
    a = simpledialog.askstring("Question 4",
        "4. Sharpest natural object\n"
        "a) Obsidian\nb) Iron\nc) Diamond\nd) Magnet")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 5
while True:
    a = simpledialog.askstring("Question 5",
        "5. Largest planet in the solar system\n"
        "a) Earth\nb) Jupiter\nc) Saturn\nd) Mars")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 6
while True:
    a = simpledialog.askstring("Question 6",
        "6. Fastest land animal\n"
        "a) Cheetah\nb) Lion\nc) Horse\nd) Tiger")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 7
while True:
    a = simpledialog.askstring("Question 7",
        "7. Hardest natural substance\n"
        "a) Gold\nb) Iron\nc) Diamond\nd) Quartz")
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 8
while True:
    a = simpledialog.askstring("Question 8",
        "8. Sharpest natural object\n"
        "a) Obsidian\nb) Iron\nc) Diamond\nd) Magnet")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 9
while True:
    a = simpledialog.askstring("Question 9",
        "9. Largest ocean in the world\n"
        "a) Atlantic\nb) Indian\nc) Arctic\nd) Pacific")
    if a is None: break
    elif a.lower().strip() == "d":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 10
while True:
    a = simpledialog.askstring("Question 10",
        "10. Fastest bird\n"
        "a) Falcon\nb) Eagle\nc) Sparrow\nd) Owl")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 11
while True:
    a = simpledialog.askstring("Question 11",
        "11. Largest mammal\n"
        "a) Elephant\nb) Blue Whale\nc) Giraffe\nd) Hippo")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 12
while True:
    a = simpledialog.askstring("Question 12",
        "12. Hottest planet\n"
        "a) Mercury\nb) Venus\nc) Mars\nd) Jupiter")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 13
while True:
    a = simpledialog.askstring("Question 13",
        "13. Tallest mountain\n"
        "a) K2\nb) Kangchenjunga\nc) Everest\nd) Lhotse")
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 14
while True:
    a = simpledialog.askstring("Question 14",
        "14. Smallest country\n"
        "a) Monaco\nb) Vatican City\nc) Nauru\nd) San Marino")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 15
while True:
    a = simpledialog.askstring("Question 15",
        "15. Lightest element\n"
        "a) Hydrogen\nb) Helium\nc) Lithium\nd) Oxygen")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 16
while True:
    a = simpledialog.askstring("Question 16",
        "16. Largest desert\n"
        "a) Sahara\nb) Gobi\nc) Arabian\nd) Antarctic")
    if a is None: break
    elif a.lower().strip() == "d":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 17
while True:
    a = simpledialog.askstring("Question 17",
        "17. Fastest marine animal\n"
        "a) Swordfish\nb) Sailfish\nc) Shark\nd) Tuna")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 18
while True:
    a = simpledialog.askstring("Question 18",
        "18. Most abundant gas\n"
        "a) Oxygen\nb) CO2\nc) Nitrogen\nd) Hydrogen")
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 19
while True:
    a = simpledialog.askstring("Question 19",
        "19. National bird of India\n"
        "a) Peacock\nb) Eagle\nc) Sparrow\nd) Parrot")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 20
while True:
    a = simpledialog.askstring("Question 20",
        "20. Coldest planet\n"
        "a) Neptune\nb) Uranus\nc) Saturn\nd) Jupiter")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 21
while True:
    a = simpledialog.askstring("Question 21",
        "21. Smallest planet\n"
        "a) Mercury\nb) Mars\nc) Venus\nd) Earth")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 22
while True:
    a = simpledialog.askstring("Question 22",
        "22. Fastest fish\n"
        "a) Tuna\nb) Marlin\nc) Sailfish\nd) Swordfish")
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 23
while True:
    a = simpledialog.askstring("Question 23",
        "23. Longest river\n"
        "a) Nile\nb) Amazon\nc) Yangtze\nd) Mississippi")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 24
while True:
    a = simpledialog.askstring("Question 24",
        "24. Largest moon\n"
        "a) Titan\nb) Ganymede\nc) Callisto\nd) Europa")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 25
while True:
    a = simpledialog.askstring("Question 25",
        "25. Hottest planet\n"
        "a) Mercury\nb) Venus\nc) Mars\nd) Jupiter")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 26
while True:
    a = simpledialog.askstring("Question 26",
        "26. Largest bird\n"
        "a) Ostrich\nb) Eagle\nc) Albatross\nd) Flamingo")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 27
while True:
    a = simpledialog.askstring("Question 27",
        "27. Strongest muscle\n"
        "a) Heart\nb) Jaw\nc) Quadriceps\nd) Gluteus")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 28
while True:
    a = simpledialog.askstring("Question 28",
        "28. Largest continent\n"
        "a) Africa\nb) Asia\nc) Europe\nd) North America")
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 29
while True:
    a = simpledialog.askstring("Question 29",
        "29. Fastest insect\n"
        "a) Dragonfly\nb) Horsefly\nc) Hawk Moth\nd) Beetle")
    if a is None: break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 30
while True:
    a = simpledialog.askstring("Question 30",
        "30. Most populated country\n"
        "a) USA\nb) India\nc) China\nd) Russia")
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")    