# Querry entry.
age_in_five_years_time = 5
the_current_year = int(input("What year is it this year?"))
date_of_birth = int(input("Enter your year of birth:"))

#Logical coding
age_in_five_years_time2 = int(the_current_year - date_of_birth)+int(age_in_five_years_time)

#Results
print(f"I will be {age_in_five_years_time2}years old in five years time.")

#OR
#Querry entry.
age_now = int(input("How old are you now?"))

#Logical coding
age_in_five_years_time +=age_now

#Results
print(f"I will be {age_in_five_years_time}years old in five years time.")
