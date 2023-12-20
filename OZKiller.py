from random import randint
def create_Table(DiagramSplitSymbol, DiagramDivideSymbol, DiagramSpaceSymbol, PrintSymbolLine, PrintSymbolCell, MaxSymbol, DiagramSetting):

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

def Pool():
    create_Table('l', '|', '', '', '', 0,
                 f'\033[37ml[ {P[1]} ] l[ {P[2]} ] l[ {P[3]} ] l[ {P[4]} ] l[ {P[5]} ] | l[ {P[6]} ] l[ {P[7]} ] l[ {P[8]} ] l[ {P[9]} ] l[ {P[10]} ] | l[ {P[11]} ] l[ {P[12]} ] l[ {P[13]} ] l[ {P[14]} ] l[ {P[15]} ] | l[ {P[16]} ] l[ {P[17]} ] l[ {P[18]} ] l[ {P[19]} ] l[ {P[20]} ] | l[ {P[21]} ] l[ {P[22]} ] l[ {P[23]} ] l[ {P[24]} ] l[ {P[25]} ] |')

Game = True
if Game == True:
    y = 0
    z = 0
    x = 0
    s = 0
    k = 0
    p = 0
    GoodGame = 0
    Killer = '\033[31mKiller\033[37m'
    SpeedBoost = '\033[34mSpeedBoost\033[37m'
    Hero = '\033[32mO\033[37m'
    Enemy = '\033[31mX\033[37m'
    Chest = '\033[33mC\033[37m'
    JustSpawn = 0
    ChestPosition = 0
    Inventory = {0: 0, 1: 0, 2: 0}
    EnemyPosition = {1: '', 2: '', 3: '', 4: '', 5: ''}
    P = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' ', 14: ' ', 15: ' ', 16: ' ', 17: ' ', 18: ' ', 19: ' ', 20: ' ', 21: ' ', 22: ' ', 23: ' ', 24: ' ', 25: ' '}

    Answer = int(input())
    GamePosition = Answer
    P[GamePosition] = Hero
    Pool()

    while True:
        if GamePosition <= 0 or GamePosition > 25 or GoodGame == 1:
            P[GamePosition] = Enemy
            Pool()
            print(f'\033[31mYou Lose(\n\033[39mAll turn: \033[35m{z + 1}')
            Game = False
            break
        if EnemyPosition[1] == 0 and EnemyPosition[2] == 0 and EnemyPosition[3] == 0 and EnemyPosition[4] == 0 and EnemyPosition[5] == 0:
            print(f'\033[34mYou Win!\n\033[39mAll turn: \033[35m{z + 1}')
            Game = False
            break

        Move = input()
        if Move == '':
            Move = 'MMMM'
        if Move[0] == 'w':
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition - 5] = Hero
                P[GamePosition] = ' '
                GamePosition -= 5
            P[GamePosition - 5] = Hero
            P[GamePosition] = ' '
            GamePosition -= 5
            z += 1
            x = z - 1
        elif Move[0] == 'a':
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition - 1] = Hero
                P[GamePosition] = ' '
                GamePosition -= 1
            P[GamePosition - 1] = Hero
            P[GamePosition] = ' '
            GamePosition -= 1
            z += 1
            x = z - 1
        elif Move[0] == 'd':
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition + 1] = Hero
                P[GamePosition] = ' '
                GamePosition += 1
            P[GamePosition + 1] = Hero
            P[GamePosition] = ' '
            GamePosition += 1
            z += 1
            x = z - 1
        elif Move[0] == 's':
            if Move[len(Move) - 1] == 'S' and Inventory[1] != 0:
                Inventory[1] = 0
                P[GamePosition + 5] = Hero
                P[GamePosition] = ' '
                GamePosition += 5
            P[GamePosition + 5] = Hero
            P[GamePosition] = ' '
            GamePosition += 5
            z += 1
            x = z - 1
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

            if Inventory[1] == SpeedBoost and s == 0:
                print(f'\nWow! You get a \'{SpeedBoost}\'. Print for example \'wS\' to go 2 cells up')
                s = 1
            elif Inventory[2] == Killer and k == 0:
                print(f'\nWow! You get a \'{Killer}\'. Print for example \'aK\' to go 1 cells left and killing enemy')
                k = 1
            z += 1
            x = z - 1
        else:
            x = z

        if Move[len(Move) - 1] == 'K' and Inventory[2] == Killer and len(str(Move)) >= 2:
            for v in range(1, y + 1):
                if GamePosition == EnemyPosition[v]:
                    Inventory[2] = 0
                    EnemyPosition[v] = 0
                    p = 1
                    print('\033[36mYou are killing enemy!')
                    break
                else:
                    p = 0
            if p == 0:
                Inventory[2] = 0
                print('\033[36mYou aren\'t killing enemy(')

        if GamePosition == ChestPosition:
            ChestPosition = 0
            Inventory[0] = 1

        if z == 3 and x == z - 1:
            while True:
                Line = randint(1, 5)
                Column = randint(1, 5)
                Position = Line * Column
                if Position != GamePosition:
                    EnemyPosition[1] = Position
                    P[EnemyPosition[1]] = Enemy
                    y += 1
                    JustSpawn = 1
                    break
        if z == 6 and x == z - 1:
            while True:
                Line = randint(1, 5)
                Column = randint(1, 5)
                Position = Line * Column
                if Position != GamePosition and Position != EnemyPosition[1] and Position != ChestPosition:
                    EnemyPosition[2] = Position
                    P[EnemyPosition[2]] = Enemy
                    y += 1
                    JustSpawn = 2
                    break

        if z == 9 and x == z - 1:
            while True:
                Line = randint(1, 5)
                Column = randint(1, 5)
                Position = Line * Column
                if Position != GamePosition and Position != EnemyPosition[1] and Position != EnemyPosition[2] and Position != ChestPosition:
                    EnemyPosition[3] = Position
                    P[EnemyPosition[3]] = Enemy
                    y += 1
                    JustSpawn = 3
                    break

        if z == 12 and x == z - 1:
            while True:
                Line = randint(1, 5)
                Column = randint(1, 5)
                Position = Line * Column
                if Position != GamePosition and Position != EnemyPosition[1] and Position != EnemyPosition[2] and Position != EnemyPosition[3] and Position != ChestPosition:
                    EnemyPosition[4] = Position
                    P[EnemyPosition[4]] = Enemy
                    y += 1
                    JustSpawn = 4
                    break

        if z == 15 and x == z - 1:
            while True:
                Line = randint(1, 5)
                Column = randint(1, 5)
                Position = Line * Column
                if Position != GamePosition and Position != EnemyPosition[1] and Position != EnemyPosition[2] and Position != EnemyPosition[3] and Position != EnemyPosition[4] and Position != ChestPosition:
                    EnemyPosition[5] = Position
                    P[EnemyPosition[5]] = Enemy
                    y += 1
                    JustSpawn = 5
                    break

        if z % 3 == 0 and ChestPosition == 0 and Inventory[0] == 0 and (Inventory[1] != SpeedBoost or Inventory[2] != Killer) and x == z - 1:
            Random = randint(1, 2)
            Line = randint(1, 5)
            Column = randint(1, 5)
            Position = Line * Column
            if (Random == 1 and Position != GamePosition and Position != EnemyPosition[1] and Position != EnemyPosition[2] and Position != EnemyPosition[3] and Position != EnemyPosition[4] and Position != EnemyPosition[5] and 1 <= Position <= 25):
                ChestPosition = Position
                P[ChestPosition] = Chest

        if x == z - 1:
            for l in range(1, y + 1):
                RandomUltra = randint(1, 4)
                if EnemyPosition[l] == GamePosition:
                    GoodGame = 1
                    break
                elif EnemyPosition[l] != 0 and EnemyPosition[l] != ' ':
                    for e in range(10000):
                        if l == JustSpawn:
                            JustSpawn = 0
                            break
                        EndEnemyPosition = EnemyPosition[l]
                        Random = randint(1, 4)
                        if RandomUltra == 2 and (GamePosition - 5 == EnemyPosition[l] or GamePosition + 5 == EnemyPosition[l] or GamePosition - 1 == EnemyPosition[l] or GamePosition + 1 == EnemyPosition[l]):
                            P[EnemyPosition[l]] = ' '
                            EnemyPosition[l] = GamePosition
                            break
                        else:
                            if Random == 4:
                                EndEnemyPosition += 5
                            elif Random == 2:
                                EndEnemyPosition += 1
                            elif Random == 1:
                                EndEnemyPosition -= 1
                            elif Random == 3:
                                EndEnemyPosition -= 5
                            if EndEnemyPosition != EnemyPosition[1] and EndEnemyPosition != EnemyPosition[2] and EndEnemyPosition != EnemyPosition[3] and EndEnemyPosition != EnemyPosition[4] and EndEnemyPosition != EnemyPosition[5] and EndEnemyPosition != ChestPosition and 1 <= EndEnemyPosition <= 25:
                                P[EnemyPosition[l]] = ' '
                                EnemyPosition[l] = EndEnemyPosition
                                P[EnemyPosition[l]] = Enemy
                                break
                if EnemyPosition[l] == GamePosition:
                    GoodGame = 1
                    break

        if GoodGame != 1 and 1 <= GamePosition <= 25:
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


