#Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40.
average_marks=int(input('What is your marks(s):'))

if average_marks>79:
    print('Grade A')
elif average_marks>60:
    print('Grade B')
elif average_marks>49:
    print('Grade C')
elif average_marks>40:
    print('Grade D')
else:
    print('Grade E')     