import time

import requests #dependency

print("""
______  _                              _   _    _        _      _   _                _      _____                   _             
|  _  \(_)                            | | | |  | |      | |    | | | |              | |    /  ___|                 | |            
| | | | _  ___   ___   ___   _ __   __| | | |  | |  ___ | |__  | |_| |  ___    ___  | | __ \ `--.   ___  _ __    __| |  ___  _ __ 
| | | || |/ __| / __| / _ \ | '__| / _` | | |/\| | / _ \| '_ \ |  _  | / _ \  / _ \ | |/ /  `--. \ / _ \| '_ \  / _` | / _ \| '__|
| |/ / | |\__ \| (__ | (_) || |   | (_| | \  /\  /|  __/| |_) || | | || (_) || (_) ||   <  /\__/ /|  __/| | | || (_| ||  __/| |   
|___/  |_||___/ \___| \___/ |_|    \__,_|  \/  \/  \___||_.__/ \_| |_/ \___/  \___/ |_|\_\ \____/  \___||_| |_| \__,_| \___||_|   
                                                                                                                                  
                                                                                                                                  
""")

print("Made By ingpungya!")

print("잠시만 기다려주십시d오. 시동중 입니다.")

time.sleep(2)

url = input("웹후크 URL을 입력하여 주십시오. | ")
cond = input("웹후크 이름을 입력하여 주십시오. | ")
avturl = input("웹후크 아이콘 링크를 입력하여 주십시오. | ")
conn = input("웹후크의 일반 채팅을 입력하여 주십시오. | ")
conemad = input("웹후크 임베드 내용을 입력하여 주십시오. | ")
conetit = input("웹후크 임베드 제목을 입력하여 주십시오. | ")
counts = int(input("웹후크 전송 횟수를 입력하여 주십시오. | "))
countstime = input("웹후크 전송 딜레이를 입력하여 주십시오. | ")

time.sleep(1)

while counts > 0:
    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content": conn,
        "username": cond,
        "avatar_url" : avturl
    }

    # leave this out if you dont want an embed
    # for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"] = [
        {
            "description": conemad,
            "title": conetit
        }
    ]

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(str(err) + """
        20초뒤에 다시 전송을 시도 합니다.""")
        time.sleep(20)
    else:
        print("페이로드를 성공적으로 실행하였습니다., code {}.".format(result.status_code))
        print(str("다음 전송까지 ") + str(countstime) + str(" 초 남았습니다."))
        time.sleep(int(countstime))
        counts -= 1