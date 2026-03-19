import pandas as pd
import numpy as np
import seaborn as sns

# 1. **결측값 분석**
#    - Titanic 데이터의 결측값 시각화
#    - 각 열별 결측값 개수와 비율 계산
#    - Age 열: 177개 결측 (19.9%)
#    - Cabin 열: 687개 결측 (77.1%)
df = sns.load_dataset('titanic')
df_isnull = df.isnull().sum()
print(df.head())
print(df_isnull)

df_isnull / len(df) * 100


# 2. **전략 1: 삭제(Deletion)**
#    - `df.dropna(subset=['age'])` 사용
#    - 891행 → 714행 (177행 삭제)
#    - 데이터 손실률: 19.9%
#    - 장점: 데이터 품질 유지
#    - 단점: 정보 손실

# 3. **전략 2: 대체(Imputation) - 통계값 사용**
#    - 평균값 대체: `age.fillna(age.mean())`
#    - 중앙값 대체: `age.fillna(age.median())`
#    - 최빈값 대체: `age.fillna(age.mode()[0])`
#    - 장점: 데이터 크기 유지
#    - 단점: 분포 왜곡 가능

# 4. **전략 3: 고급 대체 - 그룹별 대체**
#    - 성별-좌석등급별 평균값으로 대체
#    - `groupby(['sex', 'pclass']).transform(lambda x: x.fillna(x.mean()))`
#    - 더 정교한 대체 가능
#    - 각 그룹별 평균값 출력

# 5. **결과 비교**
#    - 각 전략별 결측값 개수 확인
#    - 분포 변화 시각화
#    - 통계값 비교