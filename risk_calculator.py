"""Risk Calculator"""
def calculate_risk(open_ports, weak_passwords):
    results = (open_ports * 2) + (weak_passwords * 10)
    return results
try:
    ports = int(input("How many open ports are there?: "))
    passwords = int(input("How many weak passwords were detected?: "))
    result = calculate_risk(ports, passwords)
    print(result)

    if result > 50:
        print("Red Alert!")
    else:
        print("Safe")

except ValueError:
    print("Please enter a number")
