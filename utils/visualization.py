import pandas as pd
import mysql.connector
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
import seaborn as sns

class GraphViewer():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="ohgiraffers",
            password="ohgiraffers",
            database="cardb"
        )

        if self.connection.is_connected():
            print('@@@MySQL 서버에 성공적으로 연결@@@')

        self.cursor = self.connection.cursor()
        self.df = None

        rcParams['font.family'] = 'Malgun Gothic'
        rcParams['axes.unicode_minus'] = False    

    def close(self):
        self.cursor.close()
        self.connection.close()
        print('@@@MySQL 연결 종료@@@')

    def plot_car_info(self):

        engine_sql = """
        SELECT year, total FROM engine_car_info 
        """
        self.cursor.execute(engine_sql)
        result_rows = self.cursor.fetchall()

        columns = [desc[0] for desc in self.cursor.description]
        df = pd.DataFrame(result_rows, columns=columns)

        filtered_df = df[df['year'].between(2020, 2024)]
        engine_total = filtered_df.groupby('year')['total'].sum()

        eco_sql = """
        SELECT year, total FROM eco_car_info 
        """
        self.cursor.execute(eco_sql)
        result_rows =self.cursor.fetchall()

        columns = [desc[0] for desc in self.cursor.description]
        df = pd.DataFrame(result_rows, columns=columns)

        filtered_df = df[df['year'].between(2020, 2024)]
        eco_total = filtered_df.groupby('year')['total'].sum()

        df = pd.concat([engine_total.rename('engine'), eco_total.rename('eco')], axis=1)

        years = df.index
        x = np.arange(len(years))
        bar_width = 0.2

        fig, ax1 = plt.subplots(figsize=(8, 5))

        # 첫 번째 y축: 내연기관 (왼쪽)
        color1 = 'tab:blue'
        ax1.set_xlabel('년도')
        ax1.set_ylabel('내연기관 등록대수', color=color1)

        bars1 = ax1.bar(x - bar_width/2, df['engine'], width=bar_width, color=color1, label='내연기관')
        ax1.tick_params(axis='y', labelcolor=color1)
        ax1.set_xticks(x)
        ax1.set_xticklabels(years)

        # 두 번째 y축: 친환경차 (오른쪽)
        ax2 = ax1.twinx()
        color2 = 'tab:green'
        ax2.set_ylabel('친환경차 등록대수', color=color2)

        bars2 = ax2.bar(x + bar_width/2, df['eco'], width=bar_width, color=color2, label='친환경차')
        ax2.tick_params(axis='y', labelcolor=color2)

        ax1.set_ylim(15000000, 20000000)
        ax2.set_ylim(0, 600000)

        # 범례
        bars = [bars1, bars2]
        labels = ['내연기관', '친환경차']
        ax1.legend(bars, labels, loc='upper left')

        plt.title('연도별 차량 등록대수 (내연기관 & 친환경차, 막대그래프)')
        plt.tight_layout()
        plt.show()

        return fig

    def plot_eco_info(self):

        eco_sql = """
        SELECT year, area, total FROM eco_car_info 
        """

        self.cursor.execute(eco_sql)
        result_rows = self.cursor.fetchall() # 전체 행을 다 가져옴

        columns = [desc[0] for desc in self.cursor.description]  # 컬럼명 가져오기

        # DataFrame으로 만들기
        df = pd.DataFrame(result_rows, columns=columns)

        filtered_df = df[df['year'].between(2020, 2024)]

        grouped = (
            filtered_df.groupby(['year', 'area'])['total']
            .sum()
            .reset_index()
        )

        print(grouped)

        rcParams['font.family'] = 'Malgun Gothic'
        rcParams['axes.unicode_minus'] = False

        pivot_df = grouped.pivot(index='area', columns='year', values='total').fillna(0)

        # 지역 이름을 보기 좋게 정렬 (원하시면)
        pivot_df = pivot_df.sort_index()

        # 🔷 figure 설정
        fig = plt.figure(figsize=(10, 8))

        # 🔷 히트맵 그리기
        plt.imshow(pivot_df, cmap='YlGnBu', aspect='auto')

        # x/y 축 설정
        plt.xticks(ticks=np.arange(len(pivot_df.columns)), labels=pivot_df.columns, rotation=45)
        plt.yticks(ticks=np.arange(len(pivot_df.index)), labels=pivot_df.index)

        # colorbar
        cbar = plt.colorbar()
        cbar.set_label('친환경차 등록대수')

        # 라벨 및 제목
        plt.xlabel('연도')
        plt.ylabel('지역')
        plt.title('지역별 연도별 친환경차 등록대수 (히트맵)')

        plt.tight_layout()
        # 저장
        fig.savefig("figure2.png", dpi=300)   # PNG 파일

        plt.show()

        return fig

    def plot_ev_hd_info(self):
        sql = 'select * from eco_car_info' 

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        columns = [col[0] for col in self.cursor.description]
        df = pd.DataFrame(rows, columns=columns)

        # car_code, 연도별 데이터 저장
        dfs = {4: {}, 5: {}}
        for car_code in [4, 5]:
            for year in range(2020, 2025):
                dfs[car_code][year] = df[(df['year'] == year) & (df['car_code'] == car_code)]

        # 색상 설정
        colors = {
            2020: '#e35f62',
            2021: '#e99362',
            2022: '#D1D13A',
            2023: '#61e35f',
            2024: '#5f96e3'
        }

        # 차종 이름
        car_names = {
            4: '전기차',
            5: '수소차'
        }

        figs = []  # figure 들을 담을 리스트

        # car_code 별로 figure 생성
        for car_code in [4, 5]:
            fig, ax = plt.subplots(figsize=(12, 8))
            fig.set_facecolor('white')

            for year, data in dfs[car_code].items():
                ax.plot(
                    data['area'],
                    data['total'],
                    color=colors[year],
                    linestyle='-', marker='o',
                    label=f"{year}"
                )

            ax.set_xlabel('지역', labelpad=15)
            ax.set_ylabel('차량 등록 대수(누적)', labelpad=15)
            ax.set_title(f'연도-지역별 {car_names[car_code]} 등록 현황', fontsize=18)
            ax.grid(True)

            ax.legend(
                loc='upper left',
                fontsize=12,
                frameon=True,
                shadow=True,
                title='연도'
            )

            plt.tight_layout()
            figs.append(fig)

        return figs[0], figs[1]

    def plot_subsidy_info(self):

        eco_sql = """
        SELECT car_code, year, area, amount FROM subsidy 
        """

        self.cursor.execute(eco_sql)
        result_rows = self.cursor.fetchall() # 전체 행을 다 가져옴

        columns = [desc[0] for desc in self.cursor.description]  # 컬럼명 가져오기

        df = pd.DataFrame(result_rows, columns=columns)
        filtered_df = df[df['year'].between(2020, 2024)]

        df_car_code_4 = filtered_df[filtered_df['car_code'] == 4].groupby(['year', 'area'])['amount'].sum().reset_index()
        df_car_code_5 = filtered_df[filtered_df['car_code'] == 5].groupby(['year', 'area'])['amount'].sum().reset_index()

        pivot_4 = df_car_code_4.pivot(index='area', columns='year', values='amount').fillna(0)

        fig1 = plt.figure(figsize=(10, 8))
        sns.heatmap(pivot_4, annot=True, fmt=".0f", cmap="YlGnBu")
        plt.title('전기차 지역별 연도별 보조금')
        plt.xlabel('년도')
        plt.ylabel('지역')

        pivot_5 = df_car_code_5.pivot(index='area', columns='year', values='amount').fillna(0
                                                                                            )
        fig2 = plt.figure(figsize=(10, 8))
        sns.heatmap(pivot_5, annot=True, fmt=".0f", cmap="YlGnBu")
        plt.title('수소차 지역별 연도별 보조금')
        plt.xlabel('년도')
        plt.ylabel('지역')
        plt.show()

        return fig1, fig2