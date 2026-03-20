import tkinter as tk
import re
import validators

# Function to check URL
def check_url():
    url = entry.get()
    score = 0

    # Check if URL is valid
    if not validators.url(url):
        result_label.config(text="❌ Invalid URL", fg="orange")
        return

    # Rule 1: URL length
    if len(url) > 50:
        score += 1

    # Rule 2: Contains '@'
    if '@' in url:
        score += 2

    # Rule 3: Suspicious words
    suspicious_words = ['login', 'secure', 'verify', 'update', 'bank', 'account']
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Rule 4: Contains IP address
    if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url):
        score += 2

    # Rule 5: Hyphen in domain
    if '-' in url:
        score += 1

    # Rule 6: Uses http instead of https
    if url.startswith("http://"):
        score += 1

    # Final decision
    if score >= 3:
        result_label.config(text="⚠️ Phishing URL Detected", fg="red")
    else:
        result_label.config(text="✅ Safe URL", fg="green")


# GUI setup
root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("400x250")

tk.Label(root, text="Enter URL:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Check URL", command=check_url).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
