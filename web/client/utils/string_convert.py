def get(text):
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
                    res += f'"{str(f_r).strip()}",'
    print(res)
    with open("./test.txt", 'w') as f:
        f.write(res)


get('''Maskeliya Town , Norwood , Bogawanthalawa , Brunswick , Sripada''')
