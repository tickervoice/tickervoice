import socket
import json
import tkinter as tk
from tkinter import font
import threading
import queue,os

def apply_text_formatting(text_widget, message_parts):
    """
    Inserts text into the Text widget with specified formatting.
    """
    text_widget.configure(state='normal')  # Enable editing

    for word, color in message_parts:
        if color:
            if color not in text_widget.tag_names():
                text_widget.tag_configure(color, foreground=color)
            text_widget.insert('end', word + ' ', color)
        else:
            text_widget.insert('end', word + ' ')

    text_widget.update_idletasks()  # Force UI update
    text_widget.configure(state='disabled')  # Disable editing again


def show_notification(root, message_parts, duration=5, position="bottom_center", 
                      font_family="SimHei", font_size=30, background_color="black"):
    """
    Displays a notification with the specified parameters.
    """
    notification_window = tk.Toplevel(root)
    notification_window.overrideredirect(True)
    notification_window.attributes('-topmost', True)
    notification_window.configure(bg=background_color)

    custom_font = font.Font(family=font_family, size=font_size, weight='bold')

    # Calculate text dimensions
    text_width = sum(custom_font.measure(word) for word, _ in message_parts) + 20
    text_height = custom_font.metrics("linespace")

    window_width = max(300, text_width + 100)  # Ensure minimum width
    window_height = max(100, text_height * 2)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    positions = {
        "top_left": (0, 0),
        "top_center": (screen_width // 2 - window_width // 2, 0),
        "top_right": (screen_width - window_width, 0),
        "center": (screen_width // 2 - window_width // 2, screen_height // 2 - window_height // 2),
        "bottom_left": (0, screen_height - window_height),
        "bottom_center": (screen_width // 2 - window_width // 2, screen_height - window_height - 30),
        "bottom_right": (screen_width - window_width, screen_height - window_height),
    }

    x_position, y_position = positions.get(position, positions["center"])
    notification_window.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

    # Create a text widget
    text_widget = tk.Text(notification_window, font=custom_font, bg=background_color, 
                          fg="white", bd=0, highlightthickness=0, wrap="word")
    text_widget.pack(expand=True, fill='both')

    apply_text_formatting(text_widget, message_parts)

    # Close window after duration
    root.after(duration * 1000, notification_window.destroy)


def process_queue(root, message_queue):
    """
    Processes messages from the queue and displays notifications.
    """
    try:
        while True:
            message = message_queue.get_nowait()
            message_parts = message.get('message_parts', [])
            duration = message.get('duration', 5)
            position = message.get('position', 'bottom_center')
            font_family = message.get('font_family', 'Helvetica')
            font_size = message.get('font_size', 30)
            background_color = message.get('background_color', 'black')

            show_notification(root, message_parts, duration, position, font_family, font_size, background_color)
    except queue.Empty:
        pass
    finally:
        root.after(100, process_queue, root, message_queue)


def receive_messages(message_queue):
    """
    Listens for incoming UDP messages.
    """
    server_address = ('', 5005)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)

    while True:
        data, address = sock.recvfrom(4096)
        if data:
            message = json.loads(data.decode('utf-16'))
            print(f"Received message from {address}: {message}")
            message_queue.put(message)


def main():
    root = tk.Tk()
    root.withdraw()  # Hide root window
    message_queue = queue.Queue()
    print("Listening for UDP messages on port 5005...")
    threading.Thread(target=receive_messages, args=(message_queue,), daemon=True).start()

    process_queue(root, message_queue)

    root.mainloop()


if __name__ == "__main__":
    WINDOW_TITLE = "Udp Screen Message Server"
    os.system(f"title {WINDOW_TITLE}") 
    main()
