import sys;
import json;

def Width_Fun(pinnacle_odds1, pinnacle_odds2,fair_pct1_point,fair_pct2_point,fair_odds_dec1,fair_odds_dec2, Pick, SBook_Odds):
	
	if  pinnacle_odds1 < 1 and pinnacle_odds2 < 1 :
		width = abs(pinnacle_odds1) + abs(pinnacle_odds2) - 200 
		print("Width : ",width)
		print("")

	elif pinnacle_odds1 < 1 and pinnacle_odds2 > 1 :
		width = abs(pinnacle_odds1) - pinnacle_odds2 
		print("Width : ",width)
		print("")

	elif pinnacle_odds1 > 1 and pinnacle_odds2 < 1 :
		width = abs(pinnacle_odds2) - pinnacle_odds1 
		print("Width : ",width)
		print("")
	else:
		width = 0
		
	#Just passing parameter fair odds in decimal
	fair_odds_dec1 = fair_odds_dec1
	fair_odds_dec2 = fair_odds_dec2


	return final_Output(fair_pct1_point,fair_pct2_point,Pick,SBook_Odds,width,fair_odds_dec1,fair_odds_dec2)
	
#Calc Ev Percentage

def Calc_EV_Pct(decimal_SB_odds,fair_pct):    
	
	wager_dec = abs(round(1-(decimal_SB_odds),2))
	EV_pct =  round((fair_pct * (100*wager_dec)) - ( (1-fair_pct) * 100),2)
	return EV_pct


def final_Output(fair_pct1_point,fair_pct2_point, Pick_Side,SBook_Odds,width,fair_odds_dec1,fair_odds_dec2):

	result = ""

	if width < 24 :
		Kelly_Size = 0.25
	elif width < 30 :
		Kelly_Size = 0.2
	elif width < 34 :
		Kelly_Size = 0.15
	elif width < 39 :
		Kelly_Size = 0.1
	else :
		Kelly_Size = 0.07
		

	#Sportbook Decimal Conversion
	if SBook_Odds < 1:
		decimal_SB_odds = round((100/abs(SBook_Odds)) + 1,2)
	else:
		decimal_SB_odds = round((SBook_Odds/100) + 1,2)
		
	Bet_Unit = 20
	
	if Pick_Side == 1:
		EV_PCT_Odds1 = ((decimal_SB_odds - 1) * fair_pct1_point - (1 - fair_pct1_point)) / (decimal_SB_odds - 1)
		Bet_Amt = round(EV_PCT_Odds1*100*Kelly_Size*Bet_Unit,1)
		
		EV_Pct = Calc_EV_Pct(decimal_SB_odds,fair_pct1_point)
		
		if EV_Pct > 6.99 and width > 38 :
				result += "Too much Width but Nice Value,"
				result += "Kelly Size: " + str(Kelly_Size) + ','
				result += "EV Percentage: " + str(EV_Pct) + '%,'
				result += "Bet Amount $: " + str(Bet_Amt) + ','
		elif EV_Pct > 2.24 and width < 39 :
				result += "Kelly Size: " + str(Kelly_Size) + ','
				result += "EV Percentage: " + str(EV_Pct) + '%,'
				result += "Bet Amount $: " + str(Bet_Amt) + ','
		else:
				result += "Not Optimal Bet" + ','
				
			
	elif Pick_Side == 2:
		EV_PCT_Odds2 = ((decimal_SB_odds - 1) * fair_pct2_point - (1 - fair_pct2_point)) / (decimal_SB_odds - 1) 
		Bet_Amt = round(EV_PCT_Odds2*100*Kelly_Size*Bet_Unit,1)
		
		EV_Pct = Calc_EV_Pct(decimal_SB_odds,fair_pct2_point)
		
		if EV_Pct > 6.99 and width > 38 :
			result += "Too much Width but Nice Value,"
			result += "Kelly Size: " + str(Kelly_Size)+ ','
			result += "EV Percentage: " + str(EV_Pct) + '%,'
			result += "Bet Amount $: " + str(Bet_Amt)+ ','
			
		elif EV_Pct > 2.24 and width < 39 :
			result += "Kelly Size: " + str(Kelly_Size)+ ','
			result += "EV Percentage: " + str(EV_Pct) + '%,'
			result += "Bet Amount $: " + str(Bet_Amt)+ ','
		
		else:
			result += "Not Optimal Bet,"
		
	else:
		result += "Wrong Input Sir!,"

	return result

def no_vig_odds(pinnacle_odds1, pinnacle_odds2, pick="no", book="no"):

	# Implied Percentage of Input Pinnacle Odds 

	if pinnacle_odds1 < 100 :
		implied_pct1 = round(abs(pinnacle_odds1)/(abs(pinnacle_odds1)+100) * 100,2)

	else :
		implied_pct1 = round(100/(abs(pinnacle_odds1)+100)*100,2) 

	if pinnacle_odds2 < 100 :
		implied_pct2 = round(abs(pinnacle_odds2)/(abs(pinnacle_odds2)+100) * 100,2)

	else :
		implied_pct2 = round(100/(abs(pinnacle_odds2)+100)*100,2)    

	fair_pct1 =  round( 100 * (implied_pct1 / (implied_pct1 + implied_pct2)),2)
	fair_pct2 =  round( 100 * (implied_pct2 / (implied_pct1 + implied_pct2)),2)
	
	#Converting them in Final Pct%
	fair_pct1_point = round(fair_pct1/100,4)
	fair_pct2_point = round(fair_pct2/100,4)

	#Converting to Decimal
	fair_odds_dec1 = round(1/fair_pct1_point,2)
	fair_odds_dec2 = round(1/fair_pct2_point,2)

	if fair_odds_dec1 >= 2:
		Fair_Amer_Odds_1 = (fair_odds_dec1 - 1) * 100
	else :
		Fair_Amer_Odds_1 = (-100)/(fair_odds_dec1 -1)
	if fair_odds_dec2 >= 2:
		Fair_Amer_Odds_2 = (fair_odds_dec2 - 1) * 100
	else :
		Fair_Amer_Odds_2 = (-100)/(fair_odds_dec2 -1)

	if pick == "no":
		return str(round(Fair_Amer_Odds_1)) + "," + str(round(Fair_Amer_Odds_2))
	else: return Width_Fun(pinnacle_odds1, pinnacle_odds2,fair_pct1_point,fair_pct2_point,fair_odds_dec1,fair_odds_dec2, pick, book)


strr = sys.argv[1]
# strr = "phase-2,100,200,1,5"
dataFromPHP = strr.split(',')
if dataFromPHP[0] == 'phase-1':
	result = no_vig_odds(float(dataFromPHP[1]),float(dataFromPHP[2]))
	print(result)
elif dataFromPHP[0] == 'phase-2':
	result = no_vig_odds(float(dataFromPHP[1]),float(dataFromPHP[2]), float(dataFromPHP[3]), float(dataFromPHP[4]))
	print(result)