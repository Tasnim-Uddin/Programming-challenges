import csv


def read_csv(path):  #the path is the parameter in line 39
    csv_contents = []
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            csv_contents.append(row)
    csv_file.close()
    return csv_contents

def read_html(path):
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
    html_file.close()
    return html_contents

def process(csv, html):
    previous_link = 0
    previous_initial = 0
    previous_name = 0
    i = 1
    while i < 6:
        for column in csv:
            link_csv, initial_csv, name_csv = column[0], column[1], column[2]
            html = html.replace(f'link{i}', link_csv)
            html = html.replace(f'initials{i}', initial_csv)
            html = html.replace(f'name{i}', name_csv)
            i += 1
    return html

def write_html(path, html):
    with open(path, 'w') as new_html:
        new_html.write(html)

        
if __name__ == '__main__':
    csv = read_csv(path = 'south.csv')
    html = read_html(path = 'south.html')
    html = process(csv, html)
    write_html(path = 'south_final.html', html = html)
