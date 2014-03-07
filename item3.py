'''
Created on Mar 6, 2014

'''
from lpsolve55 import *

'''
You are an office manager, and you need to ensure that on each day of the week there are enough employees to handle the demand. 
There is a weekly pattern to the demand, so that the number of employees needed on any particular day depends only upon which 
day of the week it is (e.g., Monday, Tuesday, etc.). The minimum number of employees needed on each day of the week is as follows:  

    Mon Tue Wed Thu Fri Sat Sun
    11  7   6   9   12  5   8
    
You need to meet these minimums on each day of the week. Due to regulations, each employee must work 5 days in a row, 
then take 2 days off. Each employee's 5-day work segment can start on any day of the week you choose, but they must strictly 
alternate 5 days working, followed by 2 days off. For example, if an employee's work week starts on Wednesday, they will be 
working on Wednesday, Thursday, Friday, Saturday, Sunday, and will be off on Monday and Tuesday. Every employee is paid 
the same amount, so that total costs are proportional to the number of employees you hire.
 
 Your goal is to hire the minimum number of employees sufficient to ensure that the minimums shown above are met on 
 each of the 7 days of the week. What is the minimum number of employees needed? Note that you can only hire an integer 
 number of employees starting work on any given day. Formulate this problem as a linear program.
 
    - Step 1: Define the variables of the problem. 
    - Step 2: Write the constraints. 
    - Step 3: Write the objective function. 

Solve your linear program with lp_solve. Your solution must include 
    a printout of your lp_solve input and output files and the 
    numerical answer, i.e., the minimum number of employees needed.
'''

'''
ANSWER
  Variables of the problem are:
     x1  - number of people starting on Mon
     x2  - number of people starting on Tue
     x3  - number of people starting on Wed
     x4  - number of people starting on Thu
     x5  - number of people starting on Fri
     x6  - number of people starting on Sat
     x7  - number of people starting on Sun
 
     MINIMIZE total number of employees: x1+x2+x3+x4+x5+x6+x7 
     
     SUBJECT TO:
             x1           + x4 + x5 +x6 + x7 >= 11  
             x1 + x2           + x5 +x6 + x7 >=  7
             x1 + x2 + x3           +x6 + x7 >=  6
             x1 + x2 + x3 + x4          + x7 >=  9
             x1 + x2 + x3 + x4 + x5          >= 12 
                  x2 + x3 + x4 + x5 +x6      >=  5
                       x3 + x4 + x5 +x6 + x7 >=  8
                       
        where x1,x2,x3,x4,x5,x6,x7 >= 0
'''
def answer():
    lp = lpsolve('make_lp', 0, 7)
    lpsolve('set_verbose', lp, IMPORTANT)
    ret = lpsolve('set_obj_fn', lp, [1, 1, 1, 1, 1, 1, 1])
    ret = lpsolve('add_constraint', lp, [1, 0, 0, 1, 1, 1, 1], GE, 11)
    ret = lpsolve('add_constraint', lp, [1, 1, 0, 0, 1, 1, 1], GE,  7)
    ret = lpsolve('add_constraint', lp, [1, 1, 1, 0, 0, 1, 1], GE,  6)
    ret = lpsolve('add_constraint', lp, [1, 1, 1, 1, 0, 0, 1], GE,  9)
    ret = lpsolve('add_constraint', lp, [1, 1, 1, 1, 1, 0, 0], GE, 12)
    ret = lpsolve('add_constraint', lp, [0, 1, 1, 1, 1, 1, 0], GE,  5)
    ret = lpsolve('add_constraint', lp, [0, 0, 1, 1, 1, 1, 1], GE,  8)
    ret = lpsolve('set_int', lp, [1, 2, 3, 4, 5, 6, 7])  # all variables are integers
#     ret = lpsolve('set_lowbo', lp, 1, 28.6)
#     ret = lpsolve('set_lowbo', lp, 4, 18)
#     ret = lpsolve('set_upbo', lp, 4, 48.98)
    ret = lpsolve('set_col_name', lp, 1, 'Mon')
    ret = lpsolve('set_col_name', lp, 2, 'Tue')
    ret = lpsolve('set_col_name', lp, 3, 'Wed')
    ret = lpsolve('set_col_name', lp, 4, 'Thu')
    ret = lpsolve('set_col_name', lp, 5, 'Fri')
    ret = lpsolve('set_col_name', lp, 6, 'Sat')
    ret = lpsolve('set_col_name', lp, 7, 'Sun')
    ret = lpsolve('set_row_name', lp, 1, 'TotalMon')
    ret = lpsolve('set_row_name', lp, 2, 'TotalTue')
    ret = lpsolve('set_row_name', lp, 3, 'TotalWed')
    ret = lpsolve('set_row_name', lp, 4, 'TotakThu')
    ret = lpsolve('set_row_name', lp, 5, 'TotalFri')
    ret = lpsolve('set_row_name', lp, 6, 'TotalSat')
    ret = lpsolve('set_row_name', lp, 7, 'TotalSun')
    ret = lpsolve('write_lp', lp, 'item3-input.lp')
    print lpsolve('get_mat', lp, 1, 2)
    lpsolve('solve', lp)
    print lpsolve('get_objective', lp)
    print lpsolve('get_variables', lp)[0]
    print lpsolve('get_constraints', lp)[0]
    ret = lpsolve('write_lp', lp, 'item3-output.lp')
    
    '''
    This program print the following:
    
    0.0
    13.0
    [5.0, 0.0, 0.0, 6.0, 1.0, 1.0, 0.0]      <=== x1 thru x7
    [13.0, 7.0, 6.0, 11.0, 12.0, 8.0, 8.0]   <=== number fo emp available on each day Mon-Sun
    '''

    
if __name__ == '__main__':
    answer()