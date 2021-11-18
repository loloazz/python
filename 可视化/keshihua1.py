import numpy as np
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import  Line


df  = pd.read_excel("F:\\pythonProject\\data\\1.xlsx")

xiaofenrenshu=df['customer_id'].groupby(df["age_group"]).count().tolist()

xiaofenjine=np.round_(df['previous_order_amount'].groupby(df["age_group"]).sum()/10000,2)

age=df["age_group"].sort_values().drop_duplicates().tolist()
bar = (
    Line()
    .add_xaxis(age)

    .add_yaxis("消费总人数", xiaofenrenshu)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} 人"), interval=50
        )
    )

)

line = Line().add_xaxis(age).add_yaxis("消费金额 /万元", xiaofenjine, yaxis_index=1)
bar.overlap(line)
bar.render("overlap_bar_line.html")