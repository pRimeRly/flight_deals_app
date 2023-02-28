import smtplib

# ------------Replace with your details for---------------
# -------------Required for sending notifications---------
MY_EMAIL = "sample@outlook.com"
MY_PASSWORD = "sample_password"

# -------------Replace with Server Address for your Email provider
EMAIL_SERVER_ADDRESS = "smtp-mail.outlook.com"


class NotificationManager:
    def send_emails(self, user_emails, message, flight_link):
        with smtplib.SMTP(EMAIL_SERVER_ADDRESS) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in user_emails:
                conn.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=f"Subject: New Low Price FLight! \n\n{message}\n{flight_link}".encode("utf-8"))
