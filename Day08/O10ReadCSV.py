
import csv
from prettytable import PrettyTable
with open("Employee.csv", "r") as CSVR:         # context manager
    emp_details = csv.reader(CSVR)

    #colnames = next(emp_details)
    prtytbl = PrettyTable(next(emp_details))

    # print(*colnames)

    for row in emp_details:
        # print(*row)
        prtytbl.add_row(row)


print(prtytbl)
