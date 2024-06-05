def convert_str_to_df(inp):
    inp_lst = inp.split('\n')
    inp_lst.remove(inp_lst[1])
    data_lst = []
    index = 0
    for row in inp_lst:
        data_lst.append([index])
        for cell in row.split('|'):
            data_lst[index].append(cell.strip())
        index += 1
    return pd.DataFrame(data = data_lst[1:], columns = data_lst[0]).drop(columns = [0,''])
