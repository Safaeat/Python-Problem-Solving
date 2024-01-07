age = int(input("What is your current age?"))

years = int(90-age)
month = int(years * 12)
week = int(years * 52)
day = 365 * years

print(f"You will gona leave {day} days or {week} weeks or {month} months or {years} years")