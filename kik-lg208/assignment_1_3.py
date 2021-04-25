credit_point = 1600 / 60
print("One credit point corresponds to " + str(credit_point) + " hours of work.")

hours = int(credit_point)
minutes = int((credit_point * 60) % 60)
print("This corresponds to " + str(hours) + " hours and " + str(minutes) + " minutes")

course_credits = input("How many credit points is your course? ")
work_load = credit_point * float(course_credits)
mins = int((work_load * 60) % 60)
print("You need to work " + str(int(work_load)) + " hours and " + str(mins) + " minutes to complete your course.")

weeks = input("How many weeks does your course take? ")
weekly_load = work_load / float(weeks)
m = int((weekly_load * 60) % 60)
print("You need to work " + str(int(weekly_load)) + " hours and " + str(m) + " minutes a week for your course.")
