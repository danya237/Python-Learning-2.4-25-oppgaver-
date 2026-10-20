land = ["Norge", "Sverige", "Danmark", "Finland"]

print("Hvilke land liker du best?")
input_land = input("Skriv inn et land: ")
if input_land in land:
    print(f"Du liker {input_land}!")
else:
    print(f"This country is not in the list: {input_land}.")