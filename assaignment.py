# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s=0
avg=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        p=line.find("0")
        q=line.find(" ")
        Floating=line[p:q]
        Floating=Floating.strip()
        F=float(Floating)
        F=F+0
        s=s+1
        a=F/s
        avg=avg+a
print("Average spam confidence: ",avg)
