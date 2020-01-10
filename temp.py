macroList = []

class Macro:
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

def searchMacro(src):
    srcCode = src.split()
    for i in range(len(srcCode)):
        if(srcCode[i] == '#define'):
           if(srcCode[i+2].isalnum()):
               print('Ture')
           macroList.append(Macro(srcCode[i+1], srcCode[i+2], srcCode[i+3]))
           
def expandMacro(src):
    srcCode = src.split()
    for i in range(len(srcCode)):
        if(srcCode[i-1] != '#define'):
            for macro in macroList:
                if(srcCode[i] == macro.name):
                    arg = srcCode[i+1]
                    #print(arg[1])
                    block = macro.body.replace(macro.args[1],arg[1])
                    srcCode[i] = block
                    srcCode[i+1] = ''
                    
    print(' '.join(srcCode))                

srcCode = "#define SUB (X) X=X-X #define DIV (X) X=X/X #include<bits/stdc++.h> int main() { int a = 10 ; SUB (a) ; DIV (b) ; return 0 ;}"
print("\n")
print(srcCode)
searchMacro(srcCode)    
# print('Macros', macroList[0].name)
expandMacro(srcCode)
