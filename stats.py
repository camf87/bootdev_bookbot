def get_num_words(text):
    return len(text.split())

def count_char(text):
    dict = {}
    for c in text.lower():
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1
    return dict

def sort_on(items, key):
    return items[key]

def sort_dict(dictionary):
    dict_sorted = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    res = []
    for k,v in dict_sorted:
        res.append({"char": k, "num": v})
    return res
