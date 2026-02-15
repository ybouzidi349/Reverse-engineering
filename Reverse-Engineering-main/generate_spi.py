CONFIG = {
    "f_ref_hz": 40e6,
    "modulus": 400,
    "cp_current": 0b1111,
    "r_counter": 1,

    "band_select_div": 0x382,
    "ld_mode": 0b01,
    "mux_msb": 0,
    "mux_lsb": 0b110,

    "reg3_default": 0x00000013,
    "reg5_default": 0x00040000,

    "output_enable": True,
    "fundamental": False,
    "mute_till_lock": False,
    "powerdown": False,
    "ref_divider": False,
    "ref_doubler": False,

    "rf_power": {
        "APWR": 0b11,
        "BPWR": 0b11,
        "RFA_EN": 1,
        "RFB_EN": 1
    }
}

def reg0(int_n, N, F):
    return (int(int_n) << 31) | ((N & 0xFFFF) << 15) | ((F & 0xFFF) << 3) | 0b000

def reg1(M, CPOC=1, CPL=0b01, P=0):
    return (CPOC << 31) | ((CPL & 0x03) << 29) | ((P & 0xFFF) << 15) | ((M & 0xFFF) << 3) | 0b001

def reg2(R, CP, LDF=1):
    cfg = CONFIG
    reg = 0
    reg |= 1 << 31
    reg |= 0 << 29
    reg |= cfg["mux_lsb"] << 26
    reg |= int(cfg["ref_doubler"]) << 25
    reg |= int(cfg["ref_divider"]) << 24
    reg |= (R & 0x3FF) << 14
    reg |= 1 << 13
    reg |= (CP & 0xF) << 9
    reg |= LDF << 8
    reg |= 0 << 7
    reg |= 1 << 6
    reg |= int(cfg["powerdown"]) << 5
    reg |= int(cfg["mute_till_lock"]) << 4
    reg |= 0 << 3
    reg |= 0b010
    return reg


def reg3():
    return CONFIG["reg3_default"]

def reg4(DIVA):
    cfg = CONFIG
    pwr = cfg["rf_power"]
    reg = 0
    reg |= 0b011000 << 26
    reg |= int(not cfg["fundamental"]) << 23
    reg |= (DIVA & 0x7) << 20
    reg |= (cfg["band_select_div"] & 0xFF) << 12
    reg |= 0 << 9
    reg |= int(cfg["output_enable"] and pwr["RFB_EN"]) << 8
    reg |= (pwr["BPWR"] & 0x3) << 6
    reg |= int(cfg["output_enable"] and pwr["RFA_EN"]) << 5
    reg |= (pwr["APWR"] & 0x3) << 3
    reg |= 0b100
    return reg

def reg5():
    return CONFIG["reg5_default"]

def reg_to_hex(reg):
    return f"{reg:08X}"

def choose_divider(f_out):
    if f_out < 46.875e6: return 0b111
    elif f_out < 93.75e6: return 0b110
    elif f_out < 187.5e6: return 0b101
    elif f_out < 375e6: return 0b100
    elif f_out < 750e6: return 0b011
    elif f_out < 1500e6: return 0b010
    elif f_out < 3000e6: return 0b001
    else: return 0b000

def generate_spi_registers(f_out_hz, int_n=False):
    f_ref = CONFIG["f_ref_hz"]
    M = CONFIG["modulus"]
    CP = CONFIG["cp_current"]
    R = CONFIG["r_counter"]

    DIVA = choose_divider(f_out_hz)
    diva_factor = 2 ** DIVA
    f_vco = f_out_hz * diva_factor
    f_pfd = f_ref

    N_float = f_vco / f_pfd
    N = int(N_float)
    F = 0 if int_n else int(round((N_float - N) * M))

    print(f"[INFO] f_out = {f_out_hz/1e6:.3f} MHz | DIVA = {diva_factor} | fVCO = {f_vco/1e6:.3f} MHz")
    print(f"[INFO] Mode = {'Int-N' if int_n else 'Frac-N'} | N = {N} | F = {F} | M = {M} | R = {R}")

    regs = [
        reg0(int_n, N, F),
        reg1(M),
        reg2(R, CP, LDF=int(int_n)),
        reg3(),
        reg4(DIVA),
        reg5()
    ]

    return [reg_to_hex(r) for r in regs]

if __name__ == "__main__":
    f_out_mhz = 2000
    regs = generate_spi_registers(f_out_hz=f_out_mhz * 1e6, int_n=False)
    for i, hexval in enumerate(regs):
        print(f"Reg{i}: {hexval}")
