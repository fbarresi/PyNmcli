import re


def get_header(table):
    header_line = table.split('\n')[0]
    regex_word = r'[a-zA-Z0-9_-]+'
    headers = []
    header_matches = re.finditer(regex_word, header_line)
    for header in header_matches:
        headers.append({
            'title': header.group(),
            'start': header.start()
        })

    return headers


def get_data(table):
    headers = get_header(table)
    lines = table.split('\n')
    data = []
    for i in range(1, len(lines)):
        di = dict()
        line = lines[i]
        if line == '':
            continue
        for h in range(0, len(headers)):
            header = headers[h]['title']
            start_index = headers[h]['start']
            if h >= len(headers) - 1:
                di[header] = line[start_index:].strip()
            else:
                end_index = headers[h + 1]['start']
                di[header] = line[start_index:end_index].strip()
        data.append(di)
    return data
