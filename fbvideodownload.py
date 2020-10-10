import requests as r, bs4, urllib.parse as u

#Uncode is u.unquote(url)

def HTMLParser(url):
    # print(url)
    url = r.get(url)
    UrlHTML = bs4.BeautifulSoup(url.text, 'lxml')
    videoSource = UrlHTML.findAll('a', href=True) 
    videoTag = [i for i in videoSource if 'mp4' in str(i)][0] 
    videoTag = str(videoTag).split(';')[0]
    videoUrl = videoTag.split('src=')[1]
    return u.unquote(str(videoUrl))
        
def VideoUrl(url):
    try:
        if 'www' in url:
            url = url.replace('www', 'm')
            # print(url)
        elif '//f' in url:
            url = url.replace('//f', '//m.f')
            # print(url)
        elif 'm.' in url:
            pass
        else:
            print('Non Valid URL')
        return HTMLParser(url)
    except:
        return'An error has occurred, please contact the script creator.'

if __name__ == "__main__": 
    url = input('Type your Facebook Video URL: ')
    if 'http' not in url:
        url = 'https://'+url
    print(f'Your Video URL is: {VideoUrl(url)}')
