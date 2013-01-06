#coding=gb2312
'''
Created on 2012-7-18
@author: zhaolin.huang
用此替代curl无法提交中文字符的工具
'''
import  urllib2
import  urllib
import  sys
from string import  join

def curl(url):
    def encodeUrl(url):
        "将中文URL"
        queryString = str(url).split("?")[1] if len(str(url).split("?")) > 1 else None
        if queryString:
            parameters = queryString.split("&")
            encodeParameters = {}
            for parameter in parameters:
                try:
                    key_value = parameter.split("=")
                    #value = urllib.quote(key_value[1].decode('gb2312').encode('utf8'))
                    encodeParameters[key_value[0]]=key_value[1]
                except  Exception, e:
                    print("url %s 参数异常，请查看! %s" % (parameter, e))
        return urllib.urlencode(encodeParameters)#(str(url).split("?")[0]) + "?" + join([join(params, "=") for params in encodeParameters], "&")

    response = urllib2.urlopen(str(url).split("?")[0],encodeUrl(url))
    print(response.read())


def main():
    url = join([str(i).strip() for i in sys.argv[1:]])
    curl(url)

if __name__ == "__main__":
    main()
