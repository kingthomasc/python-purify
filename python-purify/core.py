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

    def return(self, text, semail=1, sphone=1, slink=1):
        url = request_string % ("live" if self.live else "sandbox", "return", self.api_key, "&semail=%d&sphone=%d&slink=%d&text=%s" % (semail, sphone, slink, text))
        req = requests.get(url)
        return loads(req.content)

    def add_to_blacklist(self, word, ds=1):
        url = request_string % ("live" if self.live else "sandbox", "addtoblacklist", self.api_key, "&ds=%d&word=%s" % (ds, word))
        req = requests.get(url)
        return loads(req.content)

    def add_to_whitelist(self, word):
        url = request_string % ("live" if self.live else "sandbox", "addtowhitelist", self.api_key, "&word=%s" % word)
        req = requests.get(url)
        return loads(req.content)

    def remove_from_blacklist(self, word):
        url = request_string % ("live" if self.live else "sandbox", "removefromblacklist", self.api_key, "&word=%s" % word)
        req = requests.get(url)
        return loads(req.content)

    def remove_from_whitelist(self, word):
        url = request_string % ("live" if self.live else "sandbox", "removefromwhitelist", self.api_key, "&word=%s" % word)
        req = requests.get(url)
        return loads(req.content)

    def get_blacklist(self, ds=1):
        url = request_string % ("live" if self.live else "sandbox", "getblacklist", self.api_key, "&ds=%d" % ds)
        req = requests.get(url)
        return loads(req.content)

    def get_whitelist(self):
        url = request_string % ("live" if self.live else "sandbox", "getwhitelist", self.api_key, "")
        req = requests.get(url)
        return loads(req.content)

    def img_check(self, img_url, custom_img_id=None, callback=None):
        url = request_string % ("live" if self.live else "sandbox", "imgcheck", self.api_key, "&imgurl=%s%s%s" % (ds, ("&customimgid=%s" % custom_img_id if custom_img_id != None else ""), ("&callback=%s" % callback if callback != None else ""), ))
        req = requests.get(url)
        return loads(req.content)

    def img_status(self, img_id=None, custom_img_id=None):
        if img_id == None and custom_img_id == None:
            raise Exception("you must specify an img_id or custom_img_id")
        url = request_string % ("live" if self.live else "sandbox", "imgcheck", self.api_key, ("&customimgid=%s" % custom_img_id) if custom_img_id != None else ("&imgid=%s" % "imgid"))
        req = requests.get(url)
        return loads(req.content)
