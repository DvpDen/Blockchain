import hashlib, json

data_1 = {'who':'Bernardo', 'text':'Who\'s there?', 'nonce':0, 'prevhash':'0000000000000000000000000000000000000000000000000000000000000000'}
data_2 = {'who':'Andreas', 'text':'I believe in you.', 'nonce':0, 'prevhash':'5a0d090a68c996a69804322d54f8deda6dd7ebc39a1a713f9053e5237f209bde'}
def createHamletBlock(data_1, blockNo):
    
    for nonce in range(100000):
        data_1['nonce'] = nonce
        
        myjson = json.dumps(data_1);
        myhash = hashlib.sha256(myjson.encode('utf-8')).hexdigest()
        if myhash[-2:] == "de":
            print("Block " + str(blockNo) +": " + str(myjson))
            return myhash
        else:
            continue

print("Hash key: " + str(createHamletBlock(data_1, 1)))
print("Hash key: " + str(createHamletBlock(data_2, 2)))
