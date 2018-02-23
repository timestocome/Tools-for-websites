# http://github.com/timestocome


# read in sitemape.xml and convert the urls to html formatted links


import string as st
import re




# file names
link_file_name = 'links.html'
input_file_name = 'sitemap.xml'





# read in sitemap.xml and put urls to pages into an array
# don't save urls to images
def read_file():

    data = []
    urls = []
    
    with open(input_file_name, encoding='utf8') as f:

        # pull a list of links from each link
        for line in f:

            urls_list = re.findall('<loc>(.*?)<\/loc>',line)            
            data.append(urls_list)

    # pull individual urls from lists
    for i in data:
        for j in i:
             urls.append(j)
                
    return urls






# convert urls to html links, use the URL to create a title
def convert_to_links(urls):


    links = []
    
    for u in urls:
        
        # grab the url and enclose it in html
        location = '<a href="' + u + '">'

        # grab the tail end of the url to use as link description
        text_all = location.split('/')
        text = text_all[len(text_all) - 2]
        desc = re.sub(r'-', ' ', text)
        desc = desc.title()

        # put it all together
        link = '<p>' + location + desc + '</a></p>'
        
        links.append(link)

    return links





def save_links_to_file(links):

    file = open(link_file_name, 'w')
    
    for l in links:
        file.write("%s\n" % l)

    file.close()



urls = read_file()

links = convert_to_links(urls)


# save list of links to file
save_links_to_file(links)
