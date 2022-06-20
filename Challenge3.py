#!/usr/bin/python3
import json
import sys

def LoadInfo(obj):
    print("## LoadInfo")
    try:
        data = json.loads(obj)
        print("type: json")
        return 'josn' , data
    except:
        if isinstance(obj,dict):
            print("type: dict")
            return 'dict',obj
        else:
            print("type: na")
            return 'na', obj

def key_value_fn(data, key):
    print("## key_value_fn")
    keyArr = key.split('/')
    for i in range(0,len(keyArr)):
        value = data.get(keyArr[i])
        print(i, keyArr[i],value)
        if isinstance(value, dict):
            i += 1
            data = value
    return value

def main():
    print("## MAIN")
    argLen = len(sys.argv) - 1
    # print(argLen)
    if argLen != 2:
        print("Usage Error: No of Args Should be 2, <object> <key>")
        sys.exit()
    else:
        print("current argLen")
        #obj = {"a" : 1}
        obj = {"x": {"y": {"z":13 } } }
        #obj = sys.argv[1]
        key = sys.argv[2]
        print(obj)
        stat, data = LoadInfo(obj)
        print(stat, data)
        if stat == 'na':
            print("Input Error: Not a Json or Dict")
            sys.exit()
        value = key_value_fn(data,key)
        if value is None:
            print("No Value for the required key")
        else:
            print(value)
if __name__ == '__main__':
    main()
