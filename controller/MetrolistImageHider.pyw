import os
import tkinter as tk
from pathlib import Path

APP_NAME = "Metrolist Image Hider"
BG = "#10131a"


def flag_path() -> Path:
    appdata = os.environ.get("APPDATA")
    root = Path(appdata) / "Metrolist" if appdata else Path.home() / ".config" / "metrolist"
    return root / "hide-images.flag"


class Controller:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.flag = flag_path()
        root.title(APP_NAME)
        root.geometry("410x285")
        root.resizable(False, False)
        root.configure(bg=BG)

        tk.Label(
            root,
            text="METROLIST",
            bg=BG,
            fg="#8ea6ff",
            font=("Segoe UI", 10, "bold"),
        ).pack(pady=(22, 3))
        tk.Label(
            root,
            text="Image Hider",
            bg=BG,
            fg="#ffffff",
            font=("Segoe UI", 22, "bold"),
        ).pack()
        tk.Label(
            root,
            text="שליטה בהצגה ובהסתרה של תמונות ב-Metrolist",
            bg=BG,
            fg="#aab2c5",
            font=("Segoe UI", 10),
        ).pack(pady=(7, 18))

        self.status = tk.Label(
            root,
            text="",
            bg=BG,
            fg="#d9e0ef",
            font=("Segoe UI", 11, "bold"),
        )
        self.status.pack(pady=(0, 12))

        self.toggle = tk.Button(
            root,
            text="",
            command=self.toggle_images,
            font=("Segoe UI", 12, "bold"),
            width=24,
            height=2,
            relief="flat",
            bd=0,
            cursor="hand2",
            activeforeground="#ffffff",
        )
        self.toggle.pack()

        tk.Label(
            root,
            text="השינוי מתעדכן אוטומטית בתוך Metrolist",
            bg=BG,
            fg="#7f899e",
            font=("Segoe UI", 9),
        ).pack(pady=(17, 0))
        tk.Label(
            root,
            text="התמונות מוסתרות, הממשק והטקסט נשארים זמינים",
            bg=BG,
            fg="#69748a",
            font=("Segoe UI", 8),
        ).pack(pady=(5, 0))
        self.refresh()

    def hidden(self) -> bool:
        return self.flag.is_file()

    def refresh(self):
        if self.hidden():
            self.status.config(text="מצב נוכחי: התמונות מוסתרות", fg="#ffcf79")
            self.toggle.config(
                text="הצג תמונות",
                bg="#2b805d",
                fg="white",
                activebackground="#369a70",
            )
        else:
            self.status.config(text="מצב נוכחי: התמונות מוצגות", fg="#9fe0bd")
            self.toggle.config(
                text="הסתר את כל התמונות",
                bg="#5269c8",
                fg="white",
                activebackground="#647de0",
            )

    def toggle_images(self):
        try:
            self.flag.parent.mkdir(parents=True, exist_ok=True)
            if self.hidden():
                self.flag.unlink()
            else:
                self.flag.write_text("hide", encoding="utf-8")
            self.refresh()
        except OSError as exc:
            self.status.config(text=f"שגיאה בשמירת ההגדרה: {exc}", fg="#ff8e8e")


if __name__ == "__main__":
    window = tk.Tk()
    Controller(window)
    window.mainloop()
