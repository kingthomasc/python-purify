from abc import ABCMeta
from urllib import quote
from urllib2 import urlopen
from xml.etree import cElementTree as ET

from python_purify.exceptions import PurifyFormatException, PurifyException, \
    PurifyExceptionTooLarge

try:
    from simplejson import loads, dumps
except ImportError:
    from json import loads, dumps


class _AbstractPurifyBase(object):
    _request_string = None
    __metaclass__ = ABCMeta

    def __init__(self, api_key, live=True, rspformat='json', verbose=False,
                 usehttps=False, base_word_url='api1.webpurify.com', base_img_url='im-api1.webpurify.com', base_vid_url='vid-api1.webpurify.com'):
        self._base_word_url = base_word_url
        self._base_img_url  = base_img_url
        self._base_vid_url  = base_vid_url
        self._api_key = api_key
        self._live = live
        try:
            assert rspformat.lower() == 'json' or rspformat.lower() == 'xml'
        except AssertionError as e:
            raise PurifyException('format must be "json" or "xml"')
        self._rspformat = rspformat.lower()
        self._verbose = verbose
        if usehttps:
            self._protocol = 'https'
        else:
            self._protocol = 'http'

        super(_AbstractPurifyBase, self).__init__()

    @staticmethod
    def _make_options(**kwargs):
        out = []
        for key, value in kwargs.iteritems():
            if value is not None:
                envalue = quote(str(value), safe='')
                out.append('{key}={value}'.format(key=str(key), value=envalue))

        return ('&' + '&'.join(out)) if out else ''

    @staticmethod
    def _parse_json(content):
        try:
            return loads(content)
        except ValueError as e:
            if '414 Request-URI Too Large' in content:
                raise PurifyExceptionTooLarge(
                        'The URL was too long. Request not made.'
                    )
            root = ET.fromstring(content)
            err = root.find('err')
            raise PurifyFormatException(err.get('msg'), code=err.get('code'))

    @staticmethod
    def _parse_xml(content):
        if '414 Request-URI Too Large' in content:
                raise PurifyExceptionTooLarge(
                    'The URL was too long. Request not made.'
                )
        try:
            return ET.fromstring(content)  # ET.tostring(out) to get string back.
        except ET.ParseError as e:
            root = ET.fromstring(content)
            err = root.find('err')
            raise PurifyFormatException(err.get('msg'), code=err.get('code'))

    def _parse_response(self, response_txt, response_code):
        if response_code != 200:
            raise PurifyException('Error connecting with WebPurify. '
                                  'Status Code: {}'.format(response_code))
        if self._rspformat == 'json':
            return self._parse_json(response_txt)
        elif self._rspformat == 'xml':
            return self._parse_xml(response_txt)
        else:
            raise PurifyException('Unknown Format')

    def _call_method(self, method, **kwargs):
        extra = self._make_options(**kwargs)
        url = self._request_string.format(
            protocol=self._protocol,
            base_word_url=self._base_word_url,
            base_img_url=self._base_img_url,
            base_vid_url=self._base_vid_url,
            production="live" if self._live else "sandbox",
            method=method,
            key=self._api_key,
            format=self._rspformat,
            extra=extra
        )
        if self._verbose:
            print url

        response = urlopen(url)

        return self._parse_response(response.read(), response.getcode())


class WordPurify(_AbstractPurifyBase):

    _request_string = "{protocol}://{base_word_url}/services/rest/?method=webpurify.{production}.{method}&api_key={key}&format={format}{extra}"

    def check(self, text, semail=0, sphone=0, slink=0, rsp=0):
        return self._call_method('check', semail=semail, sphone=sphone,
                                 slink=slink, rsp=rsp, text=text)

    def check_count(self, text, semail=0, sphone=0, slink=0, rsp=0):
        return self._call_method('checkcount', semail=semail, sphone=sphone,
                                 slink=slink, rsp=rsp, text=text)

    def replace(self, text, replacesymbol='*', semail=0, sphone=0, slink=0,
                rsp=0):
        return self._call_method('replace', semail=semail, sphone=sphone,
                                 slink=slink, rsp=rsp,
                                 replacesymbol=replacesymbol, text=text)

    def wp_return(self, text, semail=0, sphone=0, slink=0, rsp=0):
        return self._call_method('return', semail=semail, sphone=sphone,
                                 slink=slink, rsp=rsp, text=text)

    def add_to_blacklist(self, word, ds=0):
        return self._call_method('addtoblacklist', ds=ds, word=word)

    def add_to_whitelist(self, word):
        return self._call_method('addtowhitelist', word=word)

    def remove_from_blacklist(self, word):
        return self._call_method('removefromblacklist', word=word)

    def remove_from_whitelist(self, word):
        return self._call_method('removefromwhitelist', word=word)

    def get_blacklist(self, ds=0):
        return self._call_method('getblacklist', ds=ds)

    def get_whitelist(self):
        return self._call_method('getwhitelist')


class ImagePurify(_AbstractPurifyBase):

    _request_string = "{protocol}://{base_img_url}/services/rest/?method=webpurify.{production}.{method}&api_key={key}&format={format}{extra}"

    def img_check(self, imgurl, customimgid=None, callback=None):
        return self._call_method('imgcheck', imgurl=imgurl,
                                 customimgid=customimgid, callback=callback)

    def img_status(self, imgid=None, customimgid=None):
        if imgid is None and customimgid is None:
            raise PurifyException("you must specify an imgid or customimgid")
        return self._call_method('imgstatus', imgid=imgid,
                                 customimgid=customimgid)

    def img_account(self):
        return self._call_method('imgaccount')


class VideoPurify(_AbstractPurifyBase):

    _request_string = "{protocol}://{base_vid_url}/services/rest/?method=webpurify.{production}.{method}&api_key={key}&format={format}{extra}"

    def vid_check(self, vidurl, customvidid=None, callback=None):
        return self._call_method('vidcheck', vidurl=vidurl,
                                 customvidid=customvidid, callback=callback)

    def vid_status(self, vidid=None, customvidid=None):
        if vidid is None and customvidid is None:
            raise PurifyException("you must specify an vidid or customvidid")
        return self._call_method('vidstatus', vidid=vidid,
                                 customvidid=customvidid)

    def vid_account(self):
        return self._call_method('vidaccount')
