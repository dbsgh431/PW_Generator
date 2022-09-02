import hashlib

Hash = 'md5'

site, id, length = input().split()

text = site+id
text_encode = text.encode('utf-8')
result = hashlib.new(Hash)
result.update(text_encode)

pw = result.hexdigest()[:int(length)-1] + "!"

print(pw)