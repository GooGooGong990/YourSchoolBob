import os
import re
import requests
from datetime import datetime

KEY = "" 
ATPT_OFCDC_SC_CODE = ""
SD_SCHUL_CODE = ""
MMEAL_SC_CODE = ""

try:
    today = datetime.today()
    date = today.strftime("%Y%m%d")

    response = requests.get(f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={KEY}&Type=json&pIndex=1&pSize=5&ATPT_OFCDC_SC_CODE={ATPT_OFCDC_SC_CODE}&SD_SCHUL_CODE={SD_SCHUL_CODE}&MMEAL_SC_CODE={MMEAL_SC_CODE}&MLSV_YMD={date}")
    result = response.json()["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].replace("<br/>", "\n")

    cleaned = re.sub(r"\s*\(\d+(?:\.\d+)*\)", "", result)

    lines = cleaned.split("\n")
    free = []
    filtered = []

    for i in lines:
        if "(자율)" in i:
            free.append(i.replace("(자율)", "").strip())
        else:
            filtered.append(i.strip())

    result = "\n".join(filtered)
    free = "\n".join(free)

    print("ㅡㅡㅡㅡㅡ 급식 ㅡㅡㅡㅡㅡ")
    print(result)
    print()
    print("ㅡㅡㅡㅡㅡ 자율 ㅡㅡㅡㅡㅡ")
    print(free)
    print()

    os.system("pause")
except:
    print("오류가 발생했습니다.")
    print()
    os.system("pause")
