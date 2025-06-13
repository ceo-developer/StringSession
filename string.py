from pyrogram import Client
from pyrogram.types import Message
from pyrogram.session import StringSession
import asyncio

API_ID = int(input("🔢 Enter your API_ID: "))
API_HASH = input("🔑 Enter your API_HASH: ")

async def main():
    print("\n🔁 Please login using your phone number & OTP.")
    async with Client(name="gen", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
        session_string = await app.export_session_string()
        print("\n✅ Your String Session:")
        print("-" * 40)
        print(session_string)
        print("-" * 40)
        print("\n📌 Copy & Save it securely. Don't share it with anyone.")

if __name__ == "__main__":
    asyncio.run(main())
