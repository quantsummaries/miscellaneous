def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)

    for i in range(n):
        finish = True

        fuel = 0
        distance = 0

        for j in range(i, n + i):
            f, d = petrolpumps[j % n]
            fuel += f
            distance += d
            if fuel < distance:
                finish = False
                break

        if finish:
            return i

print(truckTour([[1, 5], [10, 3], [3, 4]]))