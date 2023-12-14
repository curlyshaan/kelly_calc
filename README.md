API Docs : https://www.prop-odds.com/features

I believe using API, with one call, you can get all markets for each game_id

Core Concept and Logic : 
1. Lets start with NFL League
2. Get all Upcoming Games
3. Each game will have multiple Markets ( meaning Moneyline, UnderOver etc refer API Doc for more info)
4. Filter All Markets for each game_id which has bookie_key = 'pinnacle' and ( bookie_key = 'fanduel' and/or bookie_key = 'draftkings' )
5. I only want markets with abv conditions, do not care about other bookie_keys
6. Each market will have market_key, for every market_key, there is outcome key, then do, group by name, description, handicap, odds, max(timestamp).
7. Using the above logic, i want one row of data, i.e latest timestamp record of the group by
8. Output should be in Dataframe for each game ( we can discuss later ) 

Sample JSON data 

game_id = d8d2109c0b170ae7ad28557f818ed5b4

market = spread

API_Link 
https://api.prop-odds.com/beta/odds/d8d2109c0b170ae7ad28557f818ed5b4/spread?api_key=ZkcWPqt4RjHzatSAgz2dPh3ogeXvmLrgArPxIhPCFE
