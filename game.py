import random
import time

# TODO: box with key

legende = {"." : "floor", 
           "f" : "food",
           "M" : "Monster",
           "$" : "Gold",
           "h" : "healing potion",
           "k" : "key",
           "b" : "box",
           "*" : "flower",
           "#" : "wall",
           "<" : "Stair up",
           ">" : "Stair down",
           "s" : "sword",
           "o" : "shield",
           "a" : "axe",
           "§" : "box key",
           }

level1 = """
###################################
#>.B.o...#.....D..M.....k...o....1#
#....*...d..f............M........#
#k.a.ß...#........M..........s....#
#.........#########################
#........ZZZZZZZ...ZZZZZ..........#
#..ZZZZZZ.........Z.......Z.......#
###################################"""

level2 = """
###################################
#<...............B...............2#
#>....o.................P.........#
#..............M..................#
###################################"""

level3 = """
###################################
#<..o....#..d.......d............3#
#>......####.......#..........D...#
#......M..k........#.............k#
###################################"""

level4 = """
####################################
#<..b.............................4#
#>.................................#
#...............Z..................#
#..................................#
#..................................#
#..................................#
####################################"""

class Item():
    number = 0
    storage = []
    
    def __init__(self, x=None, y=None, z=None, carrier=None):
        self.x = x
        self.y = y
        self.z = z
        self.carrier = carrier
        self.char = "i"
        self.number = Item.number
        Item.number += 1
        Item.storage.append(self)
        self.overwrite()
        self.quality = 0.9
        self.lenght = 0
        
    def overwrite(self):
        pass
        
class Sword(Item):
    
    def overwrite(self):
        self.quality = random.choice((0.5, 0.6, 0.7, 0.7, 0.8, 0.9, 1.0))
        self.maxdamage = 10
        self.mindamage = 2
        self.defense = 0.5
        self.attack = 0.90
        self.length = 90

class Axe(Item):
    
    def overwrite(self):
        self.quality = random.choice((0.4,0.5,0.7,0.9,0.10))
        self.mindamage = 6
        self.maxdamage = 12
        self.defense = 0.2
        self.attack = 0.75
        self.lenght = 60 
        
class Dagger(Item):
    
    def overwrite(self):
        self.quality = random.choice((0.7,0.8,0.9, 1.0))
        self.mindamage = 4
        self.maxdamage = 8
        self.defense = 0.1
        self.attack = 0.85
        self.lenght = 30 
        
        
class DragonBite(Item):

	def overwrite(self):
			self.quality = 1.0
			self.mindamage = 4
			self.maxdamage = 8
			self.defense = 0.1
			self.attack = 0.80
		
class BatBite(Item):
	
	def overwrite(self):
		self.quality = 1.0
		self.mindamage = 2
		self.maxdamage = 4
		self.defense = 0.001
		self.attack = 0.25
		
	
class Fist(Item):
	
	def overwrite(self):
		self.quality = 1.0
		self.mindamage = 3
		self.maxdamage = 6
		self.defense = 0.2
		self.attack = 0.50

class Monster():
    number = 0
    zoo = []
    
    def __init__(self, x, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.char = "M"
        self.number = Monster.number
        Monster.number += 1
        Monster.zoo.append(self)
        self.hp = random.randint(10,20)
        self.attack = 0.7
        self.defense = 0.25
        self.mindamage = 1
        self.maxdamage = 3
        self.aggro = 3
        self.weapon = None
        self.weapons = []
        self.armor = None
        self.armors = []
        self.naturalweapon = "bite"
        self.naturalweapon = "skin"
        self.overwrite()

    def equip(self):
        """creates a random armor and a random weapon to use for this monster"""
        a = Armor(carrier=self.number)
        w = random.choice((Sword(carrier=self.number), Axe(carrier=self.number), Dagger(carrier=self.number)))
        self.armors.append(a.number)
        self.armor = a.number
        self.weapons.append(w.number)
        self.weapon = w.number
        
    def overwrite(self):
        pass
        
    def move(self, player):
        # moving toward player?
        dx = 0
        dy = 0
        distance = ((self.x-player.x)**2 + (self.y-player.y)**2)**0.5
        if distance < self.aggro:
            if self.x < player.x:
                dx = 1
            elif self.x > player.x:
                dx = -1
            if self.y < player.y:
                dy = 1
            elif self.y > player.y:
                dy = -1
            return dx, dy
        else:
            return self.ai()
            
    def ai(self):
        # random movement
        dx = random.choice((-1,0,0,0,1))
        dy = random.choice((-1,0,0,0,1))
        return dx, dy

class Armor(Item):
    
    def overwrite(self):
        self.quality = random.choice((0.3,0.4,0.45,0.5,0.5,0.6,0.65,0.7,0.8,0.85,0.9))
        self.damagereducing = random.randint(1,5)

class Skin(Armor):
	
	def overwrite(self):
		self.damagereducing = 0
	
class Fur(Armor):
	
	def overwrite(self):
		self.damagereducing = 0
	
class Scales(Armor):
	
	def overwrite(self):
		self.quality = 1.0
		self.damagereducing = 3
	
class Jacket(Armor):

    def overwrite(self):
        #self.quality = random.choice((0.3,0.4,0.45,0.5,0.5,0.6,0.65,0.7,0.8,0.85,0.9, 1.0))
        self.damagereducing = 2 #round(4 * self.quality,0)

class Leatherarmor(Armor):
    
    def overwrite(self):
        #self.quality = random.choice((0.3,0.4,0.45,0.5,0.5,0.6,0.65,0.7,0.8,0.85,0.9, 1.0))
        self.damagereducing = 4 #round(4 * self.quality,0)
        
class Ringmail(Armor):
    
    def overwrite(self):
        #self.quality = random.choice((0.3,0.4,0.45,0.5,0.5,0.6,0.65,0.7,0.8,0.85,0.9, 1.0))
        self.damagereducing = 6 #round(4 * self.quality,0)
    
    
class Chainmail(Armor):
    
    def overwrite(self):
        #self.quality = random.choice((0.3,0.4,0.45,0.5,0.5,0.6,0.65,0.7,0.8,0.85,0.9, 1.0))
        self.damagereducing = 7 #round(7 * self.quality,0)
    

class Platemail(Armor):

    def overwrite(self):
        #self.quality = random.choice((0.3,0.4,0.45,0.5,0.5,0.6,0.65,0.7,0.8,0.85,0.9, 1.0))
        self.damagereducing = 10 #round(10 * self.quality,0)

class Player(Monster):
    
    def overwrite(self):
        self.char = "@"
        self.hp = 250
        self.attack = 0.88
        self.defense = 0.33
        self.gold = 0
        self.keys = 0
        self.boxkey = 0
        self.hunger = 0
        self.mindamage = 1
        self.maxdamage = 10
        self.flowers = 0
        self.happyend = False
        #self.weapon = None
        #self.weapons = []
        #self.armor = None
        #self.armors = []
        self.naturalweapon = "fist"
        self.damagebonus = 0
        self.attackbonus = 0
        self.maxdambonus = 0
        self.mindambonus = 0
        #sself.weaponquality = 1.0
        self.equip()
       
    
    def select_weapon(self):
        if len(self.weapons) == 1:
            print("you have only one weapon. find more weapons!")
            return
        print("please enter number of the weapon you like to wield")
        for number, w in enumerate(self.weapons):
            print( number, "............", w)
        c = input("select weapon number to wield please >>>")
        try:
            c = int(c)
        except:
            print("please enter a number only")
            return
        if c < 0 or c > len(self.weapons) - 1:
            print("please enter a valid number only")
            return 
        self.weapon = self.weapons[c]
    
    def select_armor(self):
        if len(self.armors) == 1:
            print("you have only one armor. find more armors!")
            return
        print("please enter number of the armor you like to wield")
        for number, w in enumerate(self.armors):
            print( number, "............", w)
        d = input("select armor number to wield please >>>")
        try:
            d = int(d)
        except:
            print("please enter a number only")
            return
        if d < 0 or d > len(self.armors) - 1:
            print("please enter a valid number only")
            return 
        self.armors = self.armors[d]

class Bandit(Monster):
    
    def overwrite(self):
        self.char = "Z"
        self.hp = random.randint(15,30)
        self.defense = 0.2
        self.attack = 0.4
        self.mindamage = 7 
        self.maxdamage = 14
        self.aggro = 3
        #self.naturalweapon = "fist"
        self.equip()
   

class Dragon(Monster):
    
    def overwrite(self):
        self.char = "D"
        self.hp = random.randint(150,200)
        self.defense = 0.05
        self.attack = 0.5
        self.mindamage = 10
        self.maxdamage = 20
        self.aggro = 2
        #self.naturalweapon = "fire"
        self.armor = Scales(carrier=self.number).number
        self.weapon = DragonBite(carrier=self.number).number        
        
class Princess(Monster):
    
    def overwrite(self):
        self.char = "P"
        self.attack = 0.1
        self.mindamage = 1
        self.maxdamage = 1
        self.aggro = 2
        self.defense = 0.1
        #self.naturalweapon = "fist"
        self.weapon = Fist(carrier=self.number).number
        self.armor = Jacket(carrier=self.number).number
        
    def ai(self):
        # random movement
        dx = random.choice((-1,0,0,0,0,0,0,0,0,0,0,1))
        dy = random.choice((-1,0,0,0,0,0,0,0,0,0,0,1))
        return dx, dy
        
        
class Bat(Monster):
    
    def overwrite(self):
        self.char = "B"
        self.hp = random.randint(2, 7)
        self.defense = 0.6
        self.attack = 0.3
        self.mindamage = 0
        self.maxdamage = 3
        self.aggro = 5
        #self.naturalweapon = "bite"
        self.weapon = BatBite(carrier=self.number).number
        self.armor = Skin(carrier=self.number).number
    
    def ai(self):
        # random movement
        dx = random.choice((-2,-1,0,1,2))
        dy = random.choice((-2,-1,0,1,2))
        return dx, dy
        
  
        
def strike(a, d):
    namea = a.__class__.__name__
    named = d.__class__.__name__
    if named == "Princess":
        if a.flowers < 1:
            a.hp -= 1
            print("The princess hits you because you are not a gentleman.You need a flower!")
            return
        else:
            a.flowers -= 1
            print("You win!")
            a.happyend = True
            return
    
    # --- start attack (defender is not a princess) -----
    armora = Item.storage[a.armor]
    weapona = Item.storage[a.weapon]
    armord = Item.storage[d.armor]
    weapond = Item.storage[d.weapon]
    
    print("{} attacks (with {} and {}) against {} ( with {} and {})!".format(
         namea, weapona.__class__.__name__, armora.__class__.__name__, named,
         weapond.__class__.__name__,armord.__class__.__name__))
    r1 = random.random()   #
    attack = Item.storage[a.weapon].attack
    defense = Item.storage[d.weapon].defense
    print("attack roll: {:.2f}".format(r1))
    if r1 > attack:
        print("Oh, no! {} fumbles the attack ( > {:.2f})".format(
              namea, attack))
        return
    print("attack begins sucessfull....(< {:.2f})".format(attack ))
    #r2 = random.random()
    if r1 < defense:
        print("Sdeng! {} sucessfully blocks the attack (< {:.2f})".format(
              named, defense))
        # chance for both weapons to decrease in quality
        for c in [a, d]:
           weapondamage(c)
        
        return
    print("{} was unable to block this attack! (> {:.2f})".format(named,defense))
    # ---- hit against armor ----
    damage = random.randint(a.mindamage, a.maxdamage)
    print("Hit with {} against {}  original damage: {} ".format(weapona.__class__.__name__,
           armord.__class__.__name__, damage))
    
    d.hp -= damage
    print("{} takes {} damage and has  {} hp left.".format(
          named, damage, d.hp))
    weapondamage(a)
    if d.hp <= 0:
        print("{} wins vs  {}".format(namea, named))
 
def weapondamage(owner):
     if owner.weapon is not None:
                weapondamage = random.choice((0.0,0,0,0,0.0,0.001,0.002,0.003,0.004,0.005))
                if weapondamage > 0:
                    print("weapon of {} looses {} quality".format(owner.__class__.__name__, weapondamage))
                    Item.storage[owner.weapon].quality -= weapondamage
                    print("weapon-quality is now {:.2f}".format(Item.storage[owner.weapon].quality))
                    #owner.weaponquality -= weapondamage
                    if Item.storage[owner.weapon].quality <= 0.0:
                        print("The weapon of {} is destroyed".format(owner.__class__.__name__))
                        owner.weapon = None
    

def battle(a, d):
    #a.weaponquality -= 0.01
    print("---- Strike! -----")
    strike(a, d)
    if d.hp > 0:
        print("----Counterstrike! -----")
        strike( d, a)
    #if hero.weaponquality == 0:
        
    
def game():
    hero = Player(1,3,0)
    # ---- dungeon prepare ----
    dungeon = []
    for z, a in enumerate((level1, level2, level3, level4)):
        level = []
        for y, b in enumerate(a.splitlines()):
            line = []
            for x, c in enumerate(b):
                char = c
                if c == "M":
                    char = "." # floor
                    Monster(x,y,z)
                elif c == "B":
                    char = "." 
                    Bat(x,y,z)
                elif c == "P":
                    char = "."
                    Princess(x,y,z)
                elif c == "D":
                    char = "."
                    Dragon(x,y,z)
                elif c == "Z":
                    char = "."
                    Bandit(x,y,z)
                if char == ".":
                    # floor mit casualcheese?
                    # cheese chancs  20% -> 0.2
                    if random.random() < 0.05:
                        char = "f"
                    if random.random() < 0.:
                        char = "$"   
                line.append(char)
            level.append(line)
        dungeon.append(level)
    # dungeon is ready
                

    # --- Graphic engine----
    while hero.hp>0 and hero.hunger < 150 and not hero.happyend:
        # ...
        for y, line in enumerate(dungeon[hero.z]):
            for x, char in enumerate(line):
                for m in Monster.zoo:
                    if m.z != hero.z or m.hp <1:
                        continue
                    if m.x == x and m.y ==y:
                        print(m.char, end="")
                        break
                else:
                    print(char, end="")
            print() # line-end
        print()     # dungeon end
        if hero.weapon is None:
            weapon = hero.naturalweapon
        else:
            weapon = Item.storage[hero.weapon].__class__.__name__
        text = ""
        text += "hp: {} $: {} hungry: {} keys: {} flowers: {}".format(hero.hp, hero.gold, hero.hunger, hero.keys, hero.flowers)
        armor = Item.storage[hero.armor]
        weapon = Item.storage[hero.weapon]
        text += "\nArmor: {} ({:.1f}%) Weapon: {} ({:.1f}%) Att: {} Def: {} Mindmg: {} Maxdmg: {}".format(
                 armor.__class__.__name__, armor.quality * 100, 
                 weapon.__class__.__name__, weapon.quality * 100,
                 hero.attack, hero.defense, hero.mindamage , hero.maxdamage)
        command = input(text)
        dx = 0
        dy = 0
        if command == "a":
            dx = -1
        if command == "d":
            dx = 1
        if command == "w":
            dy = -1
        if command == "s":
            dy = 1
        if command == "i":
            hero.select_weapon()
            hero.select_armor()
        # treppen
        if command == "up" or command == "<":
            if hero.z == 0:
                print("you are at the highest floor already")
            elif dungeon[hero.z][hero.y][hero.x] == "<":
                hero.z -= 1
                continue 
            else:
                print("you must find a stair up (<)")
        
        if command == "down" or command == ">":
            if hero.z == len(dungeon)-1:
                print("you are at the lowest floor already")
            elif dungeon[hero.z][hero.y][hero.x] == ">":
                hero.z += 1
                continue
            else:
                print("you must find a stair down(>)")
        
        if command == "exit" or command == "quit" or command == "i don´t want to play any more":
            break
        if command == "help" or command == "?":
            for z in legende:
                print(z, "........", legende[z])    
        # --- Monster? ---
        for m in Monster.zoo:
            if m.number == 0:
                continue  # player ist Monster number 0
            if m.hp < 1:
                continue
            if m.z != hero.z:
                continue 
            if m.x == hero.x + dx and m.y == hero.y + dy:
                dx = 0
                dy = 0
                battle(hero, m)
                break
        #Teleporter
        if dungeon[hero.z][hero.y][hero.x] == "ß":
            for v in range(1000):
                x = random.randint(-10,10)
                y = random.randint(-10,10)
                if x == 0 and y == 0:
                    continue
                try:
                    t = dungeon[hero.z][hero.y+y][hero.x+x]
                except:
                    continue # out of dungoen error
                if t in ".kf*": # floor, key or food or flower 
                    hero.y += y
                    hero.x += x
                    break
            else:
                print("the teleporter could not find a legal field for teleportation")
                
                    
            #hero.x += 
        # --- wall ? ----
        if dungeon[hero.z][hero.y+dy][hero.x+dx] == "#":
            print("ouch, a wall!")
            dx = 0
            dy = 0
        # ---- door ? ----
        if dungeon[hero.z][hero.y+dy][hero.x+dx] == "d":
            if hero.keys < 1:
                print("closed door: find a key (k)!")
                dx = 0
                dy = 0
            else:
                hero.keys -= 1
                print("you heroically used a key to open the door")
                dungeon[hero.z][hero.y+dy][hero.x+dx] = "."
        # --- moving-hero 
        hero.x += dx
        hero.y += dy
        # ---- moving-monsters----
        print("moving monsters")
        for m in Monster.zoo:
            if m.number ==0 or m.hp <1 or m.z != hero.z:
                continue
            dx, dy = m.move(hero)
            # tries the monster to escape the dungeon?
            dest = "."
            try:
                dest = dungeon[hero.z][m.y+dy][m.x+dx]
            except:
                dx = 0
                dy = 0
            if dest in "#d":   # wall or door?
                dx = 0
                dy = 0
            # tries monster to run into other monster?
            for m2 in Monster.zoo:
                if m2.number == m.number or m2.hp <1 or m2.z != hero.z:
                    continue
                if m.x + dx == m2.x and m.y + dy == m2.y:
                    dx = 0
                    dy = 0
                    if m2.number == 0:
                        battle(m, m2)
            m.x += dx # the monster moves!
            m.y += dy
        # ----food clock ----
        hero.hunger += 1
        # ----- items -----
        # --- cheese ---
        if dungeon[hero.z][hero.y][hero.x] == "f":
            dungeon[hero.z][hero.y][hero.x] = "."   
            print("yummi cheese,")
            hero.hunger -= random.randint(3,8) 
        # --- flowers ---
        if dungeon[hero.z][hero.y][hero.x] == "*":
            dungeon[hero.z][hero.y][hero.x] = "."   
            print("oh, a flower! I need to find a princess!")
            hero.flowers += 1 
        #---gold---
        if dungeon[hero.z][hero.y][hero.x] == "$":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("oho, I am rich!")
            hero.gold += random.randint(10,20)
        # --- sword ---
        if dungeon[hero.z][hero.y][hero.x] == "s":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("Oh..a sword!")
            print("now you can fight better but your defense is lower!")
            w = random.choice(["iron sword", "magic sword" "wooden sword"])
            hero.mindambonus = random.choice((-1,0,0,1,2))
            hero.maxdambonus = random.choice((-1,-1,0, 0, 1,1,1,2))
            hero.attackbonus = random.choice((-0.1,0.1,-0.2,0.2))
            hero.defensebonus = random.choice((-0.05,-0.5,0.1 ,0,1, -0.5))
            hero.weapons.append("Sword")
            hero.mindamage += 4
            hero.maxdamage += 4
            hero.attack += 0.05
            hero.defense -= 0.05
            hero.liveweapon = 6
        # --- axe ---
        if dungeon[hero.z][hero.y][hero.x] == "s":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("Oh..an axe!")
            print("now you can fight more better but your defense is more lower!")
            hero.mindamage += 4
            hero.maxdamage += 4
            hero.attack += 0.05
            hero.defense -= 0.05
            hero.mindambonus = random.choice((-2,0,4,4,0,-2))
            hero.maxdambonus = random.choice((-1,0,6,6,0,-1))
            hero.attackbonus = random.choice((-0.1,0.1,-0.2,0.2))
            hero.defensebonus = random.choice((-0.05,-0.5, 0.1, -0.5, -0.5))
            hero.liveweapon = 4
            hero.weapons.append("Axe")
        # --- shield ---
        #if dungeon[hero.z][hero.y][hero.x] == "o":
            #dungeon[hero.z][hero.y][hero.x] = "."
            #print("Oh..a shield!")
            #print("now your defense is better but your attack is lower!")
            #hero.defense += 0.07
            #hero.attack -= 0.02
            #hero.mindambonus = random.choice((-2,0,0,0,0,0,-2))
            #hero.maxdambonus = random.choice((-1,0,0,0,0,0,-1))
            #hero.attackbonus = random.choice((0,-0.2,0,0,-0.2,0,0,0.1))
            #hero.defensebonus = random.choice((-0.1,0,0,0.5,0.5,0.5,0,0))
            #hero..append("Shield")
        # --- armor ---
        if dungeon[hero.z][hero.y][hero.x] == "o":
            dungeon[hero.z][hero.y][hero.x] = "."
            quality = ["good", "good", "perfect", "used", "broken"]
            armors = ["golden armor","silver armor","silver armor","chain armor","chain armor","chain armor"]
            q = random.choice(quality)
            a = random.choice(armors)
            if a == "golden armor":
                print("oh.. a {} golden armor!".format(q))
                hero.defensebonus = random.choice((2,3,1,2,3,1,2,3))
                hero.armors.append("{} golden armor".format(q))
            if a == "silver armor":
                print("oh.. a {} silver armor!".format(q))
                hero.defensebonus = random.choice((0.1,0.2,0.1,0.2,0.1,0.2,0,0.2))
                hero.armors.append("{} silver armor".format(q))
            if a == "chain armor":
                print("oh.. {} a chain armor!".format(q))
                hero.defensebonus = random.choice((0,0.1,0,0.1,0,0,0.1,0.1,0,0.1,0.1))
                hero.armors.append("{} chain armor".format(q)) 
                 
        # --- healing potion ----
        if dungeon[hero.z][hero.y][hero.x] == "h":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("a healing potion")
            hero.hp += random.randint(20,25)
        # ---- key----
        if dungeon[hero.z][hero.y][hero.x] == "k":
            dungeon[hero.z][hero.y][hero.x] = "." 
            print("oh, a key")
            hero.keys += 1
        # --- box ----
        if dungeon[hero.z][hero.y][hero.x] == "b":
            a = random.randint(1,10)
            b = random.randint(1,10)
            string_a = str(a)
            string_b = str(b)
            c = a * b
            questiontime = time.time()
            while True:
                print("you first have to resolve a matematical quiz! How much is " + string_a + " * " + string_b + "?")
                answer = input(">>>")
                try:
                    a = int(answer)
                except:
                    print("Wrong answer, this was not a number!!")
                    lostFood = random.randint(1,10)
                    hero.hunger += lostFood
                    print("Oh no...you lost {} food!".format(lostFood))
                    
                    continue
                if a == c:
                    print("correct answer")
                    if time.time() - questiontime < 5: 
                        # 5 seconds ?
                        print("correct answer fast enough, congratulations")
                        # belohnung
                        win = random.choice("fhg")
                        win1 = random.randint(10,20)
                        print("you receive {} {} !".format(win1,win))
                        if win == "f":
                            hero.food -= win1
                        if win == "h":
                            hero.hp += win1
                        if win == "g":
                            hero.gold += win1
                    else:
                        print("correct answer but too slow...") 
                        lostGold = random.randint(1,10)
                        hero.gold -= lostGold   
                        print("Oh no...you lose {} gold!".format(lostGold))
                    dungeon[hero.z][hero.y][hero.x] = "."
                    break
                else:
                    print("wrong answer...try again")
                    lostDamage = random.randint(1,10)
                    hero.hp -= lostDamage
                    print("Oh no...you lose {} hp!".format(lostDamage))
                    
    # --- game over ---
    print("*-*-*-*-*-*- Game Over -*-*-*-*-*-*-*-*")
    if hero.hunger >= 200:
        print("the next time eat more cheese!")
    if hero.hp < 1:
        print("the next time fight better!")
   
    # --- score ----
    print("you killed those monsters:")
    menge = 0
    friedhof = {}
    for m in Monster.zoo:
        if m.number == 0:
            continue
        if m.hp > 0:
            continue
        menge += 1
        if m.__class__.__name__ in friedhof:
            friedhof[m.__class__.__name__] += 1
        else:
            friedhof[m.__class__.__name__] = 1
    for name in friedhof:
        print(name, friedhof[name])
    print(" total kills: {} ".format(menge))
    if hero.happyend and not hero.hunger < 0 and not hero.hunger > 199:
            print("* - * - * - * - * - * - * - * - * - * - * ")
            print("The Princessin accept the flower and she married the hero") 
            print("You win!")
            print("* - * - * - * - * - * - * - * - * - * - * ")
if __name__ == "__main__":
    game()                
                
        
        
            
