def tree(spacer=' ', star='*', lines=16, count = 16, count1 = 1):
    for i in range(lines):
        print(spacer * count, star * (count1)*2)
        count -= 1
        count1 += 1
    print("M e r r y   C h r i s t m a s  2  u")
    
print("This is Fesh's surprise Xmas Trivia Script! \nPlease choose your proferred sign: % or *")
sign = input(">>> ")

if sign == '*':
    tree(star=sign)
elif sign == '%':
    tree(star=sign)
else:
    print("That was neither * nor % but Fesh thinks you'll love '*'")
    tree()