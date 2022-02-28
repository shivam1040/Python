mydic={
    "1":"2",
    "3":1,
    "5":[1,2],
    "andic":{
        "6":7,
    }

}
mydic["5"]=[1,5]
print(mydic["andic"]["6"])
print(mydic.keys()) # prints keys
print(mydic.values()) # print values
print(list(mydic.keys())) # typecast keys to list
print(mydic.items()) # prints (key, value) pairs of entire dict
updatedic={
    7:3
}
mydic.update(updatedic) #updated mydic with updatedic, values at end
print(mydic.get("harry")) # use it when you're not sure if the key is present
mydic={}
mydic["1"]="a" #adds "1":"a" in empty dictionry
# while printing dic if key are repititve then last updated key is displayed
