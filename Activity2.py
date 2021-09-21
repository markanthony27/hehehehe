print("STUDENTS AVERAGE CALCULATOR")
print("     Passed Or Failed      ")
print("Prelim Grade    : ")
prg = int(input())
print("Midterm Grade   : ")
mdg = int(input())
print("SemiFinal Grade : ")
sfg = int(input())
print("Final Grade     : ")
fg = int(input())

sum = (prg + mdg + sfg + fg)
avg = sum/4
print("Average Grade is {}.".format(avg))