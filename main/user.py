import json
import glob
import os
import random

# password generator
def generatePassword(length: int) -> str:
    password = ''
    chars = list([chr(i) for i in range(97, 97+26)])
    chars.extend([chr(i) for i in range(65, 65+26)])
    chars.extend([chr(i) for i in range(48, 48+10)])
    for _ in range(length):
        password += random.choice(chars)
    return password

# create new user function
# gender = true -> 男
# gender = false -> 女
def newUser(username: str, fullname: str, gender: bool) -> bool:
	data: dict = dict()
	data['username']: str = username
	data['fullname']: str = fullname
	data['password']: str = generatePassword(length=8)
	data['gender']: str = 'male' if gender else 'female' 
	data['shifts']: list = []

	print(json.dumps(data, ensure_ascii=False, indent=2))
	fileName: str = username + '.json'
	if os.path.exists(os.path.join('./userdata/', fileName)):
		print(fileName, 'は存在します')
		return False
	else:
		print(fileName, 'は存在しません')
		with open(os.path.join('./userdata/', fileName), mode='wt', encoding='utf-8') as f:
			json.dump(data, f, ensure_ascii=False, indent=2)
			print(fileName, 'に書き込みました。')
		return True

def existUser(username: str) -> bool:
	fileName: str = username + '.json'
	return os.path.exists(os.path.join('./userdata/', fileName))

def loadUserjson(username: str) -> dict:
	fileName: str = username + '.json'
	if existUser(username) == False:
		return None
	with open(os.path.join('./userdata/', fileName), mode='rt', encoding='utf-8') as f:
		#print('file:', str(f))
		data: dict = json.load(f)
		return data

def challenge(username: str, password: str) -> bool:
	if existUser(username) == False:
		return False
	data: dict = loadUserjson(username)
	if data == None:
		return False
	return data['password'] == password

#result: bool = newUser('test', 'testくん', True)
#print(result)
#print('existUser:', existUser('test'))
#print('challenge:', challenge('test', 'testpass'))
#print('challengeOK:', challenge('test', '6LcQmpaD'))