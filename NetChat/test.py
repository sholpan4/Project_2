import hashlib

username = "Vitaly"
passw = "1235"
salt = "sflu;krg76t4mhuiut2 iojlkjwefhk;geh29"

# hash = hashlib.md5(passw.encode('utf-8'))

# hash = hashlib.md5()
# hash = hashlib.sha1() #старый
hash = hashlib.sha512()
# hash.update(username.encode('utf-8'))
hash.update(passw.encode('utf-8'))
hash.update(salt.encode('utf-8'))
print(hash)

hash_string = hash.hexdigest()
print(hash_string)