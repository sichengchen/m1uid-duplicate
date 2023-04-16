import sys
import os
import struct
import subprocess


def change_uid_from_template(uid):
    with open('template.dump', 'rb') as f_in, open('to_write.dump', 'wb') as f_out:
        data = f_in.read(8)
        data = uid + data[8:]
        f_out.write(data)
        f_out.write(f_in.read())


def print_usage():
    print('Usage: m1uid-duplicate {-l|-u|-d} [<HEX_UID>]')
    print()
    print('Examples:')
    print()
    print('  List NFC devices:')
    print()
    print('    m1uid-duplicate -l')
    print()
    print('  Directly write a specific UID into a new card:')
    print()
    print('    m1uid-duplicate -u <HEX_UID>')
    print()
    print('  Dump a card and write its UID into a new card:')
    print()
    print('    m1uid-duplicate -d')
    print()
    print('You must install libnfc and mfoc to use this program. This program requires root privileges to run properly.')


def check_devices():
    try:
        subprocess.run(['nfc-list'])
    except Exception as e:
        print('An error occurred:', e)
        print()
        print_usage()


def write_dump_to_card():
    try:
        subprocess.run(['nfc-mfclassic', 'W', 'A', 'u', 'to_write.dump'])
    except Exception as e:
        print('An error occurred:', e)
        print()
        print_usage()


def dump_from_card():
    try:
        subprocess.run(['mfoc', '-P', '500', '-O', 'card.dump'])
        with open('card.dump', 'rb') as f_in:
            data = f_in.read()
            uid = data[:8]
            print('UID read:', hex(int.from_bytes(uid, byteorder='big')))
            os.remove('card.dump')
            return uid
    except Exception as e:
        print('An error occurred:', e)
        print()
        print_usage()


def main():
    uid = b'\x01\x02\x03\x04\x05\x06\x07\x08'

    if len(sys.argv) <= 1:
        print_usage()
    else:
        if sys.argv[1] == '-u':
            try:
                uid_str = sys.argv[2]
                uid_bytes = bytes.fromhex(uid_str)
                uid = struct.pack('8s', uid_bytes)
                print('UID read:', hex(int.from_bytes(uid, byteorder='big')))
                change_uid_from_template(uid)
                input('Dump file generated, press any key to start writing...')
                write_dump_to_card()
                os.remove('to_write.dump')
            except Exception as e:
                print('An error occurred:', e)
                print()
                print_usage()
        elif sys.argv[1] == '-l':
            try:
                check_devices()
            except Exception as e:
                print('An error occurred:', e)
                print()
                print_usage()
        elif sys.argv[1] == '-d':
            try:
                uid = dump_from_card()
                change_uid_from_template(uid)
                input('Dump file generated, press any key to start writing...')
                write_dump_to_card()
                os.remove('to_write.dump')
            except Exception as e:
                print('An error occurred:', e)
                print()
                print_usage()
        else:
            print_usage()


if __name__ == "__main__":
    main()