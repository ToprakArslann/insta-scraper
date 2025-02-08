import requests
import json
from datetime import datetime

def insta_scraper(username):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://www.instagram.com/",
        "Accept-Language": "en-US,en;q=0.9",
        "X-IG-App-ID": "936619743392459"
    }

    #Scrape data
    profile_url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
    try:
        response = requests.get(profile_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'user' in data['data']:
                user_data = data['data']['user']
                return {
                    "username": user_data["username"],
                    "full_name": user_data["full_name"],
                    "bio": user_data["biography"],
                    "followers": user_data["edge_followed_by"]["count"],
                    "following": user_data["edge_follow"]["count"],
                    "profile_pic_url": user_data["profile_pic_url_hd"],
                    "is_private": user_data["is_private"],
                    "is_verified": user_data["is_verified"],
                    "post_count": user_data["edge_owner_to_timeline_media"]["count"],
                    "external_url": user_data.get("external_url"),
                    "retrieved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
        return None
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

username = input("Please write an username:")

print(username) 
profile_data = insta_scraper(username)

if profile_data:
    print("📌 Instagram Profile Info")
    print(f"👤 Username: {profile_data['username']}")
    print(f"⭐ Full name: {profile_data['full_name']}")
    print(f"🔹 Bio: {profile_data['bio']}")
    print(f"👥 Follower count: {profile_data['followers']}")
    print(f"➡️ Following: {profile_data['following']}")
    print(f"📸 Profile picture: {profile_data['profile_pic_url']}")
    print(f"🔒 Is it private?: {'Yes' if profile_data['is_private'] else 'No'}")
    print(f"✅ Is it verified?: {'Yes' if profile_data['is_verified'] else 'No'}")
    print(f"📩 Post count: {profile_data['post_count']}")
    if profile_data['external_url']:
        print(f"⛓️‍💥 External url: {profile_data['external_url']}")
    print(f"⏳ Retrieved at: {profile_data['retrieved_at']}")



