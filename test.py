#!/usr/bin/env python

# A simple script that connects to a server and displays block headers

import time, electrum

print electrum.mnemonic.mn_encode("4f73f3f710030baed39cf7d1")
print electrum.mnemonic.mn_encode("4f73f3f710030baed39cf7d15")

print "on creation"
print electrum.mnemonic.mn_decode("soar afternoon child funny been behind any smile freeze voice coffee bee".split())

print "after encryption"
print "4f73f3f710030baed39cf7d15"

#-> the original seed was not well written.
