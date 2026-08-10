from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType


def create_bar_chart(date_list, amount_list):
    """
    使用 PyEcharts 绘制销售额柱状图（带数值标签 + 日期斜排 + 交互美化）

    :param date_list: 日期列表（升序的字符串，如 '2026-05-31'）
    :param amount_list: 销售额列表（float，与 date_list 一一对应）
    :return: Bar 图表对象
    """
    bar = (
        # 使用亮色主题，宽高自定义，让图表更美观
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1000px", height="500px"))
        # x 轴：日期
        .add_xaxis(date_list)
        # y 轴：销售额，柱子颜色 blue
        .add_yaxis(
            series_name="销售额",
            y_axis=amount_list,
            itemstyle_opts=opts.ItemStyleOpts(
                color="blue",
                border_radius=[4, 4, 0, 0],  # 柱子顶部圆角，更精致
            ),
            # 显示柱子数值标签（在柱子顶部）
            label_opts=opts.LabelOpts(
                is_show=True,
                position="top",
                font_size=12,
            ),
        )
        .set_global_opts(
            # 图表标题（居中显示）
            title_opts=opts.TitleOpts(
                title="黑马程序员分析案例",
                pos_left="center",
            ),
            # x 轴：日期斜排 45 度，避免拥挤
            xaxis_opts=opts.AxisOpts(
                name="日期",
                axislabel_opts=opts.LabelOpts(rotate=45, interval=0),
            ),
            yaxis_opts=opts.AxisOpts(name="销售额"),
            # 鼠标悬停提示框（交互）
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="shadow",
            ),
            # 顶部数据缩放，可拖动查看（交互）
            datazoom_opts=[
                opts.DataZoomOpts(type_="slider", range_start=0, range_end=100)
            ],
        )
    )
    return bar


# ===== 使用示例 =====
if __name__ == "__main__":
    date_list = ["2026-05-27", "2026-05-28", "2026-05-29", "2026-05-30", "2026-05-31"]
    amount_list = [123.3, 456.7, 321.9, 588.2, 402.5]

    chart = create_bar_chart(date_list, amount_list)
    chart.render("bar_chart.html")
    print("图表已生成：bar_chart.html")