def desinverser_trames(lines):
    trames_originales = []

    for line in lines:
        octets = line.strip().split()
        if len(octets) != 4:
            print(f"Ligne ignorée (non conforme): {line}")
            continue
        octets_inverses = octets[::-1]
        hex_value = ''.join(octets_inverses).upper()
        trames_originales.append(hex_value)

    return trames_originales

entree = """
08 01 00 00
""".strip().split('\n')

resultat = desinverser_trames(entree)

print("Trames désinversées :")
for trame in resultat:
    print(trame)
