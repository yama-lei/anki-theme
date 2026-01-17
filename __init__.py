"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    WASHI — 和纸主题
    A Japanese Editorial-Inspired Theme for Anki

    Design Philosophy:
    • Editorial magazine aesthetics with generous whitespace
    • Washi (Japanese paper) textures and subtle imperfections
    • Noto Serif JP for headlines, Inter for body text
    • Vermilion (朱色) accents inspired by traditional Japanese seals
    • Light/Dark modes with carefully crafted palettes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

from typing import Optional, Dict
from aqt import gui_hooks, mw
from aqt.qt import (
    QMenuBar, QMenu, QWidget, qtmajor, QTimer, QApplication, sip
)
from aqt.theme import theme_manager
from aqt.webview import AnkiWebView
import aqt.colors

# ═══════════════════════════════════════════════════════════════════════════════
#   COLOR PALETTES — 精心调配的色彩
# ═══════════════════════════════════════════════════════════════════════════════

WASHI_COLORS_LIGHT = {
    # Foundation — 纸张色系
    "paper_primary": "#FAF7F2",      # 主纸色 — warm cream
    "paper_secondary": "#F0EBE3",    # 次纸色 — slightly darker cream
    "paper_elevated": "#FFFFFF",     # 浮起纸色 — pure white

    # Typography — 文字色系
    "ink_primary": "#1A1A1A",        # 主墨色 — near black
    "ink_secondary": "#4A4A4A",      # 次墨色 — dark gray
    "ink_tertiary": "#8B8680",       # 三级墨色 — warm gray
    "ink_faint": "#C4BEB8",          # 淡墨色 — very light gray

    # Accent — 朱色系统
    "vermilion": "#C73E3A",          # 朱砂 — traditional Japanese red
    "vermilion_soft": "#E8A598",     # 柔朱 — soft vermilion
    "vermilion_pale": "#F5E6E4",     # 淡朱 — pale vermilion background

    # Nature — 自然色系
    "indigo": "#2F4F6F",             # 靛蓝 — muted blue
    "matcha": "#7A8B6E",             # 抹茶 — muted green
    "gold": "#B8977E",               # 金色 — muted gold

    # Structural — 结构色系
    "border_subtle": "rgba(26, 26, 26, 0.08)",
    "border_medium": "rgba(26, 26, 26, 0.12)",
    "border_strong": "rgba(26, 26, 26, 0.18)",

    "shadow_soft": "rgba(26, 26, 26, 0.04)",
    "shadow_medium": "rgba(26, 26, 26, 0.08)",
    "shadow_strong": "rgba(26, 26, 26, 0.12)",

    # Semantic — 语义色
    "success": "#5B8B6E",            # 成功 — muted green
    "warning": "#C9A66B",            # 警告 — muted amber
    "error": "#C73E3A",              # 错误 — vermilion
    "info": "#5B7A9B",               # 信息 — muted blue
}

WASHI_COLORS_DARK = {
    # Foundation — 深色纸张
    "paper_primary": "#1A1816",      # 主纸色 — dark warm brown-black
    "paper_secondary": "#24201C",    # 次纸色 — slightly lighter
    "paper_elevated": "#2C2824",     # 浮起纸色 — elevated surface

    # Typography — 深色文字
    "ink_primary": "#F5F0EB",        # 主墨色 — off-white
    "ink_secondary": "#C4BEB8",      # 次墨色 — light gray
    "ink_tertiary": "#8B8680",       # 三级墨色 — medium gray
    "ink_faint": "#4A4642",          # 淡墨色 — dark gray

    # Accent — 深色朱色
    "vermilion": "#E86864",          # 朱砂 — brighter vermilion for dark
    "vermilion_soft": "#F0A09A",     # 柔朱
    "vermilion_pale": "#3D2F2F",     # 淡朱 — dark vermilion background

    # Nature — 深色自然
    "indigo": "#7BA3D1",             # 靛蓝 — lighter blue
    "matcha": "#9DB494",             # 抹茶 — lighter green
    "gold": "#D4B89E",               # 金色 — lighter gold

    # Structural — 深色结构
    "border_subtle": "rgba(245, 240, 235, 0.08)",
    "border_medium": "rgba(245, 240, 235, 0.12)",
    "border_strong": "rgba(245, 240, 235, 0.18)",

    "shadow_soft": "rgba(0, 0, 0, 0.20)",
    "shadow_medium": "rgba(0, 0, 0, 0.30)",
    "shadow_strong": "rgba(0, 0, 0, 0.40)",

    # Semantic — 深色语义
    "success": "#9DB494",
    "warning": "#D4B89E",
    "error": "#E86864",
    "info": "#7BA3D1",
}

# ═══════════════════════════════════════════════════════════════════════════════
#   CSS STYLESHEETS — 样式表
# ═══════════════════════════════════════════════════════════════════════════════

def _get_menu_bar_css(colors: Dict[str, str]) -> str:
    return f"""
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   MENU BAR — 菜单栏
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QMenuBar {{
    background: {colors['paper_primary']};
    border: none;
    border-bottom: 1px solid {colors['border_subtle']};
    padding: 0;
    spacing: 4px;
}}

QMenuBar::item {{
    background: transparent;
    color: {colors['ink_secondary']};
    padding: 10px 14px;
    border-radius: 4px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.02em;
}}

QMenuBar::item:hover {{
    background: {colors['paper_secondary']};
    color: {colors['ink_primary']};
}}

QMenuBar::item:selected {{
    background: {colors['vermilion_pale']};
    color: {colors['vermilion']};
}}

QMenuBar::item:pressed {{
    background: {colors['vermilion_pale']};
    color: {colors['vermilion']};
}}
"""

def _get_menu_dropdown_css(colors: Dict[str, str]) -> str:
    return f"""
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   MENU DROPDOWN — 下拉菜单
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QMenu {{
    background: {colors['paper_elevated']};
    border: 1px solid {colors['border_medium']};
    border-radius: 8px;
    padding: 6px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
}}

QMenu::item {{
    padding: 8px 24px 8px 12px;
    border-radius: 4px;
    margin: 2px;
    color: {colors['ink_secondary']};
}}

QMenu::item:selected {{
    background: {colors['vermilion_pale']};
    color: {colors['vermilion']};
}}

QMenu::item:checked {{
    background: {colors['vermilion_pale']};
    color: {colors['vermilion']};
}}

QMenu::separator {{
    height: 1px;
    background: {colors['border_subtle']};
    margin: 6px 10px;
}}

QMenu::indicator {{
    width: 16px;
    height: 16px;
    left: 8px;
}}
"""

def _get_global_css(colors: Dict[str, str]) -> str:
    return f"""
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   GLOBAL STYLES — 全局样式
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QWidget {{
    background: {colors['paper_primary']};
    color: {colors['ink_primary']};
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 13px;
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   BUTTONS — 按钮
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QPushButton {{
    background: {colors['paper_elevated']};
    color: {colors['ink_primary']};
    border: 1px solid {colors['border_medium']};
    border-radius: 6px;
    padding: 8px 18px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.02em;
}}

QPushButton:hover {{
    background: {colors['vermilion']};
    color: #FFFFFF;
    border-color: {colors['vermilion']};
}}

QPushButton:pressed {{
    background: {colors['vermilion']};
    color: #FFFFFF;
    padding: 7px 17px;
}}

QPushButton:default {{
    background: {colors['vermilion']};
    color: #FFFFFF;
    border: none;
}}

QPushButton:default:hover {{
    background: {colors['vermilion_soft']};
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   INPUT FIELDS — 输入框
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QLineEdit, QTextEdit, QPlainTextEdit {{
    background: {colors['paper_elevated']};
    color: {colors['ink_primary']};
    border: 1px solid {colors['border_medium']};
    border-radius: 6px;
    padding: 10px 14px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 13px;
    selection-background-color: {colors['vermilion']};
    selection-color: #FFFFFF;
}}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
    border-color: {colors['vermilion']};
    background: {colors['paper_primary']};
}}

QLineEdit:hover, QTextEdit:hover, QPlainTextEdit:hover {{
    border-color: {colors['border_strong']};
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SCROLLBARS — 滚动条
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QScrollBar:vertical {{
    border: none;
    background: transparent;
    width: 8px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background: {colors['ink_faint']};
    border-radius: 4px;
    min-height: 32px;
}}

QScrollBar::handle:vertical:hover {{
    background: {colors['ink_tertiary']};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}

QScrollBar:horizontal {{
    border: none;
    background: transparent;
    height: 8px;
    margin: 0;
}}

QScrollBar::handle:horizontal {{
    background: {colors['ink_faint']};
    border-radius: 4px;
    min-width: 32px;
}}

QScrollBar::handle:horizontal:hover {{
    background: {colors['ink_tertiary']};
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   COMBO BOX — 下拉框
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QComboBox {{
    background: {colors['paper_elevated']};
    color: {colors['ink_primary']};
    border: 1px solid {colors['border_medium']};
    border-radius: 6px;
    padding: 8px 32px 8px 12px;
    min-width: 100px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
}}

QComboBox:hover {{
    border-color: {colors['vermilion']};
}}

QComboBox::drop-down {{
    border: none;
    width: 28px;
}}

QComboBox::down-arrow {{
    image: none;
    border: 2px solid {colors['ink_tertiary']};
    border-top: none;
    border-right: none;
    width: 5px;
    height: 5px;
    margin-right: 10px;
}}

QComboBox QAbstractItemView {{
    background: {colors['paper_elevated']};
    border: 1px solid {colors['border_medium']};
    border-radius: 6px;
    selection-background-color: {colors['vermilion_pale']};
    selection-color: {colors['vermilion']};
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SLIDER — 滑块
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QSlider::groove:horizontal {{
    border: none;
    height: 3px;
    background: {colors['border_medium']};
    border-radius: 2px;
}}

QSlider::handle:horizontal {{
    background: {colors['paper_elevated']};
    border: 2px solid {colors['vermilion']};
    width: 14px;
    height: 14px;
    margin: -6px 0;
    border-radius: 7px;
}}

QSlider::handle:horizontal:hover {{
    background: {colors['vermilion']};
    border-color: {colors['vermilion']};
}}

QSlider::sub-page:horizontal {{
    background: {colors['vermilion']};
    border-radius: 2px;
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CHECKBOX — 复选框
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QCheckBox {{
    spacing: 10px;
    color: {colors['ink_primary']};
}}

QCheckBox::indicator {{
    width: 18px;
    height: 18px;
    border: 2px solid {colors['border_medium']};
    border-radius: 4px;
    background: {colors['paper_elevated']};
}}

QCheckBox::indicator:hover {{
    border-color: {colors['vermilion']};
}}

QCheckBox::indicator:checked {{
    background: {colors['vermilion']};
    border-color: {colors['vermilion']};
}}

QCheckBox::indicator:checked::after {{
    content: "✓";
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   TABS — 标签页
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QTabWidget::pane {{
    border: none;
    background: {colors['paper_primary']};
}}

QTabBar::tab {{
    background: transparent;
    color: {colors['ink_tertiary']};
    padding: 10px 20px;
    border: none;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
    font-weight: 500;
}}

QTabBar::tab:selected {{
    color: {colors['vermilion']};
}}

QTabBar::tab:hover {{
    color: {colors['ink_primary']};
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   FRAMES & GROUPS — 框架与分组
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QFrame {{
    border: 1px solid {colors['border_subtle']};
    border-radius: 8px;
    background: {colors['paper_secondary']};
}}

QGroupBox {{
    border: 1px solid {colors['border_subtle']};
    border-radius: 8px;
    background: {colors['paper_secondary']};
    padding: 16px;
    font-family: "Inter", -apple-system, sans-serif;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 4px 10px;
    color: {colors['ink_secondary']};
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   TOOLTIP — 工具提示
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

QToolTip {{
    background: {colors['ink_primary']};
    color: {colors['paper_primary']};
    border: none;
    border-radius: 4px;
    padding: 6px 10px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 11px;
}}
"""

def _get_web_css(colors: Dict[str, str]) -> str:
    return f"""
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   WASHI WEB STYLES — 网页样式
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Noto+Serif+JP:wght@400;500;600;700&display=swap');

:root {{
    --washi-paper-primary: {colors['paper_primary']};
    --washi-paper-secondary: {colors['paper_secondary']};
    --washi-paper-elevated: {colors['paper_elevated']};
    --washi-ink-primary: {colors['ink_primary']};
    --washi-ink-secondary: {colors['ink_secondary']};
    --washi-ink-tertiary: {colors['ink_tertiary']};
    --washi-vermilion: {colors['vermilion']};
    --washi-vermilion-soft: {colors['vermilion_soft']};
    --washi-vermilion-pale: {colors['vermilion_pale']};
    --washi-border-subtle: {colors['border_subtle']};
    --washi-border-medium: {colors['border_medium']};
    --washi-shadow-soft: {colors['shadow_soft']};
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   BASE — 基础样式
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

* {{
    box-sizing: border-box;
}}

html, body {{
    font-family: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: var(--washi-ink-primary);
    background: var(--washi-paper-primary);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   TYPOGRAPHY — 排印
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

h1, h2, h3, h4, h5, h6 {{
    font-family: "Noto Serif JP", serif;
    font-weight: 600;
    letter-spacing: -0.02em;
    color: var(--washi-ink-primary);
    margin-top: 0;
}}

h1 {{ font-size: 32px; line-height: 1.2; }}
h2 {{ font-size: 24px; line-height: 1.3; }}
h3 {{ font-size: 20px; line-height: 1.4; }}
h4 {{ font-size: 16px; line-height: 1.4; }}

p {{
    margin-bottom: 1em;
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   BUTTONS — 按钮
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

button, .button, input[type="button"], input[type="submit"] {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: var(--washi-paper-elevated);
    color: var(--washi-ink-primary);
    border: 1px solid var(--washi-border-medium);
    border-radius: 6px;
    padding: 10px 20px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.02em;
    cursor: pointer;
    transition: all 0.15s ease;
}}

button:hover, .button:hover {{
    background: var(--washi-vermilion);
    color: #ffffff;
    border-color: var(--washi-vermilion);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px var(--washi-shadow-soft);
}}

button:active, .button:active {{
    transform: translateY(0);
}}

button.primary, .button.primary {{
    background: var(--washi-vermilion);
    color: #ffffff;
    border-color: var(--washi-vermilion);
}}

button.primary:hover, .button.primary:hover {{
    background: var(--washi-vermilion-soft);
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   INPUT FIELDS — 输入框
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

input[type="text"], input[type="search"], input[type="email"],
input[type="password"], input[type="number"], textarea, select {{
    width: 100%;
    background: var(--washi-paper-elevated);
    color: var(--washi-ink-primary);
    border: 1px solid var(--washi-border-medium);
    border-radius: 6px;
    padding: 10px 14px;
    font-family: "Inter", -apple-system, sans-serif;
    font-size: 13px;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
}}

input:focus, textarea:focus, select:focus {{
    outline: none;
    border-color: var(--washi-vermilion);
    box-shadow: 0 0 0 3px var(--washi-vermilion-pale);
}}

input:hover, textarea:hover, select:hover {{
    border-color: var(--washi-border-medium);
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CARDS — 卡片
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.card, .cardBody {{
    background: var(--washi-paper-elevated);
    border: 1px solid var(--washi-border-subtle);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 1px 3px var(--washi-shadow-soft);
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   LINKS — 链接
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

a, a:link, a:visited {{
    color: var(--washi-vermilion);
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.15s ease;
}}

a:hover {{
    border-bottom-color: var(--washi-vermilion);
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   NIGHT MODE — 夜间模式覆盖
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.night_mode, .nightMode {{
    background: var(--washi-paper-primary);
    color: var(--washi-ink-primary);
}}

.night_mode .card, .nightMode .card,
.night_mode .cardBody, .nightMode .cardBody {{
    background: var(--washi-paper-secondary);
    border-color: var(--washi-border-subtle);
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   UTILITY CLASSES — 工具类
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

.washi-text-display {{
    font-family: "Noto Serif JP", serif;
}}

.washi-text-muted {{
    color: var(--washi-ink-tertiary);
}}

.washi-bg-vermilion {{
    background: var(--washi-vermilion);
    color: #ffffff;
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ANIMATIONS — 动画
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

@keyframes washi-fade-in {{
    from {{
        opacity: 0;
        transform: translateY(8px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.washi-fade-in {{
    animation: washi-fade-in 0.3s ease forwards;
}}
"""

# ═══════════════════════════════════════════════════════════════════════════════
#   THEME MANAGER — 主题管理器
# ═══════════════════════════════════════════════════════════════════════════════

class WashiThemeManager:
    """和纸主题管理器"""

    # CSS cache for performance optimization
    _css_cache_light = None
    _css_cache_dark = None
    _global_css_cache_light = None
    _global_css_cache_dark = None
    _web_css_cache_light = None
    _web_css_cache_dark = None

    def __init__(self):
        self.styled_widgets = []
        self.webviews = []
        self._current_is_dark = None

    def _invalidate_css_cache(self) -> None:
        """清除CSS缓存（当主题切换时调用）"""
        self._css_cache_light = None
        _css_cache_dark = None
        self._global_css_cache_light = None
        self._global_css_cache_dark = None
        self._web_css_cache_light = None
        self._web_css_cache_dark = None

    def _get_cached_css(self, cache_attr: str, colors: Dict[str, str], css_generator_func) -> str:
        """获取缓存的CSS或生成新的CSS"""
        cache_value = getattr(self, cache_attr)
        if cache_value is not None:
            return cache_value

        # 生成并缓存CSS
        css = css_generator_func(colors)
        setattr(self, cache_attr, css)
        return css

    @property
    def is_dark(self) -> bool:
        current_dark = theme_manager.night_mode
        # 检测主题切换并清除缓存
        if self._current_is_dark != current_dark:
            self._current_is_dark = current_dark
            self._invalidate_css_cache()
        return current_dark

    @property
    def is_dark(self) -> bool:
        return theme_manager.night_mode

    @property
    def colors(self) -> Dict[str, str]:
        """获取当前主题颜色"""
        return WASHI_COLORS_DARK if self.is_dark else WASHI_COLORS_LIGHT

    def _is_widget_valid(self, widget: QWidget) -> bool:
        """检查组件是否仍然有效"""
        try:
            return widget is not None and not sip.isdeleted(widget)
        except Exception:
            return False

    def apply_stylesheet(self, widget: QWidget, css: str) -> None:
        """应用样式表到组件"""
        if self._is_widget_valid(widget):
            try:
                widget.setStyleSheet(css)
            except RuntimeError:
                pass  # Widget was deleted

    def style_menubar(self, menubar: QMenuBar) -> None:
        """样式化菜单栏"""
        css = _get_menu_bar_css(self.colors)
        self.apply_stylesheet(menubar, css)
        menubar.setMaximumHeight(36)

    def style_menu(self, menu: QMenu) -> None:
        """样式化下拉菜单"""
        css = _get_menu_dropdown_css(self.colors)
        self.apply_stylesheet(menu, css)

    def style_widget(self, widget: QWidget) -> None:
        """样式化组件"""
        if widget not in self.styled_widgets:
            self.styled_widgets.append(widget)
        css = _get_global_css(self.colors)
        self.apply_stylesheet(widget, css)

    def refresh_all(self) -> None:
        """刷新所有样式"""
        # 清理已删除的组件
        self.styled_widgets = [w for w in self.styled_widgets if self._is_widget_valid(w)]

        for widget in self.styled_widgets:
            self.style_widget(widget)

        if mw and hasattr(mw, 'form') and hasattr(mw.form, 'menubar'):
            self.style_menubar(mw.form.menubar)

# ═══════════════════════════════════════════════════════════════════════════════
#   WEB VIEW STYLING — 网页视图样式
# ═══════════════════════════════════════════════════════════════════════════════

def inject_washi_styles(web_content: aqt.webview.WebContent, context: Optional[object]) -> None:
    """注入和纸样式到网页（使用缓存优化）"""
    colors = theme_manager_instance.colors
    is_dark = theme_manager_instance.is_dark
    cache_attr = '_web_css_cache_dark' if is_dark else '_web_css_cache_light'

    # 使用缓存的CSS
    css = theme_manager_instance._get_cached_css(
        cache_attr, colors, _get_web_css
    )

    styles = f'''
    <style id="washi-theme">
        {css}
    </style>
    '''

    if hasattr(web_content, 'head'):
        web_content.head += styles

def update_webview_styles(webview: AnkiWebView) -> None:
    """更新网页视图样式（使用缓存优化）"""
    colors = theme_manager_instance.colors
    is_dark = theme_manager_instance.is_dark
    cache_attr = '_web_css_cache_dark' if is_dark else '_web_css_cache_light'

    # 使用缓存的CSS
    css = theme_manager_instance._get_cached_css(
        cache_attr, colors, _get_web_css
    )

    js = f'''
    (() => {{
        let style = document.getElementById('washi-theme');
        if (!style) {{
            style = document.createElement('style');
            style.id = 'washi-theme';
            document.head.appendChild(style);
        }}
        style.innerHTML = `{css}`;
    }})()
    '''

    try:
        webview.eval(js)
    except Exception:
        pass

# ═══════════════════════════════════════════════════════════════════════════════
#   EVENT HANDLERS — 事件处理器
# ═══════════════════════════════════════════════════════════════════════════════

def on_theme_did_change() -> None:
    """主题切换事件"""
    theme_manager_instance.refresh_all()

def on_webview_did_inject_styles(webview: AnkiWebView) -> None:
    """网页样式注入完成事件"""
    update_webview_styles(webview)

def style_dialog_widgets() -> None:
    """样式化对话框组件"""
    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, QMenu) and widget.parent():
            theme_manager_instance.style_menu(widget)
        elif widget.isWindow() and not isinstance(widget, QMenuBar):
            theme_manager_instance.style_widget(widget)

# ═══════════════════════════════════════════════════════════════════════════════
#   INITIALIZATION — 初始化
# ═══════════════════════════════════════════════════════════════════════════════

theme_manager_instance = WashiThemeManager()

if mw:
    # 样式化主窗口
    if hasattr(mw, 'form') and hasattr(mw.form, 'menubar'):
        theme_manager_instance.style_menubar(mw.form.menubar)
    theme_manager_instance.style_widget(mw)

    # 注册钩子
    gui_hooks.webview_will_set_content.append(inject_washi_styles)
    gui_hooks.webview_did_inject_style_into_page.append(on_webview_did_inject_styles)
    gui_hooks.theme_did_change.append(on_theme_did_change)

    # 定时样式化对话框
    style_timer = QTimer()
    if qtmajor > 5:
        style_timer.timeout.connect(style_dialog_widgets)
        style_timer.start(2500)

# ═══════════════════════════════════════════════════════════════════════════════
#   PUBLIC API — 公共接口
# ═══════════════════════════════════════════════════════════════════════════════

def apply_style(widget: QWidget) -> None:
    """应用和纸主题到指定组件"""
    theme_manager_instance.style_widget(widget)

def refresh_theme() -> None:
    """刷新主题"""
    theme_manager_instance.refresh_all()

def get_colors() -> Dict[str, str]:
    """获取当前主题颜色"""
    return theme_manager_instance.colors

__all__ = ['apply_style', 'refresh_theme', 'get_colors', 'WashiThemeManager']
