import struct
from generate_spi import generate_spi_registers

def registre_to_le_bytes(hexstr):
    val = int(hexstr, 16)
    return struct.pack('<I', val)

def construire_trame(f_mhz, gain):
    entete = bytes.fromhex("19 03 04 05 06 07 08 ff 00 00 00 00")
    regs_hex = generate_spi_registers(f_out_hz=f_mhz * 1e6, int_n=False)
    regs = b''.join(registre_to_le_bytes(r) for r in regs_hex)

    # cmd_gain = struct.pack('<B', gain) + b'\x00' * 4
    # TODO: The relationship between the gain parameter and the end of the USB frame is still under investigation.
    # See README for details. The gain field is currently not functional.

    cmd_gain = b''  # Placeholder: gain control not implemented

    total = len(entete) + len(regs) + len(cmd_gain)
    if total > 64:
        raise ValueError("La trame dépasse 64 octets !")
    padding = b'\x00' * (64 - total)

    trame_bytes = entete + regs + cmd_gain + padding
    return trame_bytes

def afficher_trame_hex(trame_bytes):
    hexstr = trame_bytes.hex(' ').upper()
    for i in range(0, len(hexstr), 48):
        print(hexstr[i:i+48])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Génère une trame SPI complète pour Aaronia\nExemple : python send_trame_usb.py 5904.1 2",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("frequence", type=float, help="Fréquence de sortie en MHz")
    parser.add_argument("gain", type=int, choices=range(0,4), help="Gain (0-3)")
    args = parser.parse_args()

    trame = construire_trame(args.frequence, args.gain)
    print("Trame générée :")
    afficher_trame_hex(trame)
