import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "subhojitguin2004@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "subhojitguin2004@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    send_email("""\
    Subject: Hi
    Hello how are you?
    Bye!
    """)
