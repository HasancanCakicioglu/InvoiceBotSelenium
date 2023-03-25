


def tcKontrolFunc(tc_str:str)->bool:
    if "." in tc_str:
        tc_str = tc_str.split(".")[0]  # Noktadan önceki kısmı al
    for i in tc_str:
        if i != '1':
            return True
    return False
