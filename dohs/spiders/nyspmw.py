import datetime
from dohs.items import DohsItem
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
import logging
import scrapy

class NyspmwSpider(scrapy.Spider):
    name = 'nyspmw'
    allowed_domains = ['www.dhs.state.mn.us/main/idcplg?']
    start_urls = ['https://www.dhs.state.mn.us/main/idcplg?IdcService=GET_DYNAMIC_CONVERSION&dDocName=dhs16_177448&RevisionSelectionMethod=LatestReleased']
    custom_settings={ 
        'FEED_URI':'nyspmw.json',
        'FEED_FORMAT':'json'
    }

    def parse(self, response):
        item = DohsItem()    
        print(len(response.css('table')[0].css('tr')))
        
        for row in response.css('table')[0].css('tr'):
            logger = logging.getLogger()
            fhandler = logging.FileHandler(filename='nyspmw.log', mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.DEBUG)
            except1 = row.css('td')[1].css('b::text').get()
            except2 = row.css('td')[2].css('b::text').get()
            except3 = row.css('td')[3].css('b::text').get()
            except4 = row.css('td')[4].css('b::text').get()
            except5 = row.css('td')[5].css('b::text').get()
            except6 = row.css('td')[6].css('b::text').get()
            except7 = row.css('td')[7].css('b::text').get()
            except8 = row.css('td')[8].css('b::text').get()
            except9 = row.css('td')[9].css('b::text').get()
            if (except1=="LastName" and except2 == "FirstName" and except3 == "MiddleName" and except4 == "EffectiveDateOfExclusion" and except5 == "AddressLine1" and except6 == "AddressLine2" and except7 == "City" and except8 == "ST" and except9 == "Zip"):
                pass
            else:
                formatting1 = row.css('td')[4].css('span::text').get()            
                formatting2 = datetime.datetime.strptime(formatting1, "%m/%d/%Y")
                formatting3 = formatting2.strftime("%m-%d-%Y").strip()
                item['firstName'] = row.css('td')[2].css('span::text').get()
                item['middleName'] = row.css('td')[3].css('span::text').get()
                item['lastName'] = row.css('td')[1].css('span::text').get()
                item['address1'] = row.css('td')[5].css('span::text').get()
                item['address2'] = row.css('td')[6].css('span::text').get()
                item['city'] = row.css('td')[7].css('span::text').get()
                item['stateProvince'] = row.css('td')[8].css('span::text').get()
                item['postalCode'] = row.css('td')[9].css('span::text').get()
                item['country'] = "United States of America"
                item['listedOn'] = formatting3
                item['externalSources'] = 'https://www.dhs.state.mn.us/main/idcplg?IdcService=GET_DYNAMIC_CONVERSION&dDocName=dhs16_177448&RevisionSelectionMethod=LatestReleased'
                item['type'] = "INDIVIDUAL"
                
                yield item

