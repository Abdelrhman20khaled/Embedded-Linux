def moveToDirRegister(file_name,Input_Reg):
     if Input_Reg == "DDRA" or Input_Reg == "ddra":
        file_name.seek(73)
     elif Input_Reg == "DDRB" or Input_Reg == "ddrb":
        file_name.seek(90)
     elif Input_Reg == "DDRC" or Input_Reg == "ddrc":
        file_name.seek(107)
     elif Input_Reg == "DDRD" or Input_Reg == "ddrd":
        file_name.seek(124)