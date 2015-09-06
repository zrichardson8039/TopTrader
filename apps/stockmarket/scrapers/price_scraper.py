from apps.stockmarket.models import Stock, Price
from datetime import date
import asyncio
import aiohttp
import tqdm


SEMAPHORE = asyncio.Semaphore(15)


@asyncio.coroutine
def get(url):
    response = yield from aiohttp.request('GET', url)
    return (yield from response.read_and_close())


@asyncio.coroutine
def wait_with_progress(coros):
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        yield from f


def decode_response(response):
    try:
        return (response.decode("utf-8`"))
    except:
        return []


def get_prices(response, ticker):
    response = decode_response(response)
    if(response != []):
        data = response.split('\n')
        data.pop(0)
        all_prices = []
        for row in data:
            try:
                row = row.split(',')
                price_data = []
                price_data.append(row[1])
                price_data.append(row[0])
                price_data.append(row[6])
                all_prices.append(price_data)
            except Exception as e:
                pass
    else:
        return []
    return all_prices

def write_prices_to_db(s, prices, url):
    s.prices_url = url
    for p in prices:
        price_date = date(year=int(p[1][0:4]), month=int(p[1][4:6]), day=int(p[1][6:8]))
        price_to_insert = Price(date=price_date, price=p[2], stock=s)
        price_to_insert.save()
    s.has_prices = True
    s.save(update_fields=['prices_url','has_prices'])


@asyncio.coroutine
def scrape_stock_prices(s):
    url = 'http://www.netfonds.no/quotes/paperhistory.php?paper={}.N&csv_format=csv'.format(s.ticker)
    with (yield from SEMAPHORE):
        response = yield from get(url)
    prices = get_prices(response, s.ticker)
    if(prices != []):
        write_prices_to_db(s, prices, url)
        return

    url = 'http://www.netfonds.no/quotes/paperhistory.php?paper={}.O&csv_format=csv'.format(s.ticker)
    with (yield from SEMAPHORE):
        response = yield from get(url)
    prices = get_prices(response, s.ticker)
    if(prices != []):
        write_prices_to_db(s, prices, url)


def scrape_prices():
    stocks = Stock.objects.filter(has_prices=False)
    loop = asyncio.get_event_loop()
    scrape = wait_with_progress([scrape_stock_prices(s) for s in stocks])
    loop.run_until_complete(scrape)