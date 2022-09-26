import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr


def find_position(html):
    count = 0
    i = 0
    position_list = []
    while count < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        
        look_for_pos = '"position">'
        pos_start = newstring.find(look_for_pos)
        pos_end = newstring.find('</', pos_start)
        position = newstring[pos_start+len(look_for_pos):pos_end]
        position_list.append(position)

        i = close_tr
        count += 1
        
    return position_list


def find_title(html):
    count = 0
    i = 0
    title_list = []
    while count < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]

        look_for_string = '"/search/singles/'
        string_start = newstring.find(look_for_string)
        string_end = newstring.find('a>',string_start)
        string = newstring[string_start:string_end]

        look_for_title = '/">'
        title_start = string.find(look_for_title)
        title_end = string.find('</',title_start)
        title = string[title_start+len(look_for_title):title_end]
        title_list.append(title)
                
        i = close_tr
        count += 1
        
    return title_list


def find_artist(html):
    count = 0
    i = 0
    artist_list = []
    while count < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]

        look_for_string = '"/artist/'
        string_start = newstring.find(look_for_string)
        string_end = newstring.find('a>',string_start)
        string = newstring[string_start:string_end]

        look_for_artist = '/">'
        artist_start = string.find(look_for_artist)
        artist_end = string.find('</',artist_start)
        artist = string[artist_start+len(look_for_artist):artist_end]
        artist_list.append(artist)
        
        i = close_tr
        count += 1
    
    return artist_list

def output_table(position,title,artist):
    print(f'{"NUMBER":<16} {"SONG":<35} {"ARTIST":<16}')
    for p, t, a in zip(position, title, artist):
        print(f'{p:<16} {t:<35} {a:<16}')


if __name__ == "__main__":
    html = scrape(url)
    position = find_position(html)
    title = find_title(html)
    artist = find_artist(html)
    table = output_table(position,title,artist)


    
