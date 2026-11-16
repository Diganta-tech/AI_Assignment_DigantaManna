responses = {
    "Login Issue": (
        "Please use the 'Forgot Password' option on the login page "
        "to reset your password. If the problem continues, "
        "please contact the support team."
    ),

    "Application Error": (
        "We apologize for the inconvenience. Please try refreshing "
        "the application or restarting it. If the error continues, "
        "please share the error message with our support team."
    ),

    "Account Update": (
        "Your account update request has been noted. Please check "
        "your account settings and ensure that the updated information "
        "is correct. Contact support if you need further assistance."
    ),

    "Performance": (
        "We apologize for the slow performance. Please check your "
        "internet connection and try again. If the issue persists, "
        "please contact our technical support team."
    ),

    "Report": (
        "Please visit the Reports section and select the required "
        "report to download it. If you cannot access the report, "
        "please contact the support team."
    )
}


def generate_response(category):
    return responses.get(
        category,
        "Thank you for contacting us. Our support team will review "
        "your issue and assist you shortly."
    )
