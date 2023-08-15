def getIncomeTax(salary):
    personal_allowance=11850
    taxable_income=salary -personal_allowance
    if taxable_income <= 34500:
        return taxable_income*0.2
    elif taxable_income <= 150000:
        return taxable_income*0.4
    else:
        return taxable_income*0.45
   
# print(getIncomeTax(125000))

# 3. Write a Python function to multiply all the numbers in a list. 

def multiply_numbers(number_list):
    calculation_times=1
    
    for i in number_list :
       calculation_times= calculation_times*number_list[i]
       print(calculation_times)


number_list=[1,2,3,4]

for i in number_list :
    calculation_times=1
    calculation_times= calculation_times*number_list[i]
    i=i+1
    print(calculation_times)
