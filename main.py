# main.py
import json
import tkinter as tk
from tkinter import messagebox

# 加载课程数据
def load_courses():
    with open('courses.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 查找课程
def find_course(course_id):
    for course in courses:
        if course['courseId'] == course_id:
            return course
    return None

# 添加到日历（模拟）
def add_to_calendar(course):
    messagebox.showinfo("添加到日历", f"已添加课程: {course['title']}")

# 搜索课程
def search_course():
    course_id = entry.get()
    course = find_course(course_id)
    if course:
        result_text.delete(1.0, tk.END)  # 清空文本框
        result_text.insert(tk.END, f"课程名称: {course['title']}\n")
        result_text.insert(tk.END, f"上课时间: {course['schedule']}\n")
        result_text.insert(tk.END, f"授课教师: {course['instructor']}\n")
        result_text.insert(tk.END, f"上课地点: {course['location']}\n")
        result_text.insert(tk.END, f"备注: {course['notes']}\n")
        add_button.config(state=tk.NORMAL)  # 启用添加按钮
        global current_course
        current_course = course
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "未找到该课程")
        add_button.config(state=tk.DISABLED)  # 禁用添加按钮

# 初始化 Tkinter
root = tk.Tk()
root.title("课程调度器")

# 输入框和搜索按钮
entry_label = tk.Label(root, text="输入课号:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)
search_button = tk.Button(root, text="搜索课程", command=search_course)
search_button.pack(pady=5)

# 结果显示文本框
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

# 添加到日历按钮
add_button = tk.Button(root, text="添加到日历", state=tk.DISABLED, command=lambda: add_to_calendar(current_course))
add_button.pack(pady=5)

# 加载课程数据
courses = load_courses()
current_course = None

# 运行主循环
root.mainloop()