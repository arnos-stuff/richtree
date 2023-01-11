import os
import json
from extras import EMOJI_DATA

nosymbols = [
    "&", "-", "(", ")", "[", "]", "{", "}", ":", ";", "!", "?", ".", ",", "/",
    "\\", "|", "*", "+", "=", "<", ">", "@", "#", "$", "%", "^", "~", "`",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]

unicode_blacklist = [ u"\ud83c", u"\ud83d", u"\ud83e", u"\ud83f" ]

notokens = [
    "skin", "tone", "man", "woman", "girl", 'boy'
]

def rmsymb(word, symb):
    return word.replace(symb, "")

def cleanup(word):
    curr = word
    for nsymb in nosymbols:
        curr = rmsymb(curr, nsymb)
    return curr

def blacklist(word):
    word = word.lower()
    for ublack in unicode_blacklist:
        if ublack in word:
            return True
    return False

####################
### AT WORK ########
####################


data = {
    
}

for unicode in EMOJI_DATA:
    info = EMOJI_DATA[unicode]
    str_unicode = str(unicode)
    if (
        not blacklist(str_unicode)
        and info["status"] <= 2
        ):
        name = info["en"].replace(":","")
        if not any(ntk in name for ntk in notokens):
            name = cleanup(name).lower().split('_')
            if isinstance(name, list):
                name = "".join(w[:3] for w in name)
                data[name] = unicode
            else:
                data[name] = unicode

outfile = "symbols-extras.json"
os.remove(outfile) if os.path.isfile(outfile) else None
json.dump(data,open(outfile, "w+"))
