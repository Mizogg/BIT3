# MUST EDIT LINE 8 Username LINE 9 Password LINE 40 Send to email basic send to email no save to file or any other extras
from bit import *
from bit.format import bytes_to_wif
import random
import urllib.request
import smtplib
gmail_user = 'youremail@gmail.com'
gmail_password = 'YOURPASSWORD' # You may have to make a app password under your google account https://support.google.com/accounts/answer/185833?hl=en
x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
count=0
total=0
while True:
    ran= random.randint(x,y)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    caddr = key.address
    uaddr = key1.address
    saddr = key.segwit_address
    count+=1
    total+=3
    contents1 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + caddr).read()
    contents2 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + uaddr).read()
    contents3 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + saddr).read()
    print ('Scan Number : ', str (count), ' : ' + 'Total Wallets Checked : ', str (total), ':COMPRESSED= ', str(contents1.decode('UTF8')), ':UNCOMPRESSED= ', str(contents2.decode('UTF8')), ':SEGWIT= ', str(contents3.decode('UTF8')), end='\r')
    if int(contents1) > 0 or int(contents2) > 0 or int(contents3) > 0:
        print('\n <=========== WINNER Total Received Ammount WINNER ===========>\n', '\nCongraz BTC COMPRESSED wallet with a Received    : ', caddr, '        : Received= ', str(contents1.decode('UTF8')), '\nCongraz BTC UNCOMPRESSED wallet with a Received  : ', uaddr, '        : Received= ', str(contents2.decode('UTF8')), '\nCongraz BTC SEGWIT wallet with a Received        : ', saddr, '        : Received= ', str(contents3.decode('UTF8')),'\nPrivateKey (wif) Compressed : ', wif1, '\nPrivateKey (wif) UnCompressed : ', wif, '\nMatching Key ==== Found!!! PrivateKey  (hex): ', key.to_hex(), '\nMatching Key ==== Found!!! PrivateKey  (dec): ', seed)
        sent_from = gmail_user
        to = ['youremail@gmail.com', 'anotheremail@gmail.com'] # ['youremail@gmail.com'] to just you or send to more add ,
        subject = 'OMG Super Important Message'
        body = '\n=====Bitcoin Address with Total Received Ammount=====' + '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '  : Received = ' + str(contents1.decode('UTF8')) + '\nBitcoin Address UnCompressed :' + uaddr + '  : Received = ' + str(contents2.decode('UTF8')) + '\nBitcoin Segwit Address       :' + saddr + '  : Received = ' + str(contents3.decode('UTF8')) + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif + '\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====\n'
        
        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        
            print ('Email sent!')
        except:
            print ('Something went wrong...')