import urllib2
import csv
import re
import decimal
import argparse


def downloadData(url):
    # file = urllib2.urlopen(url)
    # file = url

    with open(url, 'rb') as file:
        d_list = []
        read_file = csv.reader(file)
        for row in read_file:
            d_list.append(row)
    return d_list

def search_match(data):
    img = 0
    not_img = 0
    total = 0
    for i in data:
        string = str(i)
        regex = re.search(r'(PNG|JPEG|JPG|GIF)', string)
        if regex:
            img += 1
        else:
            not_img += 1
        total += 1
    imgs = (float(img)*100/total)
    not_imgs = (float(not_img)*100/total)
    return imgs

def browser_search(data):
    s_count = 0
    ie_count = 0
    chrome_count = 0
    firefox_count = 0
    for i in data:
        string = str(i)
        safari = re.search(r'(?=(Mac OS X)(Safari))', string)
        ie = re.search(r'(MSIE)', string)
        chrome = re.search(r'(Chrome)', string)
        firefox = re.search(r'(Firefox)', string)
        if ie:
            ie_count += 1
            i = ie.group(0)
        elif chrome:
            chrome_count += 1
            c = chrome.group(0)
        elif firefox:
            firefox_count += 1
            f = firefox.group(0)
        else:
            s_count += 1
    L = [s_count, ie_count, chrome_count, firefox_count]
    pop = max(L)
    return pop, c



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='enter the data url')
    args = parser.parse_args()
    if args.url:
        data = downloadData(args.url)
        results = search_match(data)
        print 'Image requests account for {}% of all requests'.format(results)
        browser_num, browser_pop = browser_search(data)
        print 'The most popular browser is: {} with {} hits'.format(browser_pop, browser_num)
    else:
        exit()