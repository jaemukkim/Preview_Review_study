## 주제 5: 날짜와 시간 처리 함수 구현
#Python의 `datetime`, `timedelta`, `calendar` 모듈을 활용하여 다음 5개의 날짜 처리 함수를 구현하세요.

from datetime import datetime
import calendar
from datetime import timedelta

def validate_date(date_str:str, format="%Y-%m-%d") -> bool:
    """날짜 형식 검증"""
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def get_weekday_name(index:int) -> str:
    """한국어 요일/월 이름"""
    WEEKDAY_NAMES = ["월", "화", "수", "목", "금", "토", "일"]
    return WEEKDAY_NAMES[index]

def get_holidays_of_2024() -> dict:
    """한국 공휴일 (2024년)"""
    return {
        "2024-01-01": "신정", "2024-03-01": "삼일절", "2024-05-05": "어린이날",
        "2024-06-06": "현충일", "2024-08-15": "광복절", "2024-10-03": "개천절",
        "2024-10-09": "한글날", "2024-12-25": "크리스마스"
    }

## 문제: 나이 계산기 
# 생년월일을 입력받아 현재 나이(만 나이)와 다양한 정보를 출력하는 함수를 작성하세요.

def calculate_age_info(birth_date):
    if not validate_date(birth_date):
        print("형식에 맞게 작성해주세요. YYYY-MM-DD")
        return

    birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.now()
    #만 나이 계산
    age = today.year - birth_dt.year - ((today.month, today.day) < (birth_dt.month, birth_dt.day)) # 생일 안 지났으면 1, 지났으면 0 
    return {
        "만 나이" : age,
        "태어난 요일" : get_weekday_name(birth_dt.weekday()),
        "살아온 총 일수" : (today - birth_dt).days,
        "올해 생일 통과 유무" : (today.month, today.day) >= (birth_dt.month, birth_dt.day) # 현재날짜가 생일날짜보다 크면 True
    }
# **출력 예시:**
# - 만 나이
# - 태어난 요일
# - 살아온 총 일수
# - 올해 생일 통과 유무
print("생년월일을 입력하세요 YYYY-MM-DD")
birth_dt = input()
print(calculate_age_info(birth_dt))



## 문제: 근무일 계산기 
# 시작일과 종료일을 입력받아 주말과 공휴일을 제외한 실제 근무일을 계산하는 함수를 작성하세요.

def calculate_working_days(start_date, end_date, holidays=None):
    if not validate_date(start_date):
        print("시작일을 형식에 맞게 작성해주세요. (YYYY-MM-DD)")
        return
    elif not validate_date(end_date):
        print("종료일을 형식에 맞게 작성해주세요. (YYYY-MM-DD)")
        return
        

    st_dt = datetime.strptime(start_date, "%Y-%m-%d")
    ed_dt = datetime.strptime(end_date, "%Y-%m-%d")
    holidays = get_holidays_of_2024()

    working_days = 0 # 근무일수
    weekends = 0     # 주말
    holiday_cnt = 0  # 공휴일
    #총 일수 계산
    total_days = (ed_dt - st_dt).days + 1
    
    for i in range(total_days):
        # 현재 날짜 계산
        current_date = st_dt + timedelta(days=i)
        #주말과 공휴일 확인
        is_weekend = current_date.weekday() >= 5
        is_holiday = current_date.strftime("%Y-%m-%d") in holidays

        if is_weekend:
            weekends +=1
        elif is_holiday:
            holiday_cnt +=1
        else: #공휴일과 주말이 아닌 경우
            working_days +=1

    return {
        "총 일수" : total_days,
        "주말 수" : weekends,
        "공휴일 수" : holiday_cnt,
        "실제 근무일" : working_days
    }

print("근무 시작일을 입력하세요. YYYY-MM-DD")
st_dt = input()
print("근무 종료일을 입력하세요. YYYY-MM-DD")
ed_dt = input()
print(calculate_working_days(st_dt, ed_dt))



## 문제: 프로젝트 일정 관리기
# 프로젝트 시작일과 소요 기간(근무일 기준)을 입력받아 완료 예정일을 계산하는 함수를 작성하세요.

# def calculate_project_schedule(start_date, duration_days, holidays=None):
#     """
#     프로젝트 시작일과 소요 기간으로 완료일을 계산합니다.
    
#     Args:
#         start_date (str): 프로젝트 시작일
#         duration_days (int): 소요 근무일
#         holidays (list): 공휴일 리스트
    
#     Returns:
#         dict: 프로젝트 일정 정보
#     """
#     start_date = datetime.strptime(start_date, "%Y-%m-%d")
#     duration_days = 
#     holidays = get_holidays_of_2024()


# **출력 예시:**
# - 프로젝트 완료 예정일
# - 소요 근무일
# - 총 달력 일수
# - 프로젝트 기간 중 공휴일 수
# - 마일스톤 날짜들 (25%, 50%, 75% 진행 시점)


