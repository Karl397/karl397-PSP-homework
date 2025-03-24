import tkinter as tk
from tkinter import messagebox
import time
import winsound  # Windows系统使用，其他系统需替换为相应声音库


class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("番茄钟")
        self.root.geometry("300x200")

        self.work_time = 25 * 60  # 25分钟工作时间（秒）
        self.short_break = 5 * 60  # 5分钟短休息
        self.long_break = 15 * 60  # 15分钟长休息
        self.pomodoros = 0  # 完成的番茄钟计数
        self.current_time = self.work_time
        self.is_running = False
        self.is_work = True  # 当前是否为工作时间

        # 界面组件
        self.label = tk.Label(self.root, text="25:00", font=("Arial", 40))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="开始", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.root, text="重置", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

        self.status_label = tk.Label(self.root, text="准备开始", fg="gray")
        self.status_label.pack(pady=5)

        self.root.mainloop()

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(text="暂停")
            self.update_timer()
        else:
            self.is_running = False
            self.start_button.config(text="继续")

    def reset_timer(self):
        self.is_running = False
        self.current_time = self.work_time
        self.is_work = True
        self.pomodoros = 0
        self.update_display("25:00", "准备开始", "gray")
        self.start_button.config(text="开始")

    def update_timer(self):
        if self.is_running and self.current_time > 0:
            mins, secs = divmod(self.current_time, 60)
            self.update_display(f"{mins:02d}:{secs:02d}", "工作中" if self.is_work else "休息中",
                                "red" if self.is_work else "green")
            self.current_time -= 1
            self.root.after(1000, self.update_timer)
        elif self.current_time == 0:
            self.is_running = False
            self.play_sound()
            self.handle_phase_end()

    def handle_phase_end(self):
        if self.is_work:
            self.pomodoros += 1
            if self.pomodoros % 4 == 0:
                self.current_time = self.long_break
                messagebox.showinfo("完成", "进入长休息（15分钟）")
            else:
                self.current_time = self.short_break
                messagebox.showinfo("完成", "进入短休息（5分钟）")
            self.is_work = False
        else:
            self.current_time = self.work_time
            messagebox.showinfo("完成", "开始新的番茄钟（25分钟）")
            self.is_work = True
        self.start_timer()  # 自动开始下一阶段

    def update_display(self, time_str, status, color):
        self.label.config(text=time_str)
        self.status_label.config(text=status, fg=color)

    def play_sound(self):
        # Windows系统播放提示音（其他系统需替换）
        winsound.Beep(1000, 500)  # 频率1000Hz，持续500ms


if __name__ == "__main__":
    PomodoroTimer()