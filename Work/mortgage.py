# mortgage.py
#
# Exercise 1.7
    # mortgage = 500000.0
    # years = 30
    # rate = 0.05
    # monthly_payment = 2684.11
    # total_paid = 0.0

    # while mortgage > 0:
    #     mortgage = mortgage * (1+rate/12) - monthly_payment # 还贷和复利是不一样的，M本月的复利是 M * (1 + rate/12), 扣除了本月的还款MP后, 再计算下月的复利
    #     total_paid = total_paid + monthly_payment

    # print('Total paid', round(total_paid,2))

# Exercise 1.8
    # M = 500000.0
    # m_s = 0
    # R = 0.05
    # m_p = 2684.11
    # TP = 0.0

    # while M > 0:
    #     while m_s < 12: 
    #         M = M * (1 + R/12) - m_p - 1000
    #         m_s = m_s + 1
    #         TP = TP + m_p +1000
    #         print('total payment:', round(TP,2), 'total time:', m_s)   
    #     M = M * (1 + R/12) - m_p
    #     m_s = m_s + 1
    #     TP = TP + m_p
    # print('total payment:', round(TP,2), 'total time:', m_s)

# Excercise 1.9
M = 500000.0
m_s = 0
eps_m = 5 * 12 + 1
持续时间 = 4
epe_m = int(((eps_m - 1)/12 + 持续时间) * 12)
R = 0.05
m_p = 2684.11
e_p = 1000
TP = 0.0

while M > 0:
    m_s += 1
    M = M * (1 + R/12) - m_p
    TP = TP + m_p
    while eps_m <= m_s <= epe_m:
        M = M * (1 + R/12) - m_p - e_p
        m_s = m_s + 1
        TP = TP + m_p + e_p
    print(f'要花费{m_s}个月, 总计付款${TP:0.2f}元.')