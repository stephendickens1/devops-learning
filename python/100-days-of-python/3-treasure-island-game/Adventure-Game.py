import time
import os
import sys

foghorn = 0
carjack = 0

def threedots():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

def manydots():
    for i in range(3):
        threedots()

def weaponselection():
    weapon = input().lower()
    if weapon == "a":
        global foghorn
        foghorn += 1
        typewriter_effect("You have taken the foghorn. This could be useful for scaring animals away")
    else:
        global carjack
        carjack += 1
        typewriter_effect("You've taken the carjack. It can be swung with force and lift things")
    manydots()

def typewriter_effect(text):
    delay=0.1
    for char in text:
        print(char, end='', flush=True)  # Use flush=True to immediately display the character
        time.sleep(delay)
    print()

def crocodile():
    typewriter_effect("""
                         _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
             ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~     
          
          """)
    
def death():
    typewriter_effect("YOU HAVE DIED")
    time.sleep(2)
    typewriter_effect("""
    ...----....
                         ..-:"''         ''"-..
                      .-'                      '-.
                    .'              .     .       '.
                  .'   .          .    .      .    .''.
                .'  .    .       .   .   .     .   . ..:.
              .' .   . .  .       .   .   ..  .   . ....::.
             ..   .   .      .  .    .     .  ..  . ....:IA.
            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM      
            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
                ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
                 "::....::.:::..:..::IIIIIHHHHMMMHHMV"
                   "::.::.. .. .  ...:::IIHHMMMMHMV"
                     "V::... . .I::IHHMMV"'
                       '"VHVHHHAHHHHMMV:"'
                      
                      GAME OVER GAME OVER GAME OVER
                      
                      """)
print("""
    
                    .--------------------------------------------.
           ( WELCOME TO RHINO HUNT! CAN YOU FIND THE RHINO? )
          //'--------------------------------------------'
         /      , _.-~~-.__            __.,----.
      (';    __( )         ~~~'--..--~~         '.
(    . \"..-'  ')|                     .       \  '.
 \\. |\.'                    ;       .  ;       ;   ;
  \ \'"   /9)                 '       .  ;           ;
   ; )           )    (        '       .  ;     '    .
    )    _  __.-'-._   ;       '       . ,     /\    ;
    '-'"'--'      ; "-. '.    '            _.-(  ".  (
                  ;    \,)    )--,..----';'    >  ;   .
                   \   ( |   /           (    /   .   ;
     ,   ,          )  | ; .(      .    , )  /     \  ;
,;'-PjP;.';.-.;._,;/;,;)/;.;.);.;,,;,;,,;/;;,),;.,/,;.).,;,

""")

typewriter_effect("Hello adventurer. What is your name?\n")

name = input()

while True:
    typewriter_effect(f"Are you ready to hunt for Rhinos {name}? Type Y and hit enter to begin. Type anything else to walk away...\n")
    
    ready = input().lower()

    if ready == "y":
        break
    else:
        typewriter_effect(f"What brought you here {name}?")
        threedots()
        time.sleep(1)
        typewriter_effect(f"\nYou came here for a reason")
        threedots()
        time.sleep(1)
        print("\n")

typewriter_effect(f"You have always felt it {name}...")
time.sleep(3)
typewriter_effect("Your whole life has led up to this moment...")
time.sleep(3)
typewriter_effect("Let's go looking for some Rhinos")
time.sleep(3)

typewriter_effect("""\n\n\nYou enter a clearing. The first signs of life after 30 minutes of driving.
You exit the Jeep, painted with the dirt of the sahara. Your boots 
thud against what was once soil, pushing clouds of sand into the air.""")

typewriter_effect("TIME TO PREPARE")
manydots()
typewriter_effect("""You should take something useful with you. You can carry one item.
A - A loud foghorn
or
B - A car jack.
Type "A" or "B" to select""")

weaponselection()

typewriter_effect("""The dust settles. Your eyes adjust to the sun. You see two things of note:""")

manydots()

typewriter_effect("""A - To your left is a trail, sloping downwards. The dust turns to mud, the path becoming uncharacteristcally
damp. The paths swirls behind a large rock, alluding to a watering hole being behind it.""")

manydots()

typewriter_effect("""B - To your right, bushes. You can't see anything behind them, but you see plumes of dust
billowing high into the air from behind them""")

manydots()

typewriter_effect("""Which path do you take? A or B?""")

firstchoice = input().lower()

if firstchoice == "a":
    typewriter_effect("""You follow mud, squelching boots giving you away. But nothing scurries away as you progress behind the rock.
    You press your body against the boulder, leaning hard as you peak behind it.
    A watering hole...with no rhinos. But you are not alone. IT'S A CROCODILE WEARING THOSE EAR
    DEFENDERS PEOPLE ON CONSTRUCTION SITES WEAR!""")
    crocodile()
    manydots()
    typewriter_effect("The ear defender wearing crocodile attacks!")
    manydots()
    if foghorn == 1:
        typewriter_effect("""You grab your trusty foghorn to scare the crocodile away.
    But his paranoia for loud noises has prepared him well, your foghorn has no effect against
    his well defended ears""")
        death()
        sys.exit
    else:
        typewriter_effect("""You ignore the fact a crocodile has ear defenders on. As he lunges toward
        you, you slip your trusty car jack into his mouth. He bites down and...nothing! Saved
        by the car jack!""")
else:
    typewriter_effect("""Yeah there are rhinos behind that's it you win very good.""")
