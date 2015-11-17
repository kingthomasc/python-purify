# update soon with python unittests...
from python_purify.core import WordPurify

wordapi = '**'
imgapi = '**'

bad = 'asdf'
good = 'That\'s a nice hat.'

jpurify = WordPurify(wordapi, live=False, debug=True)




resp = jpurify.add_to_blacklist(bad, ds=1)
assert resp.get('rsp').get('success') == '1'

resp = jpurify.get_blacklist()
assert bad in resp.get('rsp').get('word')

resp = jpurify.add_to_whitelist(bad + bad)
assert resp.get('rsp').get('success') == '1'

resp = jpurify.get_whitelist()
assert bad + bad in resp.get('rsp').get('word')

resp = jpurify.check(bad)
assert resp.get('rsp').get('found') == '1'

resp = jpurify.check(good)
assert resp.get('rsp').get('found') == '0'

resp = jpurify.check_count(' '.join([bad, good, bad]))
assert resp.get('rsp').get('found') == '2'

resp = jpurify.check_count(''.join([bad, bad]))
assert resp.get('rsp').get('found') == '0'

resp = jpurify.wp_return(' '.join([bad, good]))
assert bad in resp.get('rsp').get('expletive')

resp = jpurify.replace(' '.join([bad, good]), replacesymbol='8')
assert bad.replace(bad, '8' * len(bad)) in resp.get('rsp').get('text')

resp = jpurify.remove_from_whitelist(''.join([bad, bad]))
assert resp.get('rsp').get('success') == '1'

resp = jpurify.check_count(''.join([bad, bad]))
assert resp.get('rsp').get('found') == '1'

resp = jpurify.remove_from_blacklist(bad)
assert resp.get('rsp').get('success') == '1'

resp = jpurify.check(bad)
assert resp.get('rsp').get('found') == '0'