print("Type Your Bank USSD CODE: ")

Banks = {'*901#' : 'Access Bank',
         '*894#' : 'First Bank',
         '*826#' : 'Union Bank',
         '*919#' : 'UBA Bank',
         '*737#' : 'GT Bank', 
         '*966#' : 'Zenith Bank\n'}
for key in Banks:
    print(key,'::',Banks[key])
Bank_Options = input("Select an option: ")

if Bank_Options in Banks.keys():
    print("You Have Selected",Banks[Bank_Options])
    
    if Bank_Options == '*966#':
        zenith_services = {'1': 'Check Account Balance',
                    '2': 'Bank Transfer',
                    '3': 'Airtime Transfer',
                    '4': 'Check Balance'}
        for key in zenith_services:
            print(key,zenith_services[key])
            
    if Bank_Options == '*894#':
        first_services = {'1': 'Quick Banking',
                    '2': 'Open an accounts',
                    '3': 'Loans',
                    '4': 'First Monie'}
        for key in first_services:
            print(key,first_services[key])
        quick = input("Select an option: ")
        if quick == '1':
            q_bank = {'1' : 'Transfers',
                      '2' : 'Airtime Self',
                      '3' : 'Airtime Others',
                      '4' : 'Enquiry Services',
                      '5' : 'Data',
                      '6' : 'Pay Bills',
                      '7' : 'Insurance',
                      '8' : 'other services',
                      '9' : 'Merchant Services',
                      '10' : 'Card Control',
                      '11' : 'Reserve Cash\n'}
            for key in q_bank:
                print(key, q_bank[key])
            trans = input('Select an option: ')
            if trans == '1':
                bank_trans = {'1' : 'Access Bank',
                              '2' : 'GT Bank',
                              '3' : 'Skye Bank',
                              '4' : 'First Bank',
                              '5' : 'Fidelity Bank',
                              '6' : 'Diamond Access',
                              '7' : 'FCMB',
                              '8' : 'UBA',
                              '9' : 'Wema Bank',
                              '10': 'Key Stone Bank',
                              '11': 'Zenith Bank\n'}
                for key in bank_trans:
                    print(key,bank_trans[key])
                bank_trans_option = input('Select Bank: ')
                if bank_trans_option in bank_trans:
                    transf = input('Enter Amount: ')
                    tran_sf = input('Enter Account Number: ')
                    trans_pin = input('Enter Your Pin: ')
                    if trans_pin != '2121':
                        print("invalid pin")
                    else:
                        print('Transaction SuccessFull')
                else:
                    print('Invalid Option')
            
            elif trans == '2':
                airtime = input('Enter amount: ')
                air_pin = input('Enter pin to confirm: ')
                if air_pin != '2121':
                    print('Invalid Code')
                else:
                    print('Transaction Successful!')
            else:
                print('Invalid Option Selected')
            
            elif trans == '3':
                airtime_other = input('Enter Phone Number: ')
                
            
    if Bank_Options == '*919#':
        uba_services = {'1': 'Check Account Balance',
                    '2': 'Bank Transfer',
                    '3': 'Airtime Transfer',
                    '4': 'Check Balance'}
        for key in uba_services:
            print(key,uba_services[key])
            
        if Bank_Options == '*737#':
            Gt_services = {'1': 'Account Balance',
                    '2': 'Transfer',
                    '3': 'Airtime',
                    '4': 'Balance'}
        for key in Gt_services:
            print(key,Gt_services[key])
else:
    print("Invalid USSD CODE") 