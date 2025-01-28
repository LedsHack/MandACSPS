def func(get, ret=""):
    if(len(get) == len(ret)):
        return ret
    else:
        ret += get[len(get) - len(ret) - 1]
        return(func(get, ret))
print(func(input("Слово: ")))