#-------------------------------------------------------------------------------
# Name:        json2dict
# Purpose:     map a JSON string to a dictionary
#
# Author:      anand
#
# Created:     07/10/2016
# Copyright:   (c) anand 2016
# Licence:     None
#-------------------------------------------------------------------------------
import string

result = {}

def json2dict(string):
    # replace { } ' and split into list
    string = string.replace("{","").replace("}","").replace("'","").split(",")

    # split string by separator & store value into key-ith index of dict
    for i in string:
        k, v = i.split(":")
        result[k] = v

    return result

def main():
    x = json2dict("{'totalCount':'1','ID':'1029','IP':'10.0.0.1'}")
    print(x)


if __name__ == '__main__':
    main()