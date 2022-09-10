
unit = int(input())
bill = 0.0
if unit==0:
    bill = 30
elif unit>0 and unit <= 60 :
    if(unit <=30):
       bill = unit*2.5 + 30
    else :
        bill = 30*2.5+(unit-30)*4.85+60
else : 
    if(unit <= 90 ) :
        bill = 60*7.85+(unit-60)*10+90
    elif(unit <=120) :
        bill = 60*7.85+30*10+90+(unit-90)*27.75+480
    elif(unit <=180) :
        bill = 60*7.85+30*10+90+30*27.75+480+(unit-120)*32+480
    else :
        bill = 60*7.85+30*10+90+30*27.75+480+60*32+480+(unit-180)*45+540
        
print(bill)
        