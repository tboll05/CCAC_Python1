#This program contains 3 different dictionaires that contain course numbers, room numbers, instructors, and meeting time.
#The user is asked to enter a course number and if this is a valid entry the program will return the corresponding information.
#If the entry is invalid the user will be prompt that it is invalid.  The input is case sensitive but can be made case insensitive by using .upper()

room_number_dict = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}

instructor_dict = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}

time_dict = {'CS101':'8:00 am', 'CS102':'9:00 am', 'CS103':'10:00 am', 'NT110':'11:00 am', 'CM241':'12:00 pm'}


course_number = input("Enter a course number: \n")

if course_number not in room_number_dict:
    print(f'{course_number} is an invalid course number.')

else: 
    print(f'The details for course {course_number} are:')
    print('Room: ' + room_number_dict[course_number])
    print('Instructor: ' + instructor_dict[course_number])
    print('Time: ' + time_dict[course_number])