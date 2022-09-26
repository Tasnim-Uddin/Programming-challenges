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
    while count < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]
        
        look_for_pos = '"position">'
        pos_start = newstring.find(look_for_pos)
        pos_end = newstring.find('</', pos_start)
        position = newstring[pos_start+len(look_for_pos):pos_end]
        
        i = close_tr
        count += 1
        return position

def find_title(html):
    count = 0
    i = 0
    while count < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]

        look_for_string = '"/search/singles/'
        string_start = newstring.find(look_for_string)
        string_end = newstring.find('</',string_start)
        string = newstring[string_start:string_end]

        look_for_title = '/">'
        title_start = string.find(look_for_title)
        title_end = string.find('</',title_start)
        title = string[title_start+len(look_for_title):title_end]
        
        i = close_tr
        count += 1
        return title

def find_artist(html):
    count = 0
    i = 0
    while count < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        newstring = html[open_tr:close_tr]

        look_for_string = '"/artist/'
        string_start = newstring.find(look_for_string)
        string_end = newstring.find('</',string_start)
        string = newstring[string_start:string_end]

        look_for_artist = '/">'
        artist_start = string.find(look_for_artist)
        artist_end = string.find('</',artist_start)
        artist = string[artist_start+len(look_for_artist):artist_end]
        
        i = close_tr
        count += 1
        return artist


if __name__ == "__main__":
    html = scrape(url)

    print(f'{"POSITION":<16} {"SONG":<35} {"ARTIST":<16}')

    position = find_position(html)
    title = find_title(html)
    artist = find_artist(html)

    print(f'{position:<16} {title:<35} {artist:<16}')

