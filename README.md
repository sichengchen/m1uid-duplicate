# m1uid-duplicate

## Usage

`m1uid-duplicate {-l|-u|-d} [<HEX_UID>]`

### Examples

- List NFC devices:
  
    `m1uid-duplicate -l`

- Directly write a specific UID into a new card:
  
    `m1uid-duplicate -u <HEX_UID>`
    
- Dump a card and write its UID into a new card:
  
    `m1uid-duplicate -d`

You must install `libnfc` and `mfoc` to use this program. This program requires root privileges to run properly.