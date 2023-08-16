#intext = "ritankar"
#$l = len(intext)
#for i in range (l-1,-1,-1):
    #outtext = intext[i]
    #print(outtext,end="")

intext = "Ritankar is good"
leng = len(intext)
outext = ""
for i in range(0,leng+1):
    if intext[i:] != " ":
        outext = outext+intext[-1:]
        intext = intext[:leng-1]
        print(outext)
        leng = leng-1