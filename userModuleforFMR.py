
#Task: Name of function 
#Element: list of data elements
def filterX(Task, Elements):
    Result =[]
    for no in Elements:
        if(Task(no)==True):
            Result.append(no)
    return Result
 
def mapX(Task, Elements):
    Result=[]
    for i in Elements:
        Ret= Task(i)
        Result.append(Ret)
    return Result

def reduceX(Task, Elements):
    Result=[]
    Sum=0
    for no in Elements:
        Sum =Task(Sum,no)
    return Sum