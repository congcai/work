# 实例001：数字组合
# 题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析 遍历全部可能，把有重复的剃掉
#方法一
# tatol=0
# for i in range(1,5):
#     for j in range (1,5):
#         for k in range(1,5):
#             if (i!=j) and (j!=k) and (k!=i):
#                 print(i,j,k)
#                 tatol+=1
# print(tatol)
#方法二
# import itertools
# sum2=0
# a=[1,2,3,4]
# for i in itertools.permutations(a,3):
#     print(i)
#     sum2+=1
# print(sum2)

# 实例002：“个税计算”
# 题目 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
# 程序分析 分区间计算即可。
# profit=int(input("请输入利润："))
# bonus=0
# thresholds=[100000,100000,200000,200000,400000]
# rates=[0.1,0.075,0.05,0.03,0.015,0.01]
# for i in range(len(thresholds)):
#     if profit<=thresholds[i]:
#         bonus+=profit*rates[i]
#         profit=0
#         break
#     else:
#         bonus+=thresholds[i]*rates[i]
#         profit-=thresholds[i]
# bonus+=profit*rates[-1]
# print(bonus)



