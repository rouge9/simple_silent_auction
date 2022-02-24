def silent(name,money):

    list[name] = money



list = {}
flag = True
while flag == True:
    n = input("type name")
    m = int(input("type money"))
    silent(n, m)

    char = input("to continue press 'y' to cancel press 'n' ")
    if char == "n":
        flag = False
temp= 0
for item in list:
    bid = list[item]
    if bid > temp:
        temp = bid

for bids in list:
    new_bid = list[bids]
    if new_bid == temp:
        print(f"the winner is {bids}")


