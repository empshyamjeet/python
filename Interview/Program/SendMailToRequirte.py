import smtplib
import ssl
from email.message import EmailMessage
import mimetypes
import time
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# -----------------------
# Configuration
# -----------------------

SENDER_EMAIL = "er.shyamjeet@gmail.com"
SENDER_PASSWORD =   # Use Gmail App Password here
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
MAX_THREADS = 5  # Adjust but keep Gmail-safe
ATTACHMENT_PATH = "/Volumes/Personal/python/Interview/Program/Shyamjeet_backbase.pdf"
#ATTACHMENT_PATH = "/Volumes/Personal/python/Interview/Program/Shyamjeet_backbase.pdf"
RECIPIENTS_FILE = "/Volumes/Personal/python/Interview/Program/recipients.txt"
FAILED_LOG = "failed_recipients.txt"

# -----------------------
# Read recipients
# -----------------------
def read_recipients(file_path):
    with open(file_path, 'r') as file:
        recipients = file.read().splitlines()
    return recipients

# -----------------------
# Send single email
# -----------------------
def sendMail(recipient):
    subject = "QA automation || 11 Years || PAN INDIA || LWD 24th Oct 2025"
    body = """\
Hi,

I am looking for QA automation jobs in PAN India.

Full Name: Shyamjeet kumar sharma
Contact Number: 9162969666
Email ID: er.shyamjeet@gmail.com / empshyamjeet@gmail.com
Date of Birth (DOB): 13th Aug 1992
Current Location: Hyderbad
Preferred Location: Only Noida, Gurugram and Delhi NCR - Remote
Current Working Mode :  Hybrid
Total Experience: 11 years
Relevant Experience: Same 11 years
Number of Projects Completed: 5 +
Current Organization: Backbase
Current Designation: Sr. Automation QA 
Current CTC: 33 lpa + 2.5 lpa
Expected CTC: 33 lpa + 2.5 lpa
Official Notice Period: 30 days
Offers in Hand: No
LinkedIn Profile Link: https://www.linkedin.com/in/shyamjeetkumarsharma/
Employment Type: FTE
Any Interviews/Offers in Pipeline: NA
Documents Available (Y/N): Y

Thanks,  
Shyamjeet Sharma
"""
    # Create EmailMessage object
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach file
    file_name = ATTACHMENT_PATH.split("/")[-1]
    mime_type, _ = mimetypes.guess_type(ATTACHMENT_PATH)
    if mime_type is None:
        mime_type = "application/octet-stream"
    maintype, subtype = mime_type.split("/")
    with open(ATTACHMENT_PATH, "rb") as f:
        msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=file_name)

    # Send email via SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    # Random delay to avoid spam detection
    time.sleep(random.uniform(0.5, 2))  # 0.5–2 sec delay
    print(f"Sent to: {recipient}")

# -----------------------
# Main function
# -----------------------
def main():
    recipients = read_recipients(RECIPIENTS_FILE)
    start_time = datetime.now()
    print("Start Time:", start_time.strftime("%Y-%m-%d %H:%M:%S"))

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = {executor.submit(sendMail, r): r for r in recipients}
        for future in as_completed(futures):
            recipient = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error sending to {recipient}: {e}")
                with open(FAILED_LOG, "a") as f:
                    f.write(f"{recipient}: {e}\n")

    end_time = datetime.now()
    print("End Time:", end_time.strftime("%Y-%m-%d %H:%M:%S"))
    duration = end_time - start_time
    print("Duration:", duration)

# -----------------------
# Run
# -----------------------
if __name__ == "__main__":
    main()
