def towerBreakers(n, m):
    if m == 1:
        # person 1 cannot do anything
        return 2

    if n % 2 == 0:
        # person 2 always replicates what person 1 does
        return 2
    else:
        # person 1 reduces one tower to height 1, which effectively reduces the number of towers by 1
        # so that the number of towers becomes even and person 1 is in the position of person 2
        return 1

print(towerBreakers(2,6))
print(towerBreakers(2,2))
print(towerBreakers(1,4))