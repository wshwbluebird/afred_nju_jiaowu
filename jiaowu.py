# encoding: utf-8


from bs4 import BeautifulSoup
import urllib2
import cookielib
import alfred


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_recent_posts():
     cookie = cookielib.CookieJar()
     handler = urllib2.HTTPCookieProcessor(cookie)
     opener = urllib2.build_opener(handler)
     url_old = 'http://desktop.nju.edu.cn:8080/jiaowu/login.do?userName=xxxxxxxx&password=xxxxxxxx'
     response = opener.open(url_old)
     source = response.read()

     soup = BeautifulSoup(source, "lxml")
     precc = soup.find(id="Function")
     cc = precc.ul.find_all("li")

     profix = "http://desktop.nju.edu.cn:8080/jiaowu/"
     feedback = alfred.Feedback()
     feedback.clean()
     for line in cc:
          name = line.get_text()
          href = (profix + line.find("a").get("href"))
          iconp = str(line.find("img").get('src'))
          feedback.addItem(
                 title=name,
                 subtitle='join the web',
                 arg=href,
                 autocomplete=href,
                 icontype='fileicon',
                 icon=iconp
           )
     feedback.output()


def main():
      get_recent_posts()


if __name__ == "__main__":
    main()





