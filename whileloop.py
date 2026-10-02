battery = 100

while battery > 0:
    battery -= 15

    if battery == 40:
        continue

    if battery <= 10:
        break

    print("battery now:", battery)