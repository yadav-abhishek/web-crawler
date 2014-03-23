#This procedure will look for the next link in the page, if it finds one it
#returns the next link or else returns None and 0

import urllib
def get_page(url):
    try :
        return urllib.urlopen(url).read()
    except :
        return ""



def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1 :
        return None,0

    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1 : end_quote]
    return url, end_quote

#This is the starting of the web crawler code.

page = get_page('http://xkcd.com/353')
while True :
    url , endpos = get_next_target(page)
    if url:
        print url
        page = page[endpos:]
        #print endpos
    else:
        break









