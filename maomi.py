import requests,re,os
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
def download(p,n):    
    res = requests.get("https://www.npa69.com/tupian/list-{}-{}.html".format(p,n+1),headers = headers)
    index_html = res.text
    pages = re.findall('<a href="(.*?)" title=".*?" target="_blank">',index_html)
    print(pages)
    for page in pages:
        r = requests.get("https://www.npa69.com"+page,headers = headers)
        r.encoding = "utf-8"
        # print(r.request.headers)
        html = r.text
        # print(html)
        dir_name = re.findall('<!--<title>(.*?)</title>-->',html)[0]
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        urls = re.findall('data-original="(.*?)"',html)
        print(urls)
        if len(urls) != 0:
            for url in urls:
                print("download")
                file_name = url.split("/")[-1]
                img = requests.get(url,headers = headers)
                name = dir_name + "/" + file_name
                with open(name,"wb") as f:
                    f.write(img.content)
for i in range(100):
    download("清纯唯美",i)
    
