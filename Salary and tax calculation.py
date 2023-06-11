def initial_display():
    print(f'''
        
                Sunway Account Department          
                   Maitidevi, Kathmandu            
                        Welcome to                 
              Salary & Tax Calculation System      
        ''')

def staff_info():
    staff_name = []
    staff_address = []
    staff_pan = []
    staff = []
    staff_income = []
    status = []
    taxamount = []
    staffno = int(input("Enter the number of staff you want to provide data: "))
    for i in range(staffno):
        print(f"Enter for the {i + 1} Staff Information: ")
        staff_name.append(input(f"Enter Staff Name[{i + 1}]: "))
        staff_address.append(input(f"Enter Address[{i + 1}]: "))
        staff_pan.append(input(f"Enter PAN No[{i + 1}]: "))
        status.append(input(f"Enter 'Y' for Married and 'N' for Unmarried Status[{i + 1}]: "))
        staff.append(input(f"Enter FY[{i + 1}]: "))
        staff_income.append(int(input(f"Enter Staff per month income[Rs.][{i + 1}]: ")))
        if status == "Y":
            taxamount.append(calculate_tax_of_married(staff_income[i]))
        else:
            taxamount.append(calculate_tax_of_staff(staff_income[i]))
    for i in range(staffno):
        display_staff_info(staff_name[i], staff_address[i], staff_pan[i], staff_income[i], taxamount[i], staff[i],
                           status[i])
        f = open("D:/programming files/data/data.txt", "a")
        f.write("Staff name: " + staff_name[i] + ", ")
        f.write("Staff address: " + staff_address[i] + ", ")
        f.write("Staff PAN: " + staff_pan[i] + ", ")
        f.write("For Year: " + staff[i] + ", ")
        f.write("Married Status: " + status[i] + ",")
        f.write("Staff income: " + str(staff_income[i]) + ", ")
        f.write("Tax amount: " + str(taxamount[i]) + "\n")
        f.close()


def calculate_tax_of_staff(salary):
    global tax_amount
    income = salary * 12
    if income <= 400000:
        tax_amount = income * 0.01
    elif 400000 < income <= 500000:
        tax_amount = (400000 * 0.01) + ((income - 400000) * 0.10)
    elif 400000 < income <= 700000:
        tax_amount = (400000 * 0.01) + (100000 * 0.10) + (income - 500000) * 0.20
    elif 400000 < income <= 1300000:
        tax_amount = (400000 * 0.01) + (100000 * 0.10) + (200000 * 0.20) + (income - 700000) * 0.30
    elif income >= 2000000:
        tax_amount = (400000 * 0.01) + (income - 400000 * 0.36)
    return tax_amount


def calculate_tax_of_married(salary):
    income = salary * 12
    if income <= 450000:
        tax_amount = income * 0.01
    elif 450000 < income <= 550000:
        tax_amount = (450000 * 0.01) + ((income - 450000) * 0.10)
    elif 450000 < income < 750000:
        tax_amount = (450000 * 0.01) + (100000 * 0.10) + (income - 550000) * 0.20
    elif 450000 < income < 1300000:
        tax_amount = (450000 * 0.01) + (100000 * 0.10) + (200000 * 0.20) + (income - 7500000) * 0.30
    elif income > 2000000:
        tax_amount = (400000 * 0.01) + (income - 400000 * 0.36)
    return tax_amount


def display_staff_info(name, address, pan, salary, tax_amount, yt, status):
    initial_display()
    print(f'''
     Name of the staff: {name}                  Address: {address}
     PAN no: {pan}                              For Year:{yt}
     Married Status: {status}
    ''')
    if salary * 12 <= 400000:
        s_lab = "1%"
    elif salary * 12 <= 500000:
        s_lab = "10%"
    elif salary * 12 <= 600000:
        s_lab = "20%"
    elif salary * 12 <= 1000000:
        s_lab = "30%"
    elif salary * 12 > 2000000:
        s_lab = "36%"

    print(f'''
    Staff {name} with PAN {pan} fall under {s_lab} Tax salb.
    {name} with (PAN {pan}) has to pay tax to government is [Rs.]= {tax_amount}
    ''')


staff_info()
