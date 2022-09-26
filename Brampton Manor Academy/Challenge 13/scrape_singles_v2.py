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
    i = 0

    while True: #this must change
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
        
        newstring = html[open_tr:close_tr]
        lookingfor = '"position">'
        pos_start = newstring.find(lookingfor)
        pos_end = newstring.find('</', pos_start)
        print(newstring[pos_start+len(lookingfor):pos_end])

        i = close_tr
