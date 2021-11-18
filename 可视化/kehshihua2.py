# 按照用户类型（customer_type）分别
# 对用户数（customer_id）进行计数，
# 对消费金额（salse）进行求和汇总，
# 对最近30天在app上有参与活动（promote_last_30）的人数进行统计，


import numpy as np
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import  Pie
df  = pd.read_excel("F:\\pythonProject\\data\\1.xlsx")
# 按照用户类型（customer_type）分别对用户数（customer_id）进行计数
# 1）各类型人数占比
# 2）各类型总消费金额占比
# 3）各类型参与活动比例

kehuleixing=np.round_((df['customer_id'].groupby(df["customer_type"]).count())/df['customer_id'].count().tolist(),2)
print(kehuleixing)
type=df["customer_type"].sort_values().drop_duplicates().tolist()

sum_salse=np.round_(df['salse'].groupby(df["customer_type"]).sum()/df['salse'].sum().tolist(),2)

print(sum_salse)

sum_promote=np.round_(df['promote_last_30'].groupby(df["customer_type"]).sum()/df['promote_last_30'].sum().tolist(),2)

print(sum_promote)

c = (
    Pie()
    .add("", [list(z) for z in zip(type, kehuleixing)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-各类型人数占比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
)


d= (
    Pie()
    .add("", [list(z) for z in zip(type, sum_salse)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-各类型总消费金额占比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base1.html")
)


e= (
    Pie()
    .add("", [list(z) for z in zip(type, sum_promote)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-各类型参与活动比例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base2.html")
)


