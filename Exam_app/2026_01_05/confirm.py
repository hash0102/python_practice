from urllib import parse

url = "https://example.com:8080/path/to/page?x=Bob Mike&y=2 section"
res1= parse.urlparse(url)
print(res1)

print('-' * 30)

res2= parse.parse_qs(res1.query)
print(res2)

print('-' * 30)

res3 = parse.urlencode(res2, quote_via=parse.quote)
print(res3)

print('-' * 30)

res4 = parse.urlencode(res2, quote_via=parse.quote_plus)
print(res4)