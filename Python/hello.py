def bmi(h, w = False, j = False):
    
    s_weight = round(22*(h/100)**2, 2)
    x = round(w/((h/100)**2), 2)
    
    if x < 16:
        advice_w = "痩せすぎです"
        
    elif 16 <= x < 17:
        advice_w = "痩せています"
        
    elif 17 <= x < 18.5:
        advice_w = "痩せ気味です"
        
    elif 18.5 <= x < 25:
        advice_w = "普通体重です"
        
    elif 25 <= x < 30:
        advice_w = "前肥満です"
        
    elif 30 <= x < 35:
        advice_w = "肥満（1度）です"
        
    elif 35 <= x < 40:
        advice_w = "肥満（2度）です"
        
    else:
        advice_w = "肥満（3度）です"
    
    if x < 18.5:
        advice_j = "低体重です"
        
    elif 18.5 <= x < 25:
        advice_j = "普通体重です"
        
    elif 25 <= x < 30:
        advice_j = "肥満（１度）です"
        
    elif 30 <= x < 35:     
        advice_j = "肥満（2度）です"
        
    elif 35 <= x < 40:
        advice_j = "肥満（3度）です"
        
    elif x > 40:
        advice_j = "肥満です"
    
    if w == False:
        return s_weight
    
    elif j == True:
        return x, s_weight, advice_j
    
    else:
        return x, s_weight, advice_w

sample_1 = bmi(170, 60)
sample_2 = bmi(175, 65, True)
sample_3 = bmi(180)

print(sample_1)
print(sample_2)
print(sample_3)