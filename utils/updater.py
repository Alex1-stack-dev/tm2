import requests
LATEST_URL = 'https://example.com/latest_version.txt'  # Your server/wiki with latest version string
__version__ = '1.0.0'  # Match your app version

def check_for_update():
    try:
        latest = requests.get(LATEST_URL, timeout=2).text.strip()
        if latest and latest != __version__:
            return True, latest
    except Exception:
        pass
    return False, __version__
# Example (called on startup):
# is_new, new_v = check_for_update()
