from apps.stockmarket.models import Stock
import requests
import re


def get_stock_info():
    regex = '<a rel="nofollow" class="external text" href="(.+?)">(.+?)</a></td>\n<td><a href="(.+?)" title="(.+?)">(.+?)</a></td>'
    pattern = re.compile(regex)

    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    htmltext = response.text
    data = re.findall(pattern, htmltext)

    company_ticker_pair = []
    for listing in data:
        current_biz = []
        current_biz.append(listing[1])
        current_biz.append(listing[4])
        company_ticker_pair.append(current_biz)

    return company_ticker_pair


def scrape_stocks():
    companies = get_stock_info()
    for company in companies:
        s = Stock(name=company[1], ticker=company[0])
        s.save()
        print("Entered: {}".format(company[0]))