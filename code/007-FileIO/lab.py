def readData():
    file = open("car-sale.csv", "r")
    data = file.readlines()

    print(data)

    months = data[0].split(",")
    ford = data[1]
    volks = data[2]
    merc = data [3]
    vaux = data[4]
    bmw = data [5]
    print("**********************************")
    ford = splitData(ford)
    volks = splitData(volks)
    merc = splitData(merc)
    vaux = splitData(vaux)
    bmw = splitData(bmw)

    # Task 1 - Sum of cars by Ford
    print(sum(ford))

    # Task 2 - Sum of cars sold in may
    print(months)
    sub_total = 0
    sub_total += ford[4]
    sub_total += volks[4]
    sub_total += vaux[4]
    sub_total += merc[4]
    sub_total += bmw[4]
    print(sub_total)

def splitData(data):
    data1 = data.strip().split('","') # splitting by '","'
    data2 = data1[0].split(',"')
    data1 = data2 + data1
    del data1[2]
    del data1[0]
    print(data1)
    stripped_list = []
    for new_data in data1:
        stripped_data = new_data.replace(',','')
        stripped_list.append(int(stripped_data.replace('"','')))
    return stripped_list



readData()