import csv
import json

def transformCSVDataToJSData():
    csvFile = input('Enter the path to your CSV file: ')
    outputFile = input('Enter the path to your output JSON file: ')

    with open(csvFile, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)
        result = []

        for row in reader:
            obj = {}

            for i in range(len(headers)):
                if headers[i] == '经纬度':
                    lon, lat = row[i].split(',')
                    obj['lon'] = float(lon.strip())
                    obj['lat'] = float(lat.strip())
                else:
                    obj[headers[i]] = row[i]

            result.append(obj)

    with open(outputFile, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    return result

transformCSVDataToJSData()