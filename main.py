import urllib.request
import json

print('%s出行无忧%s' % ('-' * 30,'-' * 30))
qidian = input('请输入起点名称:')
qidian_chengshi = input('请输入起点所在的城市:')
zhongdian = input('请输入终点名称:')
zhongdian_chengshi = input('请输入终点所在的城市:')

qidian = urllib.parse.quote(qidian)
qidian_chengshi = urllib.parse.quote(qidian_chengshi)
zhongdian = urllib.parse.quote(zhongdian)
zhongdian_chengshi = urllib.parse.quote(zhongdian_chengshi)

print('请选择出行方式:')
print('1.驾车')
print('2.步行')
print('3.公交')
print('4.骑行')
print('5.出租汽车')
cxfs_id = input('请输入:')
if cxfs_id == '1':
    cxfs =  'driving'
elif cxfs_id == '2':
    cxfs = 'walking'
elif cxfs_id == '3':
    cxfs = 'transit'
elif cxfs_id == '4':
    cxfs = 'riding'
elif cxfs_id == '5':pass
else:
    print('您的输入有误，已经为您选择默认值驾车。')
    cxfs = 'driving'
    
if cxfs_id != '5':
    print('请选择导航偏好:')
    print('1.不走高速')
    print('2.最少时间')
    print('3.最短路径')

    pianhao = int(input('请输入:')) + 9
else:
    pianhao=12
    cxfs = 'driving'

key = 'mBhpRaBTS9iEOZ13kWVPxZ3DTOiZHSGF'

request = urllib.request.urlopen('http://api.map.baidu.com/direction/v1?mode=%s&origin=%s&destination=%s&origin_region=%s&destination_region=%s&output=json&tactics=%s&ak=%s'
                       % (cxfs,qidian,zhongdian,qidian_chengshi,zhongdian_chengshi,pianhao,key))

datas = json.loads(request.read().decode('utf-8'))

step_count = 0
buf = ''

if datas['status'] != 0:
    print('%d:%s' % (datas['status'],datas['message']))
    exit(0)

flag = True

if cxfs_id == '1':
    while flag == True:
        try:
            buf = datas['result']['routes'][0]['steps'][step_count]['instructions']
            buf = buf.replace('<b>','')
            buf = buf.replace('</b>','')
            buf = buf.replace('<font color="0x000000">','')
            buf = buf.replace('</font>','')
            buf = buf.replace('<br/>','')
            buf = buf.replace('<font color="0xDC3C3C">','，')
            print('第%d步:%s' % (step_count + 1,buf))
            step_count += 1
        except IndexError:
            flag = False
        except KeyError:
            flag = True
            try:
                print('您输入的地点过于模糊，请尝试输入以下起点。')
                while flag == True:
                    try:
                        print(datas['result']['origin']['cityName'],datas['result']['origin']['content'][step_count]['name'],'地址:',datas['result']['origin']['content'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                print('请尝试以下终点')
                flag = True
                step_count = 0
                while flag == True:
                    try:
                        print(datas['result']['destination']['cityName'],datas['result']['destination']['content'][step_count]['name'],'地址:',datas['result']['destination']['content'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                        exit(0)
                
            except IndexError:
                print('获取数据错误。')
                exit(0)

    jvli=0
    info = ''

    if datas['result']['routes'][0]['distance'] <= 1000:
        jvli = datas['result']['routes'][0]['distance']
        info = '以上方案距离为%d米，预计耗时%d秒，' % (jvli,datas['result']['routes'][0]['duration'])
    elif datas['result']['routes'][0]['distance'] >= 1000:
        jvli = datas['result']['routes'][0]['distance'] / 1000
        miao = datas['result']['routes'][0]['duration']
        info = '以上方案距离为%g公里，预计耗时%d秒，' % (jvli,miao)

    info += '过路费%s元' % datas['result']['routes'][0]['toll']
        
    print(info)

elif cxfs_id == '2':
    while flag == True:
        try:
            buf = datas['result']['routes'][0]['steps'][step_count]['instructions']
            buf = buf.replace('<b>','')
            buf = buf.replace('</b>','')
            buf = buf.replace('</br>','')
            print('第%d步:%s' % (step_count + 1,buf))
            step_count += 1
        except IndexError:
            flag = False
        except KeyError:
            flag = True
            try:
                print('您输入的地点过于模糊，请尝试输入以下起点。')
                while flag == True:
                    try:
                        print(datas['result']['origin']['cityName'],datas['result']['origin']['content'][step_count]['name'],'地址:',datas['result']['origin']['content'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                print('请尝试以下终点')
                flag = True
                step_count = 0
                while flag == True:
                    try:
                        print(datas['result']['destination']['cityName'],datas['result']['destination']['content'][step_count]['name'],'地址:',datas['result']['destination']['content'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                        exit(0)
                
            except IndexError:
                print('获取数据错误。')
                exit(0)

    jvli=0
    info = ''

    if datas['result']['routes'][0]['distance'] <= 1000:
        jvli = datas['result']['routes'][0]['distance']
        info = '以上方案距离为%d米，预计耗时%d秒' % (jvli,datas['result']['routes'][0]['duration'])
    elif datas['result']['routes'][0]['distance'] >= 1000:
        jvli = datas['result']['routes'][0]['distance'] / 1000
        miao = datas['result']['routes'][0]['duration']
        info = '以上方案距离为%g公里，预计耗时%d秒' % (jvli,miao)
        
    print(info)


elif cxfs_id == '3':
    while flag == True:
        try:
            buf = datas['result']['routes'][0]['scheme'][0]['steps'][step_count][0]['stepInstruction']
            buf = buf.replace('<font color="#313233">','')
            buf = buf.replace('</font>','')
            buf = buf.replace('<font color="#7a7c80">','')
            buf = buf.replace('</font>','')
            print('第%d步:%s' % (step_count + 1,buf),end = '')
            print(',预计通过要%d秒' % datas['result']['routes'][0]['scheme'][0]['steps'][step_count][0]['duration'],end='')
            try:
                print('(首班车：%s，末班车：%s)' % 
                    (datas['result']['routes'][0]['scheme'][0]['steps'][step_count][0]['vehicle']['start_time'],datas['result']['routes'][0]['scheme'][0]['steps'][step_count][0]['vehicle']['end_time']))
            except TypeError:
                print('')
            else:
                print('')
            step_count += 1
        except IndexError:
            flag = False
        except KeyError:
            flag = True
            try:
                print('您输入的地点过于模糊，请尝试输入以下起点。')
                while flag == True:
                    try:
                        print(datas['result']['origin'][step_count]['name'],'地址:',datas['result']['origin'][step_count]['address'])
                        step_count += 1
                    except KeyError:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                print('请尝试以下终点')
                flag = True
                step_count = 0
                while flag == True:
                    try:
                        print(datas['result']['destination'][step_count]['name'],'地址:',datas['result']['destination'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                        exit(0)
                
            except IndexError:
                print('获取数据错误。')
                exit(0)

    jvli=0
    info = ''

    if datas['result']['routes'][0]['scheme'][0]['distance'] <= 1000:
        jvli = datas['result']['routes'][0]['scheme'][0]['distance']
        miao = datas['result']['routes'][0]['scheme'][0]['duration']
        info = '以上方案距离为%d米，预计耗时%d秒，公交（地铁）票总价为%g元（%d分）' % (jvli,miao,datas['result']['routes'][0]['scheme'][0]['price'] / 100,datas['result']['routes'][0]['scheme'][0]['price'])
    elif datas['result']['routes'][0]['scheme'][0]['distance'] >= 1000:
        jvli = datas['result']['routes'][0]['scheme'][0]['distance'] / 1000
        miao = datas['result']['routes'][0]['scheme'][0]['duration']
        info = '以上方案距离为%g公里，预计耗时%d秒，公交（地铁）票总价为%g元（%d分）' % (jvli,miao,datas['result']['routes'][0]['scheme'][0]['price'] / 100,datas['result']['routes'][0]['scheme'][0]['price'])
        
    print(info)

elif cxfs_id == '4':
    while flag == True:
        try:
            buf = datas['result']['routes'][0]['steps'][step_count]['instructions']
            buf = buf.replace('<b>','')
            buf = buf.replace('</b>','')
            buf = buf.replace('</br>','')
            print('第%d步:%s' % (step_count + 1,buf))
            step_count += 1
        except IndexError:
            flag = False
        except KeyError:
            flag = True
            try:
                print('您输入的地点过于模糊，请尝试输入以下起点。')
                while flag == True:
                    try:
                        print(datas['result']['origin']['cityName'],datas['result']['origin']['content'][step_count]['name'],'地址:',datas['result']['origin']['content'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                print('请尝试以下终点')
                flag = True
                step_count = 0
                while flag == True:
                    try:
                        print(datas['result']['destination']['cityName'],datas['result']['destination']['content'][step_count]['name'],'地址:',datas['result']['destination']['content'][step_count]['address'])
                        step_count += 1
                    except:
                        flag = False
                        if step_count == 0:
                            print('[空]')
                        exit(0)
                
            except IndexError:
                print('获取数据错误。')
                exit(0)

    jvli=0
    info = ''

    if datas['result']['routes'][0]['distance'] <= 1000:
        jvli = datas['result']['routes'][0]['distance']
        info = '以上方案距离为%d米，预计耗时%d秒' % (jvli,datas['result']['routes'][0]['duration'])
    elif datas['result']['routes'][0]['distance'] >= 1000:
        jvli = datas['result']['routes'][0]['distance'] / 1000
        miao = datas['result']['routes'][0]['duration']
        info = '以上方案距离为%g公里，预计耗时%d秒' % (jvli,miao)
        
    print(info)

elif cxfs_id == '5':
    print(datas['result']['taxi']['remark'])
    print('预计:%s元' % datas['result']['taxi']['detail'][0]['total_price'])
