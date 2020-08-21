import csv

def modify_csv_by_column_name_order(file):
    f = open(file, 'r')
    if f.mode == 'r':
        freader = csv.reader(f)
        fheader = next(freader)
        f.seek(0)
        fheader.sort()
        fdictread = csv.DictReader(f)
        all_data = []
        for row in fdictread:
            all_data.append(row)
        f.close()
        f = open(file, "w", newline='')
        fdictwrite = csv.DictWriter(f,fheader)
        fdictwrite.writeheader()
        for row in all_data:
            fdictwrite.writerow(row)
        f.close()
    else:
        print("File can't be read {}".format(file))


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

if __name__ == "__main__":
    modify_csv_by_column_name_order(r"C:\Users\ddey\Documents\PythonSv\output_08_20_20_16_18_48.csv")