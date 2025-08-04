age = input("Enter your current age:")
age_as_int = int(age)

years_remaining = 65-age_as_int
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
months_remaining = years_remaining*12
print(f"you have {days_remaining} days, {weeks_remaining} weeks,{months_remaining}months")