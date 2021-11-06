"""Classes for sanakirja API

"""
import requests


class Sana():
    """Class for a dictonary entry.

    This is a class for a record structure for the sanakirja dictionary.

    Attributes:
        exp (string): the word
        desc (string): the description of the word

    """

    def __init__(self, rec):
        """Constructor.

        Args:
            rec(dictionary): string in json format

        """
        self.exp = rec['expression']
        self.desc = rec['description']

    def dump(self):
        """Print formatted record.
        """
        print(f"[{self.exp}] means [{self.desc}]")


class SanaKirja():
    """Class for sanakirja dictonary.

    This is a class for the sanakirja dictionary.

    Attributes:
        url (string): the server url

    """

    def __init__(self, url=None):
        """Constructor.

        Args:
            lst(string): server url
        """
        if url:
            self.url = url
        else:
            self.url = "http://localhost:5000"

    def rand(self):
        """Obtain a random entry.
        """
        r = requests.get(self.url + "/rand")
        return r.json()

    def nrand(self, n):
        """Obtain n random entry.
        """
        r = requests.get(f"{self.url}/nrand/{n}")
        return r.json()

    def dump(self, lst):
        """Print formatted list of records.

        Args:
            lst(list): list of Sana objects
        """
        for item in lst:
            item.dump()
