import requests
from simplejson import loads, dumps

request_string = "http://api1.webpurify.com/services/rest/?method=webpurify.%s.%s&api_key=%s&rsp=1&format=json%s"

class Purify():
    def __init__(self, api_key, live=True):
        self.api_key = api_key
        self.live = live

    def check(self, text, semail=1, sphone=1, slink=1):
        url = request_string % ("live" if self.live else "sandbox", "check", self.api_key, "&semail=%d&sphone=%d&slink=%d&text=%s" % (semail, sphone, slink, text))
        req = requests.get(url)
        return loads(req.content)

    def check_count(self, text, semail=1, sphone=1, slink=1):
        url = request_string % ("live" if self.live else "sandbox", "checkcount", self.api_key, "&semail=%d&sphone=%d&slink=%d&text=%s" % (semail, sphone, slink, text))
        req = requests.get(url)
        return loads(req.content)

    def replace(self, text, replace_symbol='*', semail=1, sphone=1, slink=1):
        url = request_string % ("live" if self.live else "sandbox", "replace", self.api_key, "&replacesymbol=%s&semail=%d&sphone=%d&slink=%d&text=%s" % (replace_symbol, semail, sphone, slink, text))
        req = requests.get(url)
        return loads(req.content)
