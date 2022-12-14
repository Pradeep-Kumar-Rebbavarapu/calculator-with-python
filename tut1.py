PI = 3.141592653589793
e = 2.718281828459045
Addition = lambda x,y: x + y
Subtraction = lambda x,y:x - y
Multiplication = lambda x,y:x*y
Division = lambda x,y:x/y
Exponential = lambda x,y:e**y if x=="e" else float(x)**y
factorial = lambda n:n*factorial(n-1) if n>0 else 1

def sinx(x):
    sign = 1
    total_sum = 0
    if x%PI==0:
        return 0
    for i in range(1,31,2):
        sinx = ((sign)*(x**i))/factorial(i)
        total_sum = total_sum + sinx
        sign = -1 * sign
    return total_sum
def cosx(x):
    sign = 1
    total_sum = 0
    if x!=0 and x%(PI/2)==0 and x%(PI)!=0:
        return 0
    for i in range(0,31,2):
        cosx = ((sign) * (x**i))/factorial(i)
        total_sum = total_sum + cosx
        sign = -1*(sign)
    return total_sum
tanx = lambda x:'not defined' if cosx(x)==0 else sinx(x)/cosx(x)
cotx = lambda x:'not defined' if sinx(x)==0 else cosx(x)/sinx(x)
secx = lambda x:'not defined' if cosx(x)==0 else 1/cosx(x)
cosecx = lambda x:'not defined' if sinx(x)==0 else 1/sinx(x)
operators = ['-','+','*','/','^']
while True:
    try:
        ch = input('===>') 
        if ch=="q" or ch=='Q':
            print('Thank You')
            break 
        string_with_no_white_spaces = ch.replace(' ','').lower()
        if '(' and ')' in string_with_no_white_spaces:
            angle_value_in_radian = string_with_no_white_spaces.split('(')[1].replace(")","")
            trig_string = string_with_no_white_spaces.replace("(","").replace(angle_value_in_radian,'').replace(")","")
            angle_string_list = []
            
            if 'pi' in angle_value_in_radian:
                if '/' in angle_value_in_radian:
                    if angle_value_in_radian.lower().split('/')[0] == "pi":
                        trig_list = [trig_string,PI/int(angle_value_in_radian.lower().split('/')[1])]
                    else:
                        trig_list = [trig_string,int(angle_value_in_radian.lower().split('/')[0].split('pi')[0])*PI/int(angle_value_in_radian.lower().split('/')[1])]

                else:
                    if len(angle_value_in_radian.split('pi')[0])==0:
                        trig_list = [trig_string,PI]
                    else:
                        trig_list = [trig_string,int(angle_value_in_radian.aplit('pi')[0]) * PI]
            else:
                trig_list = [trig_string,angle_value_in_radian]
                
            
            
            if trig_list[0]=="sin":
                print(sinx(float(trig_list[1])))
            if trig_list[0]=="cos":
                print(cosx(float(trig_list[1])))
            if trig_list[0]=="tan":
                print(tanx(float(trig_list[1])))
            if trig_list[0]=="cot":
                print(cotx(float(trig_list[1])))
            if trig_list[0]=="cosec":
                print(cosecx(float(trig_list[1])))
            if trig_list[0]=="sec":
                print(secx(float(trig_list[1])))
            
        elif '(' and ')' and "!" not in string_with_no_white_spaces:
            string_list_with_operator = [i for i in string_with_no_white_spaces]
            for i in operators:
                if i in string_with_no_white_spaces:
                    s = string_with_no_white_spaces.replace(i,'')
                    string_list_without_operator = string_with_no_white_spaces.split(i)
            for i in s:
                only_operator_list = string_list_with_operator.remove(i)
            
        
            string_list = string_list_without_operator + string_list_with_operator
            
            if string_list[2]=="+":
                print(Addition(float(string_list[0]),float(string_list[1])))
            if string_list[2]=="-":
                print(Subtraction(float(string_list[0]),float(string_list[1])))
            if string_list[2]=="*":
                print(Multiplication(float(string_list[0]),float(string_list[1])))
            if string_list[2]=="/":
                print(Division(float(string_list[0]),float(string_list[1])))
            if string_list[2]=="^":
                print(Exponential(string_list[0],float(string_list[1])))
        elif '!' in string_with_no_white_spaces:
            
            print(factorial(int(string_with_no_white_spaces.split('!')[0]))) 
        
    except Exception as e:
        print('Please Input Valid Values')
     
    
    
    
    



