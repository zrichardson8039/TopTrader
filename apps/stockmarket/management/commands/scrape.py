from django.core.management.base import BaseCommand
from apps.stockmarket.scrapers.stock_scraper import scrape_stocks
from apps.stockmarket.scrapers.price_scraper import scrape_prices
from apps.stockmarket.models import Stock, Price


class Command(BaseCommand):

    def handle(self, *args, **options):
        # scrape_stocks()
        # scrape_prices()
        # print(len(Price.objects.all())