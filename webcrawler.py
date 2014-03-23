#This procedure will look for the next link in the page, if it finds one it
#returns the next link or else returns None and 0


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1 :
        return None,0

    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1 : end_quote]
    return url, end_quote

#This is the starting of the web crawler code.

page = ' <a href="http://chat.stackexchange.com"     data-gps-track="site_switcher.click({ item_type:6 })" >chat</a> '

url , endpos = get_next_target(page)

print url
print endpos









