import datetime
import os
import random
import math
import time
import sys

try:
    from colored import fg, attr
except:
    I = input('Warning: Module named \'colored\' is not installed \n Would you like to install it? [y/N] : ')
    if I.lower() == 'y':
        os.system('pip install colored')
    exit()

def clearScreen():
    print('print "\033c"')

# Colour Printing
class colours:
    leafSymbols = ['#','$','%','&','@','*',',']
    woodSymbols = ['/','\\','|','_','-']

    leafColors = {  
        'light_leaves' : [40,46,47,82,83,84,148],
        'yellow_leaves' : [226,227],
        'mint_leaves' : [77,113,114,120],
        'green_leaves' : [28,34,40,76,112],
        'dark_leaves' : [29,35,36,42,72,78],
        'brown_leaves' : [58,64,106,107],
        'autumn_leaves' : [11,202,208,214,220,226,178]
    }

    woodColors = {
        'yellow_wood' : [221,227,228],
        'light_wood' : [3,179,222],
        'dark_wood' : [94,130],
        'pink_wood' : [209,215],
        'lred_wood' : [173,216],
        'red_wood' : [166,202],
        'moss_wood' : [101,137]
    }

def printColour(string, colours, bold=True, singleChar=False):
    coin = [True, False]
    
    if singleChar:
        output = string
    else:
        output = random.choice(string)

    if random.choice(coin) and bold:
        print ((fg(random.choice(colours)) + attr('bold') + output + attr('reset')), end="")
    else:
        print ((fg(random.choice(colours)) + output + attr('reset')), end="")

class pots:
    defaultPot = {
        'root' : (1,14),
        'max' : 22,
        'label' : 3,
        'labelStart' : 4,
        'labelEnd' : 25,
        'pot' : [
            '__                        __',
            '\\\\=-=-=-=-=-=-=-=-=-=-=-=-//',
            ' \\\\                      // ',
            '  \\\\_|=-=-=-=-=-=-=-=-|_//  ']
    }

    flatPot = {
        'root' : (1,11),
        'max' : 0,
        'label' : 0,
        'labelStart' : 0,
        'labelEnd' : 0,
        'pot' : [
            '_____________________',
            '\\___________________/',
            ' ^                 ^ ']
    }

    plantPot = {
        'root' : (1,9),
        'max' : 13,
        'label' : 4,
        'labelStart' : 3,
        'labelEnd' : 15,
        'pot' : [
            '_________________',
            '\\_______________/',
            ' |             | ',
            ' |             | ',
            ' |  _________  | ',
            ' \\_/         \\_/ ']
    }

    roundPot = {
        'root' : (1,11),
        'max' : 18,
        'label' : 3,
        'labelStart' : 3,
        'labelEnd' : 20,
        'pot' : [
            '  //______________\\\\  ',
            ' //                \\\\ ',
            '||                  ||',
            ' \\\\________________// ']
    }

class bonsai:
    def __init__(self, leafType, woodType, age=0, sHeight=os.get_terminal_size()[1], sLength=os.get_terminal_size()[0], seed=0):
        #if seed != 0:
        #    random.seed(seed)
        #    self.seed = seed
        #else:
        #    self.seed = random.randrange(sys.maxsize)
        #    random.seed(self.seed)
        #self.seed = seed
        #random.seed(self.seed)

        self.leafType = leafType
        self.woodType = woodType

        self.screen = []
        self.sHeight = sHeight
        self.sLength = sLength

        self.age = age
        self.root = [0,0]
        self.pots = pots()

        self.addScreen()
        self.addColours()

    def addColours(self):
        if self.leafType in colours.leafColors:
            self.leaf_c = colours.leafColors[self.leafType]
        else:
            self.leaf_c = colours.leafColors['green_leaves']
        self.leaf_ch = colours.leafSymbols

        if self.woodType in colours.woodColors:
            self.wood_c = colours.woodColors[self.woodType]
        else:
            self.wood_c = colours.woodColors['moss_wood']

    def addScreen(self):
        for h in range(self.sHeight):
            addH = []
            for l in range(self.sLength):
                addH.append(' ')
            self.screen.append(addH)

    def addPot(self, label='', type='default'):
        if type.lower() == 'plantpot':
            pot = self.pots.plantPot
        elif type.lower() == 'flatpot':
            pot = self.pots.flatPot
            label = ''
        elif type.lower() == 'roundpot':
            pot = self.pots.roundPot
        else:
            pot = self.pots.defaultPot

        # Adding Root
        self.root[0] = self.sHeight - len(pot['pot']) + pot['root'][0] - 1
        self.root[1] = math.trunc((self.sLength - len(pot['pot'][0])) / 2) + pot['root'][1]

        # Adding Pot
        startLine = self.sHeight - len(pot['pot'])
        for line in range(len(pot['pot'])):

            # Without Words
            if label == '':
                    
                # Add Pot
                spaceSize = math.trunc((self.sLength - len(pot['pot'][0])) / 2)
                    
                for space in range(spaceSize):
                    self.screen[startLine + line][space] = ' '

                for char in range(len(pot['pot'][line])):
                    self.screen[startLine + line][char + (spaceSize)] = '\033[1m' + pot['pot'][line][char] + '\033[0m'
                    
                for space in range(spaceSize):
                    self.screen[startLine + line][space + len(pot['pot'][0]) + (spaceSize)] = ' '

                self.screen[startLine + line][-1] = ' '

            # With Words
            elif len(label) <= pot['max']:

                # Calculate Input String
                labelString = ''

                if len(label) == pot['max']:
                    labelString = label
                else:
                    labelSpaceSize = math.trunc((pot['max'] - len(label)) / 2)
                    labelString += ' ' * labelSpaceSize + label + ' ' * labelSpaceSize

                    if labelSpaceSize != (len(pot['pot'][0]) - pot['max']) / 2:
                        labelString += ' '

                # Add Pot
                spaceSize = math.trunc((self.sLength - len(pot['pot'][0])) / 2)
                for space in range(spaceSize):
                    self.screen[startLine + line][space] = ' '
                    
                # Add Label
                if line == pot['label'] - 1:
                    for char in range(len(pot['pot'][line])):
                        if char >= pot['labelStart']-1 and char < pot['labelEnd']:
                            self.screen[startLine + line][char + (spaceSize)] = labelString[math.trunc( char - ( (len(pot['pot'][line]) - len(labelString)) / 2 ) )] 
                        else:
                            self.screen[startLine + line][char + (spaceSize)] = '\033[1m' + pot['pot'][line][char] + '\033[0m'
                    
                # Don't add Label
                else:
                    for char in range(len(pot['pot'][line])):
                        self.screen[startLine + line][char + (spaceSize)] = '\033[1m' + pot['pot'][line][char] + '\033[0m'
                    
                for space in range(spaceSize):
                    self.screen[startLine + line][space + len(pot['pot'][0]) + (spaceSize)] = ' '

                self.screen[startLine + line][-1] = ' '
                
            # Error
            else:
                exit()

        # Add Root Stem
        stem = './~~~\\.'
        for i in range(self.root[1]-3 , self.root[1]+4):
            self.screen[self.root[0]][i] = 'w' + stem[i - (self.root[1]-3)]

        self.root[0] -= 1

    def printSelf(self, cls=True):
        if cls:
            clearScreen()

        for line in self.screen:
            for char in line:
                if char == 'l~':
                    printColour(self.leaf_ch, self.leaf_c)
                elif char[0] == 'w':
                    printColour(char[1], self.wood_c, False, True)
                else:
                    print(char, end="")
            print('')

    def calculateDistribution(self, direction):
        if direction == 'SW':
            return [[1,1,'SE']]*10 + [[0,1,'E']]*7 + [[-1,1,'NE']]*3 + [[-1,0,'N']]*3 + [[-1,-1,'NW']]*7 + [[0,-1,'W']]*20 +  [[1,-1,'SW']]*30
        elif direction == 'W':
            return [[1,1,'SE']]*3 + [[0,1,'E']]*3 + [[-1,1,'NE']]*3 + [[-1,0,'N']]*7 + [[-1,-1,'NW']]*20 + [[0,-1,'W']]*60 +  [[1,-1,'SW']]*10
        elif direction == 'NW':
            return [[1,1,'SE']]*1 + [[0,1,'E']]*3 + [[-1,1,'NE']]*7 + [[-1,0,'N']]*20 + [[-1,-1,'NW']]*60 + [[0,-1,'W']]*20 +  [[1,-1,'SW']]*3
        elif direction == 'N':
            return [[1,1,'SE']]*1 + [[0,1,'E']]*7 + [[-1,1,'NE']]*20 + [[-1,0,'N']]*60 + [[-1,-1,'NW']]*20 + [[0,-1,'W']]*7 +  [[1,-1,'SW']]*1
        elif direction == 'NE':
            return [[1,1,'SE']]*3 + [[0,1,'E']]*20 + [[-1,1,'NE']]*60 + [[-1,0,'N']]*20 + [[-1,-1,'NW']]*7 + [[0,-1,'W']]*3 +  [[1,-1,'SW']]*1
        elif direction == 'E':
            return [[1,1,'SE']]*10 + [[0,1,'E']]*60 + [[-1,1,'NE']]*20 + [[-1,0,'N']]*7 + [[-1,-1,'NW']]*3 + [[0,-1,'W']]*3 +  [[1,-1,'SW']]*3
        elif direction == 'SE':
            return [[1,1,'SE']]*30 + [[0,1,'E']]*20 + [[-1,1,'NE']]*7 + [[-1,0,'N']]*3 + [[-1,-1,'NW']]*3 + [[0,-1,'W']]*7 +  [[1,-1,'SW']]*10

    def growBranch(self, direction='', size=-1, sleep=0.0, autoMate=True, branchSections=-1, noClip=True):
        coin = [-1,1]

        # Set Starting Position
        currentPos = [0,0]
        currentPos[0] += self.root[0]
        currentPos[1] += self.root[1]

        #######################################################################################
                                            # Grow Branch #

        # Default Direction Automation
        if autoMate:
            if branchSections < 1:
                branchSections = random.choice([1,2,3,4])

            size = random.randint(15,20)
            timeLine = []

            westoreast = random.choice([True,False])

            for section in range(branchSections):
                if westoreast:
                    direction = random.choice(['N','NW','W'])
                else:
                    direction = random.choice(['N','NE','E'])

                for i in range(math.trunc(size/branchSections)):
                    timeLine.append(direction)

        if math.trunc(size/branchSections) * branchSections != size:
            while len(timeLine) != size:
                timeLine.append(timeLine[-1])
        
        if sleep != 0:
            self.printSelf()
            time.sleep(sleep)
        
        # Main Growth
        for step in range(1, size):
            if autoMate:
                try:
                    distro = random.choice(self.calculateDistribution(timeLine[step]))
                except:
                    print(timeLine)
                    print()
                    exit()
            else:
                distro = random.choice(self.calculateDistribution(direction))

            if self.screen[currentPos[0]][currentPos[1]] == ' ' or self.screen[currentPos[0]][currentPos[1]][0] == 'w':
                if distro[2] == 'SW':
                    self.screen[currentPos[0]][currentPos[1]] = 'w/'
                    self.screen[currentPos[0]][currentPos[1]-1] = 'w/'
                elif distro[2] == 'W':
                    self.screen[currentPos[0]][currentPos[1]] = 'w~'
                    self.screen[currentPos[0]-1][currentPos[1]] = 'w~'
                elif distro[2] == 'NW':
                    self.screen[currentPos[0]][currentPos[1]] = 'w\\'
                    self.screen[currentPos[0]][currentPos[1]-1] = 'w\\'
                elif distro[2] == 'N':
                    self.screen[currentPos[0]][currentPos[1]] = 'w|'
                    self.screen[currentPos[0]][currentPos[1]-1] = 'w|'
                elif distro[2] == 'NE':
                    self.screen[currentPos[0]][currentPos[1]] = 'w/'
                    self.screen[currentPos[0]][currentPos[1]-1] = 'w/'
                elif distro[2] == 'E':
                    self.screen[currentPos[0]][currentPos[1]] = 'w_'
                    self.screen[currentPos[0]-1][currentPos[1]] = 'w_'
                elif distro[2] == 'SE':
                    self.screen[currentPos[0]][currentPos[1]] = 'w\\'
                    self.screen[currentPos[0]][currentPos[1]-1] = 'w\\'
                currentPos[0] += distro[0]
                currentPos[1] += distro[1]
            

            if sleep != 0:
                self.printSelf()
                time.sleep(sleep)

        #######################################################################################
                                            # Grow Leaves #
        # Main Growth
        leaves = []
        if currentPos[0] > self.sHeight - 7 and noClip:
            pass
        else:
            leaves.append(currentPos)
            for step in range(1, random.randint(10,15)):
                currentLeafPos = random.choice(leaves)

                for addLeaf in range(9):
                    distro = random.choice([[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,1],[0,1],[0,-1],[2,0],[-2,0],[0,2],[0,-2]])

                    addLeafPos = [0,0]
                    addLeafPos[0] = currentLeafPos[0] + distro[0]
                    addLeafPos[1] = currentLeafPos[1] + distro[1]
                    try:
                        self.screen[addLeafPos[0]][addLeafPos[1]] = 'l~'
                    except:
                        pass

                    leaves.append(addLeafPos)

                if sleep != 0:
                    self.printSelf()
                    time.sleep(sleep)

                leaves.remove(currentLeafPos) 

        self.printSelf()

#b = bonsai('autumn_leaves','dark_wood')
#b.addPot(label='', type='')
#b.printSelf()
#input('>> ')
#b.printSelf()
#b.printRoot()
#b.growArm(sleep=0.05, direction='NE')
#b.growArm(sleep=0.05, direction='NW')
#b.growBranch(sleep=0.05)
#b.growBranch(sleep=0.05)
#b.growBranch(sleep=0.05)
#b.printSelf()

if __name__ == "__main__":
    sleepTime = 0
    leafType = ''
    woodType = ''
    message = ''

    # Help
    if '-h' in sys.argv:
        print('python3 bonsai.py -[h, l, t, c, w, m, v, vv, d, s] {...}\n\n-h  :: Help command\n-l  :: Show live growth\n-t  :: Delay between growth\n-c  :: Type of leaves (-hc for list)\n-w  :: Type of wood (-hw for list)\n-m  :: Write a message on the pot\n-v  :: Verbose customation\n-vv :: More verbose customation\n-d  :: Add date to pot\n-s  :: Use custom seed')
        exit()
    elif '-hc' in sys.argv:
        print('List of leaf types: \n\nlight_leaves\nyellow_leaves\nmint_leaves\ngreen_leaves\ndark_leaves\nbrown_leaves\nautumn_leaves')
        exit()
    elif '-hw' in sys.argv:
        print('List of wood types: \n\nyellow_wood\nlight_wood\ndark_wood\npink_wood\nlred_wood\nred_wood\nmoss_wood')
        exit()

    # Verbose Outputs
    verboseOut = False
    if '-vv' in sys.argv:
        verboseOut = True

        seed = int(input('Enter seed ("0" for random): '))
        noClip = input('Use NoClip function [Y/n]: ').lower != 'n'

        sleepTime = float(input('Delay between growth: '))
        print('List of leaf types: \n\n 0 : light_leaves\n 1 : yellow_leaves\n 2 : mint_leaves\n 3 : green_leaves\n 4 : dark_leaves\n 5 : brown_leaves\n 6 : autumn_leaves\n')
        leaves = ['light_leaves', 'yellow_leaves', 'mint_leaves', 'green_leaves', 'dark_leaves', 'brown_leaves', 'autumn_leaves']
        leafType = leaves[int(input('Enter number of leaf type: '))]

        print('List of leaf types: \n\n 0 : yellow_wood\n 1 : light_wood\n 2 : dark_wood\n 3 : pink_wood\n 4 : lred_wood\n 5 : red_wood\n 6 : moss_wood\n')
        woods = ['yellow_wood', 'light_wood', 'dark_wood', 'pink_wood', 'lred_wood', 'red_wood', 'moss_wood']
        woodType = woods[int(input('Enter number of wood type: '))]

        branches = int(input('Amount of branches ("0" for random): '))

        message = input('Enter pop label: ')
        useDateTime = input('Use Date [y/N]: ')
        if useDateTime.lower()  == 'y':
            message = str(datetime.date.today())

    elif '-v' in sys.argv:
        sleepTime = float(input('Speed of growth: '))
        print('List of leaf types: \n\n 0 : light_leaves\n 1 : yellow_leaves\n 2 : mint_leaves\n 3 : green_leaves\n 4 : dark_leaves\n 5 : brown_leaves\n 6 : autumn_leaves\n')
        leaves = ['light_leaves', 'yellow_leaves', 'mint_leaves', 'green_leaves', 'dark_leaves', 'brown_leaves', 'autumn_leaves']
        leafType = leaves[int(input('Enter number of leaf type: '))]

        print('List of leaf types: \n\n 0 : yellow_wood\n 1 : light_wood\n 2 : dark_wood\n 3 : pink_wood\n 4 : lred_wood\n 5 : red_wood\n 6 : moss_wood\n')
        woods = ['yellow_wood', 'light_wood', 'dark_wood', 'pink_wood', 'lred_wood', 'red_wood', 'moss_wood']
        woodType = woods[int(input('Enter number of wood type: '))]

        message = input('Enter pop label: ')

    # Set Params
    if '-s' in sys.argv:
        index = sys.argv.index('-s')
        seed = int(sys.argv[index+1])
    else:
        seed = random.randrange(sys.maxsize
    random.seed(seed)

    if '-l' in sys.argv:
        sleepTime = 0.05
    if '-t' in sys.argv:
        index = sys.argv.index('-t')
        sleepTime = float(sys.argv[index+1])
    if '-c' in sys.argv:
        index = sys.argv.index('-c')
        leafType = sys.argv[index+1]
    if '-w' in sys.argv:
        index = sys.argv.index('-w')
        woodType = sys.argv[index+1]

    if '-d' in sys.argv:
        message = str(datetime.date.today())
    elif '-m' in sys.argv:
        index = sys.argv.index('-w')
        message = sys.argv[index+1]

    if verboseOut != True:
        # Plant Pot
        b = bonsai(leafType,woodType,seed=seed)
        b.addPot(label=message, type='')
        b.printSelf()

        for i in range(random.randint(2,6)):
            b.growBranch(sleep=sleepTime)
    
        b.printSelf()
        doNext = input('')
        if doNext == 'seed':
            clearScreen()
            b.printSelf()
            print(seed)
        else:
            exit()

    else:
        b = bonsai(leafType,woodType,seed=seed)
        b.addPot(label=message, type='')

        if branches < 1:
            branches = random.randint(2,6)

        for i in range(branches):
            b.growBranch(sleep=sleepTime, noClip=noClip)

        b.printSelf()
        doNext = input('')
        if doNext == 'seed':
            clearScreen()
            b.printSelf()
            print(seed)
        else:
            exit()

# self.screen[startLine + line][char + (spaceSize)] = labelString[math.trunc( char - ( (len(pot['pot'][line]) - len(labelString)) / 2 ) )] 
