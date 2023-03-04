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
    if(ag.estatus == 1):
        arrowAg = '►'
    print("Process:",process)
    print("             ╔═══════════╦═════════════╦═════════════╦══════════════╗")
    print("             ║   AGENTE  ║  Fumador_T  ║  Fumador_P  ║  Fumador_C   ║")
    print("             ╠═══════════╬═════════════╬═════════════╬══════════════╣")
    print("             ║     {}     ║      {}      ║      {}      ║      {}       ║".format(ag.estatus,0,0,0))
    print("             ╚═══════════╩═════════════╩═════════════╩══════════════╝")
    print("            Fumador_T      ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("AGENTE   ┏━━━━━━━━━━━━┓   Fumador_P")
    print(" ___     ┃            ┃")
    print("|•.•|    ┃  {}  ┃".format(ag.getIng1()))
    print("/[I]\  {} ┃  {}  ┃".format(arrowAg,ag.getIng2()))
    print("_| \_    ┃            ┃")
    print("         ┗━━━━━━━━━━━━┛")
    print("            Fumador_C      ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")
    print("                   ")

class agente:
    estatus=0
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
    nExec = 5
    for n in range(nExec):
        ag.estatus = 1
        ag.ing1 = "        "
        ag.ing2 = "        "
        clear()
        draw(ag, "Agente esta generando ingredientes")
        await ag.generateIngs()
        clear()
        draw(ag, "Agente Coloco los ingredientes en la mesa")
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(runAlgorithm())