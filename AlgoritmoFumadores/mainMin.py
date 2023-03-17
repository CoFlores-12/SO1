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

class Fumador:
    status = 0
    ingrediente = "        "

    def __init__(self, ingrediente):
        self.status = 0
        self.ingrediente = ingrediente
        
    async def validarIngredientes(self, ingrediente1, ingrediente2):
        if (self.ingrediente == "TABACO"):
            if (ingrediente1 == "PAPEL" or ingrediente1 == "CERILLOS") and (ingrediente2 == "PAPEL" or ingrediente2 == "CERILLOS"):
                return True
        if (self.ingrediente == "PAPEL") and(ingrediente1 == "CERILLOS" or ingrediente1 == "TABACO") and (ingrediente2 == "CERILLOS" or ingrediente2 == "TABACO"):
            return True
        if (self.ingrediente == "CERILLOS") and(ingrediente1 == "PAPEL" or ingrediente1 == "TABACO") and (ingrediente2 == "PAPEL" or ingrediente2 == "TABACO"):
            return True
        return False
    
    async def fumando(self):
        await asyncio.sleep(4)

class agente:
    status=0
    allIngs = ["TABACO", "PAPEL", "CERILLOS"]
    ing1=""
    ing2=""

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
    fumador1 = Fumador('TABACO')
    fumador2 = Fumador('PAPEL')
    fumador3 = Fumador('CERILLOS')
    nExec = 5
    for n in range(nExec):
        clear()
        print("Generando ingredientes...")
        await ag.generateIngs()
        print("ingredientes generados por el agente: {}, {}".format(ag.ing1, ag.ing2))
        await asyncio.sleep(2)

        print("     Fumador_T verifica los ingredientes")
        await asyncio.sleep(2)
        if await fumador1.validarIngredientes(ag.ing1, ag.ing2):
            print("         Fumador_T se pone a fumar")
            await asyncio.sleep(4)
            continue

        print("     Fumador_P verifica los ingredientes")
        await asyncio.sleep(2)
        if await fumador2.validarIngredientes(ag.ing1, ag.ing2):
            print("         Fumador_P se pone a fumar")
            await asyncio.sleep(4)
            continue

        print("     Fumador_C verifica los ingredientes")
        await asyncio.sleep(2)
        if await fumador3.validarIngredientes(ag.ing1, ag.ing2):
            print("         Fumador_C se pone a fumar")
            await asyncio.sleep(4)

if __name__ == "__main__":
    asyncio.run(runAlgorithm())