import re


def get_header(table):
    header_line = table.split('\n')[0]
    regex_word = r'\w+'
    headers = re.findall(regex_word, header_line)
    return headers


def get_data(table):
    headers = get_header(table)
    header_line = table.split('\n')[0]
    lines = table.split('\n')
    data = []
    for i in range(1, len(lines)):
        di = dict()
        line = lines[i]
        if line == '' : 
            continue
        for h in range(0, len(headers)):
            header = headers[h]
            start_index = header_line.find(header)
            if h >= len(headers) -1 :
                di[header] = line[start_index:].strip()
            else :
                end_index = header_line.find(headers[h + 1])
                di[header] = line[start_index:end_index].strip()
        data.append(di)
    return data
