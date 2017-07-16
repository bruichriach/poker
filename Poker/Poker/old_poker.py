def input_command(message,hand_size):
    global main_loop
    global hand_loop
    input = raw_input(message)
    if input == "xx":
        main_loop = False
        hand_loop = False
        return input
    elif input == "x":
        hand_loop = False
        return input
    else:
        if (2*(len(input)/2)==len(input)):
            if (len(input) == 2*hand_size):
                input=camel_case(input)
                if valid_cards(input):
                    print "Valid Hand:", input
                    return input
                else:
                    print "Invalid Hand"
                    return input_command(message,hand_size)
            else:
                print "Wrong number of cards"
                return input_command(message,hand_size)
        else:
            print "Invalid Input"
            return input_command(message,hand_size)
        
def camel_case(message):
    new_message=""
    for a in xrange(0,len(message),2):
        new_message += message[a].upper()
        new_message += message[a+1].lower()
    return new_message
        
        
def valid_cards(hand):
    if (2*(len(hand)/2)==len(hand)):
        for a in xrange(0,len(hand),2):
            for b in xrange(0,a,2):
                if (hand[a:a+2] == hand[b:b+2]):
                    return False
            for b in range(0,4):
                if (hand[a+1] == suits[b]):
                    break
                if (b == 3):
                    return False
            for b in range(0,13):
                if (hand[a] == ranks[b]):
                    break
                if (b == 12):
                    return False
        return True
    else:
        return False
        

def catagorise_hand(hand):
    if (len(hand) == 4 and valid_cards(hand)):
        if (hand[0] == hand[2]):
            return hand[0] + hand[2]
        else:
            first = ranks.index(hand[0])
            second = ranks.index(hand[2])
            if (first > second):
                rank_sort = hand[2] + hand[0]
            else:
                rank_sort = hand[0] + hand[2]
            if (hand[1] == hand[3]):
                return rank_sort + "s"
            else:
                return rank_sort + "o"
    else:
        print "not a valid hand"

print "'xx' closes the program. 'x' restarts hand."
ranks = "AKQJT98765432"
suits = "hcds"
main_loop = True
while main_loop:
    hand_loop = True
    player_hand = input_command("Input the player hand: ",2)
    while hand_loop:
        print player_hand, catagorise_hand(player_hand)
        table_cards = input_command("Input the table cards: ",5)
        if not (hand_loop):
            break
        print "here"
        player_hand = input_command("Input the player hand: ",2)
