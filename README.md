<h1 align="center">YourSchoolBob</h1>

> I believe you know how to do it
* 파이썬 나이스 API 급식식단정보 프로그램

## 사용법
* **main.py**
```py
KEY = "" # 인증키
ATPT_OFCDC_SC_CODE = "" # 시도교육청코드
SD_SCHUL_CODE = "" # 행정표준코드
MMEAL_SC_CODE = "" # 식사코드
```
|변수명|타입|변수 설명|
|---|---|---|
|ATPT_OFCDC_SC_CODE|STRING(필수)|시도교육청코드|
|SD_SCHUL_CODE|STRING(필수)|행정표준코드|
|MMEAL_SC_CODE|STRING(선택)|식사코드|
|MLSV_YMD|STRING(선택)|급식일자|
|MLSV_FROM_YMD|STRING(선택)|급식시작일자|
|MLSV_TO_YMD|STRING(선택)|급식종료일자|

## 공식문서
* 공식문서는 [나이스 교육정보 개방 포털](https://open.neis.go.kr/portal/data/dataset/searchDatasetPage.do/)에서 확인하실 수 있습니다.
