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

def draw(ag, f1,f2,f3, process):
    arrowAg = ' ' #active: ►
    arrowF1 = ' ' #active: ▼
    arrowF2 = ' ' #active: ◄
    arrowF3 = ' ' #active: ▲
    if(ag.status == 1):
        arrowAg = '►'
    if(f1.status == 1):
        arrowF1 = '▼'
    if(f2.status == 1):
        arrowF2 = '◄'
    if(f3.status == 1):
        arrowF3 = '▲'
    print("Process:",process)
    print("             ╔═══════════╦═════════════╦═════════════╦══════════════╗")
    print("             ║   AGENTE  ║  Fumador_T  ║  Fumador_P  ║  Fumador_C   ║")
    print("             ╠═══════════╬═════════════╬═════════════╬══════════════╣")
    print("             ║     {}     ║      {}      ║      {}      ║      {}       ║".format(ag.status,f1.status,f2.status,f3.status))
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

class Fumador:
    status = 0
    ingrediente = "        "

    def __init__(self, ingrediente):
        self.status = 0
        self.ingrediente = ingrediente
        
    async def validarIngredientes(self, ingrediente1, ingrediente2):
        if (self.ingrediente == " TABACO "):
            if (ingrediente1 == " PAPEL  " or ingrediente1 == "CERILLOS") and (ingrediente2 == " PAPEL  " or ingrediente2 == "CERILLOS"):
                return True
        if (self.ingrediente == " PAPEL  ") and(ingrediente1 == "CERILLOS" or ingrediente1 == " TABACO ") and (ingrediente2 == "CERILLOS" or ingrediente2 == " TABACO "):
            return True
        if (self.ingrediente == "CERILLOS") and(ingrediente1 == " PAPEL  " or ingrediente1 == " TABACO ") and (ingrediente2 == " PAPEL  " or ingrediente2 == " TABACO "):
            return True
        return False
    
    async def fumando(self):
        await asyncio.sleep(4)

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
    fumador1 = Fumador(' TABACO ')
    fumador2 = Fumador(' PAPEL  ')
    fumador3 = Fumador('CERILLOS')
    nExec = 5

    for n in range(nExec):
        ag.status = 1
        fumador1.status = 0
        fumador2.status = 0
        fumador3.status = 0
        ag.ing1 = "        "
        ag.ing2 = "        "
        clear()
        draw(ag, fumador1, fumador2, fumador3, "Agente esta generando ingredientes")
        await ag.generateIngs()
        clear()
        draw(ag, fumador1, fumador2, fumador3, "Agente Coloco los ingredientes en la mesa")
        await asyncio.sleep(2)
        ag.status = 0
        fumador1.status = 1
        clear()
        draw(ag, fumador1, fumador2, fumador3, "Fumador 1 Verificando los ingredientes")
        await asyncio.sleep(2)
        if await fumador1.validarIngredientes(ag.ing1, ag.ing2):
            clear()
            draw(ag, fumador1, fumador2, fumador3, "Fumador 1 Fumando")
            await fumador1.fumando()
            continue
        await asyncio.sleep(2)
        fumador1.status = 0
        fumador2.status = 1
        clear()
        draw(ag, fumador1, fumador2, fumador3, "Fumador 2 Verificando los ingredientes")
        await asyncio.sleep(2)
        if await fumador2.validarIngredientes(ag.ing1, ag.ing2):
            clear()
            draw(ag, fumador1, fumador2, fumador3, "Fumador 2 Fumando")
            await fumador2.fumando()
            continue
        await asyncio.sleep(2)
        fumador2.status = 0
        fumador3.status = 1
        clear()
        draw(ag, fumador1, fumador2, fumador3, "Fumador 3 Verificando los ingredientes")
        await asyncio.sleep(2)
        if await fumador3.validarIngredientes(ag.ing1, ag.ing2):
            clear()
            draw(ag, fumador1, fumador2, fumador3, "Fumador 3 Fumando")
            await fumador3.fumando()
            continue

if __name__ == "__main__":
    asyncio.run(runAlgorithm())