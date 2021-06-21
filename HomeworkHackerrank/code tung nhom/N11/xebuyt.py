def solved(days):
        last_day = days[-1]
        day_set = set(days)
        days = [0] * (last_day+1)
        
        for i in range(last_day + 1):
            if i in day_set:
                if i - 7 < 0:
                    days[i] = min(days[i-1] + 2, 7, 25)
                    
                elif i - 7 > -1 and i-30 <= 0:
                    days[i] = min(days[i-1] + 2, days[i - 7] +7, 25)
                
                elif i - 30 > -1:
                    days[i] = min(days[i-1] + 2, days[i - 7] + 7, days[i - 30]+25)
            else:
                days[i] = days[i-1]
        return days[last_day]
days= [int(x) for x in input().split()]
print(solved(days))