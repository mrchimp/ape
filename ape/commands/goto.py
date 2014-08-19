
import ape.lib.basecommand
import os
import argparse
from urllib.request import Request, urlopen
from urllib.request import URLError
from bs4 import BeautifulSoup

class Command(ape.lib.basecommand.BaseCommand):

    prog_name = 'cd'
    prog_description = 'Change working directory.'

    def add_arguments(self):
        self.parser.add_argument('url',
            default = '.',
            help = "The URL to display.",
            nargs=1)

    def call(self):
        """
        A very basic web browser. Shows a plain-text version of 
        a URL.\nUsage: 'GOTO <url>'
        """

        url = ''.join(self.args.url)

        if url[0:7] != 'http://' and url[0:8] != 'https://':
            url = 'http://' + url

        req = Request(url)

        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print("Failed to reach server.")
                print("Reason: ", e.reason)
            elif hasattr(e, 'code'):
                print("The server couldn't fulfill the request.")
                print("Error code: ", e.code)

            return False
        else:
            html = response.read()
            soup = BeautifulSoup(html)
            # output = soup.body.get_text()
            
            for el in soup.find_all(["h1", "h2", "h3", "p"]):
                if el.string:
                    print(el.string)
                else:
                    print()

            # print('URL: ' + response.geturl())
            # print('Meta:\n ' + str(response.info()))
            # print("\n\nContent:\n")
            # print(output)


if __name__ == "__main__":
    calc_inst = Command()
    calc_inst.call('')
