import smtplib

content = 'HI PYTHON'
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('pikutrump007@gmail.com','kunalowl')
mail.sendmail('pikutrump007@gmail.com','kajalkatiyar008@gmail.com',content)
mail.close()
