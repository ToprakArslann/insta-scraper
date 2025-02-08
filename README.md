# Instagram Profile Scraper

A simple Python script to fetch public Instagram profile information using Instagram's GraphQL API. This tool allows you to retrieve basic profile statistics and information without requiring login or authentication.

## Features

- Fetch basic profile information
- No authentication required
- Clean formatted output
- Error handling
- No external dependencies except `requests`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ToprakArslann/insta-scraper.git
cd insta-scraper
```

2. Install required package:
```bash
pip install requests
```

## Usage

```python
python scraper.py
```
When prompted, enter the Instagram username you want to analyze.

## Example Output
```
📌 Instagram Profile Info
👤 Username: example
⭐ Full name: Example User
🔹 Bio: This is a bio
👥 Follower count: 10000
➡️ Following: 10
📸 Profile picture: example-picture
🔒 Is it private?: No
✅ Is it verified?: Yes
📩 Post count: 100
⏳ Retrieved at: 2025-02-09 00:00:00
```

## Disclaimer

This tool is for educational purposes only. Please respect Instagram's terms of service and rate limiting when using this script.
