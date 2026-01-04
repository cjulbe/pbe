# RFID UID Reader (RC522 + GTK3)

This is a **very basic academic project** developed for the **Projecte Bàsic d’Enginyeria** course at **UPC (Universitat Politècnica de Catalunya)**, within the context of **Telemàtica specialization**.

The project reads the **UID of an RFID card** using an **MFRC522 (RC522) module** and displays it in a simple **GTK3 graphical interface**.

## Structure
- **Puzzle 1**: RFID UID reading using RC522 (SPI, Python)
- **Puzzle 2**: GTK3 interface that **imports and uses Puzzle 1** to display the UID

## Requirements
- Raspberry Pi
- RC522 RFID reader
- Python 3
- GTK3
- SPI enabled

## Libraries
- `mfrc522`
- `spidev`
- `gi` (GTK3)
