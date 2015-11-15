from lxml import html
import re, requests

import sys
import codecs

from wolf import data

class TestGrabberBase:
    def can_grab_from(self, url):
        return any(re.fullmatch(r, url) != None for r in self.get_valid_urls())
        
    def grab_tests(self, url):
        request = requests.get(url)
        tree = html.fromstring(request.text)
        return self.parse_tests(tree)

class CfTestGrabber(TestGrabberBase):
    def get_valid_urls(self):
        return [
            "^http://codeforces.com/contest/\d+/problem/\w+$",
        ]
    
    def extract_pre_block_content(tree, className):
        xpath = '//div[@class="{className}"]/pre'.format(className = className)
        return [ '\n'.join(n.xpath('text()')) for n in tree.xpath(xpath)]
    
    def parse_tests(self, tree):
        inputs = CfTestGrabber.extract_pre_block_content(tree, 'input')
        outputs = CfTestGrabber.extract_pre_block_content(tree, 'output')
        return list(data.Test(i, o) for (i, o) in zip(inputs, outputs))
        
available_grabbers = [
    CfTestGrabber(),
]
