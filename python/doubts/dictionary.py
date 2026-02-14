users = {
	"ramesh@gmail.com":{"name":"Ramesh", "email":"ramesh@gmail.com", "password":"123", "tweets":[]}, 
	"suresh@gmail.com":{"name":"Suresh", "email":"suresh@gmail.com", "password":"987"}
}

for key in users:
    user = users[key]
    name = user["name"]
    tweets = user["tweets"]
    secondTweet = tweets[1]
    # print(f"{key} -> {users[key]['tweets'][2]}")
    

