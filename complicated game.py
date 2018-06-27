
print ("You find yourself trapped alone on an island")

print()

print("You must escape and find supplies in order to escape before it is too late")

print()

print ("You have nothing but a map and must decide where to explore before it reaches dark...")


commands = ["North","South","East","West","Get","Use"]

print ( "You are coordinates 1,1 on your map.")

print()

print ("Which direction would you like to go?")


X, Y = 8, 8;
Matrix = [[0 for x in range(X)] for y in range(X)]

Matrix[1][1] = "You are at Sea"

Matrix[1][2] = "You reach a secret compound that requires a key... You must explore more."

Matrix[2][1] = "Another endless piece of grassland, hurry as daylight it running out."

Matrix[2][2] = "You have reached the coast and see a petrifying monster and realise that you must run."                    

Matrix[3][2] = "You sigh of relief as you have discovered food, however you see something awful approaching and must run"

Matrix[3][3] = "You look over a cliff and see a huge and terrifying monster approaching, you need to run."

Matrix[2][3] = "You find a shimmering key and realise that it is your way home, it then goes pitch black, the monster got you..."

Matrix[4][2] = "You reach for a bronze key and then everything goes black- the creature hit you..."

Matrix[2][4] = "You reach for a silver key, it goes black- the monster got to you..."

Matrix[5][5] = "The monster spots you as you step on a twig accidently- now what?!"

Matrix[5][3] = "Your leg steps on its tail and its eyes open"

Matrix[2][5] = "You're sprinting away but as you run you feel like something is watching you from the trees"

Matrix[5][2] = "It screeches as you have realised that you have only angered it further, you sprint away only to feel as if something is watching you from the trees"

Matrix[2][6] = "Oh no, you realise that the fire you started has created a way for the monster to find you!"

Matrix[6][2] = "The fire is big and smoke rises and then it hits you- it's a way for the creature to find you"

Matrix[2][7] = "As you follow the footprints, you realise that it was a trap as you fall into a bear trap- now what you wonder as you hear the creature approaching"

Matrix[7][2] = "You step into a bear trap and are stuck with a look of horror on your face as you hear the creature approaching"

Matrix[3][7] = "Game over"

Matrix[7][3] = "Game over"


choice1 = int( input ("Should you 1 - Go north? 2 - Go east?"))

if choice1 == 1:
    
    print (Matrix[1][2])

       
elif choice1 == 2:

    print (Matrix[2][1])

print ("Where to now?")

choice2 = int( input ("Should you 1 - Go north? 2 -Go east? 3 -Go west?"))
               
               
if choice2 == 1:

    print(Matrix[2][2])
               
               
elif choice2 == 2:

    print(Matrix[3][2])
               
else:
    print(Matrix[3][3])


print (" You need to decide now where to go next!")

choice3 = int( input ("Run 1- north 2- east 3- west"))
               
if choice3 == 1:

    print(Matrix[2][3])
    
elif choice3 ==2:

    print(Matrix[4][2])

else:

    print(Matrix[2][4])

print()

print("You wake up to find yourself on the muddy floor in a cave with a shadow looming above you")

print()

print("What should you do. Choose carefully as it could lead to game over...")

print()

choice4 = int(input ("You can either 1- explore the light to the left of you 2- Tip toe over the monster's body as it sleeps"))

if choice4 == 1:

    print(Matrix[5][5])

else:

    print(Matrix[5][3])

print("The sun is setting and you must run in any direction. Make the wrong choice and you won't have enough supplies to survive...")


print()

print("It slowly creeps towards you and you take a deep breathe in")

choice5 = int(input("You can either 1- Run! or 2- Hit it with a sharp pebble that is on the floor next to you"))

if choice5 == 1:

    print(Matrix[2][5])

else:

    print(Matrix[5][2])

print()

choice6 = int(input ("You find shelter and start a fire to cook 1- Fish or 2- Coconut"))

if choice6 == 1:

    print(Matrix[2][6])

else:

    print(Matrix[6][2])

print()

print("You need to run, however you are tired and want to confront the monster")

print()

print("You decide to kill the beast.")

print()

choice7 = int(input ("Should you 1- Follow the beast's large footprints? 2- Follow the trail back to the cave you ran away from"))

if choice7 == 1:

    print(Matrix[2][7])

else:

    print(Matrix[7][2])

print()

print("You have to make a decision")

choice8 = int(input ("Should you 1- Look like bait and kill the beast when it thinks you are unconcious or 2- Cute yourself loose and hide behind a tree,ready to kill the creature"))

if choice8 ==1:
    

    print(Matrix[3][7])

else:
    
    print(Matrix[7][3])

print()

print("Your plan failed, it turns out that you were right. There was something in the trees there was a herd of creatures that you couldn't escape...")


    




              



              







    

              



    
        


               

               
               
               

    

       





