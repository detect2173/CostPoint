from tkinter import *
import ctypes  # An included library with Python install. Used to create message box
import time
from tkinter import *

import arrow
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
global user_acct
global user_proj
global user_notes
options = Options()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def setvars():
    global user_acct
    global user_proj
    global user_notes
    user_acct = acct_entry.get()
    user_proj = proj_entry.get()
    user_notes = notes_entry.get(index1=1.0, index2="end-1c")



root = Tk()
root.title('Account#/Project#/Notes')
root.geometry('550x300')
root.wm_maxsize(width=550, height=300)
root.iconbitmap('cp.ico')
proj_lbl = Label(text='Project Number:')
proj_lbl.pack()
project = StringVar(root, value='7003.01.006.05')
proj_entry = Entry(root, textvariable=project)
# proj_entry.grid(row=0, column=0, pady=5)
proj_entry.pack(pady=5)
acct_lbl = Label(text='Account Number:')
acct_lbl.pack()
account = StringVar(root, value='610-201-30')
acct_entry = Entry(root, textvariable=account)
# acct_entry.grid(row=0, column=1, pady=5)
acct_entry.pack(pady=5)
notes_lbl = Label(text='Notes:')
notes_lbl.pack(pady=15)
notes = 'SHRO incentive program restocking for prize vault/attire'
notes_entry = Text(root, width=50, height=6, wrap='word')
notes_entry.insert(END, notes)

notes_entry.pack(pady=5)


def quit_win():
    root.destroy()


set_var = Button(root, text='Submit',command=lambda: [setvars(), quit_win()])
set_var.pack(pady=10, padx=20)

root.mainloop()


def two_weeks():
    today = arrow.now()
    today2 = today.shift(weeks=2)
    new_date = today2.format('MM/DD/YYYY')
    return new_date


a = Service(executable_path=r"C:\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(options=options, service=a)
# driver.maximize_window()
root.quit()
driver.get("https://cp.etrky.com/cpweb/cploginform.htm")
fName = driver.find_element(By.NAME, "USER")
fName.send_keys("JBERRY")
lName = driver.find_element(By.NAME, "CLIENT_PASSWORD")
lName.send_keys("jb7535")
email_address = driver.find_element(By.NAME, "DATABASE")
email_address.send_keys("DELTEKCP")
button = driver.find_element(By.NAME, "Login")
button.click()
time.sleep(4)

materials = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div')
materials.click()
time.sleep(1)
procurement = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div')
procurement.click()
time.sleep(1)
req = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div')
req.click()
time.sleep(1)
manage = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div')
manage.click()
time.sleep(5)
app_process = driver.find_element(By.ID, 'RQ_APPR_PROC_CD')
app_process.send_keys('PR-APPR7')
time.sleep(1)
submit_app = driver.find_element(By.ID, 'SUBMIT_APPRVL')
submit_app.click()
time.sleep(1)
organization = driver.find_element(By.ID, 'RQST_ORG_ID')
organization.send_keys('1.01.07.01')
time.sleep(1)
req_date = driver.find_element(By.ID, 'TGT_PLACE_DT')
req_date.click()
date = two_weeks()
req_date.send_keys(date)
time.sleep(1)
buyer = driver.find_element(By.ID, 'BUYER_ID')
buyer.send_keys('NFOGEL')
time.sleep(1)
proc_type = driver.find_element(By.ID, 'PROCURE_TYPE_CD')
proc_type.send_keys('NR')
time.sleep(1)
phone = driver.find_element(By.ID, 'RQST_PHONE_ID')
phone.send_keys('802-877-0189')
time.sleep(1)
accounting = driver.find_element(By.XPATH, '/html/body/div[10]/div[15]/div[4]/form/div[7]/div[1]/span[6]')
accounting.click()
time.sleep(2)
project = driver.find_element(By.ID, 'PROJ_ID')
project.send_keys(user_proj)
time.sleep(2)
account = driver.find_element(By.ID, 'ACCT_ID')
account.send_keys(user_acct)
time.sleep(2)
inv_abbr = driver.find_element(By.ID, 'INVT_ABBRV_CD')
inv_abbr.send_keys('700300')
time.sleep(2)
other = driver.find_element(By.XPATH, '/html/body/div[10]/div[15]/div[4]/form/div[7]/div[1]/span[10]')
other.click()
time.sleep(2)
date2 = driver.find_element(By.ID, 'RQST_DT')
date2.send_keys(date)
time.sleep(1)
ship = driver.find_element(By.ID, 'SHIP_ID')
ship.send_keys('WH-NJCC')
time.sleep(1)
deliver_to = driver.find_element(By.ID, 'DEL_TO_FLD')
deliver_to.send_keys('Logistics/SHRO-JBERRY')
time.sleep(1)
vendor = driver.find_element(By.ID, 'VEND_ID')
vendor.send_keys('013365')  # This is for Mitchell's Tees & Signs
time.sleep(1)
notes_tab = driver.find_element(By.XPATH, '/html/body/div[10]/div[15]/div[4]/form/div[7]/div[1]/span[14]')
notes_tab.click()
time.sleep(2)
notes = driver.find_element(By.ID, 'RQ_NOTES')
notes.send_keys(user_notes)

header = driver.find_element(By.XPATH, '/html/body/div[10]/div[15]/div[4]/form/div[7]/div[1]/span[2]')
header.click()
Mbox('READY!', 'You are logged in, pre-filled and ready to start entering line items!', 1)
