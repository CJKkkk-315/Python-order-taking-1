import requests
from bs4 import BeautifulSoup
from time import sleep
def get_all_books():
    """
        获取该页面所有符合要求的书本的链接
    """
    url = 'http://search.dangdang.com/?key=python&act=input'
    book_list = []
    
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')

    book_ul = soup.find_all('ul', {'class': 'bigimg'})
    book_ps = book_ul[0].find_all('p',{'class':'name','name':'title'})
    for book_p in book_ps:
        book_a = book_p.find('a')
        book_url = book_a.get('href')
        book_title = book_a.get('title')
        #print(book_title+"\n"+book_url)
        book_list.append(book_url)
        
    return book_list

#获取每本书的url，并打印出来
books = get_all_books()
for book in books:
    print(book)

def get_book_information(book_url):
    """
        获取书籍的信息
    """
    print(book_url)
    headers = {  
     'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'  
    }  
    r= requests.get('http:' + book_url,headers=headers)
    try:
        #r = requests.get(book_url, timeout=60)
        soup = BeautifulSoup(r.text, 'lxml')
        book_info = []

        #获取书籍名称
        div_name = soup.find('div', {'class': "name_info",'ddt-area':"001"})
        h1 = div_name.find('h1')
        book_name = h1.get('title')
        book_info.append(book_name)
        #获取书籍作者
        div_author = soup.find('div',{'class':'messbox_info'})
        span_author = div_author.find('span',{'class':'t1','dd_name':'作者'})
        book_author = span_author.text.strip()[3:]
        book_info.append(book_author)

        #获取书籍出版社
        div_press = soup.find('div',{'class':'messbox_info'})
        span_press = div_press.find('span',{'class':'t1','dd_name':'出版社'})
        book_press = span_press.text.strip()[4:]
        book_info.append(book_press)

        #获取书籍价钱
        div_price = soup.find('div',{'class':'price_d'})
        book_price = div_price.find('p',{'id':'dd-price'}).text.strip()
        book_info.append(book_price)
    except:
        pass

    return book_info
import csv

#获取每本书的信息，并把信息保存到csv文件中
def main():
    header = ['书籍名称','作者','出本社','当前价钱']
    with open('DeepLearning_book_info.csv','w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i,book in enumerate(books):
            if i%10 == 0:
                print('获取了{}条信息，一共{}条信息'.format(i,len(books)))

            l = get_book_information(book)
            print(l)
            sleep(3)
            writer.writerow(l)
if __name__ == '__main__':
    main()
