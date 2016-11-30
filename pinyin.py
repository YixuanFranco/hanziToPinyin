#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
import os.path
import json
import sys
import csv


"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path
import json
import sys

class PinYin(object):
    def __init__(self, dict_file='word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                try:
                    line = f_line.split('    ')
                    self.word_dict[line[0]] = line[1]
                except:
                    line = f_line.split('   ')
                    self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string=""):
        result = []
        if not isinstance(string, unicode):
            string = string.decode("utf-8")
        
        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())

        return result


    def hanzi2pinyin_split(self, string="", split=""):
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)





if __name__ == "__main__":
    test = PinYin()
    test.load_word()


# 读取 try.json 文件, 然后把所有的 key 批量转成拼音
    with open('data.json', 'r') as f:
        data = json.load(f)
    with open('comma.csv', 'wb') as f:
        for key, value in data.items():
            writer = csv.writer(f)  
            someiterable = "%s" % test.hanzi2pinyin_split(string=key, split=" ")            
            writer.writerow(someiterable)


f = open('comma.csv','r')
filedata = f.read()
f.close()

newdata = filedata.replace(",","")

f = open('finalPinyin.csv','w')
f.write(newdata)
f.close()
                 



