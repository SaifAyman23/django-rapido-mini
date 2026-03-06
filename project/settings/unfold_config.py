# settings.py - Updated with Django 6.0 Theme for django-unfold
# Dark Mode Only - Production Ready Configuration

from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

######################################################################
# Unfold
######################################################################
UNFOLD = {
    "SITE_TITLE": _("Django Rapido MINI"),
    "SITE_HEADER": _("Django Rapido MINI"),
    "SITE_SUBHEADER": _("Lightweight Django template"),
    "SHOW_HISTORY": True,
    "SHOW_LANGUAGES": True,
    "LANGUAGE_FLAGS": {
        "ar": "sa",
        "en": "us",
    },
}
    "COLORS": {
        "base": {
            "50": "oklch(99% 0 0)",               # #fcfcfc - Pure white
            "100": "oklch(97% 0 0)",              # #f7f7f7 - Light neutral
            "200": "oklch(93% 0 0)",              # #ededed - Soft neutral
            "300": "oklch(85% 0 0)",              # #d9d9d9 - Medium neutral
            "400": "oklch(70% 0 0)",              # #b3b3b3 - Neutral gray
            "500": "oklch(55% 0 0)",              # #8c8c8c - Mid gray
            "600": "oklch(40% 0 0)",              # #666666 - Dark gray
            "700": "oklch(30% 0 0)",              # #4d4d4d - Darker gray
            "800": "oklch(20% 0 0)",              # #333333 - Deep gray
            "850": "oklch(15% 0 0)",              # #262626 - Almost black
            "900": "oklch(10% 0 0)",              # #1a1a1a - Near black
            "925": "oklch(7% 0 0)",               # #121212 - Darker black
            "950": "oklch(5% 0 0)",               # #0d0d0d - True black
            "975": "oklch(3% 0 0)"                # #080808 - Pure black
        },
        "primary": {
            "50": "oklch(97% 0.012 18)",          # #fff6f6 - Lightest red tint
            "100": "oklch(94% 0.028 18)",         # #ffe6e6 - Pale red
            "200": "oklch(88% 0.06 18)",          # #ffcccc - Soft red
            "300": "oklch(78% 0.12 18)",          # #ff9b9b - Light red
            "400": "oklch(68% 0.18 18)",          # #ff5e5e - Medium red
            "500": "oklch(56.5% 0.22 18)",        # #db2525 - Target red
            "600": "oklch(48% 0.21 18)",          # #b81f1f - Deep red
            "700": "oklch(40% 0.19 18)",          # #991919 - Dark red
            "800": "oklch(32% 0.16 18)",          # #7a1414 - Darker red
            "900": "oklch(24% 0.12 18)",          # #5c0f0f - Blood red
            "950": "oklch(16% 0.08 18)"           # #3d0a0a - Almost black red
        },
        "font": {
            "subtle-light": "var(--color-base-500)",      # #8c8c8c - Mid gray
            "subtle-dark": "var(--color-base-400)",       # #b3b3b3 - Neutral gray
            "default-light": "var(--color-base-900)",     # #1a1a1a - Near black
            "default-dark": "var(--color-base-100)",      # #f7f7f7 - Light neutral
            "important-light": "var(--color-base-950)",   # #0d0d0d - True black
            "important-dark": "var(--color-base-50)"      # #fcfcfc - Pure white
        },
        "semantic": {
            "accent": "var(--color-primary-500)",         # #db2525 - Target red
            "accent-light": "var(--color-primary-300)",   # #ff9b9b - Light red
            "accent-dark": "var(--color-primary-700)",    # #991919 - Dark red
            "accent-bright": "oklch(65% 0.25 18)",        # #ff4545 - Bright red
            "accent-dim": "oklch(56.5% 0.22 18 / 0.08)",  # #db2525 with 8% opacity
            "accent-glow": "oklch(56.5% 0.22 18 / 0.25)", # #db2525 with 25% opacity
            
            "blue": "oklch(55% 0.15 250)",                # #3a7eb0 - Tech blue
            "blue-light": "oklch(92% 0.02 250)",          # #e1ecf9 - Pale blue
            "blue-dim": "oklch(55% 0.15 250 / 0.12)",     # #3a7eb0 with 12% opacity
            
            "green": "oklch(55% 0.15 145)",               # #39a34a - Green
            "green-light": "oklch(92% 0.03 145)",         # #e6f9ea - Pale green
            "green-dim": "oklch(55% 0.15 145 / 0.12)",    # #39a34a with 12% opacity
            
            "amber": "oklch(70% 0.15 75)",                # #c98a2b - Warm amber
            "amber-light": "oklch(95% 0.03 75)",          # #fff1d6 - Pale amber
            "amber-dim": "oklch(70% 0.15 75 / 0.12)",     # #c98a2b with 12% opacity
            
            "red": "var(--color-primary-500)",            # #db2525 - Target red
            "red-light": "var(--color-primary-100)",      # #ffe6e6 - Pale red
            "red-dim": "var(--color-primary-500 / 0.12)", # #db2525 with 12% opacity
            
            "purple": "oklch(55% 0.15 290)",              # #7a5fb0 - Muted purple
            "purple-light": "oklch(95% 0.02 290)",        # #f0e8ff - Lavender
            "purple-dim": "oklch(55% 0.15 290 / 0.12)",   # #7a5fb0 with 12% opacity
            
            "electric": "oklch(75% 0.15 195)",            # #4dc9c9 - Electric teal
            "navy": "var(--color-base-900)",              # #1a1a1a - Near black
            "ink": "var(--color-base-950)"                # #0d0d0d - True black
        },
        "background": {
            "primary-light": "oklch(100% 0 0)",           # #ffffff - Pure white
            "primary-dark": "var(--color-base-950)",      # #0d0d0d - True black
            "secondary-light": "var(--color-base-50)",    # #fcfcfc - Pure white
            "secondary-dark": "var(--color-base-900)",    # #1a1a1a - Near black
            "tertiary-light": "var(--color-base-100)",    # #f7f7f7 - Light neutral
            "tertiary-dark": "var(--color-base-850)",     # #262626 - Almost black
            "elevated-light": "oklch(100% 0 0)",          # #ffffff - Pure white
            "elevated-dark": "var(--color-base-800)"      # #333333 - Deep gray
        },
        "border": {
            "light-light": "var(--color-base-200)",       # #ededed - Soft neutral
            "light-dark": "var(--color-base-700)",        # #4d4d4d - Darker gray
            "strong-light": "var(--color-base-400)",      # #b3b3b3 - Neutral gray
            "strong-dark": "var(--color-base-600)"        # #666666 - Dark gray
        },
        "text": {
            "primary-light": "var(--color-base-950)",     # #0d0d0d - True black
            "primary-dark": "var(--color-base-50)",       # #fcfcfc - Pure white
            "secondary-light": "var(--color-base-700)",   # #4d4d4d - Darker gray
            "secondary-dark": "var(--color-base-300)",    # #d9d9d9 - Medium neutral
            "tertiary-light": "var(--color-base-500)",    # #8c8c8c - Mid gray
            "tertiary-dark": "var(--color-base-400)",     # #b3b3b3 - Neutral gray
            "inverse-light": "oklch(100% 0 0)",           # #ffffff - Pure white
            "inverse-dark": "var(--color-base-950)"       # #0d0d0d - True black
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "command_search": True,
        "navigation": [
            {
                "title": _("Navigation"),
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": _("Users & Groups"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "account_circle",
                        "link": reverse_lazy("admin:common_customuser_changelist"),
                    },
                    {
                        "title": _("Admin Logs"),
                        "icon": "hourglass_bottom",
                        "link": reverse_lazy("admin:admin_logentry_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}

UNFOLD_STUDIO_ENABLE_CUSTOMIZER = True

UNFOLD_STUDIO_DEFAULT_FRAGMENT = "color-schemes"

UNFOLD_STUDIO_ENABLE_SAVE = False

UNFOLD_STUDIO_ENABLE_FILEUPLOAD = False

UNFOLD_STUDIO_ALWAYS_OPEN = True

UNFOLD_STUDIO_ENABLE_RESET_PASSWORD = True

