while True:
    import random
    class Two_cards:

        def __init__(self,name):
            self.name = name
            self.card_list = []
            self.one_card = random.randint(0,10)
            self.two_card = random.randint(0,10)
            self.card_list.append(self.one_card)
            self.card_list.append(self.two_card)

        def draw(self):
            self.draw_card = random.randint(0,10)
            self.card_list.append(self.draw_card)


        def display(self):
            print("Card one is ", self.card_list)
            
        def total_dis(self):
            self.total = sum(self.card_list)
            print("your point of ", self.name, " is ",self.total )

    #This is the player one
    p1 = Two_cards("player one ")
    p1.total_dis()
    p1draw_count = 0
    while p1.total < 21 and p1draw_count <6:
        think = input("are u draw y / n ==> ")
        if think == "y":
            p1.draw()
            p1.total_dis()
            p1draw_count += 1
            if p1.total >= 21:
                break
        else:
            break

    #This is the player two
    p2 = Two_cards("player two ")
    p2.total_dis()
    p2draw_count = 0
    while p2.total < 21 and p2draw_count < 6:
        think = input("are u draw y / n ==> ")
        if think == "y":
            p2.draw()
            p2.total_dis()
            p2draw_count += 1
            if p2.total >= 21:
                break
        else:
            break

    #This is the competation
    if p1.total <=21 and p2.total <= 21:
        if p1.total > p2.total:
            print("player one win")
        elif p1.total == p2.total:
            print("Draw, no one win")
        else:
            print("player two win")
    elif p1.total > 21 and p2.total > 21:
        if p1.total > p2.total:
            print("Player two win")
        else:
            print("Player one win")
    else:
        if p1.total > 21 and p2.total < 21:
            print("player two win")
        else:
            pass
        if p1.total<21 and p2.total > 21:
            print("player one win")


    exit = input("Are you want to play again? y/n ==>")
    if exit == "y":
        continue
    elif exit == "n":
        break
    else:
        print("error")
        break