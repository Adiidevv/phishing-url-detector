# 🛡️ Phishing URL Detector

A Python-based GUI application that detects phishing URLs using rule-based analysis techniques.

---

## 🚀 Project Overview

Phishing attacks are one of the most common cybersecurity threats where attackers create fake websites to steal sensitive information such as login credentials, banking details, and personal data.

This project helps users identify whether a URL is safe or potentially malicious using multiple detection rules.

---

## 🧠 How It Works

The application analyzes the URL based on the following factors:

* URL length (long URLs are suspicious)
* Presence of '@' symbol
* Suspicious keywords (login, verify, bank, secure, update, account)
* Use of IP address instead of domain name
* Use of HTTP instead of HTTPS
* Presence of hyphens (-)

Based on these checks, the system classifies the URL as:

* ✅ Safe URL
* ⚠️ Phishing URL
* ❌ Invalid URL

---

## 🖥️ Features

* Simple and user-friendly GUI using Tkinter
* Real-time URL validation
* Rule-based phishing detection
* Beginner-friendly cybersecurity project
* Fast and lightweight

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI Development)
* Validators Library
* Regular Expressions (re module)

---

## ▶️ How to Run the Project

### 1. Install required library

pip3 install validators

### 2. Run the program

python3 phishing_detector.py

---

## 📌 Example

Input:
http://secure-login-bank.xyz

Output:
⚠️ Phishing URL Detected

---

## 📈 Future Improvements

* Machine Learning-based phishing detection
* Integration with real-time phishing detection APIs
* Domain reputation checking
* Convert into browser extension
* Add URL blacklist database

---

## 🎯 Project Purpose

This project was developed to understand the fundamentals of cybersecurity and phishing detection techniques using Python.

---

## 👨‍💻 Author

Adidev S  
BCA Student | Cybersecurity & Data Analytics Learner 
