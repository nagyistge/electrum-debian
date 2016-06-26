
from mnemonic import Mnemonic
from old_mnemonic import words as old_wordlist

words1 = set(Mnemonic('en').wordlist)
words2 = set(old_wordlist)
words = words1.union(words2)
for w in sorted(words):
    p = '*' if (w in words2 and not w in words1) else ''
    print p+w
