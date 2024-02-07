import string
import random

# 1
def pass_gen(length=8):
    reses = string.ascii_letters + string.digits + string.punctuation
    passkey = "".join(random.choice(reses)for i in range(length))
    return passkey

print(f"Generatsiyadan o'tgan parol: {pass_gen()}")


# 2
def juft_gen(limit):
    for son in range(2, limit+ 1, 2):
        yield son

use1 = int(input("\nIstalgan son kiriting va uni juftliklarda tekshiring: "))
juft = juft_gen(use1)
print("Generatsiyadan o'tgan juftliklar:")
for son in juft:
    print(son)


# 3
def toq_gen(limit):
    for son in range(1, limit+ 1, 2):
        yield son

use2 = int(input("\nIstalgan son kiriting va uni toqliklarda tekshiring: "))
toq = toq_gen(use2)
print("Generatsiyadan o'tgan toqliklar:")
for son in toq:
    print(son)


# 4
def tub_gen(son):
    if son <2:
        return False
    for i in range(2, int(son**0.5)+1):
        if son%i==0:
            return False
    return True
def tub_gen2(limit):
    umum = sum(son for son in range(2, limit+1) if tub_gen(son))
    yield limit - umum

use3 = int(input("\nTub son kiriting: "))
youtube = tub_gen2(use3)
print(f"{use3}gacha tub sonlarni ayirishdan keyingi xolat:", next(youtube))