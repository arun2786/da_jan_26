# List -> []
# Tuple -> () or none
# Set -> {} => no duplicates, unordered, unindexed
musicList = {
    "Jai ho", 
    "Sandese aate hain", 
    "jai jai santoshi maa",
    "Sandese aate hain", 
    "Jai ho", 
    "Sandese aate hain", 
    "Jai ho", 
    "Sandese aate hain", 
    "jai jai santoshi maa",
    "Sandese aate hain", 
    "Jai ho", 
    "Sandese aate hain", 
    "jai jai santoshi maa"
}

print(type(musicList))
print(musicList)


musicList.add("Sandese aate hain")
musicList.add("Sandese aate hain")
musicList.add("Sandese aate hain")
musicList.add("Sandese aate hain")
musicList.add("Mere desh ki dharti")

musicList.remove("Sandese aate hain")

print(f"Total: {len(musicList)}")

for song in musicList:
    print(song)