#숫자 야구 게임

randnum=0 #최종 숫자
a=0 #백의 자리 숫자
b=0 #십의 자리 숫자
c=0 #일의 자리 숫자
num_set={a,b,c} #사용된 숫자

def random_number():
    import random
    global randnum
    global a
    global b
    global c
    global num_set

    numbers=[0,1,2,3,4,5,6,7,8,9]

    while (a==0): #0이 될 수 없음
        a=random.choice(numbers)
    numbers.remove(a)

    b=random.choice(numbers)
    numbers.remove(b)

    c=random.choice(numbers)

    num_set={a,b,c}

    randnum=100*a+10*b+c 

    #print(randnum)

def answer_check():
    chance=9 #9번의 기회가 주어짐
    global num_set
    global a
    global b
    global c

    while (chance!=0):
    #사용자 답
        answer=int(input("숫자 입력:"))
        user_a=int(answer/100)
        user_b=int((answer%100)/10)
        user_c=int((answer%100)%10)
        user_num_set={user_a,user_b,user_c}
        
        #print(num_set)
        #print(user_num_set)
        
        if answer==randnum: #숫자와 그 위치가 모두 일치
            print(f"3 STRIKE! 축하합니다! (시도 횟수:{10-chance})")
            break;
        else: #숫자와 위치가 모두 다름
            chance-=1
            if len(num_set & user_num_set)==0:
                print("OUT!")
            elif len(num_set & user_num_set)==1:
                if (a==user_a) or (b==user_b) or (c==user_c):
                    print("1 STRIKE!")
                else:
                    print("1 BALL!")
            elif len(num_set & user_num_set)==2:
                if ((a==user_a) and (b==user_b)) or ((a==user_a) and (c==user_c)) or ((c==user_c) and (b==user_b)):
                    print("2 STRIKE!")
                elif (a==user_a) or (b==user_b) or (c==user_c):
                    print("1 BALL, 1 STRIKE!")
                else:
                    print("2 BALL!")
            elif len(num_set & user_num_set)==3:
                if (a==user_a) or (b==user_b) or (c==user_c):
                    print("2 BALL, 1 STRIKE!")
                else:
                    print("3BALL!")
    if chance==0:
        print("주어진 기회가 모두 소진되었습니다.")

def baseball():
    random_number()
    answer_check()

start=input("숫자야구를 시작하려면 'Enter'\n")
if start=="":
    baseball()


    

