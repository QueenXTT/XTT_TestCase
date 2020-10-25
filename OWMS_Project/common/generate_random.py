# -*- Coding: UTF-8 -*-
# Author  : Queen_XTT

import random

def test_generateRandom(pre,sum,leng):
    """
    生成固定字符+随机数
    :param pre: 拼接的字符
    :param sum: 随机数
    :param leng: 设定随机数长度
    """
    randomNum = random.randint(0, sum)
    lastString = "%s%s" % (pre, str(randomNum).zfill(leng))
    return lastString

def generatorLetter(length=10):
    string = ""
    list_string = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(int(length)):
        s = random.choice(list_string)
        string = string + s
    return string

def generatorEmail():
    list_string = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list_num = ["0","1","2","3","4","5","6","7","8","9"]
    list_sign = ["@129.com","@126.com","@111.com","@333.com","@163.com","@qq.com","@xx.com"]
    requiredString = random.choice(list_string) + random.choice(list_string) + random.choice(list_string) + random.choice(list_num) + random.choice(list_num) + random.choice(list_num) + random.choice(list_sign)
    return requiredString

if __name__ == "__main__":
    print(test_generateRandom("yxy_",9999,4))
    print(generatorLetter())
    # generatorEmail()
    s="XTT_订单测试_"
    opens = "{}{}".format(s,generatorLetter())
    remark = "自动化_{}".format(generatorLetter())
    print(opens)
    print(remark)
    ss = generatorEmail()
    print(ss)