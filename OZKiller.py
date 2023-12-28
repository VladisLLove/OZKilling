from random import randint
def create_Table(DiagramSplitSymbol, DiagramDivideSymbol, DiagramSpaceSymbol, PrintSymbolLine, PrintSymbolCell, MaxSymbol, DiagramSetting):
    if type(DiagramSetting) is type([]):
        Table = DiagramSetting
    else:
        Table = DiagramSetting.split(DiagramSplitSymbol)
        for y in range(len(Table)):
            if Table[0] == '':
                Table.remove('')
            elif Table[0].find(DiagramDivideSymbol) >= 0:
                Table.append((Table[0].replace(DiagramDivideSymbol, '')).strip())
                Table.pop(0)
                Table.append(DiagramDivideSymbol)
            else:
                Table.append(Table[0].strip())
                Table.pop(0)

    a = {'key': 0}
    i = 0
    for x in range(len(Table)):
        if Table[x].find('\x1b') >= 0:
            a['key'] = Table[x]
            c = a['key'][5:]
        else:
            a['key'] = Table[x]
            c = a['key']

        if MaxSymbol > 0:
            if len(c) % 2 == 0:
                sint = ((MaxSymbol - len(c)) // 2) + 1
                eint = sint
            else:
                sint = round((MaxSymbol - len(c)) // 2)
                eint = sint + 1
            s = ' ' * sint
            e = ' ' * eint
        else:
            s = ''
            e = ''

        if PrintSymbolCell == '':
            print('', end='')
        else:
            print(f'\033[39m{PrintSymbolCell}', end='')

        if Table[x][0] == DiagramDivideSymbol:
            if PrintSymbolLine != '':
                print('')
                for y in range(i):
                    print(f'\033[39m{PrintSymbolLine}', end='')
                print('')
            else:
                print('')
            i = 0
        elif Table[x][0] == DiagramSpaceSymbol:
            SpaceString = int(a['key'].replace(DiagramSpaceSymbol, ''))
            print(' ' * SpaceString, end='')
            i += 1
        else:
            print(f'{s}{a['key']}{e}', end='')
            i += 1

def DiagramSettings(Length, Width):
    DiagramSetting = ''
    for x in range(1, (Length * Width) + 1):
        DiagramSetting += f'l[ {P[x]} ]'
        if x % Width == 0:
            DiagramSetting += '|'
    return DiagramSetting
def Pool():
    create_Table('l', '|', '', '', '', 0, f'\033[37m{DiagramSettings(LengthPool, WidthPool)}')

# GAME SETTINGS
Turn = 0
TurnChecker = 0
SomebodyKillingChecker = 0
PositionChestChecker = 0
PositionEnemyChecker = 0
SpeedBoostChecker = 0
WhoChestSpawn = 0
KillerChecker = 0
GoodGame = 0
JustSpawn = 0
EnemyOnPool = 1
ChestOnPool = 1
PoolCells = 1
Killer = '\033[31mKiller\033[37m'
SpeedBoost = '\033[34mSpeedBoost\033[37m'
Hero = '\033[32mO\033[37m'
Enemy = '\033[31mX\033[37m'
Chest = '\033[33mC\033[37m'

# GAME RULES
Answer = input()
if Answer[0: 7].lower() == 'setting':
    WidthPool = int(input('Enter width Pool: '))
    LengthPool = int(input('Enter length Pool: '))
    MaxEnemy = int(input('Enter max enemy on Pool: '))
    MaxChest = int(input('Enter max chest on Pool: '))
    TurnSpawnEnemy = 3
    TurnSpawnChest = 3
    ChanceKilling = '1/2'
    if Answer.lower() == 'setting+':
        TurnSpawnEnemy = int(input('Enter turn when enemies will appear: '))
        TurnSpawnChest = int(input('Enter turn when chest will appear: '))
        ChanceKilling = input('Enter the probability (for example \'1/3\') of a die next to an enemy: ')
else:
    WidthPool = 5
    LengthPool = 5
    MaxEnemy = 5
    MaxChest = 1
    TurnSpawnEnemy = 3
    TurnSpawnChest = 3
    ChanceKilling = '1/2'

# GAME SETTING
LiveEnemy = MaxEnemy
Inventory = {0: 0, 1: 0, 2: 0}
ChestPosition = {x: 0 for x in range(1, MaxChest + 1)}
EnemyPosition = {x: 0 for x in range(1, MaxEnemy + 1)}
P = {x: ' ' for x in range(1, (WidthPool * LengthPool) + 1)}

ChanceKilling = ChanceKilling.split('/')
ChanceKilling1 = int(ChanceKilling[0])
ChanceKilling2 = int(ChanceKilling[1])

# START GAME
Answer = int(input())
GamePosition = Answer
P[GamePosition] = Hero
Pool()


while True:
    # GAME CHECKER
    if GamePosition < 1 or GamePosition > (LengthPool * WidthPool) or GoodGame == 1:
        P[GamePosition] = Enemy
        Pool()
        print(f'\033[31mYou Lose(\n\033[39mAll turn: \033[35m{Turn + 1}')
        break
    if LiveEnemy == 0:
        print(f'\033[34mYou Win!\n\033[39mAll turn: \033[35m{Turn + 1}')
        break

    # PLAYER MOVE
    Move = input()
    if Move == '':
        Move = 'MMMM'
    if Move[0] == 'w':
        if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
            Inventory[1] = 0
            P[GamePosition] = ' '
            GamePosition -= WidthPool
        P[GamePosition] = ' '
        GamePosition -= WidthPool
        P[GamePosition] = Hero
        Turn += 1
        TurnChecker = 0
    elif Move[0] == 'a':
        if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
            Inventory[1] = 0
            P[GamePosition] = ' '
            GamePosition -= 1
        P[GamePosition] = ' '
        GamePosition -= 1
        P[GamePosition] = Hero
        Turn += 1
        TurnChecker = 0
    elif Move[0] == 'd':
        if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
            Inventory[1] = 0
            P[GamePosition] = ' '
            GamePosition += 1
        P[GamePosition] = ' '
        GamePosition += 1
        P[GamePosition] = Hero
        Turn += 1
        TurnChecker = 0
    elif Move[0] == 's':
        if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
            Inventory[1] = 0
            P[GamePosition] = ' '
            GamePosition += WidthPool
        P[GamePosition] = ' '
        GamePosition += WidthPool
        P[GamePosition] = Hero
        Turn += 1
        TurnChecker = 0
    # GIVE LOOT
    elif Move == 'open' and Inventory[0] == 1:
        Inventory[0] = 0
        Random = randint(1, 7)
        if 1 <= Random <= 4:
            if Inventory[1] == SpeedBoost:
                Inventory[2] = Killer
            else:
                Inventory[1] = SpeedBoost
        elif 5 <= Random <= 7:
            if Inventory[2] == Killer:
                Inventory[1] = SpeedBoost
            else:
                Inventory[2] = Killer

        # RULE CHECKER
        if Inventory[1] == SpeedBoost and SpeedBoostChecker == 0:
            print(f'\nWow! You get a \'{SpeedBoost}\'. Print for example \'wS\' to go 2 cells up')
            SpeedBoostChecker = 1
        elif Inventory[2] == Killer and KillerChecker == 0:
            print(f'\nWow! You get a \'{Killer}\'. Print for example \'aK\' to go 1 cells left and killing enemy')
            KillerChecker = 1
        Turn += 1
        TurnChecker = 0
    else:
        Turn = TurnChecker

    # KILLING ENEMY
    if Move[len(Move) - 1] == 'K' and Inventory[2] == Killer and len(str(Move)) >= 2:
        for v in range(1, MaxEnemy + 1):
            if GamePosition == EnemyPosition[v]:
                Inventory[2] = 0
                EnemyPosition[v] = 0
                LiveEnemy -= 1
                SomebodyKillingChecker = 1
                print('\033[36mYou are killing enemy!')
                break
            else:
                SomebodyKillingChecker = 0
        if SomebodyKillingChecker == 0:
            Inventory[2] = 0
            print('\033[36mYou aren\'t killing enemy(')

    # GIVE CHEST
    for x in range(1, MaxChest + 1):
        if GamePosition == ChestPosition[x]:
            Inventory[0] = 1
            ChestPosition[x] = 0
            ChestOnPool -= 1

    # ENEMY SPAWN
    if EnemyOnPool <= MaxEnemy and Turn % TurnSpawnEnemy == 0 and Turn != TurnChecker:
        while True:
            Line = randint(1, WidthPool)
            Column = randint(1, LengthPool)
            Position = Line * Column
            for x in range(1, MaxEnemy + 1):
                if Position != EnemyPosition[x]:
                    PositionEnemyChecker = 1
                else:
                    PositionEnemyChecker = 0
                    break
            for x in range(1, MaxChest + 1):
                if Position != ChestPosition[x]:
                    PositionChestChecker = 1
                else:
                    PositionChestChecker = 0
                    break
            if PositionEnemyChecker == 1 and PositionChestChecker == 1 and Position != GamePosition and 1 <= Position <= (LengthPool * WidthPool):
                PositionEnemyChecker = 0
                PositionChestChecker = 0
                EnemyPosition[EnemyOnPool] = Position
                P[EnemyPosition[EnemyOnPool]] = Enemy
                JustSpawn = EnemyOnPool
                EnemyOnPool += 1
                break

    # CHEST SPAWN
    if Turn % TurnSpawnChest == 0 and ChestOnPool <= MaxChest and Inventory[0] == 0 and (Inventory[1] != SpeedBoost or Inventory[2] != Killer) and Turn != TurnChecker:
        Random = randint(1, 2)
        Line = randint(1, WidthPool)
        Column = randint(1, LengthPool)
        Position = Line * Column
        for x in range(1, MaxEnemy + 1):
            if Position != EnemyPosition[x]:
                PositionEnemyChecker = 1
            else:
                PositionEnemyChecker = 0
                break
        for x in range(1, MaxChest + 1):
            if Position != ChestPosition[x]:
                PositionChestChecker = 1
            else:
                PositionChestChecker = 0
                break
        for x in range(1, MaxChest + 1):
            if ChestPosition[x] == 0:
                WhoChestSpawn = x
                break
            else:
                continue
        if Random == 1 and PositionChestChecker == 1 and Position != GamePosition and PositionEnemyChecker == 1 and Position >= 1 and Position <= (LengthPool * WidthPool):
            ChestPosition[WhoChestSpawn] = Position
            P[ChestPosition[WhoChestSpawn]] = Chest
            ChestOnPool += 1
        PositionEnemyChecker = 0
        PositionChestChecker = 0

    # ENEMY MOVE
    if Turn != TurnChecker:
        for x in range(1, MaxEnemy + 1):
            RandomUltra = randint(1, ChanceKilling2)
            if EnemyPosition[x] == GamePosition:
                GoodGame = 1
                break
            elif EnemyPosition[x] != 0 and EnemyPosition[x] != '':
                for e in range(5000):
                    if JustSpawn == x:
                        JustSpawn = 0
                        break
                    EndEnemyPosition = EnemyPosition[x]
                    Random = randint(1, 4)
                    if RandomUltra <= ChanceKilling1 and (GamePosition - WidthPool == EnemyPosition[x] or GamePosition + WidthPool == EnemyPosition[x] or GamePosition - 1 == EnemyPosition[x] or GamePosition + 1 == EnemyPosition[x]):
                        GoodGame = 1
                        P[EnemyPosition[x]] = ' '
                        EnemyPosition[x] = GamePosition
                        break
                    else:
                        if Random == 4:
                            EndEnemyPosition += WidthPool
                        elif Random == 2:
                            EndEnemyPosition += 1
                        elif Random == 1:
                            EndEnemyPosition -= 1
                        elif Random == 3:
                            EndEnemyPosition -= WidthPool
                        for y in range(1, MaxEnemy + 1):
                            if EndEnemyPosition != EnemyPosition[y]:
                                PositionEnemyChecker = 1
                            else:
                                PositionEnemyChecker = 0
                                break
                        for k in range(1, MaxChest + 1):
                            if EndEnemyPosition != ChestPosition[k]:
                                PositionChestChecker = 1
                            else:
                                PositionChestChecker = 0
                                break
                        if PositionEnemyChecker == 1 and PositionChestChecker == 1 and 1 <= EndEnemyPosition <= (LengthPool * WidthPool) and EndEnemyPosition != GamePosition:
                            P[EnemyPosition[x]] = ' '
                            EnemyPosition[x] = EndEnemyPosition
                            P[EnemyPosition[x]] = Enemy
                            break
                PositionEnemyChecker = 0
                PositionChestChecker = 0

    # INVENTORY CHECKER
    if GoodGame != 1 and 1 <= GamePosition <= (WidthPool * LengthPool):
        Pool()
        if Inventory[0] == 1:
            print('You are have a chest, print \'open\' that open chest')
        if Inventory[1] != 0 and Inventory[2] != 0:
            print(f'Inventory: {Inventory[1]}, {Inventory[2]}')
        elif Inventory[1] != 0:
            print(f'Inventory: {Inventory[1]}')
        elif Inventory[2] != 0:
            print(f'Inventory: {Inventory[2]}')
        else:
            print('Your inventory is clear')
