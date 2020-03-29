import smtplib
from  email.mime.text import MIMEText

##MIMEText
class SendMail():
    global send_user
    global smtp_host
    global password
    smtp_host = "smtp.leofs.com.cn"
    send_user = "xuyh@leofs.com.cn"
    password = "x"

    def send_mail(self,user_list,sub,content):
        user = "XUYH" + "<" + send_user + ">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub    #主题
        message['From'] = user
        message['To'] = ';'.join(user_list)         #多个收件人 就用分号隔开

        server = smtplib.SMTP()
        server.connect(smtp_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())

        server.close()

if __name__ == '__main__':
    sm = SendMail()
    user_list = ["xuyh@leofs.com.cn","yellhao@sina.com"]
    user_list = ["xuyh@leofs.com.cn"]
    sm.send_mail(user_list,"测试邮件-python","a b c d e f g bababa \n 这是测试邮件哈")