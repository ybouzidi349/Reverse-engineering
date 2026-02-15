import hid
import time
import textwrap

VENDOR_ID = 0x04d8
PRODUCT_ID = 0xf3b5

WIRESHARK_HEX_STREAM = """
19 03 04 05 06 07 08 ff 00 00 00 00 00 00 32 00
11 80 00 80 42 6e 00 18 b3 84 00 e8 fc 00 a2 63
05 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
"""

def parse_hex_stream(hex_stream):
    cleaned = hex_stream.replace('\n', ' ').replace('\r', '').strip()
    try:
        data = bytes.fromhex(cleaned)
    except ValueError as e:
        raise ValueError("Erreur dans le format hexadécimal : " + str(e))
    if len(data) != 64:
        raise ValueError(f"Longueur de trame invalide : {len(data)} octets (attendu : 128)")
    return data

def main():
    try:
        trame = parse_hex_stream(WIRESHARK_HEX_STREAM)

        print("Connexion à l'appareil HID...")
        dev = hid.device()
        dev.open(VENDOR_ID, PRODUCT_ID)

        print("Appareil connecté !")
        print(f"Fabricant : {dev.get_manufacturer_string()}")
        print(f"Produit   : {dev.get_product_string()}")
        print(f"Envoi de la trame ({len(trame)} octets)...")

        dev.write(trame)
        time.sleep(0.1)
        print("Trame envoyée avec succès.")

        dev.close()

    except Exception as e:
        print("[Erreur] :", e)

if __name__ == "__main__":
    main()
