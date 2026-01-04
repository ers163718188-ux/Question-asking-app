import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()  

print (messagebox.showinfo("Hi", "How are you?"))# you can remove print function if you want it will doesn't affect the program 


start = ""
while start.lower().strip() != "start":
    start = simpledialog.askstring("Input", "Write start to start the test")
    
    if start.lower().strip() != "start":
        messagebox.showwarning("Error", "Error! Please try again")


answer = ""
while answer != "gaya bh1":
    answer = simpledialog.askstring("INPUT", "3. Which is the nearest blackhole to earth?")
    if answer is None:
        break
    answer = answer.lower().strip()
    if answer != "gaya bh1":
        messagebox.showwarning("Error", "Please try again")
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
        messagebox.showwarning("Error", "Try again")
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



answerc = ""
questionhello=(
"4. Sharpest natural object\n "
"a)obsidian\n"
"b)iron\n"
"c)diamond\n"
"d)magnet\n"
)
while answerc.lower().strip() != "a":
	answerc = simpledialog.askstring("question.4." , questionhello)
	if answerc is None:
		break
	else:
         messagebox.showinfo(" " , "correct")

answer5 = ""
question5 = (
    "5. Largest planet in the solar system\n"
    "a) Earth\n"
    "b) Jupiter\n"
    "c) Saturn\n"
    "d) Mars\n"
)
while answer5.lower().strip() != "b":
    answer5 = simpledialog.askstring("Question 5", question5)
    if answer5 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 6: Fastest land animal
answer6 = ""
question6 = (
    "6. Fastest land animal\n"
    "a) Cheetah\n"
    "b) Lion\n"
    "c) Horse\n"
    "d) Tiger\n"
)
while answer6.lower().strip() != "a":
    answer6 = simpledialog.askstring("Question 6", question6)
    if answer6 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 7: Hardest natural substance
answer7 = ""
question7 = (
    "7. Hardest natural substance\n"
    "a) Gold\n"
    "b) Iron\n"
    "c) Diamond\n"
    "d) Quartz\n"
)
while answer7.lower().strip() != "c":
    answer7 = simpledialog.askstring("Question 7", question7)
    if answer7 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 8: Sharpest natural object
answer8 = ""
question8 = (
    "8. Sharpest natural object\n"
    "a) Obsidian\n"
    "b) Iron\n"
    "c) Diamond\n"
    "d) Magnet\n"
)
while answer8.lower().strip() != "a":
    answer8 = simpledialog.askstring("Question 8", question8)
    if answer8 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

answer9 = ""
question9 = (
    "9. Largest ocean in the world\n"
    "a) Atlantic Ocean\n"
    "b) Indian Ocean\n"
    "c) Arctic Ocean\n"
    "d) Pacific Ocean\n"
)
while answer9.lower().strip() != "d":
    answer9 = simpledialog.askstring("Question 9", question9)
    if answer9 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 10: Fastest bird
answer10 = ""
question10 = (
    "10. Fastest bird\n"
    "a) Falcon\n"
    "b) Eagle\n"
    "c) Sparrow\n"
    "d) Owl\n"
)
while answer10.lower().strip() != "a":
    answer10 = simpledialog.askstring("Question 10", question10)
    if answer10 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 11: Largest mammal
answer11 = ""
question11 = (
    "11. Largest mammal on Earth\n"
    "a) Elephant\n"
    "b) Blue Whale\n"
    "c) Giraffe\n"
    "d) Hippo\n"
)
while answer11.lower().strip() != "b":
    answer11 = simpledialog.askstring("Question 11", question11)
    if answer11 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 12: Hottest planet
answer12 = ""
question12 = (
    "12. Hottest planet in the solar system\n"
    "a) Mercury\n"
    "b) Venus\n"
    "c) Mars\n"
    "d) Jupiter\n"
)
while answer12.lower().strip() != "b":
    answer12 = simpledialog.askstring("Question 12", question12)
    if answer12 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 13: Tallest mountain
answer13 = ""
question13 = (
    "13. Tallest mountain in the world\n"
    "a) K2\n"
    "b) Kangchenjunga\n"
    "c) Mount Everest\n"
    "d) Lhotse\n"
)
while answer13.lower().strip() != "c":
    answer13 = simpledialog.askstring("Question 13", question13)
    if answer13 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 14: Smallest country
answer14 = ""
question14 = (
    "14. Smallest country by area\n"
    "a) Monaco\n"
    "b) Vatican City\n"
    "c) Nauru\n"
    "d) San Marino\n"
)
while answer14.lower().strip() != "b":
    answer14 = simpledialog.askstring("Question 14", question14)
    if answer14 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 15: Lightest element
answer15 = ""
question15 = (
    "15. Lightest element in the periodic table\n"
    "a) Hydrogen\n"
    "b) Helium\n"
    "c) Lithium\n"
    "d) Oxygen\n"
)
while answer15.lower().strip() != "a":
    answer15 = simpledialog.askstring("Question 15", question15)
    if answer15 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 16: Largest desert
answer16 = ""
question16 = (
    "16. Largest desert in the world\n"
    "a) Sahara\n"
    "b) Gobi\n"
    "c) Arabian\n"
    "d) Antarctic Desert\n"
)
while answer16.lower().strip() != "d":
    answer16 = simpledialog.askstring("Question 16", question16)
    if answer16 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 17: Fastest marine animal
answer17 = ""
question17 = (
    "17. Fastest marine animal\n"
    "a) Swordfish\n"
    "b) Sailfish\n"
    "c) Shark\n"
    "d) Tuna\n"
)
while answer17.lower().strip() != "b":
    answer17 = simpledialog.askstring("Question 17", question17)
    if answer17 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 18: Most abundant gas
answer18 = ""
question18 = (
    "18. Most abundant gas in the Earth's atmosphere\n"
    "a) Oxygen\n"
    "b) Carbon Dioxide\n"
    "c) Nitrogen\n"
    "d) Hydrogen\n"
)
while answer18.lower().strip() != "c":
    answer18 = simpledialog.askstring("Question 18", question18)
    if answer18 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 19: National bird of India
answer19 = ""
question19 = (
    "19. National bird of India\n"
    "a) Peacock\n"
    "b) Eagle\n"
    "c) Sparrow\n"
    "d) Parrot\n"
)
while answer19.lower().strip() != "a":
    answer19 = simpledialog.askstring("Question 19", question19)
    if answer19 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 20: Coldest planet
answer20 = ""
question20 = (
    "20. Coldest planet in the solar system\n"
    "a) Neptune\n"
    "b) Uranus\n"
    "c) Saturn\n"
    "d) Jupiter\n"
)
while answer20.lower().strip() != "b":
    answer20 = simpledialog.askstring("Question 20", question20)
    if answer20 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 21: Smallest planet
answer21 = ""
question21 = (
    "21. Smallest planet in the solar system\n"
    "a) Mercury\n"
    "b) Mars\n"
    "c) Venus\n"
    "d) Earth\n"
)
while answer21.lower().strip() != "a":
    answer21 = simpledialog.askstring("Question 21", question21)
    if answer21 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 22: Fastest fish
answer22 = ""
question22 = (
    "22. Fastest fish in the ocean\n"
    "a) Tuna\n"
    "b) Marlin\n"
    "c) Sailfish\n"
    "d) Swordfish\n"
)
while answer22.lower().strip() != "c":
    answer22 = simpledialog.askstring("Question 22", question22)
    if answer22 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 23: Longest river
answer23 = ""
question23 = (
    "23. Longest river in the world\n"
    "a) Nile\n"
    "b) Amazon\n"
    "c) Yangtze\n"
    "d) Mississippi\n"
)
while answer23.lower().strip() != "b":
    answer23 = simpledialog.askstring("Question 23", question23)
    if answer23 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 24: Largest moon
answer24 = ""
question24 = (
    "24. Largest moon in the solar system\n"
    "a) Titan\n"
    "b) Ganymede\n"
    "c) Callisto\n"
    "d) Europa\n"
)
while answer24.lower().strip() != "b":
    answer24 = simpledialog.askstring("Question 24", question24)
    if answer24 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 25: Hottest planet
answer25 = ""
question25 = (
    "25. Hottest planet in the solar system\n"
    "a) Mercury\n"
    "b) Venus\n"
    "c) Mars\n"
    "d) Jupiter\n"
)
while answer25.lower().strip() != "b":
    answer25 = simpledialog.askstring("Question 25", question25)
    if answer25 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 26: Largest bird
answer26 = ""
question26 = (
    "26. Largest bird in the world\n"
    "a) Ostrich\n"
    "b) Eagle\n"
    "c) Albatross\n"
    "d) Flamingo\n"
)
while answer26.lower().strip() != "a":
    answer26 = simpledialog.askstring("Question 26", question26)
    if answer26 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 27: Strongest muscle
answer27 = ""
question27 = (
    "27. Strongest muscle in the human body\n"
    "a) Heart\n"
    "b) Jaw muscle\n"
    "c) Quadriceps\n"
    "d) Gluteus maximus\n"
)
while answer27.lower().strip() != "b":
    answer27 = simpledialog.askstring("Question 27", question27)
    if answer27 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 28: Largest continent
answer28 = ""
question28 = (
    "28. Largest continent by area\n"
    "a) Africa\n"
    "b) Asia\n"
    "c) Europe\n"
    "d) North America\n"
)
while answer28.lower().strip() != "b":
    answer28 = simpledialog.askstring("Question 28", question28)
    if answer28 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 29: Fastest insect
answer29 = ""
question29 = (
    "29. Fastest insect\n"
    "a) Dragonfly\n"
    "b) Horsefly\n"
    "c) Hawk Moth\n"
    "d) Beetle\n"
)
while answer29.lower().strip() != "a":
    answer29 = simpledialog.askstring("Question 29", question29)
    if answer29 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")

# Question 30: Most populated country
answer30 = ""
question30 = (
    "30. Most populated country in the world\n"
    "a) USA\n"
    "b) India\n"
    "c) China\n"
    "d) Russia\n"
)
while answer30.lower().strip() != "c":
    answer30 = simpledialog.askstring("Question 30", question30)
    if answer30 is None:
        break
    else:
        messagebox.showinfo("", "Correct!")       