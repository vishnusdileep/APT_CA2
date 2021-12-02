regular_hours_worked = int(input("enter hours worked"))
regular_rate = 16.00
regular_pay = regular_rate * regular_hours_worked
overtime_rate = 24.00
overtime_hours = int(input("enter overtime hours worked"))
overtime_pay = overtime_rate * overtime_hours

gross_pay = regular_pay + overtime_pay

standard_rate = regular_rate * 40

higher_rate_pay = gross_pay - standard_rate

standard_tax = 0.2 * standard_rate
higher_tax = 0.4 * higher_rate_pay

total_tax = standard_tax + higher_tax

tax_credit = int(input("enter tax credit"))

net_deductions = total_tax - tax_credit

net_pay = gross_pay - net_deductions

print("regular_hours_worked : ", regular_hours_worked)
print("regular_rate : ", regular_rate)
print("regular_pay : ", regular_pay)
print("overtime_rate : ", overtime_rate)
print("overtime_hours : ", overtime_hours)
print("overtime_pay : ", overtime_pay)
print("gross_pay : ", gross_pay)
print("standard_rate : ", standard_rate)
print("higher_rate_pay : ", higher_rate_pay)
print("standard_tax : ", standard_tax)
print("higher_tax : ", higher_tax)
print("total_tax : ", total_tax)
print("tax_credit : ", tax_credit)
print("net_deductions : ", net_deductions)
print("net_pay : ", net_pay)







