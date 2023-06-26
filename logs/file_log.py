#输出控制台
import logging

#1、设置log名称
loger = logging.getLogger("file_log")
#2、设置log级别
loger.setLevel(logging.DEBUG)
#3、创建handder
fh_stream=logging.StreamHandler()
fh_file=logging.FileHandler('./test.log')
#4、设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel((logging.WARNING))
#5、定义输出格式
formatter=logging.Formatter('%(asctime)s%(name)s%(levelname)s%(message)s')
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)
#6、添加hedler
loger.addHandler(fh_stream)
loger.addHandler((fh_file))
#7、运行输出
loger.info("this is a info")
loger.debug("this is a debug")
loger.warning("this is a warning")
