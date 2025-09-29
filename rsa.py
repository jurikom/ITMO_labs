alf_lat_assi = [chr(i) for i in range(32, 127)]

def is_prime(x):
    if x < 2:
        return 0
    for i in range(2, int(x**0.5)+1):#проверка на все делители числа
        if x % i == 0:
            return 0
    return 1
#очень долгий и не эфективный способ
'''def gcd(x, y):
    deliteli_x = dels(x)
    deliteli_y = dels(y)
    for del_x in deliteli_x[::-1]:
        for del_y in deliteli_y[::-1]:
            if del_x == del_y:
                return del_y
    return 0'''
#алгоритм евклида в этом плане в сто раз лучше
def gcd(x, y):
    while x % y != 0:
        x, y = y, x % y
    return y

def multiplicative_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:#самая простая проверка на мультипликативность через перебор
            return d
    return None

def generate_keypair(p: int, q: int):
    if not (is_prime(p) and is_prime(q)):#обязательно должны быть простыми и разными
        return None
    if q == p:
        return None
    n_obshae = p * q
    if n_obshae < len(alf_lat_assi):#проверка на размер n он не может быть слишком маленьким
        return None
    phi_ot_n = (p - 1) * (q - 1)
    els = []
    for el in range(2, phi_ot_n):
        if gcd(el, phi_ot_n) == 1:
            els.append(el)
    if not els:
        return None
    e_public = els[0]
    d_personal = multiplicative_inverse(e_public, phi_ot_n)
    return ((e_public, n_obshae),(d_personal, n_obshae))

def decrypt(private_key, cipher_list):
    if private_key == 0:
        return ''
    result = ''
    private_key = private_key[1]
    n = private_key[1]
    d_private= private_key[0]
    for el in cipher_list:
        m = (el ** d_private) % n
        bucva = alf_lat_assi[m]
        result += bucva
    return result

def encrypt(public_key, text):
    if public_key == 0:
        return ''
    result=[]
    public_key=public_key[0]
    n = public_key[1]
    e_public = public_key[0]
    for el in text:
        m = alf_lat_assi.index(el)
        c = (m ** e_public) % n
        result.append(c)
    return result
key = generate_keypair(61, 53)
encr = encrypt(key,"nih04f1ub04uf")
print(encr)
print(decrypt(key,encr))