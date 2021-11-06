import requests


class Sana():
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
    def __init__(self, url):
        """Constructor.

        Args:
            lst(string): server url
        """
        self.url = url

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
