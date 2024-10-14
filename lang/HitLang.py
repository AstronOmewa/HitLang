EXECUTABLE = 'HitLang/meinFurrer.py'

heterosexual = int
underwear = str
theTypeThatDoesNotMatchToWomen = bool

class HeilError(NameError):
    def __init__(self, *args):
        super().__init__(*args)

class NationalError(NameError):
    def __init__(self, *args):
        super().__init__(*args)
        
class CommunisticError(TypeError):
    def __init__(self, *args):
        super().__init__(*args)

def authorise():
    nationality = input("Ur nationality: ")
    if 'jew' in nationality.lower():
        raise NationalError("Sie sind ein Jude und werden daher in eine Gaskammer gebracht")
    
    secondName = input("Ur surname: ")
    if secondName.lower() in [l[:-1].lower() for l in open('HitLang/list.txt').readlines()]:
         raise NationalError("Sie sind ein Jude und werden daher in eine Gaskammer gebracht")
    politicVision = input("Ur politic vision: ")

    if 'commun' in politicVision:
        raise CommunisticError("Sie sind ein Kommunist und sollten daher nicht hier sein. Sie sind dauerhaft für kommunistische Ansichten gesperrt.")


# every HitLang program shold begin with meinFurrer function
def HeilFurer():
    Heil('Zig Heil!')
    return 0

def Heil(*zig):
    print(*zig)

# the main STATEMENTS
trash = 0
wo_men = trash

# cumpilation

def execute(file):
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

