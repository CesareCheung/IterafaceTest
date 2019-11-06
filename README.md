
#接口自动化
###框架结构：Python3+Requests+Excel+PyMsql


 ####1.  base ：基类
 
          runmethod ：对Get/Post请求方式进行封装
   
 ####2.  data ： 数据依赖层

          data_config :获取对应模块所在的列
       
          dependent_data ：解决数据依赖问题
       
          get_data ：获取excel中对应模块中的对应行的数据
       
 #### 3.   dataconfig ：用例层
 
          case1：测试用例
         
          data：接口请求参数
         
          token：实时获取到的token
  
 ####4. main：运行程序

          run_test：主运行程序
   
 ####5. util ：公共方法
  
          common_util：判断两个值是否一致，用于做断言
    
          connect_db：连接及操作数据库
    
          operation_excel：操作Excel，读取及回写数据
    
          operation_header：实时获取token
    
          operation_json：操作读取json文件（方便后面接口读取对应的参数）
    
          send_email：发送邮件方法封装