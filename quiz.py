'''

from cryptography.fernet import fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcuXfAVFLkbi1HRj_SL2kcvaGzrIp-Hj0ZpDURX_RySRvumo_itr1HMf3vkieA6Fpy-pkYpTAfiIgFi6sCD7huAg84nt493bzFyWgg9S-9znzK8GX-ManTY8rddNItp2bKpFtUFlxrZSvDCXKojNv6JclP0Z1PlwJUayKbzDhuWFJGiLQikTnPWA3kfY6Sz42ftFbA'



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
message = b'gAAAAABcuXfAVFLkbi1HRj_SL2kcvaGzrIp-Hj0ZpDURX_RySRvumo_itr1HMf3vkieA6Fpy-pkYpTAfiIgFi6sCD7huAg84nt493bzFyWgg9S-9znzK8GX-ManTY8rddNItp2bKpFtUFlxrZSvDCXKojNv6JclP0Z1PlwJUayKbzDhuWFJGiLQikTnPWA3kfY6Sz42ftFbA'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

'''
Running the app from my terminal using python quiz.py, I got the output below:
b'https://engineering-application.britecore.com/e/t19e119s3t/testImplementationEngineer'
'''
