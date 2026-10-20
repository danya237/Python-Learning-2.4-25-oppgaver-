bokstaver = ["a", "b", "a", "c", "a", "b", "a"]

input_bokstav = input("Spører deg om en bokstav for å regne hvor mange ganger den opptrer: ")

teller = 0
for bokstav in bokstaver:
    if bokstav == input_bokstav:
        teller += 1

print(f"Bokstaven '{input_bokstav}' opptrer {teller} ganger i listen.")