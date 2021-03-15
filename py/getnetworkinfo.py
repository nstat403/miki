
#-*- coding:utf-8 -*-
#import logging
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('program start')
#logging.disable(logging.CRITICAL)
import json
import subprocess
import datetime

def gettimecode():
    timecode=datetime.datetime.now()
    timestr=datetime.datetime.strftime(timecode,'%Y%m%d-%H:%M:%S')
    return timestr




def getnetworkinfo():
    cmd='termux-telephony-deviceinfo'
    result=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    d=json.loads(result.stdout)
    if d['network_operator']=='44011':#44011raku
        d['networkName']='rakuten'
        d['waveName']=d['network_operator']
    else:
        d['networkName']='other'
        d['waveName']=d['network_operator']
    return d




def getgps():
    cmd='termux-location'
    result=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    d=json.loads(result.stdout)
    return d


if __name__=='__main__':
    timestr=gettimecode()
    info=getnetworkinfo()
    gps=getgps()
    #print(timestr)
    #print(gps['latitude'])
    #print(timestr,gps['latitude'],gps['longitude'],d['altitude'])
    #print(timestr,info['waveName'],info['networkName'])
    print(timestr,gps['latitude'],gps['longitude'],gps['altitude'],info['waveName'],info['networkName'])
    
    pass


    
