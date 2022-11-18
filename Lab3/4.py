S1="Marcel se numeste Marcel"
S2="El nu e Marcel"
Dict1={x:3 for x in S1.split()}
Dict2={x:7 for x in S2.split()}
Dict3 = Dict2.copy()
for a,b in Dict1.items():
    Dict3[a] = Dict3.get(a, 0) + b
print(Dict3)
