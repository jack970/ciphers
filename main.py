import ciphers

frase = "Cases, spaces, punctuation!"

viginere_encode = ciphers.Viginere(frase, "teste").encoder()
viginere_decode = ciphers.Viginere(viginere_encode, "teste").decoder()

print(f"viginere_encode: {viginere_encode}")
print(f"viginere_decode: {viginere_decode}")

ascii_encode = ciphers.AsciiShift(frase, 47)
ascii_decode = ciphers.AsciiShift(ascii_encode, 47)

print(f"ascii_encode: {ascii_encode}")
print(f"ascii_decode: {ascii_decode}")