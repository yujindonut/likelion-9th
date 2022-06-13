
## parser.py 
import requests 
import time
from bs4 import BeautifulSoup 
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blog.settings") 
import django 
django.setup() ## BlogData를 import해옵니다 
from crawling.models import BlogData 
def parse_blog(): 
    #req = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%B0%B1%EC%8B%A0&oquery=%EC%BD%94%EB%A1%9C%EB%82%98&tqi=hdyUzwprvhGssj%2F41fwssssssU8-138263') 
    req = requests.get('https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98%20%EB%B0%B1%EC%8B%A0&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0')
    html = req.text 
    soup = BeautifulSoup(html, 'html.parser') 
    my_titles = soup.select( 'a.news_tit' ) 
    data = {} 
    for title in my_titles: 
        data[title.text] = title.get('href') 
    return data ## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다. if __name__=='__main__': blog_data_dict = parse_blog() for t, l in blog_data_dict.items(): BlogData(title=t, link=l).save() 

if __name__=='__main__': 
    #while True:
    blog_data_dict = parse_blog() 
    for t, l in blog_data_dict.items(): 
        BlogData(title=t, link=l).save() 
    print('작동중')
        #time.sleep(600)