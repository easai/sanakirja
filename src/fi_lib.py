def dump(ans):
    exp = ans['expression']
    desc = ans['description']
    print(f"[{exp}] means [{desc}]")

def dump_list(lst):
    for item in lst:
        dump(item)
