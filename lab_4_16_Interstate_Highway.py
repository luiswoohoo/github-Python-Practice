highway = int(input())

if ((highway < 1) or (highway > 999) or ((highway % 100) == 0)):
    print(highway, "is not a valid interstate highway number.")

elif ((highway >= 1) and (highway <= 99) and ((highway % 2) == 0)):
    print(highway, "is primary, going east/west.")

elif ((highway >= 1) and (highway <= 99) and ((highway % 2) != 0)):
    print(highway, "is primary, going north/south.")

