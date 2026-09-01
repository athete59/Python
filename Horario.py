time_ = "17:57"


def seven_segmentify(time_: str) -> str:
    i = 0
    linha1=" "
    linha2=" "
    linha3= " "
    while i<len(time_):
        if time_[i] in {"0", "2", "3", "5", "6", "7", "8", "9"}:
            linha1+=" _ "
        elif time_[i] in {"1","4", ":"}:
            linha1+="   "
        else:
            print("Hora inválida")

        if time_[i] in {"2", "3","4", "5","6", "8", "9"}:
            if time_[i] in {"2", "3"}:
               linha2+=  " _|"
            elif time_[i] in {"5","6"}:
                linha2+= "|_ "
            elif time_[i] in {"4","8","9"}:
               linha2+="|_|"
        elif time_[i] in "0":
            linha2+="| |" 
        elif time_[i] in ":":
            linha2+=" . "
        else:
            linha2+="  |"
               
        
        

        if time_[i] in {"0", "6", "8"}:
            linha3+="|_|"
        elif time_[i] in {"1", "4", "7"}:
            linha3+="  |"
        elif time_[i] in {"3", "5", "9"}:
            linha3+=" _|"
        elif time_[i] in ":":
            linha3+=" . "
        else:
            linha3+="|_ "
        i+=1

       
     
    print(linha1)
    print(linha2)
    print(linha3)
    return " "

resultado = seven_segmentify(time_)

print(resultado)
