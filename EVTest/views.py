from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime as d1
from django.template import Template, Context
from EVTest.models import Stateofcharge
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.pyplot import plot, savefig
import random
import uuid
import json
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt

mu = 1
sigma = 0.3
# global TEST
RECORDTIMES = 0
STARTTIME = 0
SOCSTART = 0
SOCCHANGE = 24
SOCInitial = 1.2  # 电动汽车初始电量
EPriceSampleTime = 1  # 每15min发布实时电价
chargeSampleTime = 2  # 每2min获取电动汽车电池信息
sampleNo = int((1440 / EPriceSampleTime) + 1)  # 实时电价取样点97


# Create your views here.


# # startTime, SOCStart, SOCChange
# def getSoc(request):
#     SOCStart = float(request.GET.get("n1"))
#     SOCChange = float(request.GET.get("n2"))
#     startTime = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
#     [Time, SOC, index0, index1] = chargeProcess(startTime, SOCStart, SOCChange)
#     [chargingElectric, priceAverage, priceFinal] = calculateThePrice(Time, SOC)
#     # response = JsonResponse({'Time': json.dumps(Time.tolist()), 'SOC': json.dumps(SOC.tolist()), 'index0': index0, 'index1': index1})
#     # response = JsonResponse({'SOCStart': str(SOCStart), 'SOCFinal': str(SOC[len(SOC) - 1]),
#     #     #                          'SOCChange': str(SOCChange), 'realSOCChange': str(chargingElectric),
#     #     #                          'startTime': str(Time[0]), 'endTime': str(Time[len(Time) - 1]),
#     #     #                          'priceAverage': str(priceAverage), 'finalPay': str(priceFinal)})
#     response = JsonResponse({'realSOCChange': str(chargingElectric),
# #                              'chargeTime': str(int((Time[len(Time) - 1] - Time[0]) * 60000)),  # ms
# #                              'finalPay': str(priceFinal)})
#     sql1 = []
#     # print(Time.tolist())
#
#     global RECORDTIMES
#     try:
#         RECORDTIMES = int(Electricprice.objects.latest('id').identify)
#         RECORDTIMES += 1
#     except:
#         RECORDTIMES += 1
#     for i in range(0, len(Time.tolist())):
#         sql1.append(Electricprice(identify=RECORDTIMES, time=Time.tolist()[i], soc=SOC.tolist()[i]))
#     Electricprice.objects.bulk_create(sql1)
#     return response

def homeprocess(request):
    return render(request, "index.html")


# 电池充放电前后端测试
def charge(request):
    datalist = []
    result = ""
    if request.method == "POST":
        SOCStart = int(request.POST.get("initalSOC", None))
        SOCChange = int(request.POST.get("changeSOC", None))
        startTime = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
        [Time, SOC, index0, index1] = chargeProcess(startTime, SOCStart, SOCChange)
        [chargingElectric, priceAverage, priceFinal] = calculateThePrice(Time, SOC)
        sql1 = []
        global RECORDTIMES
        try:
            RECORDTIMES = int(Electricprice.objects.latest('id').identify)
            RECORDTIMES += 1
        except:
            RECORDTIMES += 1
        for i in range(0, len(Time.tolist())):
            sql1.append(Electricprice(identify=RECORDTIMES, time=Time.tolist()[i], soc=SOC.tolist()[i]))
        Electricprice.objects.bulk_create(sql1)

    if request.method == "GET":
        chargeTimes = request.GET.get("chargeTimes", None)
        result = Electricprice.objects.filter(identify=chargeTimes)
        for var in result:
            d = {"time": var.time, "soc": var.soc}
            datalist.append(d)
        print(datalist)
        list = Electricprice.objects.filter(identify=chargeTimes)
        x = []
        y = []
        for var in list:
            x.append(var.time)
            y.append(var.soc)
        plt.plot(x, y, '-')
        plt.title('电动汽车SOC', fontproperties='SimHei', fontsize=15)
        plt.xlabel('时间(min)', fontproperties='SimHei', fontsize=15)
        plt.ylabel('电池状态(kWh)', fontproperties='SimHei', fontsize=15)
        plt.savefig('static/img/load.jpg')
        plt.close()
    return render(request, "charge.html", {"data": datalist})


def discharge(request):
    return render(request, 'discharge.html')


# 电池充电后端
def chargeTest(request):
    flag = 0  # 充电
    SOCStart = float(request.GET.get("n1"))
    SOCChange = float(request.GET.get("n2"))
    UserID = str(request.GET.get("n3"))
    chargeTime = getChargingDate()[0]
    chargePower = getChargingDate()[1]
    j = 0
    k = 0
    Time2str = []
    now = datetime.datetime.now()
    st2minute = time.localtime().tm_hour * 60 + time.localtime().tm_min
    index0 = int(np.ceil(st2minute / chargeSampleTime))
    SOC = np.zeros(len(chargePower))
    SOC[0] = SOCStart
    SOCNow = SOCStart
    for i in range(index0 + 1, int(len(chargePower))):
        j += 1
        SOCNow += (chargePower[i] * chargeSampleTime) / 60
        SOC[j] = SOCNow
        k = i
        if ((SOCNow - SOCStart) > SOCChange + 0.1):
            break
    Time = chargeTime[index0:k]
    SOC = SOC[0:j]
    for i in range(0, len(Time)):
        hour = int(Time[i] / 60)
        minute = int(Time[i] % 60)
        if (i == 0):
            dt_obj = datetime.datetime(now.year, now.month, now.day, hour, minute, now.second)
        else:
            second = random.randint(0, 59)
            dt_obj = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
        Time2str.append(dt_obj.strftime("%Y-%m-%d %H:%M:%S"))
    Time = Time.astype(int)
    #    print(Time)
    #    print(Time2str)
    #    print(SOC)
    SOC = np.around(SOC, decimals=2)
    [chargingElectric, priceAverage, priceFinal] = calculateThePrice(Time, SOC)
    sql1 = []
    for i in range(0, len(Time.tolist())):
        sql1.append(
            Stateofcharge(uuid=str(uuid.uuid1()), userid=UserID, soc=SOC.tolist()[i], times=Time2str[i],
                          flag=flag, money=str(priceFinal)))
    Stateofcharge.objects.bulk_create(sql1)
    response = JsonResponse({'startTime': str(Time2str[0]),
                             'realSOCChange': str(chargingElectric),
                             'chargeTime': str(int((Time[len(Time) - 1] - Time[0]) * 60000)),  # ms
                             'finalPay': str(priceFinal)})
    return response


# 记录放电数据
#####输入参数:
#    SOC 当前电量 kWh
#    W 总耗电量 kWh
#    T 总时间 min
#    N 点的总个数
#####输出参数:
#    flag:=1放电标志 =0充电标志
#    k:电动汽车停止运行的点
#    time2str:充电时间列表
#    soc:电量列表
def dischargeTest(request):
    SOC = float(request.GET.get("n1"))
    W = float(request.GET.get("n2"))
    T = float(request.GET.get("n3"))
    N = int(request.GET.get("n4"))
    UserID = str(request.GET.get("n5"))
    flag = 1
    time2str = []
    sql1 = []
    a = time.time()  # 获取当前时间s
    print("当前时间为:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)))
    print("转化为分钟后:%fs" % (a))
    w = W / (N - 1)  # 平均耗电量
    t = T * 60 / (N - 1)  # 平均时间s
    times = np.zeros(N)
    socs = np.zeros(N)
    socs[0] = SOC
    times[0] = a
    for i in range(1, N):
        socs[i] = socs[i - 1] - w
        times[i] = times[i - 1] + t
        k = i
        if socs[i] <= 3.1:  # soc低于3kWh停止运行
            break
    times = times[0:k + 1]
    socs = socs[0:k + 1]
    for i in range(0, k + 1):
        time2str.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(times[i])))
    for i in range(0, len(time2str)):
        sql1.append(
            Stateofcharge(uuid=str(uuid.uuid1()), userid=UserID, soc=socs.tolist()[i], times=time2str[i], flag=flag,
                          money=str("-")))
    Stateofcharge.objects.bulk_create(sql1)
    response = JsonResponse({'time2str': str(time2str),
                             'socs': str(json.dumps(socs.tolist())),  # ms
                             'k': str(k),
                             'flag': str(flag)})
    return response


#################################################以下为使用到的函数*****************************************************

##################################################
# 电动汽车电量跟踪及电价计费V1.0版本                #
# 电量跟踪包括充电、放电和行驶时SOC的变换情况        #
# 最终需要根据拍卖电量自动确定时间                  #
# 输入参数：开始充电时间、充电量                    #
# 系统输出：自动开始充电，并记录至该电动汽车数据库中 #
##################################################


# 获取实时电价数据
def getPrice():
    np.random.seed(1000)
    time = np.linspace(0, 1440, num=sampleNo, endpoint=True)
    Price = np.abs(np.random.normal(mu, sigma, sampleNo))
    return [time, Price]


# 获取充电负荷曲线
def getChargingDate():
    np.random.seed(1000)
    time = np.linspace(0, 1440, num=int(1440 / chargeSampleTime), endpoint=True)
    power = np.random.binomial(10, 0.8, size=int(1440 / chargeSampleTime))
    #    time=np.sort(np.random.randint(0,1440,2))
    #    time=np.arange(time[0],time[1]+chargeSampleTime,chargeSampleTime)
    #    power=np.linspace(1,4,num=len(time),endpoint=True)
    return [time, power]


# 输入：
# startTime:开始充电时间 min
# SOCStart:开始充电时的电量
# SOCFinal:需要充多少电
# 输出:
# chargeTime:充电时间
# SOC:电量记录
def chargeProcess(SOCStart, SOCChange):
    chargeTime = getChargingDate()[0]
    chargePower = getChargingDate()[1]
    j = 0
    k = 0
    Time2str = []
    now = datetime.datetime.now()
    st2minute = time.localtime().tm_hour * 60 + time.localtime().tm_min
    index0 = int(np.ceil(st2minute / chargeSampleTime))
    SOC = np.zeros(len(chargePower))
    SOC[0] = SOCStart
    SOCNow = SOCStart
    for i in range(index0 + 1, int(len(chargePower))):
        j += 1
        SOCNow += (chargePower[i] * chargeSampleTime) / 60
        SOC[j] = SOCNow
        if ((SOCNow - SOCStart) > SOCChange + 0.1):
            k = i
            break
    Time = chargeTime[index0:k]
    SOC = SOC[0:j]
    for i in range(0, len(Time)):
        hour = int(Time[i] / 60)
        minute = int(Time[i] % 60)
        if (i == 0):
            dt_obj = datetime.datetime(now.year, now.month, now.day, hour, minute, now.second)
        else:
            second = random.randint(0, 59)
            dt_obj = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
        Time2str.append(dt_obj.strftime("%Y-%m-%d %H:%M:%S"))
    Time = Time.astype(int)
    #    print(Time)
    #    print(Time2str)
    #    print(SOC)
    index1 = k
    SOC = np.around(SOC, decimals=2)
    return [Time, Time2str, SOC, index0, index1]


# 计算充电电价
def calculateThePrice(Time, SOC):
    # 计算充电电量
    a = SOC
    chargingElectric = a[len(a) - 1] - a[0]

    # 计算时间
    time = Time
    # 充电起始时间
    tCharge1 = time[0]
    # 充电起始时间左边电价时间
    t11 = int(np.floor(tCharge1 / EPriceSampleTime) * EPriceSampleTime)
    # 充电起始时间左边电价时间
    t12 = int(np.ceil(tCharge1 / EPriceSampleTime) * EPriceSampleTime)

    # 充电结束时间
    tCharge2 = time[len(time) - 1]
    # 充电结束时间左边电价时间
    t21 = int(np.floor(tCharge2 / EPriceSampleTime) * EPriceSampleTime)
    # 充电结束时间左边电价时间
    t22 = int(np.ceil(tCharge2 / EPriceSampleTime) * EPriceSampleTime)
    #    print(tCharge1,t11,t12,tCharge2,t21,t22)

    # 计算t12---t21之间的电价
    price1 = getPrice()[1][int(t12 / EPriceSampleTime):int(t21 / EPriceSampleTime) + 1]
    area1 = (t12 - tCharge1) * getPrice()[1][int(t11 / EPriceSampleTime)]  # 左侧不完整面积
    area2 = np.sum(price1 * EPriceSampleTime)  # 实时电价完整面积
    area3 = (tCharge2 - t21) * getPrice()[1][int(t21 / EPriceSampleTime)]  # 右侧不完整面积
    #    print(area1,area2,area3)
    priceAverage = (area1 + area2 + area3) / (tCharge2 - tCharge1)
    priceFinal = round(chargingElectric * priceAverage, 2)
    #    print(priceAverage)
    return [chargingElectric, priceAverage, priceFinal]


# 绘制电价及充电负荷曲线
def plotElectricPrice(Time, SOC, index0, index1):
    plt.figure(figsize=(8, 8))
    plt.subplot(3, 1, 1)
    plt.step(getPrice()[0], getPrice()[1], where='post', label='post')
    plt.title('电价计算', fontproperties='SimHei', fontsize=20)

    plt.ylabel('实时电价(元/kWh)', fontproperties='SimHei', fontsize=15)
    plt.xlim(getChargingDate()[0][index0], getChargingDate()[0][index1] - 1)

    plt.subplot(3, 1, 2)
    plt.step(getChargingDate()[0], getChargingDate()[1], where='post', label='post')
    plt.ylabel('充电负荷(kW)', fontproperties='SimHei', fontsize=15)
    plt.xlim(getChargingDate()[0][index0], getChargingDate()[0][index1] - 1)

    plt.subplot(3, 1, 3)
    plt.plot(Time, SOC)
    plt.ylabel('电池状态(kWh)', fontproperties='SimHei', fontsize=15)
    plt.xlabel('时间(min)', fontproperties='SimHei', fontsize=15)
    plt.xlim(getChargingDate()[0][index0], getChargingDate()[0][index1] - 1)
    plt.show()


# 记录放电数据
#####输入参数:
#    SOC 当前电量 kWh
#    W 总耗电量 kWh
#    T 总时间 min
#    N 点的总个数
#####输出参数:
#    flag:=1放电标志 =0充电标志
#    k:电动汽车停止运行的点
#    time2str:充电时间列表
#    soc:电量列表
def dischargeProcess(SOC, W, T, N):
    #    timenow=time.localtime().tm_hour*60+time.localtime().tm_min
    flag = 1
    time2str = []
    a = time.time()  # 获取当前时间s
    print("当前时间为:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)))
    print("转化为分钟后:%fs" % (a))
    w = W / (N - 1)  # 平均耗电量
    t = T * 60 / (N - 1)  # 平均时间s
    times = np.zeros(N)
    socs = np.zeros(N)
    socs[0] = SOC
    times[0] = a
    for i in range(1, N):
        socs[i] = socs[i - 1] - w
        times[i] = times[i - 1] + t
        k = i
        if socs[i] <= 3.1:  # soc低于3kWh停止运行
            break
    times = times[0:k + 1]
    socs = socs[0:k + 1]
    for i in range(0, k + 1):
        time2str.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(times[i])))
    print("Final point:")
    print(k)
    print("time2str:")
    print(time2str)
    print("socs")
    print(socs)
    return [time2str, socs, k, flag]
