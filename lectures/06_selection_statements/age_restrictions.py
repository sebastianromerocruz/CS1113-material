CURRENT_YEAR = 2022
AMERICAN_DRINKING_AGE = 21

user_birth_year = int(input("What year were you born in? "))
difference = CURRENT_YEAR - user_birth_year

if user_birth_year < 0:
    print("Invalid input")
elif difference < 0:
    print("No entry for unborn users.")
elif difference >= AMERICAN_DRINKING_AGE:
    print("Welcome!")
else:
    print("No entry for underage users.")