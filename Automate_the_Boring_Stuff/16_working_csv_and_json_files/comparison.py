import csv

# Read csv file
f1= open('D:/csv_files/devices_usage.csv', 'r')
f2= open('D:/csv_files/lusd_verified_verizon.csv', 'r')

#Turn file into a Dictionary list
list1 = csv.DictReader(f1)
list2 = csv.DictReader(f2)

#Read only the column named 'column_IMEI' store it in a list
imei_1 = []
for column in list1:
    imei_1.append(column['column_IMEI'])

#Read only the column named 'column_IMEI' store it in a list
imei_2 = []
for column in list2:
    imei_2.append(column['column_IMEI'])

#Compare the values of two lists output the similarity store it in a list
imei_3 = []
for column in imei_1:
    if column in imei_2:
        if column is not imei_3:
            imei_3.append(column)

#Test the new list
# print(imei_3)

#Create a csv file
file = open('D:/csv_files/same_imei_hotspots.csv', 'w', newline='')

#Write to the csv file
outputWriter = csv.writer(file)
outputWriter.writerow(['IMEI_Column'])
outputWriter.writerows([imei_3])
file.close()