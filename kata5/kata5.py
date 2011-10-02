#!/usr/bin/env python2
# -*- encoding: utf-8 -*-


"""Implementation a spell checker using a bloom filter

Bloom filters are very simple. Take a big array of bits, initially all
zero. Then take the things you want to look up (in our case we’ll use
a dictionary of words). Produce n independent hash values for each
word. Each hash is a number which is used to set the corresponding bit
in the array of bits. Sometimes there’ll be clashes, where the bit
will already be set from some other word. This doesn’t matter.

"""

DICT = "words"

from array import array

# create an hash for each word in the dictionary

class SpellChecker(object):
    def populate(self):
        pass

    def check(self, word):
        pass

    def spell_test(self, words):
        """Take an iterable of words and return a list containing the
        words which are not in the dictionary
        """
        not_found = [w for w in words if not self.check(w)]
        return not_found


class NaiveChecker(SpellChecker):

    def __init__(self):
        self.words = None
        super(NaiveChecker, self).__init__()

    def populate(self):
        # one liner to read everything
        self.words = set(x.strip() for x in open(DICT).readlines())

    def check(self, word):
        return word in self.words


class BloomChecker(SpellChecker):
    hash_dim = 32

    def __init__(self):
        self.hash = (2 ** self.hash_dim) - 1
        super(BloomChecker, self).__init__()

    def _hash_word(self, word):
        pass
    
    def populate(self):
        pass

    def check(self, word):
        # compute the check and check if all the bits are there
        pass

# add some ways to compute the speed of the different approaches and
# the memory consumption