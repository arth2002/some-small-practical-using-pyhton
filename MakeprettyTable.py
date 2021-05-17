from prettytable import PrettyTable

myTable = PrettyTable(["Er_No.", "Name", "Skill"])

myTable.add_row(["190220131103", "Arth", "Coding"])
myTable.add_row(["190220131026", "Bhavya", "Teaching"])
myTable.add_row(["190220131031", "Hiten", "Bakchodi"])
myTable.add_row(["190220131094", "Vandan", "Astha"])
myTable.add_row(["190220131134", "Yash", "OnedayMatch"])
myTable.add_row(["190220131148", "Satyendrasinh", "keepQuite"])

print(myTable)
