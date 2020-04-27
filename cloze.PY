
def sandwitch(list_a, list_b, col_num):
    assert len(list_a) == len(list_b)
    output = []
    while len(list_a) != 0:
        output.append(list_a[:col_num])
        del list_a[:col_num]
        output.append(list_b[:col_num])
        del list_b[:col_num]
    return output


data = []
with open("A.CSV", encoding='utf-8') as f:
    post = f.readlines()
    for line in post:
        test_list = line.strip().replace(' ', '').split(",")
        test_list = list(filter(None, test_list))
        data.append(test_list)


with open("b.md", "w", encoding='utf-8') as f:
    for d in data:
        f.write(f"# {d.pop(0)} \n")
        index_row = []
        ans_row = []
        for index, ans in enumerate(d):
            index_row.append(str(index + 1))
            ans_row.append(ans)
        col_num = 10
        for index, line in enumerate(sandwitch(index_row, ans_row, col_num)):
            if index == 1:
                for i in range(len(line)):
                    f.write("|-")
                f.write("|\n")
            f.write(f"|{'|'.join(line)}|\n")
        f.write("\n\n")
