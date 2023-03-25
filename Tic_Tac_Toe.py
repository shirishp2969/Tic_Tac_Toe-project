import random

put_x='X'
put_o='O'

return_string=(f"1  | 2  | 3\n"
              f"--------------\n"
              f"4  | 5  | 6\n"
              f"--------------\n"
              f"7  | 8  | 9")

x_place=[(1,4),(4,7),(1,7),(2,5),(5,8),(2,8),(3,6),(6,9),(3,9),(1,2),(2,3),(1,3),(4,5),(5,6),(4,6),(7,8),(8,9),(7,9),
         (1,5),(5,9),(1,9),(3,5),(5,7),(3,7)]
x_win_positions=[(1,4,7),(2,5,8),(3,6,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7)]
x_positions=[]
o_win_positions=[(1,4,7),(2,5,8),(3,6,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7)]
o_positions=[]
rem_positions=[1,2,3,4,5,6,7,8,9]
win=False
q=5

def predict_o(x_place,x_positions,x_win_positions):
    for place in x_place:
        p = 0
        for i in place:
            for position in x_positions:
                if i==position:
                    p+=1
        if p==2:
            for j in x_win_positions:
                my_result=set(place).issubset(j)
                if my_result==True:
                    x_win_list=list(j)
                    x_place_list=list(place)
                    for number in x_win_list:
                        if number not in x_place_list:
                                return number
            # print("satisfied")

def check_winning(x_win_positions,x_positions,o_win_positions,o_positions):
    for position in x_win_positions:
        x_win_prob = 0
        for number in position:
            if number in x_positions:
                x_win_prob+=1
            if x_win_prob==3:
                print("X Win")
                return True

def check_winning_o(x_win_positions,x_positions,o_win_positions,o_positions):
    for position in o_win_positions:
        o_win_prob = 0
        for number in position:
            if number in o_positions:
                o_win_prob+=1
            if o_win_prob==3:
                print("O Win")
                return True

def put_position_x(user_input,put,return_string):
    if user_input==1:
        x_positions.append(1)
        return return_string.replace('1',put)
    elif user_input==2:
        x_positions.append(2)
        return return_string.replace('2', put)
    elif user_input==3:
        x_positions.append(3)
        return return_string.replace('3', put)
    elif user_input==4:
        x_positions.append(4)
        return return_string.replace('4', put)
    elif user_input==5:
        x_positions.append(5)
        return return_string.replace('5', put)
    elif user_input==6:
        x_positions.append(6)
        return return_string.replace('6', put)
    elif user_input==7:
        x_positions.append(7)
        return return_string.replace('7', put)
    elif user_input==8:
        x_positions.append(8)
        return return_string.replace('8', put)
    elif user_input==9:
        x_positions.append(9)
        return return_string.replace('9', put)

def put_position_o(user_input,put,return_string):
    if user_input==1:
        o_positions.append(1)
        return return_string.replace('1',put)
    elif user_input==2:
        o_positions.append(2)
        return return_string.replace('2', put)
    elif user_input==3:
        o_positions.append(3)
        return return_string.replace('3', put)
    elif user_input==4:
        o_positions.append(4)
        return return_string.replace('4', put)
    elif user_input==5:
        o_positions.append(5)
        return return_string.replace('5', put)
    elif user_input==6:
        o_positions.append(6)
        return return_string.replace('6', put)
    elif user_input==7:
        o_positions.append(7)
        return return_string.replace('7', put)
    elif user_input==8:
        o_positions.append(8)
        return return_string.replace('8', put)
    elif user_input==9:
        o_positions.append(9)
        return return_string.replace('9', put)

is_game=True
while is_game==True:
    print(f"{return_string}\n")
    user_input=int(input("Where do you want to put X : \n"))
    rem_positions.remove(user_input)
    return_string=put_position_x(user_input,put_x,return_string)
    print(f"{return_string}\n")
    Win=check_winning(x_win_positions, x_positions, o_win_positions, o_positions)
    if Win==True:
        is_game=False
    elif len(rem_positions)==0:
        print("DRAW\n")
        is_game = False
    else:
        next_o=predict_o(x_place,x_positions,x_win_positions)
        #print(next_o)
        if next_o and next_o in rem_positions:
            # user_input = int(input("Where do you want to put O : "))
            return_string = put_position_o(next_o, put_o, return_string)
            Win = check_winning_o(x_win_positions, x_positions, o_win_positions, o_positions)
            rem_positions.remove(next_o)
            print(f"{return_string}\n")
            #print(o_positions)
            if Win == True:
                is_game = False

        else:
            next_o_random=random.choice(rem_positions)
            return_string = put_position_o(next_o_random, put_o, return_string)
            rem_positions.remove(next_o_random)
            print(f"{return_string}\n")
            Win = check_winning_o(x_win_positions, x_positions, o_win_positions, o_positions)
            if Win == True:
                is_game = False
    if len(rem_positions)==0:
        print("DRAW\n")
        is_game = False

        q-=1
    #print(rem_positions)

