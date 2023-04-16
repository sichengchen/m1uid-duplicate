# m1uid-duplicate

You must install `libnfc` and `mfoc` to use this program. This program requires root privileges to run properly.

## Usage

`m1uid-duplicate {-l|-u|-d} [<HEX_UID>]`

### Examples

- List NFC devices:
  
    `m1uid-duplicate -l`

- Directly write a specific UID (4 bytes) into a new card:
  
    `m1uid-duplicate -u <4B_UID_HEX>`

- Directly write a specific UID (8 bytes) into a new card:

    `m1uid-duplicate -U <8B_UID_HEX>`
    
- Dump a card and write its UID into a new card:
  
    `m1uid-duplicate -d`

## Buying Cards

You can buy a "CUID" (UID Changeable) card from [Taobao (China)](https://s.taobao.com/search?q=CUID) or [Alibaba (Global)](https://www.alibaba.com/trade/search?searchText=CUID).