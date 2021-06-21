days = input().split()
days = list(map(int,days))

def shouldBuy7(day_start,days):
    if len(days) <= 3:
        return [False,-1] 
    limit = day_start + 6
    count = 0;
    for i in range(len(days)):
        if days[i] <= limit:
            count+=1
        else:
            if count*2 >= 7:
                return [True,count]
            return [False,-1]
    if count*2 >= 7:
        return [True,count]
    return [False,-1]
def shouldBuy30(day_start,days):
    if len(days) <= 12:
        return [False,-1] 
    limit = day_start + 29
    count = 0;
    for i in range(len(days)):
        if days[i] <= limit:
            count+=1
        else:
            if count*2 >= 25:
                return [True,count]
            return [False,-1]
    if count*2 >= 25:
            return [True,count]
    return [False,-1]
def minPrice(days):
    price = 0
    i = 0
    while i < len(days):
        [buy30,index30] = shouldBuy30(days[i],days[i:])
        [buy7,index7] = shouldBuy7(days[i],days[i:])
        if buy30:
            i += index30
            price += 25
        elif buy7:
                i+=index7
                price+=7
        else:
            price+=2
            i+=1
    return price
print(minPrice(days))