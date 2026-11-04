'''
Accept average score from the student and print the result as follows:
0  to 49 Fail
50 to 69 SC
70 to 89 FC
91 to 100 E/D
Also check for invalid score 
'''
average_score = float(input('Enter your average score to print the result: '))

if average_score >= 0 and average_score <= 49:
    print('Fail')
elif average_score <= 69:
    print('Second Class')
elif average_score <= 89:
    print('First Class')
elif average_score <= 100:
    print('Distinction')
else:
    print('Invalid score')
