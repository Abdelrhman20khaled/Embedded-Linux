'''

File Name :  port_parse.py --> Version 1
Subject: Incldues solutions of task 4 in python lecture 4
Task: Write python code to generate Init function of GPIO for AVR.
By: Abdelrhman Khaled Sobhi

'''
import gen_func 

Input_Reg = input("Enter the Direction Register of Port You Need: ")
Reg_Value = None
line_index = 0
reg_inital_value = [] 
reg_final_str = ''
reg_final_value = 0
try:
    with open("port_init.c","r+") as conf_file:
     data_acq = conf_file.readlines()
     
     for i in range(8):
        pin_dir = input("Enter the Direction of the Pin Num {}: ".format(i))
        if pin_dir == 'out' or pin_dir == 'OUT':
            reg_inital_value.append('1')
        elif pin_dir == 'in' or pin_dir == 'IN':
            reg_inital_value.append('0')

     reg_final_str = '0b'+''.join(reg_inital_value[::-1])
     reg_final_value = hex(int(reg_final_str,2))
     
    

     for list_line in data_acq:
        if (Input_Reg in list_line) or (Input_Reg.upper() in list_line):
            Reg_Value = list_line  
            line_index = data_acq.index(list_line)
    
     gen_func.moveToDirRegister(conf_file,Input_Reg)
     New_Line = Reg_Value.split('=')[0]+'= '+str(reg_final_value)+';\n'
     conf_file.writelines(New_Line)
            
     

except FileNotFoundError:
    print("Error, File Not Found Check the File Name")        

   