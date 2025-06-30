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
    subject = "QA automation || 10 Years || PAN INDIA || LWD 11th Jul 2025"
    body = """
    Hi,
    
    I am looking for qa automation jobs in noida,gurgoan and delhi location, also join with same CTC.

    Full Name: Shyamjeet Kumar Sharma
    Contact Number: 8826700171
    Email ID: er.shyamjeet@gmail.com
    Date of Birth (DOB): 13/08/1990
    Current Location: Hyderabad
    Preferred Location:Hyderabad, Noida, Gurugram, Delhi NCR and Remote
    Current Working Mode :  Hybrid
    Total Experience: 10+ Years
    Relevant Experience: 10 Years
    Number of Projects Completed: 12 (Domains: Health & Banking)
    Current Organization: Backbase
    Current Designation: Senior QA Automation Engineer
    Current CTC: ₹36 LPA
    Expected CTC: join with same CTC
    Official Notice Period: 2–3 weeks (flexible depending on project ramp-down)
    Offers in Hand: No
    LinkedIn Profile Link: https://www.linkedin.com/in/shyamjeetkumarsharma/
    Employment Type: Permanent 
    Any Interviews/Offers in Pipeline: No
    Documents Available (Y/N): Yes – Offer Letters, Pay Slips, Relieving Letters, Bank Statements
    
    
    Thanks,  
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
    try:
        sendMail(recipient)
        print(recipient)
    except Exception as e:
        print(f"Error sending to {recipient}: {e}")