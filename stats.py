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