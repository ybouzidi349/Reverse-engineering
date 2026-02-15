## 🧾 REGISTRE 0 (Adresse binaire `000` – Écriture) 

| Bit(s)    | Nom          | Fonction                                                               | Taille (bits) | Exemple |
|-----------|--------------|------------------------------------------------------------------------|---------------|---------|
| 31        | `INT`        | 0 = Fractional-N, 1 = Integer-N                                        | 1             | 1       |
| 30–15     | `N[15:0]`    | Valeur entière N (boucle de rétroaction PLL)                          | 16            | 1000    |
| 14–3      | `FRAC[11:0]` | Valeur fractionnaire F (0–4095)                                        | 12            | 0250    |
| 2–0       | `ADDR`       | Adresse du registre = `000`                                           | 3             | 000     |

🔧 **Utilité** : détermine le mode Int/Frac-N et la fréquence VCO.

---

## 🧾 REGISTRE 1 (Adresse binaire `001` – Écriture)

| Bit(s)    | Nom        | Fonction                                                                 | Taille (bits) | Exemple       |
|-----------|------------|--------------------------------------------------------------------------|---------------|----------------|
| 31        | `CPOC`     | Clamp du CP en mode int-N                                                | 1             | 1              |
| 30–29     | `CPL`      | Linéarité du CP (00 = int-N, 01 = frac-N)                               | 2             | 01             |
| 28–27     | `CPT`      | Mode test du CP                                                          | 2             | 00             |
| 26–18     | `P[8:0]`   | Ajustement de phase (0 à 511)                                            | 9             | 000000000      |
| 17–3      | `M[14:0]`  | Modulus (diviseur dans F/M, de 2 à 32767)                                | 15            | 000000000101000 |
| 2–0       | `ADDR`     | Adresse du registre = `001`                                              | 3             | 001            |

🔧 **Utilité** : contrôle la linéarité et puissance du charge-pump et la modulation de phase.

---

## 🧾 REGISTRE 2 (Adresse binaire `010` – Écriture)

| Bit(s)    | Nom        | Fonction                                                                 | Taille (bits) | Exemple       |
|-----------|------------|--------------------------------------------------------------------------|---------------|----------------|
| 31        | `LDS`      | Vitesse du Lock Detect                                                   | 1             | 1              |
| 30–29     | `SDN`      | Mode bruit faible / faible spur                                          | 2             | 10             |
| 28–26     | `MUX`      | Sélection de la sortie MUX_OUT                                           | 3             | 110            |
| 25        | `DBR`      | Référence x2 activée                                                     | 1             | 0              |
| 24        | `RDIV2`    | Référence ÷2 activée                                                     | 1             | 1              |
| 23–14     | `R[9:0]`   | Compteur R (1 à 1023)                                                    | 10            | 0001100101     |
| 13–10     | `CP[3:0]`  | Courant du CP (0.3125 à 5.000 mA, via RSET)                              | 4             | 1111           |
| 9         | `LDF`      | Mode de Lock Detect (0 = frac-N, 1 = int-N)                              | 1             | 1              |
| 8         | `LDP`      | Précision du Lock Detect                                                 | 1             | 0              |
| 7         | `PDP`      | Polarité du Phase Detector (1 = positive)                               | 1             | 1              |
| 6         | `SHDN`     | Mise en veille                                                          | 1             | 0              |
| 5         | `TRI`      | Sortie CP 3-états                                                        | 1             | 0              |
| 4         | `RST`      | Reset des compteurs N et R                                              | 1             | 0              |
| 2–0       | `ADDR`     | Adresse du registre = `010`                                              | 3             | 010            |

🔧 **Utilité** : config du CP, diviseur R, activation du MUX_OUT, gestion des modes.

---

## 🧾 REGISTRE 3 (Adresse binaire `011` – Écriture)

| Bit(s)    | Nom        | Fonction                                                                 | Taille (bits) | Exemple        |
|-----------|------------|--------------------------------------------------------------------------|---------------|----------------|
| 31–26     | `VCO[5:0]` | VCO sélection manuelle (0–63)                                            | 6             | 001011         |
| 25        | `VAS_SHDN` | VAS activé/désactivé                                                     | 1             | 1              |
| 24        | `RETUNE`   | Auto-retune activé                                                      | 1             | 1              |
| 23–18     | `Reserved` | Non utilisé (mettre 0)                                                  | 6             | 000000         |
| 17        | `Reserved` | Idem                                                                    | 1             | 0              |
| 16–15     | `CDM`      | Mode CDM : 01 = fast-lock, 10 = phase shift                             | 2             | 00             |
| 14–3      | `CDIV`     | Valeur diviseur horloge (1 à 4095)                                      | 12            | 000001000010   |
| 2–0       | `ADDR`     | Adresse du registre = `011`                                              | 3             | 011            |

🔧 **Utilité** : contrôle du VCO (manuel ou auto), mode fast-lock et phase control.

---

## 🧾 REGISTRE 4 (Adresse binaire `100` – Écriture)

| Bit(s)    | Nom        | Fonction                                                                 | Taille (bits) | Exemple        |
|-----------|------------|--------------------------------------------------------------------------|---------------|----------------|
| 31–26     | `Reserved` | À 011000                                                                 | 6             | 011000         |
| 25–24     | `BS_MSBs`  | Bits MSB du Band Select Clock Divider                                   | 2             | 00             |
| 23        | `FB`       | Feedback direct (1) ou post-diviseur (0)                                | 1             | 0              |
| 22–20     | `DIVA`     | Diviseur sortie RF (1 à 128 → codé en 3 bits)                           | 3             | 101            |
| 19–12     | `BS`       | Band Select Divider (fréquence état machine VAS)                        | 8             | 00001010       |
| 11–10     | `Reserved` | À 00                                                                     | 2             | 00             |
| 9         | `BDIV`     | RFOUTB direct ou divisé                                                  | 1             | 0              |
| 8         | `RFB_EN`   | Activation RFOUTB                                                        | 1             | 1              |
| 7–6       | `BPWR`     | Puissance RFOUTB : 00(-4dBm) à 11(+5dBm)                                | 2             | 11             |
| 5         | `RFA_EN`   | Activation RFOUTA                                                        | 1             | 1              |
| 4–3       | `APWR`     | Puissance RFOUTA                                                         | 2             | 10             |
| 2–0       | `ADDR`     | Adresse du registre = `100`                                              | 3             | 100            |

🔧 **Utilité** : active les sorties RF, configure la puissance, mode feedback, diviseurs.

---

## 🧾 REGISTRE 5 (Adresse binaire `101` – Écriture)

| Bit(s)    | Nom        | Fonction                                                                 | Taille (bits) | Exemple            |
|-----------|------------|--------------------------------------------------------------------------|---------------|---------------------|
| 31–25     | `Reserved` | 0000000                                                                  | 7             | 0000000             |
| 24        | `F01`      | Active auto-int-N si F = 0                                               | 1             | 1                   |
| 23–22     | `LD[1:0]`  | Lock Detect mode: `01` = digital, `10` = analog                          | 2             | 01                  |
| 21–19     | `Reserved` | 000                                                                      | 3             | 000                 |
| 18        | `MUX_MSB`  | Bit MSB pour MUX_OUT mode (concat. avec Reg2[28:26])                    | 1             | 1                   |
| 17–3      | `Reserved` | 0s                                                                       | 15            | 000000000000000     |
| 2–0       | `ADDR`     | Adresse du registre = `101`                                              | 3             | 101                 |

🔧 **Utilité** : configure le comportement Lock Detect et sortie MUX_OUT.

---

## 🧾 REGISTRE 6 (Adresse binaire `110` – Lecture uniquement)

| Bit(s)    | Nom         | Fonction                                                                | Taille (bits) |
|-----------|-------------|-------------------------------------------------------------------------|---------------|
| 31–24     | `Reserved`  | --                                                                      | 8             |
| 23        | `POR`       | Power-On Reset (1 = non encore lu)                                     | 1             |
| 22–20     | `ADC[2:0]`  | Lecture du VCO Tune ADC (état VTUNE)                                   | 3             |
| 19–9      | `Reserved`  | --                                                                      | 11            |
| 8–3       | `V[5:0]`    | VCO actif (0–63)                                                        | 6             |
| 2–0       | `ADDR`      | Adresse = `110`                                                         | 3             |

🔧 **Utilité** : diagnostic interne – VCO actif et état du VTUNE.
