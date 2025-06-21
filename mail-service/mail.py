import smtplib

my_email = "akhilmzh1@gmail.com"
password = "save password here"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="akhil2991@gmail.com",
                        msg="Subject:Hello\n\nthis is The body of my email")
