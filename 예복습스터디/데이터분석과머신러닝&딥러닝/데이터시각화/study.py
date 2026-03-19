import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# **지시사항:**
# ##1. Gapminder 데이터셋을 불러오고, 2007년도 데이터만 필터링하세요.

# df = sns.load_dataset("gapminder")
# df = pd.DataFrame('gapminder')
# print(sns.get_dataset_names())

df = px.data.gapminder()
df_2007 = df[df["year"] == 2007]
print(df_2007.head())

# ##2. 2007년 데이터를 활용하여 아래 그래프를 하나의 Figure 안에 2개의 subplot으로 구성하세요.

# (1) 서브플롯 1: 산점도
# 	x축: gdpPercap
# 	y축: lifeExp
# 	각 점은 country
# 	점 크기: pop(인구), 적절히 스케일 조정
# 	점 색상: continent 별로 다르게 표시
# 	범례(legend) 포함
# 	그래프 제목: "Life Expectancy vs GDP per Capita (2007)"

# (2) 서브플롯 2: 대륙별 평균 수명 막대 그래프
# 	x축: continent
# 	y축: lifeExp 평균값
# 	막대 색상은 임의로 지정
# 	각 막대 위에 평균 수명 값을 텍스트로 표시
# 	그래프 제목: "Average Life Expectancy by Continent (2007)"

# [Figure 전체 조건]
# 	figsize는 (14, 6) 이상
# 	plt.tight_layout()으로 레이아웃 조정
# 	각 subplot에 축 라벨 표시



