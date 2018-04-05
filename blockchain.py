import hashlib, json

text = "a"
coins = []
#myhash = hashlib.sha256(text.encode('utf-8')).hexdigest()

for nonce in range(2000):
    myjson = {"text":text, "nonce":nonce}
    myjson = json.dumps(myjson);
    myhash = hashlib.sha256(myjson.encode('utf-8')).hexdigest()
    if myhash[-2:] == "de":
        print(myjson)
        print("Hash:" + str(myhash))
        print("Last 2 chars:" + str(myhash[-2:]))
        coins.append(myhash)
    else:
        continue
    

