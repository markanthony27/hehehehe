print("STUDENTS AVERAGE CALCULATOR")
print("     Passed Or Failed      ")
prg = int(input("Prelim    Grade  :  "))
mdg = int(input("Midterm   Grade  :  "))
sfg = int(input("SemiFinal Grade  :  "))
fg  = int(input("Final     Grade  :  "))

sum = (prg + mdg + sfg + fg)
avg = float(sum/4)