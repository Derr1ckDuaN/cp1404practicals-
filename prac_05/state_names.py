# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def print_all_states():
    for code, name in CODE_TO_NAME.items():
        print(f"{code} is {name}")

print_all_states()

while True:
    state_code = input("Enter short state (or press Enter to exit): ").strip()
    if state_code == "":
        break
    try:
        state_code_upper = state_code.upper()
        print(f"{state_code_upper} is {CODE_TO_NAME[state_code_upper]}")
    except KeyError:
        print("Invalid short state")
