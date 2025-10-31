import requests, sys, os
from packaging import version  # pip install packaging if needed

REPO_OWNER = "Alex1-stack-dev"
REPO_NAME = "tm2"
APP_FILENAME = sys.argv[0]
CURRENT_VERSION = "1.0.0"  # Update with your app's version string, e.g. '1.0.0'
GITHUB_API = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest'


def get_latest_github_release():
    resp = requests.get(GITHUB_API, timeout=10)
    if not resp.ok:
        print("Failed to fetch GitHub releases.")
        return None, None, None
    data = resp.json()
    tag = data.get('tag_name')
    assets = data.get('assets', [])
    exe_asset = next((a for a in assets if a['name'].endswith('.exe')), None)
    if not exe_asset:
        print('No .exe asset found in latest release.')
        return tag, None, None
    return tag, exe_asset['browser_download_url'], exe_asset['name']

def download_latest_exe(download_url, filename):
    with requests.get(download_url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def restart_app(new_exe_path):
    os.startfile(new_exe_path)
    sys.exit(0)

def check_for_update():
    latest_tag, download_url, asset_name = get_latest_github_release()
    if not latest_tag:
        print('Could not check for update.')
        return
    if version.parse(latest_tag.lstrip('v')) > version.parse(CURRENT_VERSION):
        print(f'Updating to version {latest_tag}...')
        new_exe = APP_FILENAME + '.new'
        download_latest_exe(download_url, new_exe)
        os.rename(APP_FILENAME, APP_FILENAME + '.old')
        os.rename(new_exe, APP_FILENAME)
        print('Update applied. Restarting...')
        restart_app(APP_FILENAME)
    else:
        print('You are on the latest version.')

if __name__ == '__main__':
    check_for_update()
    # Continue with normal app...
