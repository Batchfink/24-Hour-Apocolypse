import os
import random
import Player
import Weapons
from Utils import *

class ArmyBase:
    ZOMBIES = 10        # This will be the amount of enemies in an area for the player to clear out
                        #No idea how that will work... HOLY CRAP THAT'S A LOT OF DEM ZOMBZ THO
                        #You could do it so that they can choose where to go, but the better areas require
                        #more zombies to be killed
    def ArmyBase1(player):
        os.system("cls")
        q("After a long period of walking down an empty, desolate road you stumble across a desolate army base.", 0.02, player)
        input()
        os.system("cls")
        q("You peer around some of the corners, inspecting to see some zombies, but you don't.", 0.02, player)
        input()
        os.system("cls")
        q("\"Hello?\" You shout, but to no avail. No answer.", 0.02, player)
        input()
        os.system("cls")
        q("You open the rusty gate and walk towards a cylindrically shaped building.", 0.02, player)
        input()
        os.system("cls")
        q("\"Weapons?\" For whatever reason you said that out loud.", 0.02, player)
        input()
        os.system("cls")
        q("\"Don't... move...\"", 0.06)
        input()
        os.system("cls")
        q("\"I'm not... I'm not...\"", 0.02, player)
        input()
        os.system("cls")
        q("\"Drop your weapon.\"", 0.02, player)
        input()
        os.system("cls")
        q("You drop your " + player.weapon + ".", 0.02, player)
        player.weapon = Weapons.Fist()
        input()
        os.system("cls")
        q("\"Good. Now. Come here.\"", 0.02, player)
        input()
        os.system("cls")
        ans = input("Now's your chance. Attack or leave it? (a/l) ")
        if ans.lower() == "a":
            os.system("color 0c")
            os.system("cls")
            print ("You grab the weapon pointed at your head and bring it to the side, providing a straight punch to the face.")
            input()
            os.system("cls")
            player.health -= 5
            print ("You take a swipe to the leg, but an upper cut to the bowel finishes them off.")
            input()
            os.system("cls")
            q("\"Just... kill me.\"", 0.1)
            input()
            os.system("cls")
            q("\"No, I don't kill people. I just need food and weapons, then I'll be on my way.\"", 0.02, player)
            input()
            os.system("cls")
            q("\"Here, there's loads of guns in the back.\"", 0.02, player)
            input()
            os.system("cls")
            q("You're given a key to a door around the side. You help them up and proceed to walk towards the door.", 0.02, player)
            input()
            os.system("cls")
            q("\"What's your name by the way? We could do with a fighter like you in our group.\"", 0.02, player)
            input()
            os.system("cls")
            q("\"" + player.name + ". I ain't looking to join any groups though.\"", 0.02, player)
            input()
            os.system("cls")
            name = generateName()
            q("\"Shame. My name is " + name + ". We're low on food anyway, but you can take some of our emergency supplies, especially if you are going to be going back out there. No one here even knows how long this crap's been going on for, days, weeks, or even months.\"", 0.02, player)
            input()
            os.system("cls")
            q("\"So what kind of weapons do you have here?\"", 0.02, player)
            input()
            os.system("cls")
            q("\"Well, we have mainly guns, but we do have some larger tools as well.\"", 0.02, player)
            input()
            os.system("cls")
            q("\"Good.\"", 0.02, player)
            input()
            os.system("cls")
            q("Upon entering this room of weapons", 0.02, player)

