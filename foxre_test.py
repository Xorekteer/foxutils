import unittest
import foxre

class TestSplitSentences(unittest.TestCase):
    def setUp(self):
        self.ex1 = "This is an example sentence. There are many like it but this is mine. I love my example sentence."
        self.ex2 = "Okay I've been thinking... When life gives you lemons, don't make lemonade! Make life take the lemons back!"
        self.ex3 = "Stop yelling!!! I'm here already... What?! Why?!"
        self.ex4 = ">!>?>@!>@?!#@#?>!@#?>@<$?!<#@?>#!#agwudiahq2klad@2 p 93uw rq3wq2; iq2q"  

    def test_split(self):
        self.assertEqual(
            foxre.split_sentences(self.ex1),
                [
                "This is an example sentence.",
                "There are many like it but this is mine.",
                "I love my example sentence."
                ]
            )
        self.assertEqual(
            foxre.split_sentences(self.ex2),
                [
                "Okay I've been thinking...",
                "When life gives you lemons, don't make lemonade!",
                "Make life take the lemons back!"
                ]
            )
        self.assertEqual(
            foxre.split_sentences(self.ex3),
                [
                "Stop yelling!!!",
                "I'm here already...",
                "What?!",
                "Why?!"
                ]
            )
        self.assertEqual(
            foxre.split_sentences(self.ex4),
                [
                ">!>?>@!>@?!#@#?>!@#?>@<$?!<#@?>#!#agwudiahq2klad@2 p 93uw rq3wq2; iq2q"
                ]
            )
        # Empty is empty
        self.assertEqual(
            foxre.split_sentences(""), 
                [""]
            )

class TestReword(unittest.TestCase):
    def test_reword(self):
        #empty string
        self.assertEqual(
            foxre.reword(r"" , "Take me home."),
                [
                "Take",
                "me",
                "home."
                ]
            )
        self.assertEqual(
            foxre.reword(r"a" ,"I am become death, destroyer of worlds."),
                [
                "am",
                "death,"
                ]
            )
        self.assertEqual(
            foxre.reword(r"\d+", "27th May, 8th avenue, 452, NYC"),
                [
                "27th",
                "8th",
                "452,"
                ]
            )

class TestRelist(unittest.TestCase):
    def setUp(self):
        self.ex1 = [
            "The",
            "quick",
            "brown",
            "python",
            "slid",
            "under",
            "the",
            "jumpy",
            "fox."
        ]

    def test_relist(self):
        self.assertEqual(
            foxre.relist(r"py", self.ex1),
            ["python", "jumpy"]
        )
        self.assertEqual(
            foxre.relist(r"(T|t)he", self.ex1),
            ["The", "the"]
        )
        # Empty is all
        self.assertEqual(
            foxre.relist(r"", self.ex1),
            self.ex1
        )

if __name__ == "__main__":
    unittest.main()
