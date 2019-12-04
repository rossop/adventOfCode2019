
for num in range(start,end+1):
    password = str(num)
    double_cond = False
    order_cond = True
    no_repeat_cond = False
    checked = False
    unique_double = False
    for ii in range(len(password)-1):
        if int(password[ii]) > int(password[ii+1]):
            order_cond = order_cond and False
            break
        elif int(password[ii]) == int(password[ii+1]):
            double_cond = double_cond or True
            try:
                if int(password[ii+2]) == int(password[ii]):
                    no_repeat_cond = no_repeat_cond or True
                    unique_double = False
                    break
                else:
                    if not(checked):
                        checked = True
                        unique_double = unique_double or True

            except:
                continue
        else:
            continue

    if double_cond and order_cond and unique_double:
        count += 1
        print (count)