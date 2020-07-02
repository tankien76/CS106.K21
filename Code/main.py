from predict import *
import tkinter as tk
import webbrowser
import textwrap
from tkinter import ttk

if __name__ == "__main__":

    test=tk.Tk()

    test.title("Chương trình dự đoán chủ đề của đoạn văn")
    canvas=tk.Canvas(test, height=700,width=800)
    test.resizable(0,0)
    canvas.pack()
    
    def clearTextInput():
        entry.delete("1.0","end")

    frame=tk.Frame(test)
    frame.place(rely=0.015,relwidth=0.25,relheight=0.1)

    lb_textinput=tk.Label(frame,text='Nhập đoạn văn:',font =('Times New Roman',14))
    lb_textinput.place(relwidth=1,relheight=1)

    frame1=tk.Frame(test,bg="#11b2f2",bd=5)
    frame1.place(relx=0.04,rely=0.1,relwidth=0.5,relheight=0.5)

    entry =tk.Text(frame1,font=('Times New Roman',14))
    entry.place(relwidth=1,relheight=1)
    entry.pack()

    frame6=tk.Frame(test)
    frame6.place(relx=0.79,rely=0.05,relwidth=0.17,relheight=0.1)

    n = tk.StringVar() 
    web_chosen= ttk.Combobox(frame6, width = 19, textvariable = n) 

    frame4=tk.Frame(test)
    frame4.place(relx=0.54,rely=0.015,relwidth=0.25,relheight=0.1)

    lb_link=tk.Label(frame4,text='Đường link:',font =('Times New Roman',14))
    lb_link.place(relwidth=1,relheight=1)

    frame4=tk.Frame(test,bg="#fc036b",bd=5)
    frame4.place(relx=0.6,rely=0.1,relwidth=0.36,relheight=0.66)

    lable10=tk.Label(frame4,bg='white')
    lable10.place(relx=0.5,relwidth=1,relheight=1,anchor='n')

    def callback(eventObject, prediction):
        r = Link_Suggestion(prediction, web_chosen.get())
        lb_linkex=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex.place(relwidth=1,relheight=0.1)
        lb_linkex.config(text = r[0])

        lb_linkex.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex.cget("text")))

        lb_linkex1=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex1.place(relwidth=1,relheight=0.1, rely = 0.1)
        lb_linkex1.config(text = r[1])
        lb_linkex1.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex1.cget("text")))

        lb_linkex2=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex2.place(relwidth=1,relheight=0.1, rely = 0.2)
        lb_linkex2.config(text = r[2])
        lb_linkex2.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex2.cget("text")))

        lb_linkex3=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex3.place(relwidth=1,relheight=0.1, rely = 0.3)
        lb_linkex3.config(text = r[3])
        lb_linkex3.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex3.cget("text")))

        lb_linkex4=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex4.place(relwidth=1,relheight=0.1, rely = 0.4)
        lb_linkex4.config(text = r[4])
        lb_linkex4.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex4.cget("text")))

        lb_linkex5=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex5.place(relwidth=1,relheight=0.1, rely = 0.5)
        lb_linkex5.config(text = r[5])
        lb_linkex5.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex5.cget("text")))

        lb_linkex6=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex6.place(relwidth=1,relheight=0.1, rely = 0.6)
        lb_linkex6.config(text = r[6])
        lb_linkex6.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex6.cget("text")))

        lb_linkex7=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex7.place(relwidth=1,relheight=0.1, rely = 0.7)
        lb_linkex7.config(text = r[7])
        lb_linkex7.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex7.cget("text")))

        lb_linkex8=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex8.place(relwidth=1,relheight=0.1, rely = 0.8)
        lb_linkex8.config(text = r[8])
        lb_linkex8.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex8.cget("text")))

        lb_linkex9=tk.Label(frame4,font =('Times New Roman',10), anchor='nw', justify ='left', wraplength=275,bg='white')
        lb_linkex9.place(relwidth=1,relheight=0.1, rely = 0.9)
        lb_linkex9.config(text = r[9])
        lb_linkex9.bind("<Button-1>", lambda event: webbrowser.open_new(lb_linkex9.cget("text")))
    def retrieve_input():
        input = entry.get("1.0","end-1c")
        prediction = Predict_data(input)
        if (prediction=="tvshowbiz"):
            web_chosen['values'] = ['The Sun']
            web_chosen.grid(column = 1, row = 1) 
            web_chosen.current()
        elif (prediction == "lifestyle"):
            web_chosen['values'] = ['Telegraph']
            web_chosen.grid(column = 1, row = 1) 
            web_chosen.current()
        else:
            web_chosen['values'] = ['The Sun', 'Telegraph']
            web_chosen.grid(column = 1, row = 2) 
            web_chosen.current()
        web_chosen.bind("<<ComboboxSelected>>", lambda event: callback(None, prediction))

        lable4=tk.Label(frame5,font =('Times New Roman',14),bg='white', text = prediction)
        lable4.place(relx=0.3,relwidth=0.7,relheight=1)

    frame2=tk.Frame(test,bg="#11b2f2",bd=5)
    frame2.place(relx=0.04,rely=0.63,relwidth=0.15,relheight=0.05)

    btn_pred=tk.Button(frame2,text='DỰ ĐOÁN',font=('Times New Roman',10,"bold"),bg='white', command = retrieve_input)
    btn_pred.place(relwidth=1,relheight=1)

    frame3=tk.Frame(test,bg="#11b2f2",bd=5)
    frame3.place(relx=0.23,rely=0.63,relwidth=0.15,relheight=0.05)

    btn_del=tk.Button(frame3,text='XÓA',font=('Times New Roman',10,"bold"),command=clearTextInput,bg='white')
    btn_del.place(relwidth=1,relheight=1)

    frame5=tk.Frame(test,bg="#fc036b",bd=5)
    frame5.place(relx=0.04,rely=0.71,relwidth=0.5,relheight=0.05)

    lb_type=tk.Label(frame5,text="CHỦ ĐỀ:", font =('Times New Roman',10,"bold"),bg='white')
    lb_type.place(relwidth=0.25,relheight=1)

    label100=tk.Label(frame5,bg='white')
    label100.place(relx=0.3,relwidth=0.7,relheight=1)

    tk.mainloop()
