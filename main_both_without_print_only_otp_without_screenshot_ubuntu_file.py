import datetime
import tkinter
import tkinter as tk
import os
import cv2
import csv
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import time
# import face_recognition
from decimal import Decimal
import json
import requests
from datetime import datetime
import datetime
from tkinter import *
from tkinter import Menu
import pyautogui
from datetime import datetime
import imutils
import PIL.Image
import PIL.ImageTk
import re
import urllib.request
import shutil
import requests
# import urllib3
from urllib.request import urlopen
import urllib
import base64
from datetime import datetime
import datetime
import smtplib
import math as m
import random as r
import base64
from PIL import Image
import logging
from datetime import date
from numpy import asarray
# from tkinter import *
from tkinter import ttk

# import easygui

today = date.today()
log_file = "log_files/" + "/" + str(today)
if not os.path.exists(log_file):
    os.makedirs(log_file)

logging.basicConfig(filename=log_file + "/" + "time_tracker.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# from resizeimage import resizeimage
timer = 0
source = 0
biometric = 0
# base_url = "http://localhost/timetracker_new/"

# base_url = "http://3.7.103.40/timetracker/"

base_url = "https://www.airface.in/timetracker/"

# base_url = "https://www.airface.in/airface_time_tracker/"


class register:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Timetracker")
        self.root.resizable(0, 0)
        self.val = StringVar()
        canvas = tk.Canvas(self.root, height=451, width=571)
        canvas.pack()
        self.bg_img = tk.PhotoImage(file="deer_decode.gif")
        self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
        self.menu = Menu(self.root)
        self.new_item = Menu(self.menu)
        # self.new_item.add_command(label='Screen Capture', command=self.srccapture)
        # self.new_item.add_separator()
        # self.new_item.add_command(label='  Camera  ', command=self.camera)
        # self.new_item.add_separator()
        # self.menu.add_cascade(label='  Setting  ', menu=self.new_item)
        # self.new_item1 = Menu(self.menu)
        # self.root.config(menu=self.menu)
        # self.l1 = tk.Label(self.root, text="By ",fg="white",bg="#1d2736" ,font="MSGothic 26 bold")
        # self.l1.place(x=10,y=120)
        # self.l2 = tk.Label(self.root, text="ABSTECH SERVICE ",fg="white",bg="#1d2736" ,font="MSGothic 26 bold")
        # self.l2.place(x=85,y=160)
        self.quitWindow = tk.Button(text="Login", command=self.submit, fg="white", bg="#1d2736",
                                    font="MSGothic 18 bold")
        self.quitWindow.place(x=180, y=200)
        self.clearWindow = tk.Button(text=" Exit ", command=self.ExitApplication, fg="white", bg="#1d2736",
                                     font="MSGothic 18 bold")
        self.clearWindow.place(x=300, y=200)
        self.root.mainloop()

    def submit(self):
        if not os.path.exists('captures'):
            os.makedirs('captures')
        else:
            shutil.rmtree('captures')
            os.makedirs('captures')
        if not os.path.exists('detected'):
            os.makedirs('detected')
        else:
            shutil.rmtree('detected')
            os.makedirs('detected')
        if not os.path.exists('backup'):
            os.makedirs('backup')
        else:
            shutil.rmtree('backup')
            os.makedirs('backup')
        if not os.path.exists('backupimg'):
            os.makedirs('backupimg')
        else:
            shutil.rmtree('backupimg')
            os.makedirs('backupimg')

        self.root.destroy()
        login_dynamic()

    # def camera(self):
    #     self.top = tk.Toplevel(self.root, bg="#1d2736")
    #     self.l1 = tk.Label(self.top, text="  Camera  ", fg="white", bg="#1d2736", font="MSGothic 25 bold")
    #     self.l1.place(x=90, y=1)
    #     self.top.title('Camera')
    #     self.top.geometry('300x230')
    #     self.option = StringVar()
    #     # self.R1 = Radiobutton(self.top, text="Take Camera Shots \nWith Screen Shots", value="0", var=self.option,fg="white",bg="#1d2736" ,font="MSGothic 13 bold")
    #     # self.R1.place(x=10, y=50)
    #     self.label = tk.Label(self.top, text="Camera Source", fg="white", bg="#1d2736", font="MSGothic 13 bold")
    #     self.label.place(x=10, y=110)
    #     self.txt1 = tk.Spinbox(self.top, values=('Cam1', 'Cam2', 'Cam3'), textvariable=self.val, width=20, fg="#1d2736",
    #                            font=('times', 15, ' bold '))
    #     self.txt1.place(x=10, y=150)
    #     self.submit = tk.Button(self.top, text='Submit', command=self.channelno, fg="white", bg="#1d2736",
    #                             font="MSGothic 13 bold")
    #     self.submit.place(x=100, y=190)

    # def channelno(self):
    #     global source
    #     source = str(self.txt1.get())
    #     if source == "Cam1":
    #         source = 0
    #         tkinter.messagebox.showinfo(title="Information", message="Camera source set to 0")
    #     elif source == "Cam2":
    #         source = 1
    #         tkinter.messagebox.showinfo(title="Information", message="Camera source set to 1")
    #     else:
    #         source = 2
    #         tkinter.messagebox.showinfo(title="Information", message="Camera source set to 2")
    #     self.top.destroy()

    # def srccapture(self):
    #     self.top = tk.Toplevel(self.root, bg="#1d2736")
    #     self.l1 = tk.Label(self.top, text="Screen Capture ", fg="white", bg="#1d2736", font="MSGothic 19 bold")
    #     self.l1.place(x=90, y=5)
    #     self.top.title('Screencapture')
    #     self.top.geometry('300x200')
    #     self.label = tk.Label(self.top, text="Update interval", fg="white", bg="#1d2736", font="MSGothic 13 bold")
    #     self.label.place(x=10, y=50)
    #     self.txt1 = tk.Spinbox(self.top, values=('05', '15', '30'), textvariable=self.val, width=15, fg="#1d2736",
    #                            font=('times', 15, ' bold '))
    #     self.txt1.place(x=10, y=90)
    #     self.submit = tk.Button(self.top, text='Submit', command=self.timeslot, fg="white", bg="#1d2736",
    #                             font="MSGothic 13 bold")
    #     self.submit.place(x=100, y=150)
    #
    # def timeslot(self):
    #     global timer
    #     timer = int(self.txt1.get())
    #     timer = timer * 60
    #     print(timer)
    #     self.top.destroy()

    def ExitApplication(self):
        # self.root.destroy()
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            self.root.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')


def main():
    register()


def login_dynamic():
    class user_login:

        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.val = StringVar()
            canvas = tk.Canvas(self.root, height=451, width=571)
            canvas.pack()
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            # self.label_msg = canvas.create_text((150, 40), text="AIRFACE TimeTracker",justify = tk.CENTER, font="ALGERIAN 18 bold", fill="white")
            self.label_msg1 = canvas.create_text((150, 150), text="Email Id", justify=tk.CENTER,
                                                 font="MSGothic 16 bold", fill="white")
            self.txt = tk.Entry(width=26, fg="#1d2736", font=('times', 15, ' bold '))
            self.txt.place(x=220, y=138)
            self.quitWindow1 = tk.Button(text="OTP", command=self.submit1, fg="white", bg="#1d2736",
                                         font="MSGothic 15 bold")
            self.quitWindow1.place(x=220, y=190)
            # self.quitWindow = tk.Button(text="FACE", command=self.submit, fg="white", bg="#1d2736",
            #                             font="MSGothic 15 bold")
            # self.quitWindow.place(x=320, y=190)
            self.clearWindow = tk.Button(text="EXIT", command=self.ExitApplication, fg="white", bg="#1d2736",
                                         font="MSGothic 15 bold")
            self.clearWindow.place(x=320, y=190)
            self.root.mainloop()

        # def submit(self):
        #     name = self.txt.get()
        #     global timer
        #     # print(name)
        #     x, y, kname, kencod, kid, lic_key = self.authenticate(name)
        #     if x == True:
        
        #         url_project = base_url + "services/projects.php"
        #         post_data_project = {'useremail': kid, 'requesttype': "face"}
        
        #         response_project = requests.request("POST", url_project, data=post_data_project)
        #         project_result = response_project.text
        #         # print(project_result)
        #         json_data_load = json.loads(project_result)
        #         status = json_data_load['status']
        #         cap_time = int(json_data_load['cap_time'])
        #         # print("type of cap_time", type(cap_time))
        
        #         if (cap_time != 0):
        
        #             #print(cap_time)
        
        #             timer = int(cap_time) * 60
        #             # timer = timer * 60
        #             # print(type(status))
        #         else:
        
        #             timer = 600
        #         # print("timer value===========", timer)
        #         if int(status) == 1:
        #             finalarray = []
        #             finalarray_name = []
        #             finalarray_id = []
        #             project_data = json_data_load['projectdata']
        
        #             for x in range(0, len(project_data)):
        #                 finalarray_name.append(project_data[x]['name'])
        #                 # print(finalarray_name)
        #                 finalarray_id.append(project_data[x]['id'])
        
        #             finalarray = dict(zip(finalarray_name, finalarray_id))
        #             for x in finalarray:
        #                 print(finalarray[x])
        #         else:
        #             messagebox.showwarning("warning", "project not assigned")
        #             #print("project not assigned")
        #             self.root.destroy()
        #             login_dynamic()
        #         self.root.destroy()
        #         project(y, kname, kencod, kid, lic_key, finalarray)
        #     else:
        #         messagebox.showwarning("warning", "enter employee id again")

        def submit1(self):
            emp_id = self.txt.get()
            global timer

            url = base_url + "services/login.php"

            post_data = {'useremail': emp_id, 'requesttype': "otp"}
            # response = requests.post(url, data=post_data)
            headers = {
                'Cookie': 'PHPSESSID=7kjc1385c0q9vv6n54j02voec6'
            }
            files = [

            ]
            response = requests.request("POST", url, data=post_data, files=files)
            #print(response)
            myresult = response.text
            json_data_load = json.loads(myresult)
            #print(json_data_load)

            if json_data_load['status'] == 0:

                error = json_data_load['messagetxt']
                messagebox.showwarning("warning", error)
                #print(error)





            else:
                # print("Employee Id Exist")
                json_data = json_data_load['alluserinfo']
                emp_name = json_data['useruniqueid']
                lic_key = json_data['lickey']
                useremail = json_data['useremail']
                url_project = base_url + "services/projects.php"
                post_data_project = {'useremail': useremail, 'requesttype': "otp"}

                response_project = requests.request("POST", url_project, data=post_data_project)
                project_result = response_project.text
                #print(project_result)
                json_data_load = json.loads(project_result)
                #print(json_data_load)
                status = json_data_load['status']
                #print(status)
                cap_time = int(json_data_load['cap_time'])
                #print(type(cap_time))
                # print("type of cap_time", type(cap_time))
                if (cap_time != 0):

                    # print(cap_time)
                    timer = int(cap_time) * 60
                    # timer = timer * 60
                else:

                    timer = 600
                #print("timer value===========", timer)
                # print(type(status))

                if int(status) == 1:
                    finalarray = []
                    finalarray_name = []
                    finalarray_id = []
                    project_data = json_data_load['projectdata']

                    # write_to_pickle = write_projects_to_pickle(json_data_load, inputValue)

                    for x in range(0, len(project_data)):
                        finalarray_name.append(project_data[x]['name'])
                        #print(finalarray_name)
                        finalarray_id.append(project_data[x]['id'])

                    finalarray = dict(zip(finalarray_name, finalarray_id))
                    for x in finalarray:
                        print(finalarray[x])
                else:
                    messagebox.showwarning("warning", json_data_load['messagetxt'])
                    #print("project not assigned")
                    self.root.destroy()
                    login_dynamic()
                #print(useremail, lic_key)
                string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                OTP = ""
                varlen = len(string)
                for i in range(6):
                    OTP += string[m.floor(r.random() * varlen)]
                print(OTP)
                url = base_url + "sendmail.php"
                post_data = {'to_email': useremail, 'to_name': useremail, 'to_secret_key': OTP, 'page': 'otpverify',
                             'subject': 'OTP Verification'}
                response = requests.request("POST", url, data=post_data, files=files)
                self.root.destroy()
                art(useremail, emp_name, lic_key, OTP, finalarray)

        def ExitApplication(self):
            # self.root.destroy()
            MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                               icon='warning')
            if MsgBox == 'yes':
                self.root.destroy()
            else:
                tk.messagebox.showinfo('Return', 'You will now return to the application screen')

        # def authenticate(self, name):
        #     emp_id = name
        #     known_face_encodings = []
        #     known_face_names = []
        #     known_face_id = []
        #     url = base_url + "services/login.php"
        
        #     post_data = {'useremail': emp_id, 'requesttype': "face"}
        
        #     # response = requests.post(url, data=post_data)
        #     headers = {
        #         'Cookie': 'PHPSESSID=7kjc1385c0q9vv6n54j02voec6'
        #     }
        #     files = [
        
        #     ]
        #     response = requests.request("POST", url, data=post_data, files=files)
        #     #print(response)
        #     myresult = response.text
        #     json_data_load = json.loads(myresult)
        #     #print(json_data_load)
        
        #     if json_data_load['status'] == 0:
        
        #         error = json_data_load['messagetxt']
        #         messagebox.showwarning("warning", error)
        #         # print(error)
        #         return "null", "null", "null", "null", "null", "null"
        
        #     elif json_data_load['status'] == 2:
        #         error = json_data_load['messagetxt']
        #         messagebox.showwarning("warning", error)
        #         # print(error)
        #         key = cv2.waitKey(1)
        #         webcam = cv2.VideoCapture(source)
        #         inputValue = emp_id
        #         while True:
        #             try:
        #                 check, frame = webcam.read()
        #                 cv2.imshow("Capturing", frame)
        #                 key = cv2.waitKey(1)
        #                 if key == ord('s'):  # Press S to save the image
        #                     cv2.imwrite(filename='saved_img.jpg', img=frame)
        #                     webcam.release()
        #                     # img_new = cv2.imread('saved_img.jpg')
        #                     cv2.waitKey(1650)
        #                     cv2.destroyAllWindows()
        #                     #print("Image saved!")
        
        #                     if (inputValue != ""):
        #                         emp_name = json_data_load['useruniqueid']
        #                         lic_key = json_data_load['lickey']
        #                         useremail = emp_id
        #                         new_image = face_recognition.load_image_file("saved_img.jpg")
        #                         new_face_encoding = face_recognition.face_encodings(new_image)
        #                         new = ""
        
        #                         # traverse in the string
        
        #                         for x in new_face_encoding[0]:
        #                             new += str(x) + ","
        #                         str_loop = new
        
        #                         url = base_url + "services/encodings.php?useremail=" + useremail + "&licence_key=" + lic_key + "&user_unique_id=" + emp_name + "&encodings=" + str(
        #                             str_loop[:-1]) + ""
        #                         #print(url)
        #                         return_responce = requests.get(url)
        #                         #print(return_responce)
        #                     break
        #                 elif key == ord('q'):  # Press Q to quit the image
        #                     #print("Turning off camera.")
        #                     webcam.release()
        #                     #print("Camera off.")
        #                     #print("Program ended.")
        #                     cv2.destroyAllWindows()
        #                     break
        
        #             except(KeyboardInterrupt):
        #                 #print("Turning off camera.")  # turning off camera
        #                 webcam.release()
        #                 #print("Camera off.")
        #                 #print("Program ended.")
        #                 cv2.destroyAllWindows()
        #                 break
        #         return "null", "null", "null", "null", "null", "null"
        #         # return True,emp_name,emp_name,new_face_encodings,useremail,lic_key
        
        
        
        #     else:
        #         #print("Employee Id Exist")
        
        #         json_data = json_data_load['alluserinfo']
        #         encodings = json_data['userdata']
        #         emp_name = json_data['useruniqueid']
        #         lic_key = json_data['lickey']
        #         useremail = json_data['useremail']
        #         # print(emp_name)
        
        #         str_loop = []
        
        #         for j in range(0, 128):
        #             data_id = 'C' + str(j)
        #             str_loop.append(float(Decimal(encodings[data_id])))
        
        #         known_face_encodings.append(str_loop)
        #         known_face_names.append(emp_name)
        #         # print(known_face_encodings)
        #         # print(known_face_names)
        
        #         video_capture = cv2.VideoCapture(source)
        
        #         # Grab a single frame of video
        #         ret, frame = video_capture.read()
        
        #         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #         rgb_frame = frame[:, :, ::-1]
        
        #         # Find all the faces and face enqcodings in the frame of video
        #         face_locations = face_recognition.face_locations(rgb_frame)
        #         # print(face_locations)
        #         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        #         if face_locations == []:
        #             #print("face not found")
        #             messagebox.showwarning("warning", "Human Face Not Found")
        #             # easygui.msgbox("Human Face Not Found", title="Warning")
        #             video_capture.release()
        #             cv2.destroyAllWindows()
        #             return "null", "null", "null", "null", "null", "null"
        #         else:
        
        #             # Loop through each face in this frame of video
        #             for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #                 # See if the face is a match for the known face(s)
        #                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        
        #                 name = "Unknown"
        #                 # print(name)
        #                 startX, startY, endX, endY = top, right, bottom, left
        #                 face = frame[startY:endY, startX:endX]
        #                 # If a match was found in known_face_encodings, just use the first one.
        #                 # if True in matches:
        #                 #     first_match_index = matches.index(True)
        #                 #     name = known_face_names[first_match_index]
        
        #                 # Or instead, use the known face with the smallest distance to the new face
        #                 face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        #                 best_match_index = np.argmin(face_distances)
        #                 if matches[best_match_index]:
        #                     name = known_face_names[best_match_index]
        
        #                     # Draw a box around the face
        #                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #                 # cv2.imwrite()
        #                 # print(name)
        #                 # Draw a label with a name below the face
        #                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #                 font = cv2.FONT_HERSHEY_DUPLEX
        #                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 255), 1)
        #                 # cv2.imwrite('% s/% s.png' % (path, count), face)
        #                 # count+=1
        #                 if name == emp_name:
        #                     # filename1 = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        #                     # cv2.imwrite('% s/% s.png' % (path, filename1), frame)
        #                     # img = path +"/"+filename1+".png"
        #                     video_capture.release()
        #                     cv2.destroyAllWindows()
        #                     return True, name, known_face_names, known_face_encodings, useremail, lic_key
        #                 else:
        #                     #print("person not match")
        #                     messagebox.showwarning("warning", "Mismatch with the registered face")
        #                     # easygui.msgbox("Mismatch with the registered face", title="Warning")
        #                     video_capture.release()
        #                     cv2.destroyAllWindows()
        #                     return "null", "null", "null", "null", "null", "null"

    def main():
        user_login()
        # mainloop()

    if __name__ == '__main__':
        main()


def register_dynamic():
    pass
    # print("hi")


def task(y, kname, kencod, kid, lic_key, projectid, finalarray):
    class project:

        def __init__(self, y, kname, kencod, kid, lic_key, projectid, finalarray):
            self.root = tk.Tk()
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.val = StringVar()
            self.y = y
            self.kname = kname
            self.kencod = kencod
            self.kid = kid
            self.projectid = projectid
            self.lic_key = lic_key
            self.finalarray = finalarray
            canvas = tk.Canvas(self.root, height=451, width=571)
            canvas.pack()
            self.values = list(self.finalarray)
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            self.label_msg1 = canvas.create_text((150, 150), text="Task Name", justify=tk.CENTER,
                                                 font="MSGothic 16 bold", fill="white")
            self.txt1 = tk.Spinbox(self.root, values=self.values, textvariable=self.val, width=20, fg="#1d2736",
                                   font=('times', 15, ' bold '))
            self.txt1.place(x=220, y=138)

            self.quitWindow = tk.Button(text="Submit", command=self.submit, fg="white", bg="#1d2736",
                                        font="MSGothic 13 bold")
            self.quitWindow.place(x=230, y=230)
            self.clearWindow = tk.Button(text="Exit", command=self.ExitApplication, fg="white", bg="#1d2736",
                                         font="MSGothic 13 bold")
            self.clearWindow.place(x=330, y=230)
            self.root.mainloop()

        def submit(self):
            # print(self.values)
            # name = self.txt.get()
            task = self.txt1.get()
            # print("task==", task)

            if biometric == 0:
                self.root.destroy()
                sessio_dynamic1(self.y, self.kname, self.kencod, self.kid, self.lic_key, self.projectid, task)
            else:
                self.root.destroy()
                sessio_dynamic2(self.kname, self.kid, self.lic_key, self.projectid, task)

        def ExitApplication(self):
            # self.root.destroy()
            MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                               icon='warning')
            if MsgBox == 'yes':
                self.root.destroy()
            else:
                tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    def main(y, kname, kencod, kid, lic_key, projectid, finalarray):
        project(y, kname, kencod, kid, lic_key, projectid, finalarray)
        # mainloop()

    if __name__ == '__main__':
        main(y, kname, kencod, kid, lic_key, projectid, finalarray)


def project(y, kname, kencod, kid, lic_key, finalarray):
    class project:

        def __init__(self, y, kname, kencod, kid, lic_key, finalarray):
            self.root = tk.Tk()
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.val = StringVar()
            self.y = y
            self.kname = kname
            self.kencod = kencod
            self.kid = kid
            self.lic_key = lic_key
            self.finalarray = finalarray
            canvas = tk.Canvas(self.root, height=451, width=571)
            canvas.pack()
            self.values = list(self.finalarray)
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            self.label_msg1 = canvas.create_text((150, 150), text="Project Name", justify=tk.CENTER,
                                                 font="MSGothic 16 bold", fill="white")
            self.txt1 = tk.Spinbox(self.root, values=self.values, textvariable=self.val, width=20, fg="#1d2736",
                                   font=('times', 15, ' bold '))
            self.txt1.place(x=220, y=138)

            self.quitWindow = tk.Button(text="Submit", command=self.submit, fg="white", bg="#1d2736",
                                        font="MSGothic 13 bold")
            self.quitWindow.place(x=230, y=230)
            self.clearWindow = tk.Button(text="Exit", command=self.ExitApplication, fg="white", bg="#1d2736",
                                         font="MSGothic 13 bold")
            self.clearWindow.place(x=330, y=230)
            self.root.mainloop()

        def submit(self):
            # print(self.values)
            # name = self.txt.get()
            project = self.txt1.get()
            # print(project)

            url_project = base_url + "services/getprojects.php"
            post_data_project = {'projectname': project}
            # print("project data ==", post_data_project)
            response_project = requests.request("POST", url_project, data=post_data_project)
            project_result = response_project.text
            # print(project_result)
            json_data_load = json.loads(project_result)
            # print("json data ==", json_data_load)
            status = json_data_load['status']
            # print(status)
            # print(type(status))
            lst = []
            if int(status) == 1:
                projectid = json_data_load['id']
                # print(projectid)
                # print(self.kid)
                url = base_url + "services/gettask.php"

                if biometric == 0:
                    post_data = {'project_unique_id': projectid, 'lic_key': self.lic_key, 'empid': self.y}
                else:

                    post_data = {'project_unique_id': projectid, 'lic_key': self.lic_key, 'empid': self.kid}
                # response = requests.post(url, data=post_data)
                headers = {
                    'Cookie': 'PHPSESSID=7kjc1385c0q9vv6n54j02voec6'
                }
                files = [

                ]
                response = requests.request("POST", url, data=post_data, files=files)
                # print(response)
                myresult = response.text
                # print(myresult)
                json_data_load = json.loads(myresult)
                # print(json_data_load)
                # print(len(json_data_load))
                # project_data = json_data_load['projectdata']
                finalarray = []
                # print(json_data_load.values("title"))
                for i in range(0, len(json_data_load) - 2):
                    # print(json_data_load[str(i)]['title'])
                    finalarray.append(json_data_load[str(i)]['title'])
            if len(finalarray) == 0:
                finalarray.append("not available")
                self.root.destroy()
                task(self.y, self.kname, self.kencod, self.kid, self.lic_key, projectid, finalarray)
            else:
                self.root.destroy()
                task(self.y, self.kname, self.kencod, self.kid, self.lic_key, projectid, finalarray)

        def ExitApplication(self):
            # self.root.destroy()
            MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                               icon='warning')
            if MsgBox == 'yes':
                self.root.destroy()
            else:
                tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    def main(y, kname, kencod, kid, lic_key, finalarray):
        project(y, kname, kencod, kid, lic_key, finalarray)
        # mainloop()

    if __name__ == '__main__':
        main(y, kname, kencod, kid, lic_key, finalarray)

def review_face(name, kid, lic_key, projectid, task):
    class feedback():
        def __init__(self, name, kid, lic_key, projectid, task):
            self.name = name
            self.kid = kid
            self.lic_key = lic_key
            self.projectid = projectid
            self.task = task
            self.show = 1
            #print("hi review")
            self.root = tk.Tk()
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.val = StringVar()
            canvas = tk.Canvas(self.root, height=451, width=571)
            canvas.pack()
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            # self.label_msg = canvas.create_text((150, 40), text="AIRFACE TimeTracker",justify = tk.CENTER, font="ALGERIAN 18 bold", fill="white")
            self.label_msg1 = canvas.create_text((150, 150), text="Remarks", justify=tk.CENTER,
                                                 font="MSGothic 16 bold", fill="white")
            self.txt = tk.Entry(width=26, fg="#1d2736", font=('times', 13, ' bold '))
            self.txt.place(x=220, y=138, width=250, height=150)
            self.quitWindow1 = tk.Button(text="SUBMIT", command=self.feedback_main, fg="white", bg="#1d2736",
                                         font="MSGothic 15 bold")
            self.quitWindow1.place(x=220, y=300)
            # print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            # self.quitWindow = tk.Button(text="FACE", command=self.submit, fg="white", bg="#1d2736",
            #                             font="MSGothic 15 bold")
            # self.quitWindow.place(x=320, y=190)
            # self.clearWindow = tk.Button(text="SUBMIT", command=self.main, fg="white", bg="#1d2736",
            #                              font="MSGothic 15 bold")
            # self.clearWindow.place(x=320, y=190)
            self.root.mainloop()
            #print("complte------")

        def feedback_main(self):
            # pass
            # print("inside face feedback main")
            task_feedback = self.txt.get()
            #print(task_feedback)
            if task_feedback == "":

                messagebox.showwarning("warning", "you need to fill this field")
                #print("you need to fill this field ")
            else:
                # print("------inside else part of face module--------")

                url = base_url + "services/apitimetrackerinserttimesheet.php"
                # mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="airTimetracker")
                empid = str(self.kid)
                projectname = str(self.projectid)
                task_feedback = str(task_feedback)  # str(self.txt.get()
                db_time_format = "2020-10-15 10:40:32"  # datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                sc_shot = "path"
                #print("time=========", db_time_format)
                file_loc = "2456"
                file_loc1 = "1234"
                #file_loc = self.convertToBinaryData(self.kimg)
                captureddate = datetime.datetime.now().strftime('%Y-%m-%d')
                createddate = datetime.datetime.now().strftime('%Y-%m-%d')
                #print(captureddate)
                #print(createddate)
                lickey = str(self.lic_key)
                user_unique_id = str(self.name)
                duration = 5
                # duration = m.floor(duration)
                # print("*********************************************")
                # print(duration)
                # print(empid, user_unique_id)
                # print(self.task)
                #print("************************************************")
                data = {"useruniqueid": str(empid),
                        "useremail": str(user_unique_id), "datetime": str(db_time_format), "screenshot": str(sc_shot),
                        "projectid": str(projectname),
                        "faceshot": str(""), "duration": str(duration), "createddate": str(createddate),
                        "captureddate": str(captureddate), "requesttype": str("face"), "tasktitle": str(self.task),
                        "emp_feedback": str(task_feedback)}
                #print(data)
                print("------------------------------------------")
                X = requests.post(url, data)
                # # print(X)
                # print("data===========", data)
                # print("----------------------------------------------")
                #print("data=====", data)
                # print("======================done==============")
                # print(data)
                # print("======================done==============")
                # print("done")
                self.root.destroy()

                login_dynamic()

    if __name__ == '__main__':
        feedback(name, kid, lic_key, projectid, task)
        # login_dynamic()


def sessio_dynamic1(name, kname, kencod, kid, lic_key, projectid, task):
    class wfh:

        def __init__(self, name, kname, kencod, kid, lic_key, projectid, task):
            self.root = tk.Tk()
            self.show = timer  # seconds
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.canvas = tk.Canvas(self.root, height=451, width=571)
            self.canvas.pack()
            # print("----------------timer part---------------------------")
            self._start = 0.0
            self._elapsedtime = 0.0
            self._running = 0
            self.count = 0000
            self.pcount = 1000
            self.flag = 0
            self.task = task
            self.kname = kname
            self.kencod = kencod
            self.lic_key = lic_key
            self.projectid = projectid
            self.name = name
            self.kid = kid
            self.kimg = " "
            self.kimg1 = " "
            self.timestr = StringVar()
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = self.canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            # self.label_msg = self.canvas.create_text((150, 40), text="SESSION STARTED",justify = tk.CENTER, font="ALGERIAN 18 bold", fill="white")
            self.l = tk.Label(self.root, textvariable=self.timestr, fg="white", bg="#1d2736", font="MSGothic 35 bold")
            self._setTime(self._elapsedtime)
            self.l.place(x=130, y=100)
            self.screen = tk.Label(self.root, text="LATEST SCREENSHOT", fg="white", bg="#1d2736",
                                   font="MSGothic 14 bold")
            self.screen.place(x=150, y=230)
            self.start = tk.Button(text="Start", command=self.start, fg="white", bg="#1d2736", font="MSGothic 12 bold")
            self.start.place(x=140, y=160)
            self.pause = tk.Button(text="Pause", command=self.pause, fg="white", bg="#1d2736", font="MSGothic 12 bold")
            self.pause.place(x=240, y=160)
            self.stop = tk.Button(text="End", command=self.stop, fg="white", bg="#1d2736", font="MSGothic 12 bold")
            self.stop.place(x=340, y=160)
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            # self.root.after(10,self.verify)
            self.root.mainloop()

        def on_closing(self):
            messagebox.showwarning("warning", "CLick end button")

        def open_img(self, im_path):
            # Select the Imagename from a folder 
            x = im_path

            # opens the image 
            img = PIL.Image.open(x)

            # resize the image and apply a high-quality down sampling filter 
            img = img.resize((100, 100), PIL.Image.ANTIALIAS)

            # PhotoImage class is used to add image to widgets, icons etc 
            img = PIL.ImageTk.PhotoImage(img)

            # create a label 
            self.panel = tk.Label(self.root, image=img)

            # set the image as img 
            self.panel.image = img
            self.panel.place(x=195, y=270)

        def verify(self):

            self.root.after(self.show * 1000, self.loop)

        def loop(self):

            # print("starting")
            time, date = self.takeScreenshot()
            # print("screenshot done")
            x = self.authon(time)
            if x == "AUTHENTICATE":
                # print("authentication done")
                # current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # print(self.name + " " + x + " = " + current_time)
                status = self.insert(time, date)
                # print(status)
                if status == True:

                    self.verify()


                else:
                    if self._running:
                        messagebox.showwarning("warning", "Try again")
                        self.l.after_cancel(self._timer)
                        self._elapsedtime = time.time() - self._start
                        # print("elapsed time==", self._elapsedtime)
                        self._setTime(self._elapsedtime)
                        self._running = 0
                        self.flag = 1

                return

        def pause(self):
            if self._running:
                """ pause the stopwatch, ignore if stopped. """
                # print("taking screenshot")
                time11, date = self.takeScreenshot()
                # print("screen captured................")
                # print(date)
                # print("authentication started")
                x = self.authon(time11)
                # print(x)
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # print(self.name + " " + x + " = " + current_time)
                status = self.insert(time11, date)

                if status == True:

                    self.l.after_cancel(self._timer)
                    self._elapsedtime = time.time() - self._start
                    # print("elapsed time ======", self._elapsedtime)
                    self._setTime(self._elapsedtime)
                    self._running = 0
                    self.flag = 1



                else:
                    messagebox.showwarning("warning", "Authenticate to pause")

                    self._start = time.time() - self._elapsedtime
                    self._update()
                    self._running = 1
                    self.flag = 0
                    # messagebox.showwarning("warning","Authenticate to pause")

        # def start(self):
        #     # print("----------face section-------------")
        #     """ Start the stopwatch, ignore if running. """
        #     if not self._running:
        #         check = 0
        #         # print("-------------------Timer Part (Start Button)------------------------")
        #         messagebox.showwarning("warning", "Authenticate to start")
        #         # print("camera starting up")
        #         # time11,date = self.takeScreenshot()
        #         x = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        #         # print("x time value==", x)
        #         y = datetime.datetime.now().strftime('%Y-%m-%d')
        #         # print("y time value==", y)
        #         myScreenshot = pyautogui.screenshot()  # for taking screenshot
        #         # print(type(myScreenshot))

        #         myScreenshot_arr = np.asarray(myScreenshot)  # convert PIL to numpy
        #         myScreenshot_height, myScreenshot_width = myScreenshot_arr.shape[:2]
        #         # print(myScreenshot_width)
        #         # print(myScreenshot_height)
        #         # print(type(myScreenshot_width))
        #         # print(type(myScreenshot_height))
        #         # myScreenshot_height1 = asarray(myScreenshot_height)
        #         # myScreenshot_width1 = asarray(myScreenshot_width)       #PIL to numpy
        #         # print("-------------------------------------------------------------")
        #         # print(type(myScreenshot))
        #         re_wid = myScreenshot_width // 2  # numpy  evaluation
        #         re_hei = myScreenshot_height // 2
        #         # print(re_wid, re_hei)
        #         # print("-------------------------------------------------------------")
        #         # re_wid_num = myScreenshot_width1//2
        #         # re_hei_num = myScreenshot_height1//2  #numpy convert
        #         # print(re_wid_num, re_hei_num)

        #         # resize_screenshot = myScreenshot.resize((re_wid, re_hei), PIL.Image.ANTIALIAS) #resizing screenshot
        #         resize_screenshot = cv2.resize(myScreenshot_arr, (re_wid, re_hei))
        #         # resize_screenshot_arr = np.asarray(resize_screenshot)
        #         myScreenshot_res_height, myScreenshot_res_width = resize_screenshot.shape[:2]
        #         # print(myScreenshot_res_width)
        #         # print(myScreenshot_res_height)
        #         # print("resize_screenshot", resize_screenshot)
        #         # print("resize_screenshot_arr", resize_screenshot_arr)

        #         # print(type(resize_screenshot))
        #         # numpy_convert_img = asarray(resize_screenshot) #pillow to numpy convert
        #         # print(re_wid, re_hei, resize_screenshot.shape)
        #         sliced_image = resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75),
        #                        0:re_wid]  # slicing image for blurring
        #         # print(sliced_image.shape)
        #         # cv2.imshow(sliced_image)
        #         # print("sliced_image", sliced_image)
        #         blur_img = cv2.GaussianBlur(sliced_image, (7, 7), 7)
        #         # print(type(sliced_image))
        #         # print(sliced_image.shape)
        #         resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75), 0:re_wid] = blur_img
        #         # print("Screenshot", sliced_image)
        #         # cv2.imshow("numpy image", sliced_image)
        #         numpy_to_pil = Image.fromarray(resize_screenshot)  # from numpy to PIL convert
        #         # print(numpy_to_pil)

        #         numpy_to_pil.save('captures/' + x + '_screenshot.png')
        #         filename = 'captures/' + x + '_screenshot.png'

        #         # cv2.imwrite(filename, im)
        #         self.open_img(filename)
        #         self.kimg = filename
        #         # print("inside start sceen name =", filename)
        #         time11, date = x, y
        #         video_capture = cv2.VideoCapture(source)
        #         known_face_encodings = self.kencod
        #         known_face_names = self.kname
        #         path = "detected"

        #         # Grab a single frame of video
        #         ret, frame = video_capture.read()

        #         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #         rgb_frame = frame[:, :, ::-1]

        #         # Find all the faces and face enqcodings in the frame of video
        #         face_locations = face_recognition.face_locations(rgb_frame)
        #         # print(face_locations)
        #         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        #         # Loop through each face in this frame of video
        #         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #             # See if the face is a match for the known face(s)
        #             matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)

        #             name = "Unknown"
        #             startX, startY, endX, endY = top, right, bottom, left
        #             face = frame[startY:endY, startX:endX]
        #             # If a match was found in known_face_encodings, just use the first one.
        #             # if True in matches:
        #             #     first_match_index = matches.index(True)
        #             #     name = known_face_names[first_match_index]

        #             # Or instead, use the known face with the smallest distance to the new face
        #             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        #             best_match_index = np.argmin(face_distances)
        #             if matches[best_match_index]:
        #                 name = known_face_names[best_match_index]

        #             # Draw a box around the face
        #             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #             # cv2.imwrite()

        #             # Draw a label with a name below the face
        #             # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #             font = cv2.FONT_HERSHEY_DUPLEX
        #             # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0,0,255), 1)
        #             # cv2.imwrite('% s/% s.png' % (path, count), face)
        #             # count+=1

        #             if name == self.name:
        #                 check = 1
        #                 # print("inside start authenticated")
        #                 face = frame[top:bottom, left:right]
        #                 cv2.imwrite('% s/% s.png' % (path, time11), face)
        #                 faceimg = path + "/" + time11 + ".png"
        #                 self.kimg1 = faceimg
        #                 #print("inside start face = ")
        #                 self.pcount += 1
        #                 # print("inserting")
        #                 status = self.insert(time11, date)
        #                 # print(status)
        #                 video_capture.release()
        #                 cv2.destroyAllWindows()

        #         if check == 1 and status == True:
        #             # print("going to start timer")
        #             self._start = time.time() - self._elapsedtime
        #             self._update()
        #             self._running = 1
        #             self.flag = 0
        #             self.verify()

        #         else:
        #             os.remove(self.kimg)
        #             messagebox.showwarning("warning", "NOT VALIDATED")
                

        # def stop(self):
        #     """ stop the stopwatch. """
        #     # print("--------------stop section start-------------")
        #     if self.connect() and self._running:
        #         time11, date = self.takeScreenshot()
        #         x = self.authon(time11)
        #         # print(x)
        #         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #         # print(self.name+" "+x+ " = "+current_time)
        #         status = self.insert(time11, date)
        #         if status == True:

        #             self._start = time.time()
        #             # print("Total productive hour is ", self._elapsedtime)
        #             self._elapsedtime = 0.0
        #             self._setTime(self._elapsedtime)
        #             self.flag = 1
        #             shutil.rmtree('captures')
        #             shutil.rmtree('detected')
        #             shutil.rmtree('backup')
        #             shutil.rmtree('backupimg')
        #             os.makedirs('captures')
        #             os.makedirs('detected')
        #             os.makedirs('backup')
        #             os.makedirs('backupimg')
        #             self.root.destroy()
        #             review_face(name, kid, lic_key, projectid, task)
        #             # login_dynamic()


        #         else:
        #             messagebox.showwarning("warning", "Try Again")
        #     else:
        #         messagebox.showwarning("warning", "Internet required to end timer or timer is paused")
        #         # print("need internet")

        def _update(self):
            """ Update the label with elapsed time. """
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._timer = self.l.after(50, self._update)

        def _setTime(self, elap):
            """ Set the time string to Minutes:Seconds:Hundreths """
            seconds = elap
            hours = seconds // (60 * 60)
            seconds %= (60 * 60)
            minutes = seconds // 60
            seconds %= 60

            hours = int(elap / 3600)
            minutes = int(elap - hours * 60.0)
            seconds = int(elap - minutes * 60.0)
            hseconds = int((elap - minutes * 60.0 - seconds) * 100)
            hseconds = abs(hseconds)
            # self.timestr.set('%02d:%02d:%02d:%02d' % (hours,minutes, seconds, hseconds))
            seconds = elap
            hours = seconds // (60 * 60)
            seconds %= (60 * 60)
            minutes = seconds // 60
            seconds %= 60

            self.timestr.set('%02d:%02d:%02d:%02d' % (hours, minutes, seconds, hseconds))

        def connect(self, host='http://google.com'):
            try:
                urllib.request.urlopen(host)  # Python 3.x
                return True
            except:
                return False

        def convertToBinaryData(self, filename):
            # Convert digital data to binary format
            # with open(filename, 'rb') as file:
            #     binaryData = file.read()
            # return binaryData
            with open(filename, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode('utf-8')

        def takeScreenshot(self):
            if self.flag == 0:

                # x = str(self.count)

                x = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                y = datetime.datetime.now().strftime('%Y-%m-%d')
                myScreenshot = pyautogui.screenshot()
                myScreenshot_arr = np.asarray(myScreenshot)
                myScreenshot_height, myScreenshot_width = myScreenshot_arr.shape[:2]
                # print(myScreenshot_width)
                # print(myScreenshot_height)
                # print(type(myScreenshot))
                # print("-------------------------------------------------------------")
                # print(type(myScreenshot))
                re_wid = myScreenshot_width // 2  # numpy  evaluation
                re_hei = myScreenshot_height // 2
                # print(re_wid, re_hei)
                # print("-------------------------------------------------------------")
                # re_wid_num = myScreenshot_width1//2
                # re_hei_num = myScreenshot_height1//2  #numpy convert
                # print(re_wid_num, re_hei_num)

                # resize_screenshot = myScreenshot.resize((re_wid, re_hei), PIL.Image.ANTIALIAS) #resizing screenshot
                resize_screenshot = cv2.resize(myScreenshot_arr, (re_wid, re_hei))
                # resize_screenshot_arr = np.asarray(resize_screenshot)
                myScreenshot_res_height, myScreenshot_res_width = resize_screenshot.shape[:2]
                # print(myScreenshot_res_width)
                # print(myScreenshot_res_height)
                # print("resize_screenshot", resize_screenshot)
                # print("resize_screenshot_arr", resize_screenshot_arr)

                # print(type(resize_screenshot))
                # numpy_convert_img = asarray(resize_screenshot) #pillow to numpy convert
                # print(re_wid, re_hei, resize_screenshot.shape)
                sliced_image = resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75),
                               0:re_wid]  # slicing image for blurring
                # print(sliced_image.shape)
                # cv2.imshow(sliced_image)
                # print("sliced_image", sliced_image)
                blur_img = cv2.GaussianBlur(sliced_image, (7, 7), 7)
                # print(type(sliced_image))
                # print(sliced_image.shape)
                resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75), 0:re_wid] = blur_img
                # print("Screenshot", sliced_image)
                # cv2.imshow("numpy image", sliced_image)
                numpy_to_pil = Image.fromarray(resize_screenshot)  # from numpy to PIL convert
                # print(numpy_to_pil)

                numpy_to_pil.save('captures/' + x + '_screenshot.png')
                # myScreenshot.save('captures/'+x+'_screenshot.png')
                filename = 'captures/' + x + '_screenshot.png'
                self.open_img(filename)
                self.kimg = filename

                return x, y
            else:
                return "NULL", "NULL"

        # def authon(self, time1):
        #     if self.flag == 0:
        #         x = time1
        #         validstatus = 0
        #         if self._running:
        #             self.l.after_cancel(self._timer)
        #             self._elapsedtime = time.time() - self._start
        #             self._setTime(self._elapsedtime)
        #             self._running = 0
        #             self.flag = 1
        #         # print("camera starting up")
        #         video_capture = cv2.VideoCapture(source)
        #         known_face_encodings = self.kencod
        #         known_face_names = self.kname
        #         path = "detected"

        #         # Grab a single frame of video
        #         ret, frame = video_capture.read()

        #         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #         rgb_frame = frame[:, :, ::-1]

        #         # Find all the faces and face enqcodings in the frame of video
        #         face_locations = face_recognition.face_locations(rgb_frame)
        #         # print(face_locations)
        #         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        #         # Loop through each face in this frame of video
        #         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #             # See if the face is a match for the known face(s)
        #             matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)

        #             name = "Unknown"
        #             startX, startY, endX, endY = top, right, bottom, left
        #             face = frame[startY:endY, startX:endX]
        #             # If a match was found in known_face_encodings, just use the first one.
        #             # if True in matches:
        #             #     first_match_index = matches.index(True)
        #             #     name = known_face_names[first_match_index]

        #             # Or instead, use the known face with the smallest distance to the new face
        #             face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        #             best_match_index = np.argmin(face_distances)
        #             if matches[best_match_index]:
        #                 name = known_face_names[best_match_index]

        #             # Draw a box around the face
        #             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #             # cv2.imwrite()

        #             # Draw a label with a name below the face
        #             # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        #             font = cv2.FONT_HERSHEY_DUPLEX
        #             # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0,0,255), 1)
        #             # cv2.imwrite('% s/% s.png' % (path, count), face)
        #             # count+=1

        #             if name == self.name:
        #                 face = frame[top:bottom, left:right]
        #                 cv2.imwrite('% s/% s.png' % (path, x), face)
        #                 faceimg = path + "/" + x + ".png"
        #                 self.kimg1 = faceimg
        #                 self.pcount += 1
        #                 validstatus = 1
        #                 if not self._running:
        #                     self._start = time.time() - self._elapsedtime
        #                     self._update()
        #                     self._running = 1
        #                     self.flag = 0
        #                 video_capture.release()
        #                 cv2.destroyAllWindows()
        #                 return "AUTHENTICATE"
        #             elif face_locations == []:
        #                 video_capture.release()
        #                 cv2.destroyAllWindows()
        #                 # print("camera close")
        #                 os.remove(self.kimg)
        #                 messagebox.showwarning("warning", "Verification unsucessfull")
        #                 return "Verification unsucessfull"
        #             else:
        #                 os.remove(self.kimg)
        #                 # print("NULL")
        #                 return "NULL"
        #         if validstatus == 0:
        #             os.remove(self.kimg)
        #             messagebox.showwarning("warning", "Verification unsucessfull")
        #             return "Verification unsucessfull"

        #     else:

        #         return "validation off due to break"

        # def insert(self, time, date):

        #     x = time
        #     # print(time)

        #     if self.connect():

        #         # print("hi")
        #         url = base_url + "services/apitimetrackerinserttimesheet.php"
        #         # print(url)

        #         # mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="airTimetracker")
        #         empid = str(self.kid)
        #         projectname = str(self.projectid)
        #         task_feedback = "N.A."
        #         # db_time_format = "2020-07-10 10:40:32"
        #         # print(time)
        #         newdbtime = time.split("-", 1)
        #         # print(newdbtime)
        #         newdbtime = newdbtime[1]
        #         # print("next",newdbtime)
        #         newdbtime = newdbtime.replace("_", ":")
        #         newdbdate = time.split("-", 1)
        #         newdbdate = newdbdate[0]
        #         newdbdate = newdbdate.replace("_", "-")
        #         time = newdbdate + " " + newdbtime
        #         db_time_format = time
        #         duration = int(self.show) / 60
        #         duration = int(duration)
        #         # duration = 1
        #         # print("hi",db_time_format)

        #         file_loc = self.convertToBinaryData(self.kimg)
        #         file_loc1 = self.convertToBinaryData(self.kimg1)
        #         captureddate = date
        #         createddate = date
        #         lickey = str(self.lic_key)
        #         user_unique_id = self.kname
        #         # print(self.kname)
        #         # print(user_unique_id)
        #         data = {"useruniqueid": str(user_unique_id),
        #                 "useremail": str(empid), "datetime": str(db_time_format), "screenshot": str(file_loc),
        #                 "projectid": str(projectname),
        #                 "faceshot": str(file_loc1), "duration": str(duration), "createddate": str(date),
        #                 "captureddate": str(date), "requesttype": str("face"), "tasktitle": str(self.task), 
        #                 "emp_feedback": str(task_feedback)}
        #         X = requests.post(url, data)
        #         # print(data)
        #         # print("======================done==============")
        #         # print(X)
        #         # print("======================done==============")
        #         # print("done")

        #         os.remove(self.kimg)
        #         os.remove(self.kimg1)
        #         # path of the directory
        #         path = "backup/"
        #         path1 = "backupimg/"

        #         # Getting the list of directories
        #         dir = os.listdir(path)

        #         # Checking if the list is empty or not
        #         if len(dir) == 0:
        #             # print("No images pending to be updated")
        #             checkdir = os.listdir("captures")
        #             if len(checkdir) == 0:
        #                 return True
        #             else:
        #                 return False
        #         else:
        #             start_path = 'backup'  # current directory
        #             for path, dirs, files in os.walk(start_path):
        #                 for filename in files:
        #                     url = base_url + "services/apitimetrackerinserttimesheet.php"
        #                     empid = str(self.kid)
        #                     # print("probb",self.kimg)
        #                     projectname = str(self.projectid)
        #                     task_feedback = "N.A."

        #                     # print("filename=", filename)
        #                     name = "backup/" + filename
        #                     time1 = filename.strip("_screenshot.png")
        #                     time = time1
        #                     newdbtime = time.split("-", 1)
        #                     newdbtime = newdbtime[1]
        #                     newdbtime = newdbtime.replace("_", ":")
        #                     newdbdate = time.split("-", 1)
        #                     newdbdate = newdbdate[0]
        #                     newdbdate = newdbdate.replace("_", "-")
        #                     time = newdbdate + " " + newdbtime
        #                     db_time_format = time
        #                     # print("time=", db_time_format)
        #                     # db_time_format = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        #                     file_loc = self.convertToBinaryData(name)
        #                     filename1 = time1 + ".png"
        #                     file_loc1 = self.convertToBinaryData("backupimg/" + filename1)
        #                     captureddate = date
        #                     createddate = date
        #                     lickey = str(self.lic_key)
        #                     user_unique_id = str(self.kname)
        #                     data = {"useruniqueid": str(user_unique_id),
        #                             "useremail": str(empid), "datetime": str(db_time_format),
        #                             "screenshot": str(file_loc),
        #                             "projectid": str(projectname),
        #                             "faceshot": str(file_loc1), "duration": str(duration), "createddate": str(date),
        #                             "captureddate": str(date), "requesttype": str("face"), "emp_feedback": str(task_feedback)}
        #                     X = requests.post(url, data)
        #                     # print(X)

        #                     os.remove("backup/" + filename)
        #                     os.remove("backupimg/" + filename1)
        #             checkdir = os.listdir("captures")
        #             checkdir1 = os.listdir("backup")
        #             if len(checkdir) == 0 and len(checkdir1) == 0:
        #                 return True
        #             else:
        #                 return False




        #     else:
        #         # print("else part")
        #         # Source path
        #         # print(self.kimg)
        #         source = self.kimg
        #         source1 = self.kimg1

        #         source2 = source.strip('captures/')
        #         source3 = source1.strip('detected/')
        #         # Destination path
        #         destination = "backup/" + source2
        #         destination1 = "backupimg/" + source3

        #         shutil.move(source, destination)
        #         shutil.move(source1, destination1)

        #         # Move the content of
        #         # source to destination
        #         # dest = shutil.move(source, destination)
        #         # print("internet not connected")
        #         checkdir = os.listdir("captures")
        #         if len(checkdir) == 0:
        #             return True
        #         else:
        #             return False

    def main(name, kname, kencod, kid, lic_key, projectid, task):

        wfh(name, kname, kencod, kid, lic_key, projectid, task).loop()

    if __name__ == '__main__':
        main(name, kname, kencod, kid, lic_key, projectid, task)


def art(name, kid, lic_key, OTP, finalarray):
    class wfh:

        def __init__(self, name, kid, lic_key, OTP, finalarray):
            self.lic_key = lic_key
            self.name = name
            self.kid = kid
            self.OTP = OTP
            self.finalarray = finalarray
            self.root = tk.Tk()
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.val = StringVar()
            canvas = tk.Canvas(self.root, height=451, width=571)
            canvas.pack()
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            # self.label_msg = canvas.create_text((150, 40), text="AIRFACE TimeTracker",justify = tk.CENTER, font="ALGERIAN 18 bold", fill="white")
            self.label_msg1 = canvas.create_text((150, 150), text="ENTER OTP", justify=tk.CENTER,
                                                 font="MSGothic 16 bold", fill="white")
            self.txt = tk.Entry(width=26, fg="#1d2736", font=('times', 15, ' bold '))
            self.txt.place(x=220, y=138)
            self.quitWindow1 = tk.Button(text="EXIT", command=self.ExitApplication, fg="white", bg="#1d2736",
                                         font="MSGothic 13 bold")
            self.quitWindow1.place(x=390, y=190)

            self.clearWindow = tk.Button(text="SUBMIT", command=self.submit, fg="white", bg="#1d2736",
                                         font="MSGothic 13 bold")
            self.clearWindow.place(x=240, y=190)
            self.root.mainloop()

        def submit(self):
            otp = self.txt.get()
            if otp == self.OTP:
                global biometric
                biometric = 1
                y = self.name
                self.kencod = "abc"
                self.root.destroy()
                # sessio_dynamic2(self.name,self.kid,self.lic_key)
                project(y, self.name, self.kencod, self.kid, self.lic_key, self.finalarray)
            else:
                messagebox.showwarning("ERROR", "Wrong OTP")
                # print("Wrong OTP")

        def ExitApplication(self):
            # self.root.destroy()
            MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                               icon='warning')
            if MsgBox == 'yes':
                self.root.destroy()
            else:
                tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    def main(name, kid, lic_key, OTP, finalarray):
        wfh(name, kid, lic_key, OTP, finalarray)

    if __name__ == '__main__':
        main(name, kid, lic_key, OTP, finalarray)


def review(name, kid, lic_key, projectid, task):
    class feedback():
        def __init__(self, name, kid, lic_key, projectid, task):
            self.name = name
            self.kid = kid
            self.lic_key = lic_key
            self.projectid = projectid
            self.task = task
            self.show = 1
            #print("hi review")
            self.root = tk.Tk()
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.val = StringVar()
            canvas = tk.Canvas(self.root, height=451, width=571)
            canvas.pack()
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            # self.label_msg = canvas.create_text((150, 40), text="AIRFACE TimeTracker",justify = tk.CENTER, font="ALGERIAN 18 bold", fill="white")
            self.label_msg1 = canvas.create_text((150, 150), text="Remarks", justify=tk.CENTER,
                                                 font="MSGothic 16 bold", fill="white")
            self.txt = tk.Entry(width=26, fg="#1d2736", font=('times', 13, ' bold '))
            self.txt.place(x=220, y=138, width=250, height=150)
            self.quitWindow1 = tk.Button(text="SUBMIT", command=self.feedback_main, fg="white", bg="#1d2736",
                                         font="MSGothic 15 bold")
            self.quitWindow1.place(x=220, y=300)
            # print("=================================")
            # self.quitWindow = tk.Button(text="FACE", command=self.submit, fg="white", bg="#1d2736",
            #                             font="MSGothic 15 bold")
            # self.quitWindow.place(x=320, y=190)
            # self.clearWindow = tk.Button(text="SUBMIT", command=self.main, fg="white", bg="#1d2736",
            #                              font="MSGothic 15 bold")
            # self.clearWindow.place(x=320, y=190)
            self.root.mainloop()
            #print("complte------")

        def feedback_main(self):
            # pass

            task_feedback = self.txt.get()
            #print(task_feedback)
            if task_feedback == "":

                messagebox.showwarning("warning", "you need to fill this field")
                #print("you need to fill this field ")
            else:
                #print("ok")
                url = base_url + "services/apitimetrackerinserttimesheet.php"
                # mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="airTimetracker")
                empid = str(self.kid)
                projectname = str(self.projectid)
                task_feedback = str(task_feedback)  # str(self.txt.get()
                db_time_format = "2020-10-15 10:40:32"  # datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                sc_shot = "path"
                #print("time=========", db_time_format)
                file_loc = "2456"
                file_loc1 = "1234"
                #file_loc = self.convertToBinaryData(self.kimg)
                captureddate = datetime.datetime.now().strftime('%Y-%m-%d')
                createddate = datetime.datetime.now().strftime('%Y-%m-%d')
                #print(captureddate)
                #print(createddate)
                lickey = str(self.lic_key)
                user_unique_id = str(self.name)
                duration = 5
                # duration = m.floor(duration)
                # print("*********************************************")
                # print(duration)
                # print(empid, user_unique_id)
                # print(self.task)
                #print("************************************************")
                data = {"useruniqueid": str(empid),
                        "useremail": str(user_unique_id), "datetime": str(db_time_format), "screenshot": str(sc_shot),
                        "projectid": str(projectname),
                        "faceshot": str(""), "duration": str(duration), "createddate": str(createddate),
                        "captureddate": str(captureddate), "requesttype": str("otp"), "tasktitle": str(self.task),
                        "emp_feedback": str(task_feedback)}
                # print(data)
                X = requests.post(url, data)
                # print("data for otp====", data)
                # print("data=====", data)
                # print("======================done==============")
                # print(data)
                # print("======================done==============")
                # print("done")
                self.root.destroy()

                login_dynamic()

    if __name__ == '__main__':
        feedback(name, kid, lic_key, projectid, task)
        # login_dynamic()


def sessio_dynamic2(name, kid, lic_key, projectid, task):
    class wfh:

        def __init__(self, name, kid, lic_key, projectid, task):
            self.root = tk.Tk()
            self.show = timer  # seconds
            self.root.title("Timetracker")
            self.root.resizable(0, 0)
            self.canvas = tk.Canvas(self.root, height=451, width=571)
            self.canvas.pack()
            self._start = 0.0
            self._elapsedtime = 0.0
            self._running = 0
            self.count = 0000
            self.pcount = 1000
            self.flag = 0
            self.projectid = projectid
            self.lic_key = lic_key
            self.name = name
            self.kid = kid
            self.task = task
            # self.scr_cap = scr_cap
            self.kimg = " "
            self.kimg1 = " "
            self.timestr = StringVar()
            self.bg_img = tk.PhotoImage(file="deer_decode.gif")
            self.bg_label = self.canvas.create_image((0, 0), image=self.bg_img, anchor=tk.N + tk.W)
            # self.label_msg = self.canvas.create_text((150, 40), text="SESSION STARTED",justify = tk.CENTER, font="ALGERIAN 18 bold", fill="white")
            self.l = tk.Label(self.root, textvariable=self.timestr, fg="white", bg="#1d2736", font="MSGothic 35 bold")
            self._setTime(self._elapsedtime)
            self.l.place(x=130, y=100)
            # self.screen = tk.Label(self.root, text="LATEST SCREENSHOT", fg="white", bg="#1d2736",
            #                        font="MSGothic 14 bold")
            # self.screen.place(x=150, y=230)
            self.start = tk.Button(text="Start", command=self.start, fg="white", bg="#1d2736", font="MSGothic 12 bold")
            self.start.place(x=140, y=160)
            self.pause = tk.Button(text="Pause", command=self.pause, fg="white", bg="#1d2736", font="MSGothic 12 bold")
            self.pause.place(x=240, y=160)
            self.stop = tk.Button(text="End", command=self.stop, fg="white", bg="#1d2736", font="MSGothic 12 bold")
            self.stop.place(x=340, y=160)
            # self.root.after(10,self.verify)
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()

        def on_closing(self):
            messagebox.showwarning("warning", "CLick end button")

        def open_img(self, im_path):
            # Select the Imagename from a folder 
            x = im_path

            # opens the image 
            img = PIL.Image.open(x)

            # resize the image and apply a high-quality down sampling filter 
            img = img.resize((150, 150), PIL.Image.ANTIALIAS)

            # PhotoImage class is used to add image to widgets, icons etc 
            img = PIL.ImageTk.PhotoImage(img)

            # create a label 
            self.panel = tk.Label(self.root, image=img)

            # set the image as img 
            # self.panel.image = img
            # self.panel.place(x=195, y=270)

        def verify(self):
            self.root.after(self.show * 1000, self.loop)

        def loop(self):
            # print("hi")
            time, date, status_screen = self.takeScreenshot()
            # x=self.authon(time)
            if status_screen == "success":
                # print("screen donee")
                # current_time = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                # print(self.name+" "+x+ " = "+current_time)
                status = self.insert(time, date)
                # print(status)
                if status == True:
                    self.verify()
                else:
                    if self._running:
                        messagebox.showwarning("warning", "Try again")
                        self.l.after_cancel(self._timer)
                        self._elapsedtime = time.time() - self._start
                        self._setTime(self._elapsedtime)
                        self._running = 0
                        self.flag = 1

                return

        def pause(self):
            """ pause the stopwatch, ignore if stopped. """
            if self._running:
                time11, date, status_screen = self.takeScreenshot()
                if status_screen == "success":
                    status = self.insert(time11, date)
                    # print("status pause section=")
                    if status == True:

                        self.l.after_cancel(self._timer)
                        self._elapsedtime = time.time() - self._start
                        self._setTime(self._elapsedtime)
                        self._running = 0
                        self.flag = 1
                    else:
                        self._start = time.time() - self._elapsedtime
                        self._update()
                        self._running = 1
                        self.flag = 0
                        os.remove(self.kimg)

        def start(self):
            #print("------------otp section start here------------")
            """ Start the stopwatch, ignore if running. """
            if not self._running:
                x = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                y = datetime.datetime.now().strftime('%Y-%m-%d')
                myScreenshot = pyautogui.screenshot()
                myScreenshot_arr = np.asarray(myScreenshot)
                myScreenshot_height, myScreenshot_width = myScreenshot_arr.shape[:2]
                # print(myScreenshot_width)
                # print(myScreenshot_height)
                # print(type(myScreenshot))
                # print("-------------------------------------------------------------")
                # print(type(myScreenshot))
                re_wid = myScreenshot_width // 2  # numpy  evaluation
                re_hei = myScreenshot_height // 2
                # print(re_wid, re_hei)
                # print("-------------------------------------------------------------")
                # re_wid_num = myScreenshot_width1//2
                # re_hei_num = myScreenshot_height1//2  #numpy convert
                # print(re_wid_num, re_hei_num)

                # resize_screenshot = myScreenshot.resize((re_wid, re_hei), PIL.Image.ANTIALIAS) #resizing screenshot
                resize_screenshot = cv2.resize(myScreenshot_arr, (re_wid, re_hei))
                # resize_screenshot_arr = np.asarray(resize_screenshot)
                myScreenshot_res_height, myScreenshot_res_width = resize_screenshot.shape[:2]
                # print(myScreenshot_res_width)
                # print(myScreenshot_res_height)
                # print("resize_screenshot", resize_screenshot)
                # print("resize_screenshot_arr", resize_screenshot_arr)

                # print(type(resize_screenshot))
                # numpy_convert_img = asarray(resize_screenshot) #pillow to numpy convert
                # print(re_wid, re_hei, resize_screenshot.shape)
                sliced_image = resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75),
                               0:re_wid]  # slicing image for blurring
                # print(sliced_image.shape)
                # cv2.imshow(sliced_image)
                # print("sliced_image", sliced_image)
                blur_img = cv2.GaussianBlur(sliced_image, (7, 7), 7)
                # print(type(sliced_image))
                # print(sliced_image.shape)
                resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75), 0:re_wid] = blur_img
                # print("Screenshot", sliced_image)
                # cv2.imshow("numpy image", sliced_image)
                numpy_to_pil = Image.fromarray(resize_screenshot)  # from numpy to PIL convert
                # print(numpy_to_pil)
                numpy_to_pil.save('captures/' + x + '_screenshot.png')
                # print("save to captures")
                # myScreenshot.save('captures/'+x+'_screenshot.png')
                filename = 'captures/' + x + '_screenshot.png'
                # print("filename===", filename)
                self.open_img(filename)
                self.kimg = filename
                status = self.insert(x, y)
                # print("status inside start function=", status)
                if status == True:
                    self._start = time.time() - self._elapsedtime
                    self._update()
                    self._running = 1
                    self.flag = 0
                    self.loop()
                else:
                    self.l.after_cancel(self._timer)
                    self._elapsedtime = time.time() - self._start
                    self._setTime(self._elapsedtime)
                    self._running = 0
                    self.flag = 1
                    os.remove(self.kimg)

        def stop(self):
            #print("-------------stop section start here---------------")
            """ stop the stopwatch. """
            if self.connect() and self._running:
                time11, date, status_screen = self.takeScreenshot()
                if status_screen == "success":
                    status = self.insert(time11, date)
                    if status == True:
                        self._start = time.time()
                        # print("Total productive hour is ", self._elapsedtime)
                        self._elapsedtime = 0.0
                        self._setTime(self._elapsedtime)
                        self.flag = 1
                        shutil.rmtree('captures')
                        shutil.rmtree('detected')
                        shutil.rmtree('backup')
                        shutil.rmtree('backupimg')
                        os.makedirs('captures')
                        os.makedirs('detected')
                        os.makedirs('backup')
                        os.makedirs('backupimg')

                        self.root.destroy()
                        review(name, kid, lic_key, projectid, task)
                        # self.submit = tk.Button(self.root, text='Submit', fg="white", bg="#1d2736", font="MSGothic 13 bold")
                        # self.submit.place(x=100, y=150)

                    else:
                        self.l.after_cancel(self._timer)
                        self._elapsedtime = time.time() - self._start
                        self._setTime(self._elapsedtime)
                        self._running = 0
                        self.flag = 1
                        os.remove(self.kimg)

            else:
                messagebox.showwarning("warning", "Internet required to end timer or Timer is paused")
                # print("need internet")

        def _update(self):
            # print("============update time============")
            """ Update the label with elapsed time. """
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._timer = self.l.after(50, self._update)

        def _setTime(self, elap):
            seconds = elap
            hours = seconds // (60 * 60)
            seconds %= (60 * 60)
            minutes = seconds // 60
            seconds %= 60

            hours = int(elap / 3600)
            minutes = int(elap - hours * 60.0)
            seconds = int(elap - minutes * 60.0)
            hseconds = int((elap - minutes * 60.0 - seconds) * 100)
            hseconds = abs(hseconds)
            # self.timestr.set('%02d:%02d:%02d:%02d' % (hours,minutes, seconds, hseconds))
            seconds = elap
            hours = seconds // (60 * 60)
            seconds %= (60 * 60)
            minutes = seconds // 60
            seconds %= 60

            self.timestr.set('%02d:%02d:%02d:%02d' % (hours, minutes, seconds, hseconds))

        def connect(self, host='http://google.com'):
            try:
                urllib.request.urlopen(host)  # Python 3.x
                return True
            except:
                return False

        def convertToBinaryData(self, filename):
            # Convert digital data to binary format
            # with open(filename, 'rb') as file:
            #     binaryData = file.read()
            # return binaryData
            with open(filename, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode('utf-8')

        def takeScreenshot(self):
            if self.flag == 0:

                # x = str(self.count)
                x = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                y = datetime.datetime.now().strftime('%Y-%m-%d')
                myScreenshot = pyautogui.screenshot()
                myScreenshot_arr = np.asarray(myScreenshot)
                myScreenshot_height, myScreenshot_width = myScreenshot_arr.shape[:2]
                # print(myScreenshot_width)
                # print(myScreenshot_height)
                # print(type(myScreenshot))
                # print("-------------------------------------------------------------")
                # print(type(myScreenshot))
                re_wid = myScreenshot_width // 2  # numpy  evaluation
                re_hei = myScreenshot_height // 2
                # print(re_wid, re_hei)
                # print("-------------------------------------------------------------")
                # re_wid_num = myScreenshot_width1//2
                # re_hei_num = myScreenshot_height1//2  #numpy convert
                # print(re_wid_num, re_hei_num)

                # resize_screenshot = myScreenshot.resize((re_wid, re_hei), PIL.Image.ANTIALIAS) #resizing screenshot
                resize_screenshot = cv2.resize(myScreenshot_arr, (re_wid, re_hei))
                # resize_screenshot_arr = np.asarray(resize_screenshot)
                myScreenshot_res_height, myScreenshot_res_width = resize_screenshot.shape[:2]
                # print(myScreenshot_res_width)
                # print(myScreenshot_res_height)
                # print("resize_screenshot", resize_screenshot)
                # print("resize_screenshot_arr", resize_screenshot_arr)

                # print(type(resize_screenshot))
                # numpy_convert_img = asarray(resize_screenshot) #pillow to numpy convert
                # print(re_wid, re_hei, resize_screenshot.shape)
                sliced_image = resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75),
                               0:re_wid]  # slicing image for blurring
                # print(sliced_image.shape)
                # cv2.imshow(sliced_image)
                # print("sliced_image", sliced_image)
                blur_img = cv2.GaussianBlur(sliced_image, (7, 7), 7)
                # print(type(sliced_image))
                # print(sliced_image.shape)
                resize_screenshot[round(re_hei / 6.75):re_hei - round(re_hei / 6.75), 0:re_wid] = blur_img
                # print("Screenshot", sliced_image)
                # cv2.imshow("numpy image", sliced_image)
                numpy_to_pil = Image.fromarray(resize_screenshot)  # from numpy to PIL convert
                # print(numpy_to_pil)

                numpy_to_pil.save('captures/' + x + '_screenshot.png')
                # myScreenshot.save('captures/'+x+'_screenshot.png')
                filename = 'captures/' + x + '_screenshot.png'
                # print("file name inside take screenshot funtion", filename)
                self.open_img(filename)
                self.kimg = filename

                return x, y, "success"
            else:
                return "NULL", "NULL", "NULL"

        def insert(self, time, date):
            x = time
            # print(date)

            if self.connect():

                url = base_url + "services/apitimetrackerinserttimesheet.php"
                # mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="airTimetracker")
                empid = str(self.kid)
                projectname = str(self.projectid)
                task_feedback = "N.A."
                # db_time_format = "2020-07-10 10:40:32"
                newdbtime = time.split("-", 1)
                newdbtime = newdbtime[1]
                newdbtime = newdbtime.replace("_", ":")
                newdbdate = time.split("-", 1)
                newdbdate = newdbdate[0]
                newdbdate = newdbdate.replace("_", "-")
                time = newdbdate + " " + newdbtime
                db_time_format = time
                #print("time=========", db_time_format)
                file_loc = self.convertToBinaryData(self.kimg)
                file_loc1 = "1234"
                captureddate = date
                createddate = date
                lickey = str(self.lic_key)
                user_unique_id = str(self.name)
                duration = int(self.show) / 60
                duration = m.floor(duration)
                # print("*********************************************")
                # print(duration)
                # print(empid, user_unique_id)
                # print(self.task)
                data = {"useruniqueid": str(empid),
                        "useremail": str(user_unique_id), "datetime": str(db_time_format), "screenshot": str(file_loc),
                        "projectid": str(projectname),
                        "faceshot": str(""), "duration": str(duration), "createddate": str(date),
                        "captureddate": str(date), "requesttype": str("otp"), "tasktitle": str(self.task),
                        "emp_feedback": str(task_feedback)}
                #print("data=========", data)
                X = requests.post(url, data)
                #print(X)
                # print("======================done==============")
                # print("inside the otp insert section", data)
                # print("======================done==============")
                # print("done")

                os.remove(self.kimg)
                # os.remove(self.kimg1)
                # path of the directory
                path = "backup/"
                # path1 ="backupimg/"

                # Getting the list of directories 
                dir = os.listdir(path)
                # print("list of directory in insert", dir)

                # Checking if the list is empty or not 
                if len(dir) == 0:
                    # print("No images pending to be updated")
                    dirscreen = os.listdir("captures")
                    # print("output of dirscreen", dirscreen)
                    if len(dirscreen) == 0:
                        return True
                    else:
                        return False
                else:
                    start_path = 'backup'  # current directory
                    for path, dirs, files in os.walk(start_path):
                        for filename in files:
                            url = base_url + "services/apitimetrackerinserttimesheet.php"

                            empid = str(self.kid)
                            # print("probb",self.kimg)
                            projectname = str(self.projectid)
                            # task_feedback = feed
                            task_feedback = "N.A."
                            # print("task_feedback value", task_feedback)
                            # print("filename=", filename)
                            name = "backup/" + filename
                            time = filename.strip("_screenshot.png")
                            time1 = time
                            newdbtime = time.split("-", 1)
                            newdbtime = newdbtime[1]
                            newdbtime = newdbtime.replace("_", ":")
                            newdbdate = time.split("-", 1)
                            newdbdate = newdbdate[0]
                            newdbdate = newdbdate.replace("_", "-")
                            time = newdbdate + " " + newdbtime
                            db_time_format = time
                            # print("time=", db_time_format)
                            # db_time_format = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                            file_loc = self.convertToBinaryData(name)
                            filename1 = time1 + ".png"
                            file_loc1 = "1234"
                            captureddate = date
                            createddate = date
                            lickey = str(self.lic_key)
                            user_unique_id = str(self.name)
                            data = {"useruniqueid": str(empid),
                                    "useremail": str(user_unique_id), "datetime": str(db_time_format),
                                    "screenshot": str(file_loc),
                                    "projectid": str(projectname),
                                    "faceshot": str(""), "duration": str(duration), "createddate": str(date),
                                    "captureddate": str(date), "requesttype": str("otp"),
                                    "emp_feedback": str(task_feedback)}

                            X = requests.post(url, data)
                            # print("insert part of otp", data)
                            # print(X)
                            os.remove("backup/" + filename)
                            # os.remove("backupimg/"+filename1)
                    dirscreen = os.listdir("backup")
                    # print("backup dirscreen", dirscreen)
                    if len(dirscreen) == 0:
                        return True
                    else:
                        return False




            else:
                # Source path  
                # print(self.kimg)
                source = self.kimg
                # source1 = self.kimg1

                source2 = source.strip('captures/')
                # print('source2', source2)
                # source3 = source1.strip('detected/')
                # Destination path  
                destination = "backup/" + source2
                # destination1 = "backupimg/"+source3
                # print("destination", destination)
                shutil.move(source, destination)
                # shutil.move(source1, destination1)

                # Move the content of  
                # source to destination  
                # dest = shutil.move(source, destination)
                # print("internet not connected")
                dirscreen = os.listdir("captures")
                # print("capture dir screen", dirscreen)
                if len(dirscreen) == 0:
                    return True
                else:
                    return False

    def main(name, kid, lic_key, projectid, task):
        wfh(name, kid, lic_key, projectid, task).loop()

    if __name__ == '__main__':
        main(name, kid, lic_key, projectid, task)


if __name__ == '__main__':
    image_64_encode = "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"
    # print(type(image_64_encode))
    image_64_encode = bytes(image_64_encode, 'utf-8')
    image_64_decode = base64.decodestring(image_64_encode)
    image_result = open('deer_decode.gif', 'wb')  # create a writable image and write the decoding result
    image_result.write(image_64_decode)
    main()
