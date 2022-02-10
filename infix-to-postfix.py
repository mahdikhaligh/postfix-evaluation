from os import sep


OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  #operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # priorities 

def infix_to_postfix(infix): 

    stack = [] # stack
    output = '' # output 

    for ch in infix:
        if ch not in OPERATORS: 
            output += f'{ch} '

        elif ch=='(': 
            stack.append('(')

        elif ch==')':
            while stack and stack[-1] != '(':
                output += f'{stack.pop()} ' 
                
            stack.pop()
            
        else:  
            # so pop and push in output   
            while stack and stack[-1]  != '('  and PRIORITY[ch] <= PRIORITY[stack[-1]] :
                output += f'{stack.pop()} '
                
            stack.append(ch)

    while stack:
        output += f'{stack.pop()} '

    return output

 
def main():
    print('Menu: \n ---------------------------------',
          ' infix -> input exp: 1^2+x/2*(b-x) ... |(use , ).',
          ' -exit -> exit programme. \n ---------------------------------',
          
          sep='\n *')
    
    while True:
        
        infix = input('Enter infix -> ').split(',')
        if infix[0] == '-exit':
            return
        
        print(
            '',
            f' infix : {" ".join(infix)}',
            f' postfix : {infix_to_postfix(infix)} \n',
            sep='\n >>>')
        

if __name__ == '__main__':
    main()
    
#########################
##### mahdi khaligh #####
#########################    
