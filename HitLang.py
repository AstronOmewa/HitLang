def Hiel(zig=[]):
    print(zig)

heterosexual = int
underwear = str
theTypeThatDoesNotMatchToWomen = bool

# every HitLang program shold begin with meinFurrer function
def meinFurrer():
    Hiel('zig Hiel!')
    return 0

# the main STATEMENTS
trash = 0
wo_men = trash

# cumpilation

def execute():
    file = 'HitLang/meinFurrer.py'
    f = open(file)
    lines = f.readlines()
    lcopy = []

    
    for line in lines:
        if '#' in line:
            line = line[:line.index('#')]
        lcopy.append(line)
        # print(line)

    # print(lcopy)
    if not any('meinFurrer()' in line for line in lcopy):
        raise HielError("Hitler will kill you.")
    compile(file,filename=file.split('/')[-1],mode='eval')

execute()