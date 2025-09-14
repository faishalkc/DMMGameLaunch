# 🎮 DMM Game Launch

This lightweight program lets you run DMM games directly from **Steam** (or maybe another case). Simply by passing a DMM game ID to `dmmgameplayer://` protocol using the official **DMM Game Player**.

---

## 📥 Download

🔗 [**Download the latest release**](https://github.com/faishalkc/DMMGameLaunch/releases)

Extract the archive file and look for `DMMGameLaunch.exe`.

---

## 🚀 How to Use on Steam

### 1. Get Your DMM Game ID

Every DMM game has a unique ID. You can find it by:

- Checking the launch link from DMM Game Player or site
- Example:  
`dmmgameplayer://play/GCL/umamusume/cl/win`
→ **Game ID is `umamusume`**

---

### 2. Add the Launcher to Steam

1. Open **Steam**
2. Go to `Games` > `Add a Non-Steam Game to My Library`
3. Click `Browse` and select the downloaded `DMMGameLaunch.exe`
4. After adding it, right-click the game in your library → `Properties`
5. Under **Launch Options**, add the following:
`-game umamusume`

Replace `umamusume` with the game ID you want to launch

6. Rename the shortcut to match your game’s title

---

### ✅ How to Use on Command Prompt

```cmd
"C:\Tools\DMMGameLaunch.exe" -game umamusume

This will launch:
dmmgameplayer://play/GCL/umamusume/cl/win
