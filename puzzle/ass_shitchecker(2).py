logo = '''
   _____                          _    _       _
  / ____|                        | |  | |     (_)
 | (___   __ ___   ____   ___   _| |  | |_ __  _
  \___ \ / _` \ \ / /\ \ / / | | | |  | | '_ \| |
  ____) | (_| |\ V /  \ V /| |_| | |__| | | | | |
 |_____/ \__,_| \_/    \_/  \__, |\____/|_| |_|_|
                             __/ |
                            |___/
'''
# You must enter your phone number here, like this format 5556667777
# no space, no (, no ), no -, just digits!!!!! If this file is read-only, you can save as this file
PHONE_NUMBER = '13622816081'

#######################################

animal = '''
                                             ,d""7b.
                                           ,'    ,d^b.
                            __,SAVVYUNIb..d.    d'
              ,d""""-.  ,d""'              `"b.dP
            dP' ,___  `7b.                     `b
          `"788P'  `".   "                       `b
          ,d" `b      `"                          `7.
    `P""""7.   8)                                   7.
     `.    8  ,P               ,---.                 """"b.
      8.  d' ,P             ,d"   ,88b.         "b       `8
     d' `"  ,P             ""    ,P   `7b        `b     ,dP
    d'      8                    d       `b.      d8SAVVYUNI88b.
   ,'      d'                   ,8.     8   78""""""7SAVVYUNI' `"b.
   8b _   8P                 ,P'   `"""oo.,d"          ""788'     `7.
 .-""""8 d8'            ,-""7P                       .    `7.      ,8.
`b     8 88              ,d"8   d8b.                 8b    `b      d `.
  `b___8 88             '  ,8  dSAVVYUNI.           ; `b    8     ,P  8.
   8     88                8  d8"7P""8""""b..      ,8  `b  ,8"""""8'  88
   8     `b ,d"'           7  8  8   8   ,8. 7P--,dP   ,8"'     ,8' _,d8.
   7.     8d"                 8 ,db.P""bd' `7P ,d""""""""""""""""""'    8
   `b     d'                  8P'  8   88  ,P"'                         8
    7. _,d'                   7b  ,d88888"'                            d'
    ,P' '8                     SAVVYUNI'                               8
   ,P   88                     `888P'                                  8
  ,8_mGk_8                       "'                                   d'
        "8                                                    ,'     d'
         `b                                                  d8b..d""
          `b                                              ,dP'
           `7.                           ______________,d""
             `7b.                     ,d""
                `7b..             _,d"'
                     """--....-"""'
'''

TESTSET_ID = 43
VERSION = 200000000
FILES = ['sudoku_puzzle', 'solver', 'word_ladder_puzzle', 'expression_tree', 'expression_tree_puzzle']

disclaimer = u'''\u4ec5\u9650\u0053\u0061\u0076\u0076\u0079\u0055\u006e\u0069\u0020\u0058\u0020\u4e00\u52fe\u0043\u0053\u5927\u8bfe\u5802\u5b66\u751f\u4f7f\u7528\u000d\u000a\u000d\u000a\u8bf7\u786e\u4fdd\u6bcf\u6b21\u4fdd\u5b58\u4f5c\u4e1a\u6587\u4ef6\u4ee5\u540e\u518d\u5207\u6362\u5230\u8fd9\u4e2a\u6587\u4ef6\u8fd0\u884c\u000d\u000a\u8bf7\u786e\u4fdd\u9664\u4e86\u586b\u5199\u7535\u8bdd\u4ee5\u5916\u4e0d\u8981\u6539\u52a8\u8fd9\u4e2a\u6587\u4ef6\u000d\u000a\u0048\u0061\u0070\u0070\u0079\u0020\u0043\u006f\u0064\u0069\u006e\u0067\u0021\u000d\u000a'''


def print_message(message: str, priority: int = 0):
    # Print readable message
    if priority == 0:
        print(message, flush=True)
    elif priority == 1:
        print("===========================")
        print(message, flush=True)
        print("===========================")
    elif priority == 2:
        # Poop
        print("\U0001F4A9" * 10)
        print(message, flush=True)
        print("\U0001F4A9" * 10)
    elif priority == 8:
        # Heart
        print("\U0001F497" * 10)
        print(message, flush=True)
        print("\U0001F497" * 10)


def get_file_hash_string(file_name, skip=0):
    import hashlib
    hasher = hashlib.md5()
    buffer_size = 4096
    with open(file_name, 'r') as f:
        for i in range(skip):
            f.readline()
        buf = f.read(buffer_size)
        while len(buf) > 0:
            hasher.update(buf.encode('utf-8'))
            buf = f.read(buffer_size)
    file_hash = hasher.hexdigest()
    return file_hash


def get_file_hash(file_name, skip=0):
    import hashlib
    hasher = hashlib.md5()
    buffer_size = 4096
    with open(file_name, 'rb') as f:
        f.read(skip)
        buf = f.read(buffer_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(buffer_size)
    file_hash = hasher.hexdigest()
    return file_hash


def check_file_hash(m: str) -> bool:
    '''Check if the target file changed since last tester run'''
    result = True
    file_name = m + '.py'
    file_hash = get_file_hash(file_name)
    try:
        with open('savvyuni.log', 'r') as f:
            last_hash = f.readline().strip()
            result = last_hash != file_hash
    except:
        # do nothing, first run
        pass
    with open('savvyuni.log', 'w') as f:
        f.write(file_hash)
    return result


ohshit = b'CnRyeToKICAgIGZyb20gdXVpZCBpbXBvcnQgZ2V0bm9kZSBhcyBnZXRfbWFjCiAgICBtYWMgPSBzdHIoaGV4KGdldF9tYWMoKSkpWzI6XS51cHBlcigpCiAgICBpbXBvcnQgcGxhdGZvcm0KICAgIGhvc3RfbmFtZSA9IHBsYXRmb3JtLnVuYW1lKCkubm9kZQogICAgaW1wb3J0IG9zCiAgICBob3N0X25hbWUgPSBvcy5lbnZpcm9uLmdldCgnTE9HTkFNRScsIGhvc3RfbmFtZSkKICAgIGhvc3RfbmFtZSA9IG9zLmVudmlyb24uZ2V0KCdDT01QVVRFUk5BTUUnLCBob3N0X25hbWUpCiAgICBob3N0X25hbWUgPSBob3N0X25hbWUudXBwZXIoKQogICAgaW1wb3J0IGpzb24KICAgIGZyb20gdXJsbGliIGltcG9ydCByZXF1ZXN0CiAgICBQQVJBTVMgPSB7fQogICAgUEFSQU1TWyd1cGxvYWQnXSA9ICd7fScKICAgIFBBUkFNU1snaG9zdCddID0gaG9zdF9uYW1lCiAgICBQQVJBTVNbJ3Bob25lX251bWJlciddID0gUEhPTkVfTlVNQkVSCiAgICBQQVJBTVNbJ21hY19hZGRyZXNzJ10gPSBtYWMKICAgIFBBUkFNU1sndmVyc2lvbiddID0gVkVSU0lPTgogICAgUEFSQU1TWydoYXNoJ10gPSBnZXRfZmlsZV9oYXNoX3N0cmluZyhfX2ZpbGVfXywgc2tpcD0yMCkKICAgIGRhdGEgPSBqc29uLmR1bXBzKFBBUkFNUykuZW5jb2RlKCd1dGYtOCcpCiAgICByZXEgPSByZXF1ZXN0LlJlcXVlc3QoImh0dHA6Ly9vbmVob29rLnB5dGhvbmFueXdoZXJlLmNvbS9zaGl0Y2hlY2tlci90ZXN0c2V0L3t9L2F1dGhlbnRpY2F0ZSIsIGRhdGE9ZGF0YSkKICAgIHJlcS5hZGRfaGVhZGVyKCdDb250ZW50LVR5cGUnLCAnYXBwbGljYXRpb24vanNvbicpCiAgICByZXEuYWRkX2hlYWRlcignQWNjZXB0LUVuY29kaW5nJywgJ1VURi04JykKICAgIHJlc3AgPSByZXF1ZXN0LnVybG9wZW4ocmVxKQogICAgcmVzdWx0X2RhdGEgPSBqc29uLmxvYWRzKHJlc3AucmVhZCgpKQogICAgZXhjZXB0aW9uID0gTm9uZQogICAgc3VjY2VzcyA9IFRydWUKZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgcmVzdWx0X2RhdGEgPSBOb25lCiAgICBleGNlcHRpb24gPSBlCiAgICBzdWNjZXNzID0gRmFsc2UK'
NETWORK_FAIL_MESSAGE = '\u8bf7\u4f60\u786e\u4fdd\u4f60\u6709\u7f51\u7edc\u8fde\u63a5\u540c\u65f6\u4f60\u9664\u4e86\u5728\u6700\u4e0a\u9762\u586b\u5199\u7535\u8bdd\u53f7\u7801\u4ee5\u5916\u6ca1\u6709\u6539\u4efb\u4f55\u4ee3\u7801\u000d\u000a\u5982\u679c\u4f60\u4eba\u5728\u56fd\u5185\uff0c\u4f60\u6709\u53ef\u80fd\u9700\u8981\u0056\u0050\u004e'
TEST_SET_NOT_FOUND_MESSAGE = '\u627e\u4e0d\u5230\u6d4b\u8bd5\u6570\u636e\uff0c\u8bf7\u786e\u5b9a\u4f60\u6ca1\u6539\u6211\u7684\u6587\u4ef6'
PERMISSION_NOT_FOUND_MESSAGE = '\u60a8\u7684\u7535\u8bdd\u53f7\u7801\u6ca1\u6709\u4f7f\u7528\u0063\u0068\u0065\u0063\u006b\u0065\u0072\u7684\u6743\u9650\u000d\u000a\u8fd9\u8bf4\u660e\u60a8\u4e0d\u662f\u0053\u0061\u0076\u0076\u0079\u0055\u006e\u0069\u0020\u0058\u0020\u4e00\u52fe\u0043\u0053\u5927\u8bfe\u5802\u7684\u5b66\u751f\u000d\u000a\u000d\u000a\u5f88\u9057\u61be\u4ee5\u524d\u7684\u0063\u0068\u0065\u0063\u006b\u0065\u0072\u88ab\u76d7\u7528\u7684\u592a\u5389\u5bb3\uff0c\u6240\u4ee5\u53ea\u597d\u52a0\u5165\u4e86\u9632\u76d7\u63aa\u65bd\u000d\u000a\u000d\u000a\u5982\u679c\u60a8\u662f\u6211\u7684\u5b66\u751f\uff0c\u8bf7\u60a8\u5fae\u4fe1\u8054\u7cfb\u6211\u000d\u000a\u5982\u679c\u60a8\u60f3\u62a5\u540d\u6211\u7684\u8bfe\uff0c\u4e5f\u8bf7\u5fae\u4fe1\u8054\u7cfb\u6211\u000d\u000a\u6216\u8005\u4f60\u4e5f\u53ef\u4ee5\u8054\u7cfb\u0053\u0061\u0076\u0076\u0079\u0055\u006e\u0069\u5c0f\u52a9\u624b\u000d\u000a\u000d\u000a\u6211\u7684\u5fae\u4fe1\u003a\u0020\u0038\u0034\u0032\u0039\u0033\u0032\u0032\u0031'
TEST_SET_USER_NOT_SAME_MESSAGE = '\u4f60\u6709\u53ef\u80fd\u6b63\u5728\u4f7f\u7528\u672a\u7ecf\u6388\u6743\u5206\u4eab\u7684\u0063\u0068\u0065\u0063\u006b\u0065\u0072\u000d\u000a\u5982\u679c\u4f60\u662f\u0053\u0061\u0076\u0076\u0079\u0055\u006e\u0069\u0020\u0058\u0020\u4e00\u52fe\u0043\u0053\u5927\u8bfe\u5802\u7684\u5b66\u751f\uff0c\u8bf7\u8ddf\u6211\u8054\u7cfb\uff0c\u9644\u4e0a\u4f60\u7684\u7535\u8bdd\u53f7\u7801\u000d\u000a\u5982\u679c\u4f60\u4e0d\u662f\u6211\u7684\u5b66\u751f\uff0c\u4e0d\u597d\u610f\u601d\u8bf7\u4f60\u5c0a\u91cd\u6211\u7684\u52b3\u52a8'
INVALID_DATA_MESSAGE = '\u6570\u636e\u6709\u8bef\u000d\u000a\u8bf7\u786e\u4fdd\u4f60\u5728\u6587\u4ef6\u6700\u4e0a\u9762\u586b\u5199\u4e86\u7535\u8bdd\u53f7\u7801\u000d\u000a\u540c\u65f6\u8bf7\u4e0d\u8981\u5984\u56fe\u7834\u89e3\u6211\u7684\u0063\u0068\u0065\u0063\u006b\u0065\u0072'
BLACK_LISTED_MESSAGE = '\u4e0d\u597d\u610f\u601d\uff0c\u60a8\u5728\u6211\u7684\u9ed1\u540d\u5355\u4e0a\uff0c\u0038\u0038'
TESTSET_NOT_ENABLED_MESSAGE = 'Test is disabled'
UNKNOWN_ERROR_MESSAGE = '\u672a\u77e5\u9519\u8bef\uff0c\u8ddf\u6211\u8054\u7cfb'
CHECKER_CHANGED = '\u4f60\u6216\u8005\u5728\u4f7f\u7528\u65e7\u7248\u7684\u0063\u0068\u0065\u0063\u006b\u0065\u0072\u000d\u000a\u6216\u8005\u4f60\u9664\u4e86\u586b\u5199\u7535\u8bdd\u53f7\u7801\u4ee5\u5916\uff0c\u6539\u53d8\u4e86\u6211\u0063\u0068\u0065\u0063\u006b\u0065\u0072\u4efb\u4f55\u5730\u65b9\u7684\u4ee3\u7801\u000d\u000a\u8bf7\u4e0b\u8f7d\u6211\u5728\u7fa4\u91cc\u53d1\u7684\u6700\u65b0\u7684\u7248\u672c\uff0c\u53ea\u80fd\u586b\u5199\u7535\u8bdd\u53f7\u7801\uff0c\u5176\u4ed6\u4f60\u6539\u4e86\u6211\u90fd\u77e5\u9053'

NO_PHONE_NUMBER_MESSAGE = '\u8bf7\u786e\u4fdd\u4f60\u586b\u5199\u7535\u8bdd\u53f7\u7801\u5728\u6700\u4e0a\u9762\uff0c\u8fd9\u6837\u683c\u5f0f\u000d\u000a\u0050\u0048\u004f\u004e\u0045\u005f\u004e\u0055\u004d\u0042\u0045\u0052\u0020\u003d\u0020\u0027\u0035\u0035\u0035\u0036\u0036\u0036\u0037\u0037\u0037\u0037\u0027\u000d\u000a\u5e76\u4e14\u4f60\u586b\u5199\u5b8c\u4ee5\u540e\u4fdd\u5b58\u4e86\u8fd9\u4e2a\u6587\u4ef6\u0020\u000d\u000a\u5982\u679c\u4f60\u4e0b\u8f7d\u4ee5\u540e\u8fd9\u4e2a\u6587\u4ef6\u662f\u0072\u0065\u0061\u0064\u002d\u006f\u006e\u006c\u0079\u6a21\u5f0f\uff0c\u53ef\u4ee5\u53e6\u5b58\u4e3a\u0028\u0073\u0061\u0076\u0065\u002d\u0061\u0073\u0029\uff0c\u8fd9\u4e2a\u6587\u4ef6\u7684\u540d\u5b57\u4e0d\u91cd\u8981\uff0c\u53ea\u8981\u4f60\u9664\u4e86\u7535\u8bdd\u53f7\u7801\u586b\u5199\u4ee5\u5916\u4e0d\u6539\u53d8\u4efb\u4f55\u5176\u4ed6\u4fe1\u606f\u5373\u53ef\u000d\u000a'
PHONE_NUMBER_FORMAT_ERROR = '\u4e0a\u9762\u90fd\u5199\u4e86\u7535\u8bdd\u683c\u5f0f\u5c31\u662f\u5168\u6570\u5b57\uff0c\u4e0d\u7528\u002d\u6216\u8005\u0028\u6216\u8005\u7a7a\u683c\u000d\u000a\u4e0d\u8bfb\u9898\u771f\u53ef\u6015\u000d\u000a'
PHONE_NUMBER_NO_COUNTRY_CODE = '\u7535\u8bdd\u53f7\u7801\u4e0d\u7528\u586b\u5199\u56fd\u5bb6\u53f7'
PHONE_NUNBER_FORMAT_ERROR = '\u4f60\u8fde\u7535\u8bdd\u53f7\u7801\u683c\u5f0f\u6216\u8005\u4e00\u5171\u51e0\u4e2a\u6570\u5b57\u90fd\u4e0d\u77e5\u9053\u4e48\u002e\u002e\u002e\u002e'


def compress_and_encode(code: str):
    """
    Compress and encode code string into b64 string.
    """
    import zlib
    import base64
    encoded_code = code.encode('utf-8')
    compressed_code = zlib.compress(encoded_code)
    return base64.b64encode(compressed_code).decode('utf-8')


def decompress_and_decode(raw: str):
    """
    Decompress code.
    """
    import zlib
    import base64
    return zlib.decompress(base64.b64decode(raw.encode('utf-8'))).decode('utf-8')


def step1() -> str:
    if PHONE_NUMBER == '' or not isinstance(PHONE_NUMBER, str):
        print_message(NO_PHONE_NUMBER_MESSAGE, priority=1)
        exit()
    elif '-' in PHONE_NUMBER or '(' in PHONE_NUMBER or ')' in PHONE_NUMBER or ' ' in PHONE_NUMBER:
        print_message(PHONE_NUMBER_FORMAT_ERROR, priority=1)
        exit()
    elif not PHONE_NUMBER.isdigit() or (len(PHONE_NUMBER) != 10 and len(PHONE_NUMBER) != 11):
        print_message(PHONE_NUNBER_FORMAT_ERROR, priority=1)
        exit()

    payload = {}
    import base64

    uploads = []
    for name in FILES:
        with open(name + '.py') as f:
            uploads.append(f.read())
    upload = '\n'.join(uploads)
    bullshit = base64.b64decode(ohshit).decode('utf-8').format(payload, compress_and_encode(upload), TESTSET_ID)
    exec(bullshit, globals())

    if exception is not None:
        print('\U0001F480' * 20)
        print(exception)
        print('\U0001F480' * 20)
        print_message(NETWORK_FAIL_MESSAGE, priority=1)
        exit()

    result_type = result_data['type']
    result_message = result_data['message']
    result_code = result_data.get('code', None)

    if result_message is not None and len(result_message) > 0:
        print_message(result_message, priority=1)

    if result_type == 'ShitCheckerResult.OK':
        return result_code
    elif result_type == 'ShitCheckerResult.TESTSET_NOT_FOUND':
        if result_code is not None:
            exec(result_code)
        print_message(TEST_SET_NOT_FOUND_MESSAGE, priority=1)
        exit()
    elif result_type == 'ShitCheckerResult.PERMISSION_NOT_FOUND':
        if result_code is not None:
            exec(result_code)
        print_message(PERMISSION_NOT_FOUND_MESSAGE, priority=1)
        exit()
    elif result_type == 'ShitCheckerResult.TESTSET_USER_HOST_NOT_SAME':
        if result_code is not None:
            exec(result_code)
        print_message(TEST_SET_USER_NOT_SAME_MESSAGE, priority=1)
        exit()
    elif result_type == 'ShitCheckerResult.INVALID_DATA':
        if result_code is not None:
            exec(result_code)
        print_message(INVALID_DATA_MESSAGE, priority=1)
        exit()
    elif result_type == 'ShitCheckerResult.BLACK_LISTED':
        if result_code is not None:
            exec(result_code)
        print_message(BLACK_LISTED_MESSAGE, priority=1)
        exit()
    elif result_type == 'ShitCheckerResult.TESTSET_NOT_ENABLED':
        if result_code is not None:
            exec(result_code)
        print_message(TESTSET_NOT_ENABLED_MESSAGE, priority=1)
        exit()
    elif result_type == 'ShitCheckerResult.CHECKER_CHANGED':
        if result_code is not None:
            exec(result_code)
        print_message(CHECKER_CHANGED, priority=1)
        exit()
    else:
        print_message(result_type + ":" + UNKNOWN_ERROR_MESSAGE, priority=1)
        exit()


def launch(number, glo, loc):
    print(logo)
    print(disclaimer)
    global PHONE_NUMBER
    PHONE_NUMBER = number
    shit_just_got_real = step1()
    if shit_just_got_real is None:
        print_message('\u53d1\u751f\u4e86\u672a\u77e5\u9519\u8bef\u0020\u0031\u0030\u0030\u0035', priority=1)
        exit()
    # from shitchecker_data import get_checker
    # shit_just_got_real = get_checker(43, path='../../flask_savvy/')
    exec(decompress_and_decode(shit_just_got_real), glo, loc)


if __name__ == '__main__':
    number = PHONE_NUMBER
    try:
        import sys
        number = sys.argv[1]
    except Exception as e:
        pass
    launch(number, globals(), locals())
