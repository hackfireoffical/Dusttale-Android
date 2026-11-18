# Android native chart compatibility patch

The upstream Kade-derived engine gates Lua modcharts to Windows and does not bundle its LuaJIT runtime for Android. This patch ports the non-empty built-in chart motion scripts for **Hallucinations**, **Reality Check**, and **Last Hope** to Haxe for Android. It does not enable arbitrary Lua scripts or claim complete modchart parity.

The patch is applied to a fresh upstream checkout by `scripts/apply-android-patches.py` during the GitHub Actions build. The chart animations still need in-game visual/timing verification on an Android device.
