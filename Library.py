def main():
    codes_file = open('A3 Codes.txt', 'r')
    validateCode(codes_file)
    codes_file.close()


def validateCode(codes_file):
    valid_codes = []
    invalid_codes = []
    invalid_restricted_codes = []
    code = codes_file.readline().rstrip()

    while code != '':
        if len(code) >= 10 and code[3:7].isdigit() and code[9].isupper():
            valid_codes.append(code)
            if int(code[3:7]) >= 2000 and code[9] == 'R':
                invalid_restricted_codes.append(code)
        else:
            invalid_codes.append(code)

        code = codes_file.readline().rstrip()

    print('Valid Code(s) are:', valid_codes)
    print('Invalid Code(s) are:', invalid_codes)
    print('Invalid Restricted Code(s) are:', invalid_restricted_codes)


main()
