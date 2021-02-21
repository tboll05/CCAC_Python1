#This program asks the user to enter a number of seconds and then converts that amount of time in to days, hours, minutes, and seconds

seconds = int(input("Enter the number of seconds: \n"))
minutes = 0
hours = 0
days = 0

print('{} seconds are equal to:'.format(seconds))

if seconds >= 60:
    minutes = seconds // 60
    print('{} full minute(s) and {} seconds.'.format(minutes, seconds%60))
    
if seconds >= 3600:
    hours = seconds // 3600
    print('{} full hour(s) and {} seconds.'.format(hours, seconds%3600))
    
if seconds >= 86400:
    days = seconds // 86400
    print('{} full day(s) and {} seconds.'.format(days, seconds%86400))