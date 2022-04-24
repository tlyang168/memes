import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def createDicts(path):
    f = open(path, 'r')
    lines = f.readlines()
    return dict([(w.strip(), w.strip()) for w in lines])

WORD_BANK = createDicts(f"{dir_path}/words.txt")
ALLOWED_WORD_BANK = createDicts(f"{dir_path}/allowed.txt")
ALLOWED_WORD_BANK.update(WORD_BANK)
