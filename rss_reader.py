import requests


res = requests.get('https://news.yahoo.com/rss/')

content = res.text


def collect_news(content):
    '''
    Generates list filled with elements of 
    <item>...</item>
    '''
    found = content.find('<item>')

    content = content[found:]

    news = []

    while True:

        found = content.find('</item>')
        if found < 0:
            break
        new = content[:found]
        content = content[found+7:]
        news.append(new)

    return news


if __name__ == '__main__':
    print(collect_news())
