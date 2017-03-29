#coding:utf-8
from __future__ import division
from django.shortcuts import render
from .models import *
# from data import Data
# Create your views here.
# re_number为该批次总返回数 alls为返回率 hardwareQuestion为硬件返回率

# def we30c_index(request):
#     first = Data(we30c_1st,sales=1000).data()
#     second = Data(we30c_2nd,sales=5000)
#     third = Data(we30c_3th,sales=5000)
#     fouth = Data(we30c_4th,sales=5000)
#     re_number1 = first.number
#     alls_1 = first.alls
#     hardwareQuestion_1 = first.hd
#     re_number2 = second.number
#     alls_2 = second.alls
#     hardwareQuestion_2 = second.hd
#     re_number3 = third.number
#     alls_3 = third.alls
#     hardwareQuestion_3 = third.hd
#     re_number4 = fouth.number
#     alls_4 = fouth.alls
#     hardwareQuestion_4 = fouth.hd
#
#     return render(request, 'we30c.html', {'hd_1': hardwareQuestion_1, 'alls_1': alls_1,
#                                               'hd_2':hardwareQuestion_2,'alls_2':alls_2,
#                                               'hd_3':hardwareQuestion_3,'alls_3':alls_3,
#                                               'hd_4':hardwareQuestion_4,'alls_4':alls_4,
#                                               're1':re_number1,'re2':re_number2,
#                                               're3':re_number3,'re4':re_number4,
#                                               'sales_1':first_sales,'sales_2':second_sales,
#                                               'sales_3':third_sales,'sales_4':fouth_sales})

def we30c_index(request):
    #出货数
    first_sales = 1000
    second_sales = 5000
    third_sales = 5000
    fouth_sales = 5000

    re_number1 = int(len(we30c_1st.objects.all())) #总返回数
    alls_1 = re_number1 / first_sales * 100        #总返回率
    hd1 = int(len(we30c_1st.objects.filter(question_type='硬件'))) #硬件不良数
    pd1 = int(len(we30c_1st.objects.filter(question_type='软件'))) #软件不良数
    na1 = int(len(we30c_1st.objects.filter(question_type='NA')))   #NA不良数
    qd1 = hd1+pd1                                                  #实际不良数
    hd1_r = hd1 / first_sales * 100                                 #硬件不良率
    pd1_r = pd1 / first_sales * 100                                 #软件不良率
    na1_r = na1 / first_sales * 100                                 #NA不良率
    qd1_r = qd1 / first_sales * 100                                 #实际不良返回率
    back1 =  int(len(we30c_1st.objects.filter(ranges='无理由退货')))
    no1 = int(len(we30c_1st.objects.filter(ranges='未复现问题')))
    factory1 = int(len(we30c_1st.objects.filter(ranges='工厂制程问题')))
    tel1 = int(len(we30c_1st.objects.filter(ranges='遥控器不良')))
    power1 = int(len(we30c_1st.objects.filter(ranges='电源头不良')))
    HDMI1 = int(len(we30c_1st.objects.filter(ranges='HDMI线不良')))
    software1 = int(len(we30c_1st.objects.filter(ranges='软件相关问题')))
    analyse1 = int(len(we30c_1st.objects.filter(ranges='待分析')))
    RK1 = int(len(we30c_1st.objects.filter(ranges='RK芯片问题')))
    customer1 = int(len(we30c_1st.objects.filter(ranges='客户应用问题')))

    re_number2 = int(len(we30c_2nd.objects.all()))  # 总返回数
    alls_2 = re_number2 / second_sales * 100  # 总返回率
    hd2 = int(len(we30c_2nd.objects.filter(question_type='硬件')))  # 硬件不良数
    pd2 = int(len(we30c_2nd.objects.filter(question_type='软件')))  # 软件不良数
    na2 = int(len(we30c_2nd.objects.filter(question_type='NA')))  # NA不良数
    qd2 = hd2 + pd2  # 实际不良数
    hd2_r = hd2 / second_sales * 100  # 硬件不良率
    pd2_r = pd2 / second_sales * 100  # 软件不良率
    na2_r = na2 / second_sales * 100  # NA不良率
    qd2_r = qd2 / second_sales * 100  # 实际不良返回率
    back2 = int(len(we30c_2nd.objects.filter(ranges='无理由退货')))
    no2 = int(len(we30c_2nd.objects.filter(ranges='未复现问题')))
    factory2 = int(len(we30c_2nd.objects.filter(ranges='工厂制程问题')))
    tel2 = int(len(we30c_2nd.objects.filter(ranges='遥控器不良')))
    power2 = int(len(we30c_2nd.objects.filter(ranges='电源头不良')))
    HDMI2 = int(len(we30c_2nd.objects.filter(ranges='HDMI线不良')))
    software2 = int(len(we30c_2nd.objects.filter(ranges='软件相关问题')))
    analyse2 = int(len(we30c_2nd.objects.filter(ranges='待分析')))
    RK2 = int(len(we30c_2nd.objects.filter(ranges='RK芯片问题')))
    customer2 = int(len(we30c_2nd.objects.filter(ranges='客户应用问题')))

    re_number3 = int(len(we30c_3th.objects.all()))  # 总返回数
    alls_3 = re_number3 / third_sales * 100  # 总返回率
    hd3 = int(len(we30c_3th.objects.filter(question_type='硬件')))  # 硬件不良数
    pd3 = int(len(we30c_3th.objects.filter(question_type='软件')))  # 软件不良数
    na3 = int(len(we30c_3th.objects.filter(question_type='NA')))  # NA不良数
    qd3 = hd3 + pd3  # 实际不良数
    hd3_r = hd3 / third_sales * 100  # 硬件不良率
    pd3_r = pd3 / third_sales * 100  # 软件不良率
    na3_r = na3 / third_sales * 100  # NA不良率
    qd3_r = qd3 / third_sales * 100  # 实际不良返回率
    back3 = int(len(we30c_3th.objects.filter(ranges='无理由退货')))
    no3 = int(len(we30c_3th.objects.filter(ranges='未复现问题')))
    factory3 = int(len(we30c_3th.objects.filter(ranges='工厂制程问题')))
    tel3 = int(len(we30c_3th.objects.filter(ranges='遥控器不良')))
    power3 = int(len(we30c_3th.objects.filter(ranges='电源头不良')))
    HDMI3 = int(len(we30c_3th.objects.filter(ranges='HDMI线不良')))
    software3 = int(len(we30c_3th.objects.filter(ranges='软件相关问题')))
    analyse3 = int(len(we30c_3th.objects.filter(ranges='待分析')))
    RK3 = int(len(we30c_3th.objects.filter(ranges='RK芯片问题')))
    customer3 = int(len(we30c_3th.objects.filter(ranges='客户应用问题')))

    re_number4 = int(len(we30c_4th.objects.all()))  # 总返回数
    alls_4 = re_number4 / fouth_sales * 100  # 总返回率
    hd4 = int(len(we30c_4th.objects.filter(question_type='硬件')))  # 硬件不良数
    pd4 = int(len(we30c_4th.objects.filter(question_type='软件')))  # 软件不良数
    na4 = int(len(we30c_4th.objects.filter(question_type='NA')))  # NA不良数
    qd4 = hd4 + pd4  # 实际不良数
    hd4_r = hd4 / fouth_sales * 100  # 硬件不良率
    pd4_r = pd4 / fouth_sales * 100  # 软件不良率
    na4_r = na4 / fouth_sales * 100  # NA不良率
    qd4_r = qd4 / fouth_sales * 100  # 实际不良返回率
    back4 = int(len(we30c_4th.objects.filter(ranges='无理由退货')))
    no4 = int(len(we30c_4th.objects.filter(ranges='未复现问题')))
    factory4 = int(len(we30c_4th.objects.filter(ranges='工厂制程问题')))
    tel4 = int(len(we30c_4th.objects.filter(ranges='遥控器不良')))
    power4 = int(len(we30c_4th.objects.filter(ranges='电源头不良')))
    HDMI4 = int(len(we30c_4th.objects.filter(ranges='HDMI线不良')))
    software4 = int(len(we30c_4th.objects.filter(ranges='软件相关问题')))
    analyse4 = int(len(we30c_4th.objects.filter(ranges='待分析')))
    RK4 = int(len(we30c_4th.objects.filter(ranges='RK芯片问题')))
    customer4 = int(len(we30c_4th.objects.filter(ranges='客户应用问题')))





    return render(request, 'we30c.html', {'re_number1':re_number1,'alls_1':alls_1,'hd1':hd1,'pd1':pd1,'na1':na1,'sales_1':first_sales,
                                          'qd1':qd1,'hd1_r':hd1_r,'pd1_r':pd1_r,'na1_r':na1_r,'qd1_r':qd1_r,
                                          'back1':back1,'no1':no1,'factory1':factory1,'tel1':tel1,'power1':power1,
                                          'HDMI1':HDMI1,'software1':software1,'analyse1':analyse1,'RK1':RK1,'customer1':customer1,
                                          're_number2':re_number2,'alls_2':alls_2,'hd2':hd2,'pd2':pd2,'na2':na2,'sales_2':second_sales,
                                          'qd2': qd2,'hd2_r': hd2_r, 'pd2_r': pd2_r, 'na2_r': na2_r, 'qd2_r': qd2_r,
                                          'back2': back2,'no2': no2, 'factory2': factory2,'tel2': tel2,'power2': power2,
                                          'HDMI2': HDMI2,'software2':software2,'analyse2':analyse2,'RK2':RK2,'customer2':customer2,
                                          're_number3':re_number3,'alls_3':alls_3,'hd3':hd3,'pd3':pd3,'na3':na3,'sales_3':third_sales,
                                          'qd3':qd3,'hd3_r':hd3_r,'pd3_r':pd3_r,'na3_r':na3_r,'qd3_r':qd3_r,
                                          'back3':back3,'no3':no3,'factory3':factory3,'tel3':tel3,'power3':power3,
                                          'HDMI3':HDMI3,'software3':software3,'analyse3':analyse3,'RK3':RK3,'customer3':customer3,
                                          're_number4':re_number4,'alls_4':alls_4,'hd4':hd4,'pd4':pd4,'na4':na4,'sales_4':fouth_sales,
                                          'qd4':qd4,'hd4_r':hd4_r,'pd4_r':pd4_r,'na4_r':na4_r,'qd4_r':qd4_r,
                                          'back4':back4,'no4':no4,'factory4':factory4,'tel4':tel4,'power4':power4,
                                          'HDMI4':HDMI4,'software4':software4,'analyse4':analyse4,'RK4':RK4,'customer4':customer4,
                                          })



