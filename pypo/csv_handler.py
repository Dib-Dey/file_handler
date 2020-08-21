import csv

def add_access_method(_file, method):
    f = open(_file, "r")
    csv_read = csv.reader(f)
    header_col = next(csv_read)
    f.seek(0)
    print(header_col)
    csv_dict_read =csv.DictReader(f)
    file_row = []
    for row in csv_dict_read:
        #print(row)
        print(row)
        row['access methods'] = row['access methods'] +",backdoor"
        file_row.append(row)
    f.close()
    f = open(_file, "w",newline='')
    csv_writer = csv.DictWriter(f, fieldnames=header_col)
    csv_writer.writeheader()
    for row in file_row:
        csv_writer.writerow(row)
    f.close()