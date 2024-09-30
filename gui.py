import datetime
import schedule
import time
import subprocess
import os
import sys
import customtkinter
import tkinter



def gui():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")
    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("DontEvenAskMe")
    app.iconbitmap('mwc.ico')


if __name__ == '__main__':
    gui()