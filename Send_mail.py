import zmail

# 发送邮件
def send_mail(subject,content_text,attachments):
    mail_content = {
        'subject': subject,
        'content_text': content_text,
        'attachments':attachments
    }
    server = zmail.server('15811958840@163.com','Chen1995',smtp_host='smtp.163.com',smtp_port=25,smtp_ssl=False)
    #yhlist = 'zj_yfsx@163.com'
    yhlist = ['790464118@qq.com',"640074586@qq.com"]
    send = server.send_mail(yhlist, mail_content,cc=['15811958840@163.com'])


# send_mail(subject="警报：‘Timed_Task’ 模块错误",
#           content_text="错误信息", attachments=None)