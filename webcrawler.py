#This procedure will look for the next link in the page, if it finds one it
#returns the next link or else returns None and 0

import urllib




def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1 :
        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1 : end_quote]
    return url, end_quote

def get_page(url):
    try :
        return urllib.urlopen(url).read()
    except :
        return ""


def crawl_web(page):
    tocrawl = [seed]
    crawled = []
    i = 0 # A flag to make the first interation of tocrawl with pop false
    #crawled = tocrawl.pop
    while tocrawl :
        if i == 1 :
            crawled = tocrawl.pop()
        print crawled
        #page = get_page(url)
        while tocrawl :
            url , endpos = get_next_target(page)
            if url not in crawled :
                if url:
                    tocrawl.append(url)
                    page = page[endpos:]
                    print 'To Crawl:'
                    print tocrawl
                # print endpos
                else:
                    break
                    #crawled.append(tocrawl[0])
                    #del tocrawl[0]
                    """ pageToCrawl = tocrawl.pop()
                    page = get_page(pageToCrawl)
                    tocrawl.append(pageToCrawl)
                    print 'Crawled:'
                    print crawled
                    print tocrawl
                    i = 1  """
                    
                
            else :
                tocrawl.remove(url)
    return             

#This is the starting of the web crawler code.

#seed = 'http://xkcd.com/353'
seed = 'https://www.udacity.com/cs101x/index.html'
page = get_page(seed)

crawl_web(page)








