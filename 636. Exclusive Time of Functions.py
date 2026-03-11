n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
shit = []
HM = {}
shit_out = []

for log in logs:
    fid,op,time = log.split(":")

    if op == "start":
        shit.append((int(fid), int(time)))

    elif op == "end":
        fid_s, start = shit.pop()
        ftime = int(time) - start + 1
        HM[fid_s] = HM.get(fid_s, 0) + ftime

        if shit:
            paused_fid, paused_start = shit[-1]
            shit[-1] = (paused_fid, int(time) + 1)

for i in range(n):
    shit_out.append(HM[i])

#print(shit_out)
print([HM[i] for i in range(n)])