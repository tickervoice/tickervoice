#!/usr/bin/python
 # -*- coding: gb2312 -*-
import socket
import json

UDP_IP = "127.0.0.1"  # Change this to the server's IP if running on a different machine
UDP_PORT = 50001 # for telegram brige

def send_udp_message(ticker, price, interval, reminder_msg,exchange_time):
    reminder_msg = reminder_msg.replace("Buy","bullish") 
    reminder_msg = reminder_msg.replace("buy","bullish")
    reminder_msg = reminder_msg.replace("BUY","bullish")
    reminder_msg = reminder_msg.replace("Sell","bearish")
    reminder_msg = reminder_msg.replace("sell","bearish")
    reminder_msg = reminder_msg.replace("SELL","bearish")
    message = f"{ticker}|{price}|{interval}|{reminder_msg}|{exchange_time}"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    print(f"Sent: {message}")

def send_notification(
    message,
    duration=5,
    position="bottom_center",
    font_family="SimHei",
    font_size=30,
    background_color="black",
    server_ip="127.0.0.1",
    server_port=5005
):
    """
    Sends a notification message to the server.

    Parameters:
    - message: The message string to be sent.
    - duration: Duration in seconds for which the notification should be displayed.
    - position: Position on the screen where the notification should appear.
    - font_family: Font family of the message text.
    - font_size: Font size of the message text.
    - background_color: Background color of the notification window.
    - server_ip: IP address of the server.
    - server_port: Port number of the server.
    """
    # Define words to color and their corresponding colors
    color_mapping = {
        "sell": "red",
        "buy": "green",
        "pending": "yellow"
    }

    # Split the message into words
    words = message.split()

    # Create a list to hold the formatted message parts
    message_parts = []

    for word in words:
        # Remove punctuation from the word for accurate matching
        clean_word = word.strip('.,!?')
        # Check if the word should be colored
        color = color_mapping.get(clean_word.lower(), None)
        # Append the word and its color as a tuple
        message_parts.append((word, color))

    # Create the notification dictionary
    notification = {
        "message_parts": message_parts,
        "duration": duration,
        "position": position,
        "font_family": font_family,
        "font_size": font_size,
        "background_color": background_color
    }

    # Serialize the dictionary to a JSON-formatted string
    notification_json = json.dumps(notification)

    # Encode the JSON string to bytes
    notification_bytes = notification_json.encode('utf-16')

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Send the JSON bytes to the server
        sock.sendto(notification_bytes, (server_ip, server_port))
        print(f"Notification sent to {server_ip}:{server_port}")

if __name__ == "__main__":
    # Example usage
    message = "你好，世界 Consider to buy or sell."
    send_notification(message=message)
