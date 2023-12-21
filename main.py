def solution(pairs):
    s = ""
    for k,v in pairs.items():
        s += str(k)+ " = " + str(v) + ","
    return s[:-1]

def solution(pairs):
    return ','.join(f'{k} = {v}' for k,v in pairs.items())
