from os import system, name
import random
import asyncio

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def draw(ag, process):
    arrowAg = ' ' #active: ►
    arrowF1 = ' ' #active: ▼
    arrowF2 = ' ' #active: ◄
    arrowF3 = ' ' #active: ▲
    if(ag.status == 1):
        arrowAg = '►'

    print("Process:",process)
    print("             ╔═══════════╦═════════════╦═════════════╦══════════════╗")
    print("             ║   AGENTE  ║  Fumador_T  ║  Fumador_P  ║  Fumador_C   ║")
    print("             ╠═══════════╬═════════════╬═════════════╬══════════════╣")
    print("             ║     {}     ║      {}      ║      {}      ║      {}       ║".format(ag.status,0,0,0))
    print("             ╚═══════════╩═════════════╩═════════════╩══════════════╝")
    print("           Fumador_T      ")
    print("              ___  ")
    print("             |•.•| ")
    print("             /[I]\ ")
    print("             _| \_ ")
    print("               {}   ".format(arrowF1))
    print("AGENTE   ┏━━━━━━━━━━━━┓   Fumador_P")
    print(" ___     ┃            ┃      ___")
    print("|•.•|    ┃  {}  ┃     |•.•|".format(ag.getIng1()))
    print("/[I]\  {} ┃  {}  ┃  {}  /[I]\ ".format(arrowAg,ag.getIng2(), arrowF2))
    print("_| \_    ┃            ┃     _| \_")
    print("         ┗━━━━━━━━━━━━┛")
    print("               {}    ".format(arrowF3))
    print("            Fumador_C      ")
    print("               ___  ")
    print("              |•.•|")
    print("              /[I]\ ")
    print("              _| \_ ")
    print("                   ")



class agente:
    status=0
    allIngs = [" TABACO ", " PAPEL  ", "CERILLOS"]
    ing1="        "
    ing2="        "

    async def generateIngs(self):
        await asyncio.sleep(1)
        self.ing1 = self.allIngs[random.randint(0,2)]
        await asyncio.sleep(1)
        self.ing2 = self.allIngs[random.randint(0,2)]
        while self.ing1 == self.ing2:
            self.ing2 = self.allIngs[random.randint(0,2)]
    def getIng1(self):
        return self.ing1

    def getIng2(self):
        return self.ing2

async def runAlgorithm():
    ag = agente()
    ag2 = agente()
    nExec = 5

def verificar ingredientes(ing1,ing2,self)
if (ing1=CERILLOS or ing2=PAPEL)
if(ing1=PAPEL or ing2=CERILLOS)
self.fumando()
return true:
def fumando()


def run()
Fumador_T=fumadores(TABACO)
ag.generateIngs()
if (Fumador_T.verificaringrednientes(ag.ing1,ag.ing2))
ag.status=0
Fumador_T.status=1








    for n in range(nExec):
        ag.status = 1
        ag.ing1 = "        "
        ag.ing2 = "        "
        clear()
        draw(ag, "Agente esta generando ingredientes")
        await ag.generateIngs()
        clear()
        draw(ag, "Agente Coloco los ingredientes en la mesa")
        await asyncio.sleep(2)
        if
        if
        if


if __name__ == "__main__":
    asyncio.run(runAlgorithm())