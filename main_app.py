#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_app.py
import trans as tr

opt = None
text = None

try:
    opt = sys.argv[1]
    text = " ".join(sys.argv[2:])
except:
    logger.critical('書式が正しくない可能性があります。')
    exit()
opt = opt.strip("-")
print(tr.convert(text=text, lang=opt))
