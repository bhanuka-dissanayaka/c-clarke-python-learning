monthly_salary = float(input('Enter Youre Monthly salary: '))
anual_salary = monthly_salary*12
taxable_amount = anual_salary-1800000

if taxable_amount<0:
    print(f"Tax per month is 0")
elif taxable_amount<1000000:
    print(f"1st 1,000,000/12 {(taxable_amount*0.06)/12}")
elif taxable_amount<1500000:
    print(f" 1st 1,000,000/12 {(1000000*0.06)/12}\n"
          f" 2nd 500,000/12 {((taxable_amount-1000000)*0.18)/12}\n"
          f" Total Tax {(((taxable_amount-1000000)*0.18)+(1000000*0.06))/12}\n")
elif taxable_amount<2000000:
    print(f" 1st 1,000,000/12 {(1000000*0.06)/12}\n"
          f" 2nd 500,000/12 {(500000*0.18)/12}\n"
          f" 3rd 500,000/12 {(((taxable_amount-1500000)*0.24)/12)}\n"
          f"Tax per Month is {(((taxable_amount-1500000)*0.24)+(1000000*0.06)+(500000*0.18))/12}\n")
elif taxable_amount<2500000:
    print(f" 1st 1,000,000/12 {(1000000*0.06)/12}\n"
          f" 2nd 500,000/12 {(500000*0.18)/12}\n"
          f" 3rd 500,000/12 {(500000*0.24)/12}\n"
          f" 4th 500,000/12 {((taxable_amount-2000000)*0.3)/12}\n"
          f"Tax per Month is {(((taxable_amount-2000000)*0.3)+(1000000*0.06)+(500000*0.18)+(500000*0.24))/12}")
else:
    print(f" 1st 1,000,000/12 {(1000000*0.06)/12}\n"
          f" 2nd 500,000/12 {(500000*0.18)/12}\n"
          f" 3rd 500,000/12 {(500000*0.24)/12}\n"
          f" 4th 500,000/12 {(500000*0.3)/12}\n"
          f" Above 4,300,000/12	{((taxable_amount-2500000)*0.36)/12}\n"
          f"Tax per Month is {(((taxable_amount-2500000)*0.36)+(1000000*0.06)+(500000*0.18)+(500000*0.24)+(500000*0.3))/12}")



