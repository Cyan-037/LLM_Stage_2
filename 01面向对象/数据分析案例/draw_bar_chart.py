from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def draw_bar_chart_optimized(date_list, amount_list):
    """
    优化视觉表现的柱状图
    :param date_list: 日期列表（升序，字符串格式 'YYYY-MM-DD'）
    :param amount_list: 销售额列表（float）
    :return: Bar 对象
    """
    # 计算平均值（用于添加平均线）
    avg_value = sum(amount_list) / len(amount_list) if amount_list else 0

    # 创建柱状图对象，使用内置主题
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))

    # 添加 X 轴（日期）
    bar.add_xaxis(date_list)

    # 添加 Y 轴（销售额），柱子颜色为蓝色 + 微调样式
    bar.add_yaxis(
        series_name="销售额",
        y_axis=amount_list,
        color="blue",                     # 主色为蓝色
        bar_width="50%",                  # 柱宽占比
        itemstyle_opts=opts.ItemStyleOpts(
            opacity=0.85,                 # 略透明，更柔和
            border_color="rgba(0,0,255,0.3)",
            border_width=1
        ),
        label_opts=opts.LabelOpts(
            is_show=True,                 # 显示数据标签
            position="top",               # 显示在柱顶
            formatter="{c:.2f}",          # 保留两位小数
            font_size=11,
            color="#333"
        ),
        tooltip_opts=opts.TooltipOpts(
            formatter="{b}<br/>销售额: {c:.2f}"
        )
    )

    # 全局配置
    bar.set_global_opts(
        title_opts=opts.TitleOpts(
            title="黑马程序员分析案例",
            subtitle="销售额趋势（含平均线）",
            pos_left="center",
            title_textstyle_opts=opts.TextStyleOpts(font_size=18)
        ),
        xaxis_opts=opts.AxisOpts(
            name="日期",
            axislabel_opts=opts.LabelOpts(rotate=30),  # 旋转30°防重叠
            splitline_opts=opts.SplitLineOpts(is_show=False)  # 不显示x轴网格线
        ),
        yaxis_opts=opts.AxisOpts(
            name="销售额（元）",
            splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(type_="dashed")),  # 横向虚线网格
            axislabel_opts=opts.LabelOpts(formatter="{value:.2f}")
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="shadow"
        ),
        # 添加平均线（通过 markline）
        # 注意：markline 需要在 add_yaxis 之后，通过 set_series_opts 或直接调用 bar.set_series_opts
    )

    # 添加平均线（作为系列标记）
    bar.set_series_opts(
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值")
            ],
            label_opts=opts.LabelOpts(formatter="均值: {c:.2f}", color="#d14a61"),
            linestyle_opts=opts.LineStyleOpts(color="#d14a61", type_="dashed", width=2)
        )
    )

    return bar


# ========== 使用示例 ==========
if __name__ == "__main__":
    # 模拟数据（实际使用时传入你的两个列表）
    date_list = ['2026-05-31', '2026-06-01', '2026-06-02', '2026-06-03', '2026-06-04']
    amount_list = [123.3, 456.7, 789.0, 654.2, 321.5]

    # 生成优化后的图表
    chart = draw_bar_chart_optimized(date_list, amount_list)

    # 渲染为 HTML 文件（自动打开）
    chart.render("optimized_sales_bar_chart.html")