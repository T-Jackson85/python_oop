"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds random words from dictionary."""
    
    def __init__(self, path):
        """ Reads dictionary and reports the number of items being read"""
        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """ Parses dict_file into list of words"""

        return [w.strip() for w in dict_file]
   
    def random(self):
        """ Returns random words"""

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
        """ Specialized word finder that excludes blank lines"""

        def parse(self, dict_file):

            return [w.strip() for w in dict_file
                    if w.strip and not w.starts("#")]

