print("STUDENTS AVERAGE CALCULATOR")
print("     Passed Or Failed      ")
prg = int(input("Prelim    Grade  :  "))
mdg = int(input("Midterm   Grade  :  "))
sfg = int(input("SemiFinal Grade  :  "))
fg  = int(input("Final     Grade  :  "))

sum = (prg + mdg + sfg + fg)
avg = float(sum/4)
print(" ")
print("Average Grade is {}.".format((avg)))
print(" ")
if avg >= 75:
    print("You passed! Congrats Inamers")
else:
    print("You Failed! BOBO KA!")