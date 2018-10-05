import smtplib
 
def sendemail(pikutrump007@gmail.com, kajalkatiyar008@gmail.com ,
              email, hEYA PYTHoN,
              pikutrump, kunalowl,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s
' % pikutrump007@gmail.com
    header += 'To: %s
' % ','.join(kajalkatiyar008@gmail.com)
    header += 'Cc: %s
' % ','.join(cc_addr_list)
  #  header += 'Subject: %s

' % subject
    message = '''header + message''' hEYA PYTHoN
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(pikutrump,kunalowl)
    problems = server.sendmail(pikutrump007@gmail.com, kajalkatiyar008@gmail.com, message)
    server.quit()
