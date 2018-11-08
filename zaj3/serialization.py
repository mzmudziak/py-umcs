import json
#json
dictionary = {
    'k1': 'w1',
    'k2': 'w2',
    'k3': 'w3'
}

jsonStr = json.dumps(dictionary)

print(jsonStr, isinstance(jsonStr, basestring))

loadedDict = json.loads(jsonStr)
print loadedDict
print loadedDict.items()


# pickle
import pickle
jsonStr = pickle.dumps(dictionary)

print(jsonStr, isinstance(jsonStr, basestring))

loadedDict = pickle.loads(jsonStr)
print loadedDict
print loadedDict.items()
