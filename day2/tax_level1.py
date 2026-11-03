name = input('Enter employee name: ')
employee_id = int(input('Enter employee Id: '))
basic_monthly_salary = float(input('Enter basic monthly salary of the employee: '))
allowance = float(input('Enter employee allowance: '))
bonus_percentage = float(input('Enter employee bonus percentage: '))

gross_monthly_salary = basic_monthly_salary + allowance
annual_gross_salary = (gross_monthly_salary * 12) + (gross_monthly_salary * (bonus_percentage / 100) * 12)

print('-' * 38)
print('%26s :' % 'Employee ID', employee_id)
print('%26s :' % 'Employee Name', name)
print('%26s :' % 'Basic Monthly Salary', basic_monthly_salary)
print('%26s :' % 'Employee monthly allowance', allowance)
print('%26s :' % 'Gross monthly salary', gross_monthly_salary)
print('%26s :' % 'Annual gross salary', annual_gross_salary)
print('-' * 38)
'''
print(f'Employee ID: {employee_id}')
print(f'Basic Monthly Salary: {basic_monthly_salary}')
print(f'Employee monthly allowance: {allowance}')
print(f'Gross monthly salary: {gross_monthly_salary}')
print(f'Annual gross salary: {annual_gross_salary}')
'''