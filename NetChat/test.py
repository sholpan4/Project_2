import hashlib

username = 'Vitaly'
password = '1235'

hash = hashlib.sha1() #hashlib.md5(password.encode('UTF-8'))

hash.update(username.encode())
hash.update(password.encode())
print(hash)
hash_string = hash.hexdigest()
print(hash_string)