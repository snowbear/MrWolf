from lxml import html
import re
import requests

from wolf import data


class TestGrabberBase:
    def can_grab_from(self, url):
        return any(re.fullmatch(r, url) is not None for r in self._get_valid_urls())
        
    def grab_tests(self, url):
        request = requests.get(url)
        tree = html.fromstring(request.text)
        return self._parse_tests(tree)

    @staticmethod
    def _get_valid_urls(): raise NotImplementedError()

    @staticmethod
    def _parse_tests(tree): raise NotImplementedError()


class CfTestGrabber(TestGrabberBase):
    @staticmethod
    def _get_valid_urls():
        return [
            "^http://codeforces.com/contest/\d+/problem/\w+$",
        ]

    @staticmethod
    def extract_pre_block_content(tree, class_name):
        xpath = '//div[@class="{className}"]/pre'.format(className=class_name)
        return ['\n'.join(n.xpath('text()')) for n in tree.xpath(xpath)]

    @staticmethod
    def _parse_tests(tree):
        inputs = CfTestGrabber.extract_pre_block_content(tree, 'input')
        outputs = CfTestGrabber.extract_pre_block_content(tree, 'output')
        return list(data.Test(i, o) for (i, o) in zip(inputs, outputs))

available_grabbers = [
    CfTestGrabber(),
]
