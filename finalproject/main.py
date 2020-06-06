import sqlite3
from employee import Employee

conn = sqlite3.connect('empl.db')

c = conn.cursor()




def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

user = "yes"
while(user != "no"):
    emp_1 = Employee(input("First name: "), input("Last Name: "), int(input("Pay: ")))
    insert_emp(emp_1)
    conn.commit()
    user = input("Do you want to continue: (yes/no): ")

#update_pay(emp_1, 95000)
#remove_emp(emp_1)

lastname = input("Search for last name in the table: ")
emps = get_emps_by_name(lastname)
print(emps)
conn.commit()
conn.close()
