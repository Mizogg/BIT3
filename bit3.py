from bit import *
from bit.format import bytes_to_wif
import random
import urllib.request
import telebot #pip install pyTelegramBotAPI
import winsound
bot_id = open("bot_id.txt", "r").read().splitlines()[0]
bot = telebot.TeleBot(bot_id)
@bot.message_handler(commands=['start', 'stop'])
def send_welcome(message):
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 2500  # Set Duration To 1000 ms == 1 second
    count=0
    total=0
    while True:
        ran= random.randint(1809251394333065553493296640760748560207343510400633813116524750123642650624,115792089237316195423570985008687907853269984665640564039457584007913129639936)
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
            bot.reply_to(message,'\n🌟⭐️🌟 Bitcoin Address with Total Received Balance ⭐️🌟⭐️' + '\nPrivateKey (hex): ' + '\n' + key.to_hex() + '\nPrivateKey (dec): ' + '\n' + seed + '\nBitcoin Address Compressed : ' + '\n' + caddr + '\n Total Received Balance : ' + str(contents1.decode('UTF8')) + '\nBitcoin Address UnCompressed :' + '\n' + uaddr + '\n Total Received Balance : ' + str(contents2.decode('UTF8')) + '\nBitcoin Segwit Address :' + '\n' + saddr + '\n Total Received Balance : ' + str(contents3.decode('UTF8')) + '\nPrivateKey (wif) Compressed : ' + '\n' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + '\n' + wif + ' \n⭐️🌟⭐️🌟   Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD ⭐️🌟⭐️🌟 Found Total Received Balance ⭐️🌟⭐️🌟 ')
            f=open('winner.txt','a')
            f.write('\n=====Bitcoin Address with Total Received Ammount=====' + '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '  : Received = ' + str(contents1.decode('UTF8')) + '\nBitcoin Address UnCompressed :' + uaddr + '  : Received = ' + str(contents2.decode('UTF8')) + '\nBitcoin Segwit Address       :' + saddr + '  : Received = ' + str(contents3.decode('UTF8')) + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif + '\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====\n')
            f.close()
            winsound.Beep(frequency, duration)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
#Examples
#This has been made for Bitcoin Puzzle Transaction https://privatekeys.pw/puzzles/bitcoin-puzzle-tx
#Puzzle 1-10 (1,1023)     #TestScan # Already found 
#Puzzle 1-20 (1,1048575)     #TestScan # Already found 
#Puzzle 1-30 (1,1073741823)     #TestScan # Already found 
#Puzzle 1-63 (1,9223372036854775807)      # Already found
#Puzzle 64 (18446744073709551615,36893488147419103231)
#Puzzle 1-160 (1,1461501637330902918203684832716283019655932542975)
#Puzzle 64-160 (18446744073709551615,1461501637330902918203684832716283019655932542975)
#Puzzle 60 (576460752303423488,1152921504606846975)      # Already found
#Puzzle 70 (590295810358705651712,1180591620717411303423)      # Already found
#Puzzle 80 (1208925819614629174706176,2417851639229258349412351)
#Puzzle 90 (618970019642690137449562112,1237940039285380274899124223)
#Puzzle 100 (633825300114114700748351602688,1267650600228229401496703205375)
#Puzzle 110 (649037107316853453566312041152512,1298074214633706907132624082305023)
#Puzzle 120 (664613997892457936451903530140172288,1329227995784915872903807060280344575)
#Puzzle 130 (680564733841876926926749214863536422912,1361129467683753853853498429727072845823)
#Puzzle 140 (696898287454081973172991196020261297061888,1393796574908163946345982392040522594123775)
#Puzzle 150 (713623846352979940529142984724747568191373312,1427247692705959881058285969449495136382746623)
#Puzzle 160 (730750818665451459101842416358141509827966271488,1461501637330902918203684832716283019655932542975)
#Full Range Scan (1,115792089237316195423570985008687907852837564279074904382605163141518161494336)

#2^250
#1809251394333065553493296640760748560207343510400633813116524750123642650624

#2^251
#3618502788666131106986593281521497120414687020801267626233049500247285301248

#2^252
#7237005577332262213973186563042994240829374041602535252466099000494570602496

#2^253
#14474011154664524427946373126085988481658748083205070504932198000989141204992

#2^254
#28948022309329048855892746252171976963317496166410141009864396001978282409984

#2^255
#57896044618658097711785492504343953926634992332820282019728792003956564819968

#2^256
#115792089237316195423570985008687907853269984665640564039457584007913129639936
