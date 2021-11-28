# Day 1, Practical 1

employeeName = str(input('Employee Name: '))
hours = int(input('Enter number of hours: '))
ratePerHour = int(input('Rate per Hour: '))
gsis = int(input('GSIS Contribution: '))
philHealth = int(input('Phil Health: '))
otherLoan = int(input('Housing Loan: '))

grossSalary = ratePerHour * hours
tax = grossSalary * float(.25)
totalDeductions = gsis + philHealth + otherLoan + tax
netSalary = grossSalary - totalDeductions

print('\n==========PAYSLIP===============')
print('==========EMPLOYEE INFORMATION==========\n')
print('Employee Name: ', employeeName)
print('Rendered Hours: ', hours)
print('Rate per Hour: ', ratePerHour)
print('Gross Salary: ', float(grossSalary))
print('\n==========DEDUCTIONS===============')
print('SSS: ', gsis)
print('PhilHealth: ', philHealth)
print('Other Loan: ', otherLoan)
print('Tax: ', tax)
print('Total Deductions: ', totalDeductions)
print('\nNet Salary: ', "PHP{:,.2f} ".format(netSalary))