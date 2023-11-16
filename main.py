#My first game project. Just a simple game of multiple choices, to learn how to use if/elif/else

print('''
                               |        |
                               |\      /|
                               | \____/ |
                               |  /\/\  |
                              .'___  ___`.
                             /  \|/  \|/  \\
            _.--------------( ____ __ _____)
         .-' \  -. | | | | | \ ----\/---- /
       .'\  | | / \` | | | |  `.  -'`-  .'
      /`  ` ` '/ / \ | | | | \  `------'\\
     /-  `-------.' `-----.       -----. `---.
    (  / | | | |  )/ | | | )/ | | | | | ) | | )
     `._________.'_____,,,/\_______,,,,/_,,,,/  
''')
print("Oh no! Naruto lost Fabricio, his favourite mouse toy!")
print("Your mission is to find Fabricio before the dog destroys it!") 

cabinets = input("\nLet's start checking the kitchen cabinets. Which one do you chose, left or right?\n").lower()
if cabinets == "left":
    phone = input('\nOhhh, interesting! You found a strange burning phone. Type "take" to take ir or "leave" to leave it there:\n').lower()
    if phone == "leave":
        tunnel = input("\nWell, you made the right choice. As you place the phone back and close the cabinet, the phone explodes and the whole cupboard colapses, revealing it was hiding 3 tunnels behind. Do you chose tunnel 1, 2 or 3?\n")
        if tunnel == "3":
            print("\nAs you go inside the tunnel, you see a blinking red dot. As you get closer, you start to hear a clicking noise. It is a bomb? Before you have time to start to panic, you realise the sound is coming from Fabricio: THE ULTRA BLASTER MOUSE FILLED WITH CATNIP AND INTEGRATED RED DOT. Double the fun, double the trip! You take a deep breath, relieved. You grab Fabricio and run back to your house, where Naruto is waiting for you, purring and excited to have you and Fabricio back.\nTHE END")
        elif tunnel == "1":
            print("As you go inside, you realise a strange smell. It's dark, you take another step and the floor is gone! You fall inside the sewer. Luckily the giant rats adopt you as their furless baby. Downside, you'll never see light again! GAME OVER")
        else:
            print ("As you go inside, you can feel a strong smell of pizza. Out of nowhere, you got hit on the head. The last thing you see before losing consciousness is supersized turtle, with a red band over its eyes. GAME OVER")
    else:
        print("As you grab the phone as stats to walk away, it explodes! What else would you expect of a burning phone? GAME OVER")
else:
    print("You open the cabinet and a radioactive rat jumps over you, eating your nose. You bleed to death. GAME OVER")
  