COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "Blue": "#0000ff",
    "Brown": "#a52a2a"
}

def main():
    print("You can enter a colour name to get its hex code.")
    print("Press Enter to exit.")

    while True:
        colour_name = input("Enter color name: ").strip()

        if len(colour_name) == 0:
        colour_name_formatted = colour_name.title()

        if colour_name_formatted in COLOURS:
            print(f"{colour_name_formatted} is {COLOURS[colour_name_formatted]}")
        else:
            print("Invalid color name. Please try again.")

main()
