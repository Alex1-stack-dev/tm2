# Swim Meet Manager

A modular, cross-platform swim meet management suite with real-time device sync, exports, and user-friendly GUI.

## Features
- PyQt6 Tabbed GUI: Meets, Timing, Results, Settings, Help
- Live results webserver (FastAPI)
- Connect Time Machine G2, Colorado, Daktronics hardware
- Export in CSV, PDF, and Hytek formats
- Context menus, keyboard shortcuts, and inline validation
- Robust test coverage and error logging

## Installation
### Requirements
- Python 3.9+
- PyQt6: `pip install PyQt6`
- Other: `pip install fastapi pytest pytest-qt`

### Setup
```sh
git clone https://github.com/Alex1-stack-dev/tm2.git
cd tm2
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
