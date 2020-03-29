# apitest2020
apitest2020 : study api test \
学习接口自动化测试
##基本使用
###1. 启动z_djangodir 的manager.py  
    python manager.py runserver 8000

###2.  修改 data/case.xlsx 接口测试case
    
###3. 执行main/run_test.py 
    python run_test.py
    
## 结构说明
1.  base: 放置基本的测试方法
2.  case: 后期放置测试的case。比如测试单独case,多个测试case
3.  data: 放置测试时 需要的硬数据。比如xlsx,json,或者模拟的数据、文件
4.  datacfg: 获取数据的方法
5. main:  执行入口
6. utils: 存放通用的工具、操作方法
###
    z_djangodir : 简单的django 用于测试学习用 

 
