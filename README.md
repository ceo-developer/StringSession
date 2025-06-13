---

## 🔐 Telegram Session String Generator (For Pyrogram)

Easily generate a Telegram session string to access private Telegram chats using your own account.

---

### 📌 What is a Session String?

A **session string** is a secure login token that allows bots or scripts to access your Telegram account programmatically using **Pyrogram**.

---

## 📲 1. How to Use

### Termux Users:

```bash
pkg update && pkg upgrade
pkg install python git -y
pip install pyrogram tgcrypto
```

### Pydroid 3 Users:

1. Open **Pydroid 3**
2. Go to Pip → Install the following:

   * `pyrogram`
   * `tgcrypto`

---

## 💾 2. Save the Script

Create a file named `string.py` and paste this code inside:

```python
from pyrogram import Client
from pyrogram.sessions import StringSession

api_id = int(input("🔢 Enter your API ID: "))
api_hash = input("🔑 Enter your API HASH: ")

with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
    print("\n✅ Your Session String:\n")
    print(app.export_session_string())
```

---

## 🚀 3. Run the Script

### In Termux:

```bash
python3 string.py
```

### In Pydroid 3:

* Open the `.py` file → tap ▶️ Run

---

## 🧾 4. Example Output

```
🔢 Enter your API ID: 123456
🔑 Enter your API HASH: abcdef1234567890abcdef1234567890

Please enter your phone number: +91xxxxxxxxxx
Enter the OTP sent to your Telegram...

✅ Your Session String:

BQDkN7...dReWYA==
```

---

## 🛑 Important Notes

* 🗝️ You can use this session with any Pyrogram script (like Save Restricted Bot).
* 🔁 Re-generate if you logout from Telegram manually.

---

## 🙋 Help

Need help generating session or using it in bots?
DM: [@hiden\_25](https://t.me/hiden_25)

---
