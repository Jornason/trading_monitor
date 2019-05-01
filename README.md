# 交易脚本监控服务

## 环境安装

1. conda 创建python

```
conda create -n py36trading python=3.6
```

2. conda 激活环境

```
conda activate py36trading
```

3. 安装包

```
pip install pandas==0.22.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install requests==2.18.4 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pysocks==1.6.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pytz -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask==1.0.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```



## 运行方式

```
conda activate py36trading
python trading_server.py
```

## 使用方式

### 监控脚本进程

```
http://127.0.0.1:7001/process?script=[脚本名]
```

### 停止脚本进程

```
http://127.0.0.1:7001/stop?script=[脚本名]
```

### 启动脚本进程

```
http://127.0.0.1:7001/start?script=[脚本名]&log=[日志名]
```

