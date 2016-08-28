from bs4 import BeautifulSoup
import urllib2
import cookielib



import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#def makepath(icon):
    # import os
    # di = icon.split("/")
    # for word in di:
    #     if ".png"in word:
    #         pass
    #     else:
    #         try:
    #             os.mkdir()




def get_recent_src():
     cookie = cookielib.CookieJar()
     handler = urllib2.HTTPCookieProcessor(cookie)
     opener = urllib2.build_opener(handler)
     url_old = 'http://desktop.nju.edu.cn:8080/jiaowu/login.do?userName=xxxxxxxx&password=xxxxxxxx'
     response = opener.open(url_old)

     source = response.read()
     soup = BeautifulSoup(source, "lxml")
     precc = soup.find(id="Function")
     cc = precc.ul.find_all("li")
     print cc
     profix = "http://desktop.nju.edu.cn:8080/jiaowu/"
     import os
     for line in cc:
         href=(profix+line.find("a").get("href"))
         print href
         get_next_src(href)
         icon = line.find("img").get('src')
         if str(icon).startswith("image"):
             last = str(icon).rfind('/')
             path = str(icon)[:last]
             print path
             try :
                os.makedirs(path)
             except:
                pass
             content2 = urllib2.urlopen(profix+icon).read()

             with open(str(icon), 'wb') as code:
                 code.write(content2)


def get_next_src(url):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    url_old = 'http://desktop.nju.edu.cn:8080/jiaowu/login.do?userName=xxxxxxxx&password=xxxxxxxx'
    responseo = opener.open(url_old)
    response = opener.open(url)

    source = response.read()
    soup = BeautifulSoup(source, "lxml")
    precc = soup.find(id="Function")
    cc = precc.ul.find_all("li")
    print cc
    profix = "http://desktop.nju.edu.cn:8080/jiaowu/"
    import os
    for line in cc:
        name = line.get_text()
        href = (profix + line.find("a").get("href"))
        icon = line.find("img").get('src')
        if str(icon).startswith("image"):
            last = str(icon).rfind('/')
            path = str(icon)[:last]
            print path
            try:
                os.makedirs(path)
            except:
                pass
            content2 = urllib2.urlopen(profix + icon).read()

            with open(str(icon), 'wb') as code:
                code.write(content2)


def main():
    get_recent_src()


if __name__ == "__main__":
    main()
