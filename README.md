# 🎮 DMM Game Launcher for Steam (EXE Version)

This lightweight launcher lets you run DMM games directly from **Steam**, enabling:

- ✅ Steam Overlay support
- ✅ Controller support via Steam Input
- ✅ Playtime tracking
- ✅ Cleaner library organization

You simply pass a DMM game ID to the launcher, and it opens the game via `dmmgameplayer://` protocol using the official **DMM Game Player**.

> ✅ A standalone **.exe version** is available — no Python installation required.

---

## 📥 Download

🔗 [**Download the latest release**](https://github.com/yourusername/yourrepo/releases)

Look for `launch_dmm_game.exe` under **Assets**.

---

## 🚀 How to Use

### 1. Get Your DMM Game ID

Every DMM game has a unique ID. You can find it by:

- Checking the launch link from DMM Game Player or site
- Example:  
dmmgameplayer://play/GCL/851539/cl/win
→ **Game ID is `851539`**

---

### 2. Add the Launcher to Steam

1. Open **Steam**
2. Go to `Games` > `Add a Non-Steam Game to My Library`
3. Click `Browse` and select the downloaded `launch_dmm_game.exe`
4. After adding it, right-click the game in your library → `Properties`
5. Under **Launch Options**, add the following:
-game 851539

Replace `851539` with the game ID you want to launch

6. Rename the shortcut to match your game’s title

---

### ✅ Example

```bash
"C:\Tools\launch_dmm_game.exe" -game 851539

This will launch:
dmmgameplayer://play/GCL/851539/cl/win
