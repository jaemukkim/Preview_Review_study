import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 문제 3: Pandas GroupBy를 활용한 집계 데이터 분석

# 1. **Titanic 데이터셋 이해**
#    - seaborn 라이브러리로 titanic 데이터 로드: `sns.load_dataset('titanic')`
#    - 데이터 형태: 891행, 15개 열
#    - 주요 열: PassengerId, Survived, Pclass, Age, Sex, Fare, Embarked 등
#    - 결측값 확인: Age(177개), Cabin(687개), Embarked(2개) 결측
df = sns.load_dataset('titanic')
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.head())

# 2. **좌석 등급별 생존율 분석**
#    - `groupby('pclass')['survived'].mean()` 사용
#    - 예상 결과: 1등석 > 2등석 > 3등석 생존율
#    - 생존율 차이 해석
print("좌석 등급별 생존율:")
print(df.groupby('pclass')['survived'].mean().round(2))

# 3. **성별-좌석등급별 다중 집계**
#    - `groupby(['sex', 'pclass']).agg()` 사용
#    - 각 그룹별 나이 평균, 요금 최대값, 생존율 계산
#    - 가장 높은 생존율 그룹 찾기
print("성별-좌석등급별 다중 집계:")
result = df.groupby(['sex', 'pclass']).agg({'age':'mean', 'fare':'max', 'survived':'mean'}).round(2)
print(result)

high_group = result['survived'].idxmax()
high_survived_group = result.loc[high_group]
print(f"\n가장 높은 생존율 그룹 : \n{high_survived_group}")

# 4. **피벗 테이블 생성**
#    - 성별 × 좌석등급 생존율 피벗 테이블
#    - 히트맵으로 시각화하여 패턴 확인

# 모르겠어서 찾아보면서 함
pivot_table = df.pivot_table(values='survived', index='sex', columns='pclass', aggfunc='mean').round(2)
print("\n피벗 테이블:")
print(pivot_table)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='.2f')
plt.show()


# 5. **시각화**
#    - 좌석등급별 생존율 막대 그래프
#    - 성별-좌석등급 생존율 히트맵
#    - 연령대별 생존자 수
