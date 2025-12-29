# urlib.parse (https://docs.python.org/3/library/urllib.parse.html?referrer=grok.com)
# html (https://docs.python.org/3/library/html.html?referrer=grok.com)
# base64 (https://docs.python.org/3/library/base64.html?referrer=grok.com)
# codecs (https://docs.python.org/3/library/codecs.html?referrer=grok.com)
# binascii (https://docs.python.org/3/library/binascii.html?referrer=grok.com)
# unicodedata (https://docs.python.org/3/library/unicodedata.html?referrer=grok.com)

import urllib.parse
import html
import base64
import codecs
import binascii
import unicodedata
import random

hello_message0 = '''
       .---.
      /     \
      \.@-@./
      /`\_/`\
     //  _  \\
    | \     )|_
   /`\_`>  <_/ \
   \__/'---'\__/  by flavio400'''

hello_message = '''these are the types of encoding:
[+] URL
[+] Double URL
[+] HTML
[+] Unicode
[+] Base64
[+] UTF-7
[+] all (in a file.txt)
[+] all with perms (in a file.txt)'''

print(hello_message0)

payload = input('insert the payload to encode >> ')

print(hello_message)

enc_type = input('insert the tipe of encoding >> ')

if enc_type == 'URL':
    URL_encoded = urllib.parse.quote(payload)
    print(URL_encoded)

if enc_type == 'Double URL':
    Double_URL_encoded = urllib.parse.quote(urllib.parse.quote(payload))
    print(Double_URL_encoded)

if enc_type == 'HTML':
    HTML_encoded = html.escape(payload)
    print(HTML_encoded)

if enc_type == 'Unicode':
    Unicode_encoded = payload.encode('unicode-escape').decode()
    print(Unicode_encoded)

if enc_type == 'UTF-7':
    UTF7_encoded = codecs.encode(payload, 'utf-7')
    print(UTF7_encoded)

if enc_type == 'all':
    with open('enc_payloads.txt', 'w') as f:
        f.write(f"{urllib.parse.quote(payload)}\n")
        f.write(f"{urllib.parse.quote(urllib.parse.quote(payload))}\n")
        f.write(f"{html.escape(payload)}\n")
        f.write(f"{payload.encode('unicode-escape').decode()}\n")
        f.write(f"{codecs.encode(payload, 'utf-7')}\n")

if enc_type == 'all with perms':
    with open('enc_payloads2.txt', 'w') as t:
        t.write(f"{urllib.parse.quote(payload)}\n")
        t.write(f"{urllib.parse.quote(urllib.parse.quote(payload))}\n")
        t.write(f"{html.escape(payload)}\n")
        t.write(f"{payload.encode('unicode-escape').decode()}\n")
        t.write(f"{codecs.encode(payload, 'utf-7')}\n")
        # perm random
        def random_case_variant(text):
            return ''.join(random.choice([c.upper(), c.lower()]) for c in text)
        for i in range(15):
            variant = random_case_variant(payload)
            t.write(f"{variant}\n")
        # perm random e encoding URL
        for s in range(15):
            variant2 = random_case_variant(payload)
            encoded = urllib.parse.quote(variant2)
            t.write(f"{encoded}\n")
        # perm random e encoding HTML
        for x in range(15):
            variant3 = random_case_variant(payload)
            encoded2 = html.escape(variant3)
            t.write(f"{encoded2}\n")
        # perm random e endoding Double URL
        for y in range(15):
            variant4 = random_case_variant(payload)
            encoded3 = urllib.parse.quote(urllib.parse.quote(variant4))
            t.write(f"{encoded3}\n")
        print('[!!] enc_payloads2.txt generated, you might wanna use it with burp intruder')
else:
    print('please select a valid type of encoding')