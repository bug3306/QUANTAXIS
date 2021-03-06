
# shipane
cn_en_compare = {'明细': 'id',
                 '证券代码': 'code',
                 '证券名称': 'name',
                 '股票余额': 'amount',
                 '可用余额': 'sell_available',
                 '冻结数量': 'frozen',
                 '买卖标志': 'towards',
                 '操作': 'towards', #这个是模拟交易的买卖标志
                 '委托价格': 'order_price',
                 '委托数量': 'order_amount',
                 '成交价格': 'trade_price',
                 '成交数量': 'trade_amount',
                 '状态说明': 'status',
                 '备注' : 'status', ## 这个是模拟交易的status
                 '场外撤单': 'cancel_outside',
                 '场内撤单': 'cancel_inside',
                 '未成交': 'pending',
                 '全部撤单':'cancel_all',
                 '委托时间': 'order_time',
                 '合同编号':'realorder_id',# 模拟交易的委托编号
                 '撤销数量':'cancel_amount',
                 '委托编号': 'realorder_id',
                 '批次号': 'pc_id',
                 '盈亏': 'pnl',
                 '成本价': 'hold_price',
                 '盈亏比例(%)': 'pnl_ratio',
                 '市价': 'price',
                 '市值': 'market_value',
                 '交易市场': 'SSE',
                 '股东帐户': 'shareholders',
                 '实际数量': 'total_amount',
                 '可申赎数量': 'redemption_number',
                 '资讯': 'message',
                 '汇率': 'exchange_rate',
                 '沪港深港市场': 'hkmarket',
                 '成本价港币': 'hold_price_hk',
                 '买入成本价港币': 'buy_price_hk',
                 '买入在途数量': 'buy_onway',
                 '卖出在途数量': 'sell_onway'}

trade_status_cn_en_dict={
                 '场外撤单': 'cancel_outside',
                 '场内撤单': 'cancel_inside',
                 '未成交': 'pending',
                 '已成交':'finished',
                 '全部撤单':'cancel_all'}