import hashlib
import os

BUF_SIZE = 65536 

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()

companyHash = 'c15e32d27635f248c1c8b66bb012850e5b342119'

directory_in_string = 'C:/Users/38595/Desktop/racunalna_forenzika_labovi/Lab2/Vjezba3/DrugiDio/Dokazi/'
directory = os.fsencode(directory_in_string)
    
for file in os.listdir(directory):
  with open(directory_in_string + file.decode("utf-8"), 'rb') as f:
    while True:
      data = f.read(BUF_SIZE)
      if not data:
        break
      md5.update(data)
      sha1.update(data)
      sha256.update(data)

  if "{0}".format(md5.hexdigest()) == companyHash:
    print("The secret file is " + file.decode("utf-8"))
    print("MD5: {0}".format(md5.hexdigest()))

  if "{0}".format(sha1.hexdigest()) == companyHash:
    print("The secret file is " + file.decode("utf-8"))
    print("SHA1: {0}".format(sha1.hexdigest()))

  if "{0}".format(sha256.hexdigest()) == companyHash:
    print("The secret file is " + file.decode("utf-8"))
    print("SHA256: {0}".format(sha256.hexdigest()))

  md5 = hashlib.md5()
  sha1 = hashlib.sha1()
  sha256 = hashlib.sha256()

