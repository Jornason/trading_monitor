from flask import url_for, request
from util import url_decode, json_response, has_no_empty_params, tail
import requests
import urllib
import subprocess, time, sys
import configparser
import pandas as pd
import json


# '''
def run(cmd):
    child = subprocess.Popen(
        cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True)
    return child

def routes(app):
    """app routes"""

    @app.route('/')
    def index():
        """index page"""
        print('index')
        r = {}
        return json_response(200, r, True)


    # 查询脚本运行进程 script:脚本名
    @app.route("/process")
    def query_process():
        '''
        /process?script=xxx
        '''        
        print('query_process')
        script_name = request.args.get("script") or ""
        CMD = ["pgrep", "-f", script_name + '.py']
        print(CMD)
        child = subprocess.Popen(CMD, stdout=subprocess.PIPE, shell=False)
        pid = child.communicate()[0].decode('utf-8')
        if pid:
            msg = '脚本%s正在运行, pid %s' % (script_name, pid)
            r = {'msg': msg}
            return json_response(200, r, True)
        else:
            msg = '脚本%s未运行！' % script_name
            r = {'msg': msg}
            return json_response(200, r, True)


    # 结束脚本运行进程 script:脚本名
    @app.route("/stop")
    def query_stop():
        '''
        /stop?script=xxx
        '''
        print('query_stop')
        script_name = request.args.get("script") or ""
        child = subprocess.Popen(["pgrep", "-f", script_name + '.py'],
                                 stdout=subprocess.PIPE,
                                 shell=False)
        pid = child.communicate()[0].decode('utf-8')
        if pid:
            CMD = 'kill -9 ' + pid
            sub_child = run(CMD)
            r = {'msg': pformat(sub_child)}
            return json_response(200, r, True)
        else:
            msg = '脚本%s未运行！' % script_name
            r = {'msg': msg}
            return json_response(200, r, True)


    # 启动脚本运行进程 script:脚本名, log:脚本名
    @app.route("/start")
    def query_start():
        '''
        /start?script=xxx&log=output
        '''
        print('query_start')
        script_name = request.args.get("script") or ""
        LOGPATH = request.args.get("log") or "output"
        LOGPATH += '.txt'
        child = subprocess.Popen(["pgrep", "-f", script_name + '.py'],
                                 stdout=subprocess.PIPE,
                                 shell=False)
        pid = child.communicate()[0].decode('utf-8')
        if pid:
            msg = '脚本%s已运行！' % script_name
            r = {'msg': msg}
            return json_response(200, r, True)
        else:
            # LOGPATH = 'output.txt'
            CMD = 'nohup python -u ' + script_name + '.py > ' + LOGPATH + ' 2>&1 &'
            sub_child = run(CMD)
            r = {'msg': pformat(sub_child)}
            return json_response(200, r, True)




if __name__=='__main__':
    pass









