import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Hi", "How are you?")

# START
start = ""
while start.lower().strip() != "start":
    start = simpledialog.askstring("Input", "Write start to start the test")
    if start.lower().strip() != "start":
        messagebox.showerror("Error", "Error! Please try again")

# Question 1 (UNCHANGED)
answer = ""
while answer != "gaya bh1":
    answer = simpledialog.askstring(
        "INPUT",
        "1. Which is the nearest black hole to Earth?"
    )
    if answer is None:
        break
    answer = answer.lower().strip()
    if answer != "gaya bh1":
        messagebox.showerror("Error", "Please try again")
    else:
        messagebox.showinfo("", "CORRECT")

# Question 2
answerA = ""
question = (
"2. Which type of numbers include fractions?\n"
"A. Natural\nB. Whole\nC. Rational\nD. Integers"
)

while answerA.lower().strip() != "c":
    answerA = simpledialog.askstring("Question 2", question)
    if answerA is None:
        break
    if answerA.lower().strip() != "c":
        messagebox.showerror("Error", "Try again")
    else:
        messagebox.showinfo("", "CORRECT")

# Question 3
ans = ""
questionB = (
"3. What is the boundary of a black hole called?\n"
"a) Gravity wall\nb) Event horizon\nc) Dark ring\nd) Core"
)

while ans.lower().strip() != "b":
    ans = simpledialog.askstring("Question 3", questionB)
    if ans is None:
        break
    if ans.lower().strip() != "b":
        messagebox.showerror("Error", "Please try again!!!")
    else:
        messagebox.showinfo("", "CORRECT")

# Question 4
while True:
    a = simpledialog.askstring(
        "Question 4",
        "4. Which planet has the maximum number of moons?\n"
        "a) Earth\nb) Jupiter\nc) Saturn\nd) Mars"
    )
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 5
while True:
    a = simpledialog.askstring(
        "Question 5",
        "5. Which vitamin is produced by sunlight?\n"
        "a) A\nb) B\nc) C\nd) D"
    )
    if a is None: break
    elif a.lower().strip() == "d":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 6
while True:
    a = simpledialog.askstring(
        "Question 6",
        "6. SI unit of force?\n"
        "a) Joule\nb) Pascal\nc) Newton\nd) Watt"
    )
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 7
while True:
    a = simpledialog.askstring(
        "Question 7",
        "7. Gas used in photosynthesis?\n"
        "a) Oxygen\nb) Nitrogen\nc) Carbon dioxide\nd) Hydrogen"
    )
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 8
while True:
    a = simpledialog.askstring(
        "Question 8",
        "8. Capital of Australia?\n"
        "a) Sydney\nb) Melbourne\nc) Canberra\nd) Perth"
    )
    if a is None: break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 9
while True:
    a = simpledialog.askstring(
        "Question 9",
        "9. Metal liquid at room temperature?\n"
        "a) Iron\nb) Mercury\nc) Aluminium\nd) Copper"
    )
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 10
while True:
    a = simpledialog.askstring(
        "Question 10",
        "10. Largest bone in human body?\n"
        "a) Skull\nb) Femur\nc) Rib\nd) Spine"
    )
    if a is None: break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 11
while True:
    a = simpledialog.askstring(
        "Question 11",
        "11. Which is the largest mammal?\n"
        "a) Elephant\nb) Blue Whale\nc) Giraffe\nd) Hippo"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 12
while True:
    a = simpledialog.askstring(
        "Question 12",
        "12. Which planet is the hottest?\n"
        "a) Mercury\nb) Venus\nc) Mars\nd) Jupiter"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 13
while True:
    a = simpledialog.askstring(
        "Question 13",
        "13. Which is the tallest mountain in the world?\n"
        "a) K2\nb) Kangchenjunga\nc) Everest\nd) Lhotse"
    )
    if a is None:
        break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 14
while True:
    a = simpledialog.askstring(
        "Question 14",
        "14. Which is the smallest country?\n"
        "a) Monaco\nb) Vatican City\nc) Nauru\nd) Malta"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 15
while True:
    a = simpledialog.askstring(
        "Question 15",
        "15. Which is the lightest element?\n"
        "a) Hydrogen\nb) Helium\nc) Lithium\nd) Oxygen"
    )
    if a is None:
        break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 16
while True:
    a = simpledialog.askstring(
        "Question 16",
        "16. Which is the largest desert in the world?\n"
        "a) Sahara\nb) Gobi\nc) Arabian\nd) Antarctica"
    )
    if a is None:
        break
    elif a.lower().strip() == "d":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 17
while True:
    a = simpledialog.askstring(
        "Question 17",
        "17. Which is the fastest sea animal?\n"
        "a) Shark\nb) Sailfish\nc) Dolphin\nd) Whale"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 18
while True:
    a = simpledialog.askstring(
        "Question 18",
        "18. Which gas is most abundant in Earth's atmosphere?\n"
        "a) Oxygen\nb) Carbon dioxide\nc) Nitrogen\nd) Hydrogen"
    )
    if a is None:
        break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 19
while True:
    a = simpledialog.askstring(
        "Question 19",
        "19. What is the national bird of India?\n"
        "a) Peacock\nb) Eagle\nc) Sparrow\nd) Parrot"
    )
    if a is None:
        break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 20
while True:
    a = simpledialog.askstring(
        "Question 20",
        "20. Which is the coldest planet?\n"
        "a) Neptune\nb) Uranus\nc) Saturn\nd) Jupiter"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 21
while True:
    a = simpledialog.askstring(
        "Question 21",
        "21. Which is the smallest planet?\n"
        "a) Mercury\nb) Mars\nc) Venus\nd) Earth"
    )
    if a is None:
        break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 22
while True:
    a = simpledialog.askstring(
        "Question 22",
        "22. Which fish is the fastest?\n"
        "a) Tuna\nb) Marlin\nc) Sailfish\nd) Swordfish"
    )
    if a is None:
        break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 23
while True:
    a = simpledialog.askstring(
        "Question 23",
        "23. Which is the longest river?\n"
        "a) Nile\nb) Amazon\nc) Yangtze\nd) Mississippi"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 24
while True:
    a = simpledialog.askstring(
        "Question 24",
        "24. Which is the largest moon?\n"
        "a) Titan\nb) Ganymede\nc) Europa\nd) Callisto"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 25
while True:
    a = simpledialog.askstring(
        "Question 25",
        "25. Which planet has the most rings?\n"
        "a) Jupiter\nb) Saturn\nc) Uranus\nd) Neptune"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 26
while True:
    a = simpledialog.askstring(
        "Question 26",
        "26. Which is the largest bird?\n"
        "a) Ostrich\nb) Eagle\nc) Albatross\nd) Flamingo"
    )
    if a is None:
        break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 27
while True:
    a = simpledialog.askstring(
        "Question 27",
        "27. Which is the strongest muscle by force?\n"
        "a) Heart\nb) Jaw\nc) Thigh\nd) Arm"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 28
while True:
    a = simpledialog.askstring(
        "Question 28",
        "28. Which is the largest continent?\n"
        "a) Africa\nb) Asia\nc) Europe\nd) Australia"
    )
    if a is None:
        break
    elif a.lower().strip() == "b":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 29
while True:
    a = simpledialog.askstring(
        "Question 29",
        "29. Which insect can fly the fastest?\n"
        "a) Dragonfly\nb) Bee\nc) Mosquito\nd) Butterfly"
    )
    if a is None:
        break
    elif a.lower().strip() == "a":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")

# Question 30
while True:
    a = simpledialog.askstring(
        "Question 30",
        "30. Which country has the largest population (traditional GK)?\n"
        "a) USA\nb) India\nc) China\nd) Russia"
    )
    if a is None:
        break
    elif a.lower().strip() == "c":
        messagebox.showinfo("Correct", "Correct!")
        break
    else:
        messagebox.showerror("Wrong", "Wrong answer, try again")
messagebox.showinfo("Done", "Test Completed 🎉")