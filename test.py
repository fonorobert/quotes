import unittest
from randquote import randquote


class Test(unittest.TestCase):

    def setUp(self):
        self.quotes = {"0": {"c": 11, "f": 23}}

    def test_listing(self):
        #self.assertEqual(self.quotes, randquote("quotes.json"))
        #self.assertEqual(randquote("quotes.json") in (0, 1, 2), True)
        #self.assertCountEqual(randquote("quotes.json"), [{"John Dorian": "I can't do this all on my own."}, {"Szokratesz": "Keverni érdemes."}])
        self.assertEqual(randquote("quotes.json") in [{"John Dorian": "I can't do this all on my own."}, {"Szokratesz": "Keverni érdemes."}], True)

if __name__ == '__main__':
    unittest.main()
