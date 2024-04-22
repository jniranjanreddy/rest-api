from tabulate import tabulate
table = [["Sun",696000,1989100000],["Earth",6371,5973.6], ["Moon",1737,73.5],["Mars",3390,641.85]]

print(tabulate(table)) # For Simple Table


print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"])) # For Table with Headers


print(tabulate([["Name","Age"],["Alice",24],["Bob",19]], headers="firstrow")) # For Table with First Row as Headers

print(tabulate([["F",24],["M",19]], showindex="always"))