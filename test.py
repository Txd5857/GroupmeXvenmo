import email
import imaplib
import jsonpickle.pickler
import requests

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
umm = 'tenzindhondup1@gmail.com'
pwd = 'tenzinlama123'
mail.login(umm,pwd)

class JSONRequest:

    def __init__(self, text, bot_id):
        self.bot_id = bot_id
        self.text = text

def loop():
    mail.select("inbox")
    n=0
    ( retcode,messages)=mail.search(None,'(UNSEEN)')
    if retcode == 'OK':
        mail_ids = messages[0]
        id_list = mail_ids.split()
        if id_list == []:
            return None
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        typ, data = mail.fetch(str(latest_email_id), '(RFC822)' )

        for response_part in data:
            if isinstance (response_part, tuple):
                original = email.message_from_string(response_part[1].decode("utf-8"))
                sender = original['From']
                emaill = emailExtract(sender)
                #print("Got it: ", emaill)
                if emaill == "venmo@venmo.com":
                    print("Got it: ", emaill)
                    print("Got it")
                    data = original['Subject']
                    myurl = "https://api.groupme.com/v3/bots/post"
                    botID = "98eabc52d6a07d64f0b5c14a63"
                    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
                    to_post = jsonpickle.encode(JSONRequest(data,botID), unpicklable=False)
                    r = requests.post(myurl, data= to_post, headers =headers)
                    print(to_post)
                    print (data)


def emailExtract(string):
    arr = string.split("<")
    return arr[1][:-1]

if __name__ == '__main__':
    try:
        while True:
            loop()
    finally:
        print( "Thanks")
