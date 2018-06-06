from dateparser import parse
from datetime import date, datetime
import re

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class PrMaringaSpider(BaseGazetteSpider):
    TERRITORY_ID = '4115200'
    name = 'pr_maringa'
    allowed_domains = ['maringa.pr.gov.br']
    starting_year = 2015

    def start_requests(self):
        """
        @url http://venus.maringa.pr.gov.br/arquivos/orgao_oficial/paginar_orgao_oficial_ano.php
        @returns requests 1
        """
        todays_date = date.today()
        current_year = todays_date.year
        for year in range(current_year, 2006, -1):
            yield scrapy.FormRequest(
                'http://venus.maringa.pr.gov.br/arquivos/orgao_oficial/paginar_orgao_oficial_ano.php',
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                formdata={
                    'ano': str(year),
                    'entrar': 'Buscar'
                },
                callback=self.parse_year
            )

    def parse_year(self, response):
        # print(response.body)
        rows = response.css('table tr')[1:]
        for row in rows:
            gazette_id = row.css('td:nth-child(1) a::attr(href)').re_first('.*/[oO]{2}[mM] (.*)')
            gazette_date = row.css('td:nth-child(2) font > font::text').extract_first()
            yield Gazette(
                date=parse(f'{gazette_date}', languages=['pt']).date(),
                file_urls=[f'http://venus.maringa.pr.gov.br/arquivos/orgao_oficial/arquivos/oom%20{gazette_id}'],
                is_extra_edition=any(extra_char in gazette_id for extra_char in ['A', 'B', 'C', 'D']),
                territory_id=self.TERRITORY_ID,
                power='executive_legislature',
                scraped_at=datetime.utcnow()
            )
