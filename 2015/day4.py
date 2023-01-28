import hashlib
import time

baseString = "ckczppom"

start = time.time()

num = 1
while True:
    hash = hashlib.md5(f"{baseString}{num}".encode("utf-8")).hexdigest()
    if hash[:6] == "000000":
        print(num)
        break
    num += 1

end = time.time()
print(end - start)
