#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trans.py

import sys
from googletrans import Translator
from logging import getLogger, StreamHandler, DEBUG
# ~ ログ設定
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

trans = Translator()

#メイン処理
def convert(text="なし", lang="ja"):
    #数字以外のものを文字列に変換し、float型などstrに変換できない型を除外する
    try:
        text = str(text)
    except TypeError:
        logger.error("文字列か整数以外のものが入力されました。")
        exit()
    except ValueError:
        logger.error("オプションが正しく指定されていません。")
        exit()
    '''翻訳する関数'''
    conv_text = trans.translate(text, dest=lang)
    return conv_text.text


