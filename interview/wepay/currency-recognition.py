def isCurrency(strAmount):
    # Write your code here
    if not strAmount or len(strAmount) == 0:
        return False # illegal input
    
    char_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', ',', '.', '(', ')', '$', '€', '¥']
    
    for char in strAmount:
        if char not in char_set:
            return False  # input contains illegal characters
    
    if not ( strAmount[0] == '-' or ( strAmount[0] == '(' and strAmount[-1] == ')' ) or strAmount[0] in ['$', '€', '¥'] ):
        return False  # wrong starting character
    
    is_minus, is_Jy = False, False
    
    # Check if currency has minus sign
    if strAmount[0] == '-' or ( strAmount[0] == '(' and strAmount[-1] == ')' ):
        is_minus = True
        if strAmount[0] == '-':
            strAmount = strAmount[1:]
        else:
            strAmount = strAmount[1:len(strAmount) - 1]

    if not strAmount or len(strAmount) == 0:
        return False # illegal input after removing minus sign and ()
    
    
    if strAmount.find('-') != -1 or strAmount.find('(') != -1 or strAmount.find(')') != -1:
        return False  # there are extra minus sign and () in the string
        
        
    if strAmount[0] == '¥':
        is_Jy = True  # current currency is Japanese Yen
        
    if strAmount[0] not in ['$', '€', '¥']:
        return False  # currency sign should be in the first position


    strAmount = strAmount[1:]
    if not strAmount or len(strAmount) == 0:
        return False # illegal input after removing currency sign
    
        
    # now we check period / decimal sign
    if is_Jy and strAmount.find('.') != -1:
        return False  # Japanese Yen should not have decimal
        
    if not is_Jy and strAmount.find('.') != -1 and strAmount.find('.') != len(strAmount) - 3:
        return False  # wrong precision, precision but be exactly two digits


    # if not (strAmount.find('.') != -1 and not is_Jy):
    # leading zero are only valid when:
    #       $ or € with zero and decimal points appear
    #       for example : $01.25 is invalid but $0 is valid
    if not (strAmount.find('.') != -1 and strAmount[0] == '0' and strAmount.find('.') == 1 and not is_Jy):
        if len(strAmount) > 1 and strAmount[0] == '0':
            return False  # leading zero only decimals this will catch cases like $01.25
        
        if strAmount[0] == '0' and strAmount.find('.') != -1 and strAmount.find('.') != 1:
            return False # this will not catch $0
            
    # finally check the thousands operator
    if not check_decimal_with_thousands(strAmount):
        return False

    # after all those checks, if the strAmount reach here then it is a valid currency
    return True
        
        
        
def check_decimal_with_thousands(s):
    if s.find(',') == -1:
        return True  # no thousands operator, no need to check
        
    if s.find('.') != -1:
        s = s[:len(s) - 3] # remove decimal points and decimal digits since `.` appears
    
    if len(s) - 1 - 3 <= 0:
        return False  # thousands operator here but there is no enough place for it, this will catch case like `$2,3`

    for i in range(len(s) - 4, -1, -4):

        if s[i] != ',':
            return False  # thousands operator in the wrong place, this will catch case like `$230,00`
        
    return True
