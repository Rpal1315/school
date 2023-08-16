#intext = "ritankar"
#$l = len(intext)
#for i in range (l-1,-1,-1):
    #outtext = intext[i]
    #print(outtext,end="")

intext = "ritankar pal"
leng = len(intext)
outext = ""
for i in range(0,leng+1):
    if intext[i:] != " ":
        outext = outext+intext[-1:]
        intext = intext[:leng-1]
        
        leng = leng-1

print(outext)