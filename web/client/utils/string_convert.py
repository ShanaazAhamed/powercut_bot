def get(text):
    global town
    areas = text.split(",")
    res = ""
    for i in areas:
        if i == "" or i == '\n':
            continue
        else:
            r = str(i).strip()
            if r != "":
                f_r = ""
                for j in r:
                    if j != '\n':
                        f_r += j
                if f_r != "":
                    striped = str(f_r).strip()
                    town = town.strip()
                    if striped != town:
                        res += f'"{striped} - {town}",'
                    else:
                        res += f'"{striped}",'
    # print(res)
    with open("./test.txt", 'w') as f:
        f.write(res)


town = "Seethawaka"
get('''    


 Aluthambalama,miriswatta,Beragala,Higurala,Eswatta,Puwakwatta,Elstonestate, 
Ukwatta,Ilukovita,manikkawatta,Kudagama



''')
