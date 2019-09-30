#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Jamdict demo application

Latest version can be found at https://github.com/neocl/jamdict

This package uses the [EDICT][1] and [KANJIDIC][2] dictionary files.
These files are the property of the [Electronic Dictionary Research and Development Group][3], and are used in conformance with the Group's [licence][4].

[1]: http://www.csse.monash.edu.au/~jwb/edict.html
[2]: http://www.csse.monash.edu.au/~jwb/kanjidic.html
[3]: http://www.edrdg.org/
[4]: http://www.edrdg.org/edrdg/licence.html

References:
    JMDict website:
        http://www.csse.monash.edu.au/~jwb/edict.html
    Python documentation:
        https://docs.python.org/
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
@license: MIT
'''

# Copyright (c) 2016, Le Tuan Anh <tuananh.ke@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

########################################################################

import os
from jamdict import Jamdict

########################################################################

# Create an instance of Jamdict
jam = Jamdict()
print("Jamdict DB file: {}".format(jam.db_file))

# Lookup by kana
result = jam.lookup('おかえし')
for entry in result.entries:
    print(entry)
print("-----------------")

# Lookup by kanji
result = jam.lookup('御土産')
for entry in result.entries:
    print(entry)
print("-----------------")


# lookup entry by idseq
otenki = jam.lookup('id#1002470').entries[0]
kana_forms = ' '.join([x.text for x in otenki.kana_forms])
kanji_forms = ' '.join([x.text for x in otenki.kanji_forms])
print("Entry #{id}: Kanji: {kj} - Kana: {kn}".format(id=otenki.idseq, kj=kanji_forms, kn=kana_forms))
print("---------------------")
for idx, sense in enumerate(otenki):
    print("{i}. {s}".format(i=idx, s=sense))
