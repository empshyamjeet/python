import smtplib
import ssl
from email.message import EmailMessage
import mimetypes

def read_recipients(file_path):
    with open(file_path, 'r') as file:
        recipients = file.read().splitlines()
    return recipients

#login
sender_email = "er.shyamjeet@gmail.com"
sender_password = ""  # App Password

def sendMail(recipient):
    subject = "QA automation || 10 Years || PAN INDIA || LWD 20th June 2025"
    body = """
    Hi,
    
    I hope this message finds you well.
    I am writing to express my interest in QA Automation opportunities. With over 10 years of experience in automation testing, I have successfully delivered high-quality testing solutions across web, mobile, and API platforms.
    My core expertise includes:
        ✔️ Java, Selenium WebDriver, TestNG, Cucumber (BDD)  
        ✔️ Mobile Testing using Appium, and BrowserStack  
        ✔️ API Testing with REST Assured, Postman  
        ✔️ CI/CD integration with Maven, Jenkins, Git  
        ✔️ Agile/Scrum projects using Jira and Azure DevOps,AWS and GCP
    I am currently exploring challenging roles as a Senior QA Engineer / QA Automation Lead, where I can contribute to building scalable automation frameworks and a quality-first engineering culture.
    
    Please find my updated resume attached. I would be grateful if you could consider me for any relevant opportunities and keep me informed of any openings that align with my profile.
    
    Feel free to contact me at 8826700171 or er.shyamjeet@gmail.com.
    
    I am available for immediate joining or with a negotiable notice period.
    
    Thank you for your time and consideration.
    
    Best regards,  
    Shyamjeet Sharma
    """
    # Create EmailMessage object
    msg = EmailMessage()
    msg["From"] = "Shyamjeet"
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach a file
    file_path = "/Volumes/Personal/python/Interview/Program/Shyamjeet_backbase.pdf"
    #file_path = "/Volumes/Personal/python/Interview/Program/Qa automation Java Web and APIs testing.pdf"
    file_name = file_path.split("/")[-1] 
    # Detect MIME type
    mime_type, _ = mimetypes.guess_type(file_path)
    mime_type, mime_subtype = mime_type.split("/")

    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype=mime_type, subtype=mime_subtype, filename=file_name)

    # SMTP Setup and Send
    smtp_server = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Example usage
recipients = read_recipients('/Volumes/Personal/python/Interview/Program/recipients.txt')
for recipient in recipients:
    sendMail(recipient)
    print(recipient)