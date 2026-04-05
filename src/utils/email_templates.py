from pydantic import EmailStr

def request_reset_password_template(user, token):
    return f"""Hello {user.first_name}
We received a request to reset your password

Your password reset code is: {token},
This token will expire in 15 minutes,

If you didn't make this request, please ignore this email.


Best regards
The Circleground Team
"""


def verify_email_template(user, verification_token):
    return f""" Hello {user.first_name},
Welcome to Circleground! 🎉

Thank you for creating an account with us. To complete your registration,
please verify your email address using the verification code below:

Verification Code: {verification_token}

This code will expire in 15 minutes.

If you did not create this account, please ignore this email.

We’re excited to have you on board!

Best regards,
The Circleground Team
"""
