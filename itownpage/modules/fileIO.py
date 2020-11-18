import csv

class Csv:
    # CSV読み込み
    def readCsv(self, input_path,row_num):
        csv_contents = []
        with open(input_path) as file:
            reader = csv.reader(file)
            for row in reader:
                content = []
                for num in row_num:
                    content.append(row[num])
                csv_contents.append(content)
        return csv_contents

    def writeCsvAll(self, output_path, csv_contents):
        with open(output_path, 'w') as file:
            writer = csv.writer(file)
            for content in csv_contents:
                writer.writerow(content)

    def addCsv(self, output_path, content):
        with open(output_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(content)