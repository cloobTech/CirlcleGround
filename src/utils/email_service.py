import yagmail
from pydantic import EmailStr
from src.core.pydantic_confirguration import config
from src.core.exceptions import EmailServiceError




class EmailService:
    def get_email_details(self):
        return yagmail.SMTP(
            user=config.MAIL_FROM,
            password=config.MAIL_PASSWORD
        )
    def send_email(self, to: EmailStr, subject: str, contents: str | list):
        try:
                yag = self.get_email_details()
                yag.send(to=to, subject=subject, contents=contents)
                return{
                    "status": "success",
                    "message": "email successfully sent"
                }
        except Exception as e:
             
             raise EmailServiceError(
                  message="Error sending email",
                  details= e
             )

email_service = EmailService()    