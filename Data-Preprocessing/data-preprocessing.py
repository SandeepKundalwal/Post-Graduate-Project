import openpyxl, os

# Function to label each row based on bounding box information
# sender_address -> 1
# date -> 2
# subject -> 3
# body -> 4
# else -> 5
def label_row(x, y, sender_address_bbox, date_bbox, subject_bbox, body_bbox):
    x, y = float(x) + 20, float(y) - 120

    if sender_address_bbox[0] <= x <= sender_address_bbox[1] and sender_address_bbox[2] >= y <= sender_address_bbox[3]:
        return '1'
    elif date_bbox[0] <= x <= date_bbox[1] and date_bbox[2] >= y <= date_bbox[3]:
        return '2'
    elif subject_bbox[0] <= x <= subject_bbox[1] and subject_bbox[2] >= y <= subject_bbox[3]:
        return '3'
    elif body_bbox[0] <= x <= body_bbox[1] and body_bbox[2] >= y <= body_bbox[2]:
        return '4'
    else:
        return '5'

# Function to read a text file, label rows, and generate a new Excel file
def process_text_file(input_file, output_excel):
                        # [         left,              right,           bottom,           top         ]
    sender_address_bbox =   (59.999996185302734, 759.9999961853027, 274.4033966064453, 204.4033966064453)
    date_bbox =             (59.999996185302734, 759.9999961853027,  344.4034118652344, 274.4034118652344)
    subject_bbox =          (59.999996185302734, 759.9999961853027, 414.4034118652344, 344.4034118652344)
    body_bbox =             (59.999996185302734, 759.9999961853027, 1414.4033203125, 414.40338134765625)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Timestamp", "Date", "X", "Y", "Label"])  # header

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    for line in lines:
        timestamp, date, x, y = line.strip().split(',')
        label = label_row(x, y, sender_address_bbox, date_bbox, subject_bbox, body_bbox)
        ws.append([timestamp, date, x, y, label])

    wb.save(output_excel)


# process_text_file('1.txt', 'output.xlsx')

if __name__=="__main__": 
    directory_url = 'C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\T23023\\eye-data\\text'
    excel_directory_url = 'C:\\Users\\DELL\\Desktop\\Data-Collection\\GPT-50\\T23023\\eye-data\\excel\\'
    directory = os.fsencode(directory_url)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        question = filename.strip().split('_')[1]
        excel_name = question.strip().split('.')[0]
        if filename.endswith(".txt"):
            process_text_file(os.path.join(directory, filename.encode('utf-8')), os.path.join(excel_directory_url, (excel_name + '.xlsx')))
            continue
        else:
            continue



