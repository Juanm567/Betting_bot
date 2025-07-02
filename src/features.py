#use the clean data so we can use it to run calculations
whole_yes_no = input("Would you like the entire logs for every nba player - Type [YES/NO] ") 
whole_yes_no.lower()

if whole_yes_no == 'YES':
    import preprocess
    preprocess.entire_logs()
