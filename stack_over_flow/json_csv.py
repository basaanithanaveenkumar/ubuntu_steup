import json
import csv
def json2csv(input_file,output_file,key_of_nested):
    with open(input_file) as json_file:
        try:
            data = json.load(json_file)
        except ValueError as err:
            print("not a valid json")
            return False

    nested_data = data['key_of_nested']
    data_file = open(output_file, 'w')
    csv_writer = csv.writer(data_file)
    count = 0

    for emp in nested_data:
        if count == 0:
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values())

    data_file.close()
    return True