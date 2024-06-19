from pandas import DataFrame
import  smtplib #actual sending fx
from email.message import EmailMessage #themodule needed



def process_logs(logs):
    """function to check for all logs with error"""
    with open(logs, 'r') as f:
        data = f.readlines()
        result_dict = {}
        for line in data:
            if 'error' in line:
                
                with open('error_logs.txt', 'a') as f1:
                    f1.write(line)
                
    return 'error_logs.txt'

def handle_error(logs):
    """Function to handle the logs with error
    at the moment the function is writing all errors in the excel"""
    time = []
    device = []
    error = []
    with open(logs, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line. split()
            time.append(data[0:3])
            device.append(data[3:4])
            error.append(data[5:])
        
            
    df = DataFrame({'Date': time, 'Device': device, 'Error  details':error})
    df.to_excel('test.xlsx', sheet_name = 'SRX', index = False)
    return 'test.xslx' 

def input_email():
    """function to write the body of the email"""
    cont = input("Enter the email content, or input 'Proceed' to use default")
    if cont.lower() == 'proceed':
        return "Hello /n The following logs were found with error. /n  regards"
    else:
        return cont   

def email_file():
    """The function to send the email"""
    msg = EmailMessage()
    msg.set_content(input_email())
    msg['Subject'] = "Error logs"
    msg['From'] = 'xxxx@gmail.com'
    msg['To'] = 'yyy@gmail.com'
    #below email has no attachment, working on allowing the gmail app access, later on adding the attachment
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as s:
        s.login('xxxx@gmail.com', 'password')
        s.sendmail('xxxx@gmail.com','yyyy@gmail.com',msg)
        print('Message sent')
            
