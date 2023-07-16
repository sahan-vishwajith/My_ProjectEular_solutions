def fibona(n):
    '''get the n value and return fibonacci sequence of n'''
    # change the type of n
    n = int(n)
    # if n=0 ,then return 0
    if n==0:
        return 0
    # if n=1 , then return 1
    elif n==1:
        return 1
    else:
        # create two variables and put initial values
        character1 = 0
        character2 = 1
        # this loop create the elements of fibonacci sequence
        for i in range(n - 1):
            # new value equals to sum of the previous two values
            new_character = character1 + character2
            # put the new values to variables
            character1 = character2
            character2 = new_character
        return new_character

def getNum(file_name):
    '''read the file and get 'n' value'''
    # open the file
    file=open(file_name,'r')
    # read the file and store the value in n
    n=file.read()
    # return the n value
    return n
def show(n):
    ''' show the value fibonacci sequence and return that value'''
    # get the fibonacci value of n
    fibo_value=fibona(n)
    # print that value
    print('Fibonacci('+str(n)+')','=',str(fibo_value))
    # return that value
    return 'Fibonacci('+str(n)+')','=',str(fibo_value)

def saveFile(fibo_content):
    ''' save the output as a file named as "result.txt" '''
    # create a file and open that file for writing
    out_file=open('result.txt','w')
    # write the value on file
    out_file.write(fibo_content)
    # return
    return
try:
    # if there is any exception, then print " invalid input."
    # get the input as n
    n=input()
    # read the file and get the value of n
    value_n=int(getNum(n))
    # check if n is 0<=n<=20 or not
    if value_n<=20 and value_n>=0:
        # get the fibonacci value and print it
        out=show(value_n)
        #write the fibonacci value on file
        saveFile(str(out))
    # if n<0 or n>20 then print 'invalid input.'
    else:
        print('Invalid input.')
# if there is any exception then print 'invalid input.'
except:
    print('Invalid input.')