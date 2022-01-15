lis = ["Ronaldo", "Messi", "Neymar Jr.",
       "Mbappe", "Sunil Chhetri", "Pele"]

for item in lis:
    print(item, "and", end = " ")

print("all the other great footballers")

# --------------------

# the above code block would be this with join function

ye = " and ".join(lis)
print(ye, "all the other great footballers")