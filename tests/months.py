from ghcc import GHCC

user = GHCC('Graphity')
months = user.months

for month in months:
    print(month['name'])
    for day in month['days']:
        print(day)
    print()
