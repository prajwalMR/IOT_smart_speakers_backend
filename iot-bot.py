import json 
import requests
import time



TOKEN = "463773549:AAFzM-7tSC8MdtD57Q7gKkVq9Johsc53IXw"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    print(last_update)
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    update_id = updates["result"][last_update]["update_id"]
    return (text, chat_id,update_id)


def send_message_list(text,chat_id,reply_markup=None):
    print("Quering!!")
    dataTosend = ""
    print(text)
    j = 0;
    for keys,values in text.items():
        i=0;
        # print(keys)
        # print(values)
        for value in values:
            dataTosend += str(j+1)+"."+keys+"-"+value[0]+","+value[1]+"\n"
            j=j+1;
            i=i+1;
    # for i in range(0,len(text)):
        # dataTosend += str(i+1)+"."+text[i][1]+","+text[i][2]+","+text[i][3]+"\n"
    url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format(dataTosend, chat_id, reply_markup)
    # url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def send_message(values,chat_id,reply_markup=None):
    print("Quering!!")
    dataTosend = ""
    print(values)
    i = 0;
    for value in values:
        item = value.split(",")
        dataTosend += str(i+1)+"."+item[2]+"-"+item[1]+","+item[3]+"\n"
        i=i+1;

    url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format(dataTosend, chat_id, reply_markup)
    # url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def build_keyboard():
    keyboard = [["List"],["Very Important"],["Important"]]
    reply_markup = {"keyboard":keyboard}
    return json.dumps(reply_markup)

def main():
    last_textchat = (None, None, None)
    while True:
        text, chat, update_id = get_last_chat_id_and_text(get_updates())
        print(text,chat,update_id)
        if (update_id) != last_textchat[2]:
            if(text.lower() == 'start'):
                keyboard = build_keyboard()
                #   text = toSend
                r = requests.get('http//ef2a7134.ngrok.io/playsong')
                print r.status_code,"Done"
                # url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format("Playing Song", chat_id)
            elif(text.lower() == 'stop'):
                keyboard = build_keyboard()
                # text = dict1.very_important_events()
                r = requests.get('http://ef2a7134.ngrok.io/stopsong')
                print r.status_code, "Done"
                # url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format("Stoping Song", chat_id)
            elif(text.lower() == 'high'):
                keyboard = build_keyboard()
                # text = dict1.important_events()
                r = requests.get('http://ef2a7134.ngrok.io/volumeup')
                print r.status_code, "Done"         
                # url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format("Volume Up", chat_id)
            elif(text.lower() == 'low'):
                keyboard = build_keyboard()
                # text = dict1.important_events()
                r = requests.get('http://ef2a7134.ngrok.io/volumedown')
                print r.status_code, "Done"
                # url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format("Volume Down", chat_id)
            elif(text.lower() == 'next'):
                keyboard = build_keyboard()
                # text = dict1.important_events()
                r = requests.get('http://ef2a7134.ngrok.io/nextsong')
                print r.status_code, "Done"
                # url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format("Next Song", chat_id)
            elif(text.lower() == 'previous'):
                keyboard = build_keyboard()
                # text = dict1.important_events()
                r = requests.get('http://ef2a7134.ngrok.io/lastsong')
                print r.status_code, "Done"
                # url = URL + "sendMessage?text={}&chat_id={}&reply_markup={}".format("Previous Song", chat_id)
            else:
                print('Waiting For query')
            last_textchat = (text, chat, update_id)
            # print("Last Text",text, chat, update_id)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
