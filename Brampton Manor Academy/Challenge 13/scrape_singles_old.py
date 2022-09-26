import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

if __name__ == "__main__":
    html = scrape(url)











    print(f'{"POSITION":<16}')

    x = 0
    i = 0

    while x < 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)

        newstring = html[open_tr:close_tr]
        
        look_for_pos = '"position">'
        pos_start = newstring.find(look_for_pos)
        pos_end = newstring.find('</', pos_start)
        position = newstring[pos_start+len(look_for_pos):pos_end]

        look_for_song = 'href="/search/singles/'
        song_start = newstring.find(look_for_song)
        song_end = newstring.find('</',song_start)
        song = newstring[song_start+len(look_for_song):song_end]

        print(f'{position:<16} {song:<16}')




        

        i = close_tr
        x += 1

