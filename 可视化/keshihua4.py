import numpy as np
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Bar

# 按照年龄段（age_group）对各类型（customer_type）消费金额（salse）进行求和（sum）运算。
# 并把计算结果 绘制成一个 层叠柱状图

df = pd.read_excel("F:\\pythonProject\\data\\1.xlsx")

age=df["age_group"].sort_values().drop_duplicates().tolist()
xiaofenrenshu = pd.DataFrame(np.round_(df.groupby(["age_group", "customer_type"])["salse"].sum(),2)).unstack()["salse"].rename_axis().reset_index()

print(xiaofenrenshu)


stack_bar = (
    Bar(init_opts=opts.InitOpts(width="900px", height="500px"))
    .add_xaxis(xiaofenrenshu["age_group"].tolist())
    .add_yaxis("1类/千元", xiaofenrenshu["1类"].tolist(), stack="stack1")
    .add_yaxis("2类/千元", xiaofenrenshu["2类"].tolist(), stack="stack1")
    .add_yaxis("3类/元", xiaofenrenshu["3类"].tolist(), stack="stack1")
    .set_series_opts(
        label_opts=opts.LabelOpts(position="inside", color="white", font_size=15)
    ) .set_global_opts(title_opts=opts.TitleOpts(title="各类型，年龄段消费分析"))



)

stack_bar.render("duiji_base.html")
