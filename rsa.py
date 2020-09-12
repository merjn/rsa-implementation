import math
import random


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = int(temp_phi / e)
        temp2 = int(temp_phi - temp1 * e)
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def create_keypair(p, q) -> tuple:
    m = p*q
    # totient function
    l = (q-1)*(p-1)

    # create public key e.
    e = random.randrange(1, l)

    g = math.gcd(e, l)
    while g != 1:
        e = random.randrange(1, l)
        g = math.gcd(e, l)

    # create private key d.
    d = multiplicative_inverse(e, l)
    return (e, m), (d,m)


def encrypt_rsa(data: int, pubkey: tuple) -> int:
    return pow(int(data), int(pubkey[0]), int(pubkey[1]))


def decrypt_rsa(data: int, priv_key: tuple) -> any:
    """
    Decryption works like this: data^exponent % mod.
    :param data:
    :return:
    """
    exponent = priv_key[0]
    mod = priv_key[1]
    return pow(int(data), exponent, mod)
