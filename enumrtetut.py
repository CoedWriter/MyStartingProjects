l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]

# i=1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1


for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"Jarvis please buy {item}")

# ---------------------
list_1 = ["coding", "with", "harry"]
for indx, val in enumerate(list_1):
    print(indx, val)

# ----------------------
list_2 = ["Python", "Programming", "Is", "Fun"]
# Counter value starts from 5
result = enumerate(list_2, 5)
print(list(result))