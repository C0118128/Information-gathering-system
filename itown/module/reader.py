import csv

class CsvReader:
    # CSV読み込み
    def readCsv(self, csv_path,row_num):
        csv_contents = []
        with open(csv_path) as f:
            reader = csv.reader(f)
            for row in reader:
                content = []
                for num in row_num:
                    content.append(row[num])
                csv_contents.append(content)
        return csv_contents  