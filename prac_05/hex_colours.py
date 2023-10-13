COLOUR_NAME_TO_CODE = {"aqua": "#00ffff", "black": "#000000", "blue": "#0018a8", "brown": "#a52a2a",
                       "burgundy": "#800020", "celadon": "#ace1af", "chocolate": "#d2691e",
                       "citron": "#9fa91f", "copper": "#b87333", "cream": "#fffdd0"}

print(COLOUR_NAME_TO_CODE)
colour_name = input("Enter colour: ").lower()
while colour_name != "":
    if colour_name in COLOUR_NAME_TO_CODE:
        print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name])
    else:
        print("Invalid")
    colour_name = input("Enter colour: ").lower()
print("Chow")
