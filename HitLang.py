file = 'HitLang/meinFurrer.py'

def Hiel(zig=[]):
    print(zig)

heterosexual = int
underwear = str
theTypeThatDoesNotMatchToWomen = bool

class HeilError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class NationalError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        
def authorise():
    nationality = input()
    secondName = input()
    politicVision = input()

    if 'jew' in nationality.lower():
        raise NationalError("Sie sind ein Jude und werden daher in eine Gaskammer gebracht")
# every HitLang program shold begin with meinFurrer function
def HeilFurer():
    Hiel('zig Hiel!')
    return 0

# the main STATEMENTS
trash = 0
wo_men = trash

# cumpilation

def execute():
    f = open(file)
    lines = f.readlines()
    lcopy = []

    
    for line in lines:
        if '#' in line:
            line = line[:line.index('#')]
        lcopy.append(line)
        # print(line)

    # print(lcopy)
    if not any('HeilFurer()' in line for line in lcopy):
        raise HeilError("U'll get bullet in ur head.")
    compile(file,filename=file.split('/')[-1],mode='eval')

execute()