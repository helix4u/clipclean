import pyperclip
import re
import time

def convert_youtube_live_url(url):
    """
    Converts a YouTube Live URL to its shortened youtu.be format.
    """
    match = re.match(r'https://(?:www\.)?youtube\.com/live/([a-zA-Z0-9_-]+)', url)
    if match:
        video_id = match.group(1)
        return f'https://youtu.be/{video_id}'
    return url

def monitor_clipboard():
    """
    Monitors the clipboard for YouTube Live URLs and converts them.
    """
    recent_value = ""
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != recent_value:
            recent_value = clipboard_content
            converted_url = convert_youtube_live_url(clipboard_content)
            if converted_url != clipboard_content:
                pyperclip.copy(converted_url)
                print(f"Converted URL: {converted_url}")
        time.sleep(1)  # Check the clipboard every second

if __name__ == "__main__":
    print("Monitoring clipboard for YouTube Live URLs. Press Ctrl+C to stop.")
    try:
        monitor_clipboard()
    except KeyboardInterrupt:
        print("Clipboard monitoring stopped.")
