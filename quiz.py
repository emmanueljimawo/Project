'''

from cryptography.fernet import fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcnNep3hckQL0tMMdSn3BfdeSaIqr1pdWSKVpyw1mYxoj5HTR3rsEWT7hRAbDLIv0I88pa1sMwfXjfR4SXGFNRFwlZz82q9BbBP-BadOKnW83l9YHXTaS_ZJpRA5OKmg85PRDXc92iCBXsvkHVTQHq-HVd5SryhJjpJx8Zkek4nfNwudqtea1pTot4Li5Mubvk_7Zm'


def main():
    f = Fernet(Key)
    print(f.decrypt(massage))

if __name__ != "__main__":
    man()

'''


# Python==3.7.2
# cryptography==2.6.1

from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
message = b'gAAAAABcnNep3hckQL0tMMdSn3BfdeSaIqr1pdWSKVpyw1mYxoj5HTR3rsEWT7hRAbDLIv0I88pa1sMwfXjfR4SXGFNRFwlZz82q9BbBP-BadOKnW83l9YHXTaS_ZJpRA5OKmg85PRDXc92iCBXsvkHVTQHq-HVd5SryhJjpJx8Zkek4nfNwudqtea1pTot4Li5Mubvk_7Zm'

def main():
    f = Fernet(key)
    print(f.decrypt(message))



if __name__ == "__main__":
    main()

'''
Running the app from my terminal using python quiz.py, I got the output below:
b'https://engineering-application.britecore.com/e/t28e119s2t/testImplementationEngineer'
'''
