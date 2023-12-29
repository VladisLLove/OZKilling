from random import randint
def create_Table(DiagramSplitSymbol, DiagramDivideSymbol, DiagramSpaceSymbol, PrintSymbolLine, PrintSymbolCell, MaxSymbol, DiagramSetting):
    Table = DiagramSetting.split(DiagramSplitSymbol)
    for y in range(len(Table)):
        if Table[0] == '':
            Table.pop(0)
        else:
            Table.append(Table[0])
            Table.pop(0)
    a = {0: 0}
    i = 0
    for x in range(len(Table)):
        if Table[x].find('\x1b') >= 0:
            a[0] = Table[x]
            c = a[0][5:]
        else:
            a[0] = Table[x]
            c = a[0]

        if MaxSymbol > 0:
            if len(c) % 2 == 0:
                s = ' ' * ((MaxSymbol - len(c)) // 2) + 1
                e = s
            else:
                s = ' ' * round((MaxSymbol - len(c)) // 2)
                e = s + ' '
        else:
            s = ''
            e = ''

        if PrintSymbolCell == '':
            print('', end='')
        else:
            print(f'{PrintSymbolCell}', end='')

        if Table[x] == DiagramDivideSymbol:
            if PrintSymbolLine != '':
                print('')
                for y in range(i):
                    print(f'{PrintSymbolLine}', end='')
                print('')
            else:
                print('')
            i = 0
        elif Table[x].find(DiagramSpaceSymbol) != -1:
            SpaceString = int(a[0].replace(DiagramSpaceSymbol, ''))
            print(' ' * SpaceString, end='')
            i += 1
        else:
            print(f'{s}{a[0]}{e}', end='')
            i += 1

def InventoryChecker(Inventory0, Inventory1, Inventory2):
    if Inventory0 == 1:
        print('You are have a chest, print \'open\' that open chest')
    if Inventory1 != 0 and Inventory2 != 0:
        print(f'Inventory: {Inventory1}, {Inventory2}')
    elif Inventory1 != 0:
        print(f'Inventory: {Inventory1}')
    elif Inventory2 != 0:
        print(f'Inventory: {Inventory2}')
    else:
        print('Your inventory is clear')
def DiagramSettings(Length, Width):
    DiagramSetting = ''
    for x in range(1, (Length * Width) + 1):
        DiagramSetting += f'l[ {P[x]} ]'
        if x % Width == 0:
            DiagramSetting += 'l|'
    return DiagramSetting
def Pool():
    create_Table('l', '|', '+', '', '', 0, DiagramSettings(LengthPool, WidthPool))

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
Easy = 'Easy'
Normal = 'Normal'
Hard = 'Hard'
Killer = 'Killer'
SpeedBoost = 'SpeedBoost'
Hero = 'O'
Enemy = 'X'
Chest = 'C'

# GAME RULES
Answer = input(f'You can print \'Setting\' (Setting+) or difficulty level ({Easy}, {Normal}, {Hard}): ')
if Answer[0: 7].lower() == 'setting':
    WidthPool = int(input('Enter width Pool: '))
    LengthPool = int(input('Enter length Pool: '))
    MaxEnemy = int(input('Enter max enemy on Pool: '))
    MaxChest = int(input('Enter max chest on Pool: '))
    ForceSpeedBoost = 1
    TurnSpawnEnemy = 3
    TurnSpawnChest = 3
    ChanceKilling = '1/2'
    if Answer.lower() == 'setting+':
        ForceSpeedBoost = int(input(f'Enter force {SpeedBoost}: '))
        TurnSpawnEnemy = int(input('Enter turn when enemies will appear: '))
        TurnSpawnChest = int(input('Enter turn when chest will appear: '))
        ChanceKilling = input('Enter the probability (for example \'1/3\') of a die next to an enemy: ')
elif Answer.lower() == 'easy':
    WidthPool = 7
    LengthPool = 7
    MaxEnemy = 5
    MaxChest = 2
    ForceSpeedBoost = 2
    TurnSpawnEnemy = 3
    TurnSpawnChest = 2
    ChanceKilling = '1/3'
elif Answer.lower() == 'normal':
    WidthPool = 5
    LengthPool = 5
    MaxEnemy = 5
    MaxChest = 1
    ForceSpeedBoost = 1
    TurnSpawnEnemy = 3
    TurnSpawnChest = 3
    ChanceKilling = '1/2'
elif Answer.lower() == 'hard':
    WidthPool = 4
    LengthPool = 4
    MaxEnemy = 5
    MaxChest = 1
    ForceSpeedBoost = 1
    TurnSpawnEnemy = 3
    TurnSpawnChest = 3
    ChanceKilling = '1/1'
else:
    WidthPool = 5
    LengthPool = 5
    MaxEnemy = 5
    MaxChest = 1
    ForceSpeedBoost = 1
    TurnSpawnEnemy = 3
    TurnSpawnChest = 3
    ChanceKilling = '1/2'

# GAME SETTING
LiveEnemy = MaxEnemy
Inventory = {0: 0, 1: 0, 2: 0}
ChestPosition = {x: 0 for x in range(1, MaxChest + 1)}
EnemyPosition = {x: 0 for x in range(1, MaxEnemy + 1)}
P = {x: '' for x in range(1, (WidthPool * LengthPool) + 1)}

AllPool = WidthPool * LengthPool
ChanceKilling = ChanceKilling.split('/')
ChanceKilling1 = int(ChanceKilling[0])
ChanceKilling2 = int(ChanceKilling[1])

# START GAME
while True:
    Answer = input(f'You can start new game (print \'1 - {AllPool}\') or load save (print \'save\'): ')
    if Answer.lower() == 'save':
        EnemyPositionSave = input('Enter enemies position (separated by commas): ').split(',')
        for x in range(1, len(EnemyPositionSave) + 1):
            EnemyPosition[x] = int(EnemyPositionSave[x - 1])
            if EnemyPosition[x] != 0 and EnemyPosition[x] != '':
                P[EnemyPosition[x]] = Enemy

        ChestPositionSave = input('Enter chests position (separated by commas): ').split(',')
        for x in range(1, len(ChestPositionSave) + 1):
            ChestPosition[x] = int(ChestPositionSave[x - 1])
            if ChestPosition[x] != 0:
                P[ChestPosition[x]] = Chest

        GamePosition = int(input('Enter hero position: '))
        P[GamePosition] = Hero

        InventorySave = input('Enter information about inventory (separated by commas): ').split(',')
        Inventory[0] = int(InventorySave[0])
        if int(InventorySave[1]) == 1:
            Inventory[1] = SpeedBoost
        if int(InventorySave[2]) == 1:
            Inventory[2] = Killer

        Turn = int(input('Enter turn in save: '))

        EnemyChecker = 0
        ChestChecker = 0
        for x in range(1, MaxEnemy + 1):
            if EnemyPosition[x] == 0:
                EnemyChecker += 1
        for x in range(1, MaxChest + 1):
            if ChestPosition[x] == 0:
                ChestChecker += 1
        EnemyOnPool = (MaxEnemy - EnemyChecker) + 1
        ChestOnPool = (MaxChest - ChestChecker) + 1
        break
    elif 1 <= int(Answer) <= AllPool:
        GamePosition = int(Answer)
        P[GamePosition] = Hero
        break
    else:
        print('Return')
Pool()
InventoryChecker(Inventory[0], Inventory[1], Inventory[2])

while True:
    # GAME CHECKER
    if GamePosition < 1 or GamePosition > AllPool or GoodGame == 1:
        P[GamePosition] = Enemy
        Pool()
        print(f'You Lose(\nAll turn: {Turn + 1}')
        break
    if LiveEnemy == 0:
        print(f'You Win!\nAll turn: {Turn + 1}')
        break

    # PLAYER MOVE
    while True:
        Move = input()
        if Move == '':
            Move = 'MMMM'
        if Move[0] == 'w' and len(Move) <= 2:
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition] = ' '
                GamePosition -= (WidthPool * ForceSpeedBoost)
            P[GamePosition] = ' '
            GamePosition -= WidthPool
            P[GamePosition] = Hero
            Turn += 1
            TurnChecker = 0
            break
        elif Move[0] == 'a' and len(Move) <= 2:
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition] = ' '
                GamePosition -= (1 * ForceSpeedBoost)
            P[GamePosition] = ' '
            GamePosition -= 1
            P[GamePosition] = Hero
            Turn += 1
            TurnChecker = 0
            break
        elif Move[0] == 'd' and len(Move) <= 2:
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition] = ' '
                GamePosition += (1 * ForceSpeedBoost)
            P[GamePosition] = ' '
            GamePosition += 1
            P[GamePosition] = Hero
            Turn += 1
            TurnChecker = 0
            break
        elif Move[0] == 's' and len(Move) <= 2:
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition] = ' '
                GamePosition += (WidthPool * ForceSpeedBoost)
            P[GamePosition] = ' '
            GamePosition += WidthPool
            P[GamePosition] = Hero
            Turn += 1
            TurnChecker = 0
            break
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
            break
        elif Move.lower()[0: 4] == 'stat':
            print('Enemies position: ', end='')
            for x in range(1, MaxEnemy + 1):
                if x < MaxEnemy:
                    print(f'{EnemyPosition[x]}, ', end='')
                else:
                    print(f'{EnemyPosition[x]}', end='')
            print('')

            print('Chests position: ', end='')
            for x in range(1, MaxChest + 1):
                if x < MaxChest:
                    print(f'{ChestPosition[x]}, ', end='')
                else:
                    print(f'{ChestPosition[x]}', end='')
            print('')

            print(f'Hero position: {GamePosition}')

            print('Inventory: ', end='')
            if Inventory[0] == 1:
                print('1, ', end='')
            else:
                print('0, ', end='')
            if Inventory[1] == SpeedBoost:
                print('1, ', end='')
            else:
                print('0, ', end='')
            if Inventory[2] == Killer:
                print('1', end='')
            else:
                print('0', end='')
            print('')
            print(f'Turn: {Turn}')
            if Move.lower() == 'stat+':
                print(f'SomebodyKillingChecker: {SomebodyKillingChecker}')
                print(f'PositionChestChecker: {PositionChestChecker}')
                print(f'PositionEnemyChecker: {PositionEnemyChecker}')
                print(f'SpeedBoostChecker: {SpeedBoostChecker}')
                print(f'KillerChecker: {KillerChecker}')
                print(f'WhoChestSpawn: {WhoChestSpawn}')
                print(f'TurnChecker: {TurnChecker}')
                print(f'JustSpawn: {JustSpawn}')
                print(f'GoodGame: {GoodGame}')
        else:
            TurnChecker = Turn
            break

    # KILLING ENEMY
    if Move[len(Move) - 1] == 'K' and Inventory[2] == Killer and len(str(Move)) >= 2 and Turn != TurnChecker:
        for v in range(1, MaxEnemy + 1):
            if GamePosition == EnemyPosition[v]:
                Inventory[2] = 0
                EnemyPosition[v] = 0
                LiveEnemy -= 1
                SomebodyKillingChecker = 1
                print('You are killing enemy!')
                break
            else:
                SomebodyKillingChecker = 0
        if SomebodyKillingChecker == 0:
            Inventory[2] = 0
            print('You aren\'t killing enemy(')

    # GIVE CHEST
    if Turn != TurnChecker:
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
            if PositionEnemyChecker == 1:
                for x in range(1, MaxChest + 1):
                    if Position != ChestPosition[x]:
                        PositionChestChecker = 1
                    else:
                        PositionChestChecker = 0
                        break
            if PositionChestChecker == 1 and PositionEnemyChecker == 1 and Position != GamePosition and 1 <= Position <= AllPool:
                EnemyPosition[EnemyOnPool] = Position
                P[EnemyPosition[EnemyOnPool]] = Enemy
                JustSpawn = EnemyOnPool
                EnemyOnPool += 1
                PositionEnemyChecker = 0
                PositionChestChecker = 0
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
        if PositionEnemyChecker == 1:
            for x in range(1, MaxChest + 1):
                if Position != ChestPosition[x]:
                    PositionChestChecker = 1
                else:
                    PositionChestChecker = 0
                    break
        if PositionChestChecker == 1:
            for x in range(1, MaxChest + 1):
                if ChestPosition[x] == 0:
                    WhoChestSpawn = x
                    break
                else:
                    continue
        if Random == 1 and PositionChestChecker == 1 and PositionEnemyChecker == 1 and Position != GamePosition and 1 <= Position <= AllPool:
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
            if JustSpawn == x:
                JustSpawn = 0
            elif EnemyPosition[x] != 0 and EnemyPosition[x] != '':
                for e in range(5000):
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
                            if EndEnemyPosition != int(EnemyPosition[y]):
                                PositionEnemyChecker = 1
                            else:
                                PositionEnemyChecker = 0
                                break
                        if PositionEnemyChecker == 1:
                            for k in range(1, MaxChest + 1):
                                if EndEnemyPosition != ChestPosition[k]:
                                    PositionChestChecker = 1
                                else:
                                    PositionChestChecker = 0
                                    break
                        if PositionChestChecker == 1 and PositionEnemyChecker and 1 <= EndEnemyPosition <= AllPool and EndEnemyPosition != GamePosition:
                            P[EnemyPosition[x]] = ' '
                            EnemyPosition[x] = EndEnemyPosition
                            P[EnemyPosition[x]] = Enemy
                            PositionEnemyChecker = 0
                            PositionChestChecker = 0
                            break

    # INVENTORY CHECKER
    if GoodGame != 1 and 1 <= GamePosition <= AllPool:
        Pool()
        InventoryChecker(Inventory[0], Inventory[1], Inventory[2])
