guvi_games={} #dict
guvi_games[(1,2,4)]=8
guvi_games[(4,2,1)]=10
guvi_games[(1,2)]=12
sum=0
for k in guvi_games:
    sum+=guvi_games[k] # sum = sum + guvi_games[k]
print(len(guvi_games)+sum)

print(guvi_games)

guvi_games["abcd"] = "89393"
print(guvi_games)