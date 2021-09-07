import csv

if __name__ == '__main__':
    with open("data/note1.txt", "r") as f:  #or f = open()
        notes = f.read()
        # f.write()
        # f.writelines()
        # f.readline()
        # f.readlines()
        # for line in f:
        # f.read(100)
        # f.tell() // get position
        # f.seek(0) // set position
        print(notes)  # end=''
    # [x.rstrip() for x in open(path)]

    with open("data/report.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)  # delimiter='-'
        # csv_writer =csv.writer(csv_file, delimiter='\t')
        # csv_writer.writerow(line)
        # next(csv_reader)
        # csv.DictReader()
        # csv.DictWriter(file, fieldnames=[], delimiter='')
        # csv_writer.writeheader()
        for line in csv_reader:
            print(line)
