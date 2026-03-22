# 1. 다음 벡터를 생성하고 내적 계산
#    - v1 = [1, 2, 3, 4], v2 = [5, 6, 7, 8]
#    - np.dot() 또는 @ 연산자 사용
#    - 결과 출력 및 수동 검증

from pandas.core.groupby import GroupBy
from pandas import DataFrame
import numpy as np
import pandas as pd

# 1. v1 과 v2를 만든다

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

# 2. np.dot() 또는 @ 연산자를 사용한다.
# 2-1. 여기서 문제가 발생할수있는 상황 ==> v1 과 v2를 v1 = [1,2,3,4] 이런식으로 파이썬 리스트를 생성하면 계산이 안된다.

 
# 3. 결과 출력 
print(f"dot을 활용 한 결과 값 : {np.dot(v1,v2)}")
print(f"@을 활용 한 결과 값 : ",v1@v2)

# 4. 수동 검증
print("수동검증 = 1x5 + 2x6 + 3x7 + 4x8 ==> 5+12+21+32 = 70" )

# 2. 행렬 곱셈 수행
#    - 2×3 행렬 A와 3×2 행렬 B 생성
#    - A @ B 계산 (결과: 2×2 행렬)

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8],[9, 10],[11, 12]])

print(np.dot(a,b))

print("수동 검증 : [ 1*7 + 2*9 + 3*11 ] => 58"," [ 1*8 + 2*10 + 3*12 ] => 64")
print("수동 검증 : [ 4*7 + 5*9 + 6*11 ] => 139"," [ 4*8 + 5*10 + 6*12 ] => 154")

# 2. 벡터 c를 만든다.
# np.array()를 사용하면 리스트를 "수학적 벡터"로 사용할 수 있다.
c = np.array([3, 4, 5])

# L1 노름 계산
# np.linalg.norm(벡터, 1)
# 두 번째 인자 1은 "L1 노름을 계산하라"는 의미이다.
# L1 노름 공식: |3| + |4| + |5|
print(f"L1 : {np.linalg.norm(c,1)}")

# L2 노름 계산
# np.linalg.norm(벡터, 2)
# 두 번째 인자 2는 "L2 노름을 계산하라"는 의미이다.
# L2 노름 공식: √(3² + 4² + 5²)
print(f"L2 : {np.linalg.norm(c,2)}")

# L∞ 노름 계산
# np.linalg.norm(벡터, np.inf)
# np.inf는 "무한대"를 의미한다.
# 이는 L∞ 노름을 계산하라는 뜻이다.
# L∞ 공식: 값들 중 절댓값이 가장 큰 것

# 계산된 값을 화면에 출력한다.
print(f"L3 : {np.linalg.norm(c, np.inf)}")

# 계산된 값을 화면에 출력한다.

# 4. 조건부 인덱싱
#    - 배열 data = [1, 5, 3, 8, 2, 9, 4, 7, 6]
#    - 5보다 큰 값 추출
#    - 3 이상 7 이하 값 추출
#    - 짝수 값 추출

data = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])

print("5보다 큰수 : ", data[data > 5])
print("3이상 7이하 : ", data[(data >= 3) & (data <= 7)])
print("짝수만 출력 : ", data[data % 2 == 0])





#  2번문제

# 1. **DataFrame 생성 및 기본 정보 확인**
#    - 딕셔너리로부터 DataFrame 생성 (8명의 직원 데이터)
#    - 속성: 이름, 나이, 도시, 급여, 부서, 경력
#    - `df.info()`, `df.describe()` 사용하여 데이터 개요 파악

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
        'name': ['김철수', '이영희', '박민수', '최지영', '정태현', '한소희', '윤상호', '배수진'],
        'age': [25, 30, 35, 28, 42, 31, 29, 27],
        'city': ['서울', '부산', '대구', '서울', '광주', '서울', '부산', '대구'],
        'salary': [3500, 4200, 3800, 4500, 5200, 3900, 3600, 4100],
        'department': ['개발', '마케팅', '개발', '기획', '개발', '마케팅', '기획', '개발'],
        'experience': [2, 5, 8, 3, 12, 6, 4, 3]
    }

df = pd.DataFrame(data)
if __name__ == "__main__":
    print("DataFrame :",df)

    print("\nInfo:",df.info())

    print("\nDescribe :", df.describe())

    print("\nDescribe (all) :")


# 2. **단일 조건 필터링**
#    - 나이가 30 이상인 직원 추출
#    - 특정 도시(예: 서울) 거주 직원 찾기
#    - 급여가 4000 이상인 직원 필터링
    
if __name__ == "__main__":
    print("나이가 30 이상인 직원 : ", df[df['age'] >= 30])

    print("\n서울에 거주하는 직원 : ",df[df['city'] == '서울'])

    print("\n급여가 4000 이상인 직원 : ", df[df['salary'] >= 4000])


# 3. **복합 조건 필터링**
#    - AND 연산: 서울 거주 **AND** 급여 4000 이상
#    - OR 연산: 개발팀 **OR** 급여 4500 이상
#    - NOT 연산: 개발팀이 아닌 직원
    
print("서울 거주 AND 급여 4000 이상 : ", df[(df['city'] == '서울') & (df['salary'] >= 4000)])

print("\n개발팀 OR 급여 4500 이상 : " , df[(df['department'] == '개발') | (df['salary'] >= 4500)])

print("\n개발팀이 아닌 직원 : ", df[df['department'] != '개발'])


# 4. **기본 통계 및 집계**
#    - 부서별 평균 급여 계산
#    - 도시별 직원 수
#    - 경력 통계 분석

print("부서별 평균 급여 : ", df.groupby('department')['salary'].mean() )

print("\n도시별 직원 수 : ",  df.groupby('city')['name'].count())

print("\n경력 통계 분석 : ", df.groupby('experience').agg({'salary':'mean','age':'mean'}) )