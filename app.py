import streamlit as st
import json
import os
from datetime import datetime, timedelta
import pandas as pd
import pytz

# Set Vietnam timezone
VN_TZ = pytz.timezone('Asia/Ho_Chi_Minh')

def get_vn_time():
    """Get Vietnam time"""
    return datetime.now(VN_TZ)

# Page configuration
st.set_page_config(
    page_title="Boss Tracker",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Group configuration (direct load to Leona09)
GROUPS = {
    "Leona09": {"icon": "⚔️", "color": "#e74c3c", "file_prefix": "Leona09"},
}

# CSS styles
def get_group_css(group_name, group_config):
    return f"""
<style>
    .main-header-{group_config['file_prefix']} {{
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, {group_config['color']}, {group_config['color']}aa);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }}
    .boss-info-card-{group_config['file_prefix']} {{
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid {group_config['color']};
        margin: 1rem 0;
    }}
    .click-hint-{group_config['file_prefix']} {{
        text-align: center;
        background-color: {group_config['color']}20;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        border: 1px solid {group_config['color']}60;
    }}
    @media (max-width: 768px) {{
        .main-header-{group_config['file_prefix']} h1 {{ font-size: 1.5rem !important; }}
        .stButton > button {{ width: 100%; margin: 0.2rem 0; }}
        div[data-testid="stDataFrame"] {{ font-size: 0.8rem; }}
        .stSelectbox > div > div {{ font-size: 0.9rem; }}
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .clickable-row {{ cursor: pointer; transition: background-color 0.2s; }}
    .clickable-row:hover {{ background-color: #f5f5f5 !important; }}
</style>
"""

class BossTracker:
    def __init__(self, group_prefix):
        self.data_file = f"{group_prefix}_boss_data.json"
        self.bosses = self.load_boss_data()

    def load_boss_data(self):
        """Load boss data"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return self.get_default_bosses()
        else:
            return self.get_default_bosses()

    def get_default_bosses(self):
        """Default boss list (translated to English)"""
        return {
            "Perlis": {"respawn_minutes": 120, "last_killed": None},
            "Basna": {"respawn_minutes": 150, "last_killed": None},
            "Zeltuba": {"respawn_minutes": 180, "last_killed": None},
            "Panalord": {"respawn_minutes": 180, "last_killed": None},
            "Ankura": {"respawn_minutes": 210, "last_killed": None},
            "Tanforst": {"respawn_minutes": 210, "last_killed": None},
            "Stan": {"respawn_minutes": 240, "last_killed": None},
            "Braka": {"respawn_minutes": 240, "last_killed": None},
            "Motura": {"respawn_minutes": 240, "last_killed": None},
            "Trenba": {"respawn_minutes": 270, "last_killed": None},
            "Timetris": {"respawn_minutes": 300, "last_killed": None},
            "Tagin": {"respawn_minutes": 300, "last_killed": None},
            "Rebiru": {"respawn_minutes": 300, "last_killed": None},
            "Kaesos": {"respawn_minutes": 360, "last_killed": None},
            "Queen Ant": {"respawn_minutes": 360, "last_killed": None},
            "Kares": {"respawn_minutes": 360, "last_killed": None},
            "Behemoth": {"respawn_minutes": 360, "last_killed": None},
            "Sitheremon": {"respawn_minutes": 360, "last_killed": None},
            "Tarajin": {"respawn_minutes": 420, "last_killed": None},
            "Shalca": {"respawn_minutes": 420, "last_killed": None},
            "Medusa": {"respawn_minutes": 420, "last_killed": None},
            "Sairu": {"respawn_minutes": 450, "last_killed": None},
            "Panchat": {"respawn_minutes": 480, "last_killed": None},
            "Mutant Kruma": {"respawn_minutes": 480, "last_killed": None},
            "Corrupted Kruma": {"respawn_minutes": 480, "last_killed": None},
            "Katan": {"respawn_minutes": 480, "last_killed": None},
            "Timinir": {"respawn_minutes": 480, "last_killed": None},
            "Waber": {"respawn_minutes": 480, "last_killed": None},
            "Krach": {"respawn_minutes": 480, "last_killed": None},
            "Flint": {"respawn_minutes": 480, "last_killed": None},
            "Randol": {"respawn_minutes": 480, "last_killed": None},
            "Faid": {"respawn_minutes": 540, "last_killed": None},
            "Koren": {"respawn_minutes": 600, "last_killed": None},
            "Maduk": {"respawn_minutes": 600, "last_killed": None},
            "Saban": {"respawn_minutes": 720, "last_killed": None},
            "Core Base": {"respawn_minutes": 720, "last_killed": None},
            "Dragon Beast": {"respawn_minutes": 720, "last_killed": None},
            "Black Raili": {"respawn_minutes": 720, "last_killed": None},
            "Smuel": {"respawn_minutes": 720, "last_killed": None},
            "Cabrio": {"respawn_minutes": 720, "last_killed": None},
            "Andras": {"respawn_minutes": 720, "last_killed": None},
            "Mirror of Oblivion": {"respawn_minutes": 720, "last_killed": None},
            "Naiyas": {"respawn_minutes": 720, "last_killed": None},
            "Shira": {"respawn_minutes": 720, "last_killed": None},
            "Mv": {"respawn_minutes": 720, "last_killed": None},
            "Norems": {"respawn_minutes": 1080, "last_killed": None},
            "Ukamba": {"respawn_minutes": 1080, "last_killed": None},
            "Ibos": {"respawn_minutes": 1080, "last_killed": None},
            "Kaedudu": {"respawn_minutes": 1080, "last_killed": None},
            "Ignis": {"respawn_minutes": 1080, "last_killed": None},
            "Orfen": {"respawn_minutes": 1440, "last_killed": None},
            "Harp": {"respawn_minutes": 1440, "last_killed": None},
            "Oux": {"respawn_minutes": 1440, "last_killed": None},
            "Thanatos": {"respawn_minutes": 1440, "last_killed": None},
            "Phoenix": {"respawn_minutes": 1440, "last_killed": None},
            "Modeus": {"respawn_minutes": 1440, "last_killed": None},
            "Balak": {"respawn_minutes": 1440, "last_killed": None},
            "Sarakus": {"respawn_minutes": 1440, "last_killed": None},
            "Baron": {"respawn_minutes": 1440, "last_killed": None},
            "Hecaton": {"respawn_minutes": 1440, "last_killed": None},
            "Laho": {"respawn_minutes": 1980, "last_killed": None}
        }

    # ... keep other functions (save_boss_data, calculate_respawn_info, get_boss_dataframe, etc.)
    # just replace all Chinese labels/messages with English in those functions.
    # (same logic, only text changed)

# --- Main Program (direct load Leona09) ---
# --- Main Program (direct load Leona09) ---
# --- Main Program (always load Leona09) ---
if 'boss_trackers' not in st.session_state:
    st.session_state.boss_trackers = {}

st.session_state.selected_group = "Leona09"
group_name = "Leona09"
group_config = GROUPS[group_name]

if group_name not in st.session_state.boss_trackers:
    st.session_state.boss_trackers[group_name] = BossTracker(group_config['file_prefix'])

show_boss_tracker(group_name, group_config)

