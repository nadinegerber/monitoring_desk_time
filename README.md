# Chrono-Health & Focus Monitor

A minimalist, lightweight terminal-based background automation tool engineered to protect developers from digital eye strain and prolonged sedentary behavior. This utility implements a multi-sensory notification system, combining local audio text-to-speech instructions with native visual system desktop dialog prompts.

## Features
- **Zero-CPU Standby Footprint:** Utilizes operating system kernel-level thread scheduling (`time.sleep`) instead of continuous active polling loops to preserve machine battery lifespan.
- **20-20-20 Rule Enforcement:** Automatically triggers visual and vocal reminders every 20 minutes to reduce eye muscle fatigue.
- **Randomized Ergonomic Assignments:** Keeps wellness breaks unpredictable and engaging by drawing physical stretches randomly from a customizable runtime matrix.
- **Blocking Modal User Interface:** Deploys native system-level alert dialog windows that remain pinned to the foreground until manually dismissed by clicking "OK".

---

## Technical Architecture & Requirements

This core repository branch is engineered natively for **macOS** environments and requires no third-party library dependencies out of the box.

- **Audio Subsystem:** Invokes the native macOS Unix speech synthesis binary `say`.
- **User Interface Subsystem:** Deploys AppleScript modal popups via the native `osascript` wrapper.

---

## Cross-Platform Porting (Windows Implementation Guide)

Because the default execution engine relies directly on underlying macOS operating system binaries, Windows users will experience a runtime error out of the box. To adapt this project to run seamlessly on a Windows architecture, follow these two porting steps:

### 1. Install Cross-Platform Dependencies
Open your command prompt or terminal environment and install the required speech and notification packages via `pip`:
```bash
pip install pyttsx3 win10toast
```

### 2. Replace the `trigger_alert` Function Block
Open `monitor.py` in your text editor (e.g., Sublime Text), locate the `trigger_alert` function block, and replace it entirely with the following Windows-compatible wrapper code:

```python
def trigger_alert(display_message, speech_text, alert_title):
    """
    Windows-specific cross-platform notification override.
    Utilizes pyttsx3 for localized audio synthesis and win10toast for system notifications.
    """
    # Import modules internally to prevent system dependency crashes on alternate OS platforms
    import pyttsx3
    from win10toast import ToastNotifier

    # 1. Initialize and execute text-to-speech engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)  # Set speech tempo to 145 words-per-minute
    engine.say(speech_text)
    engine.runAndWait()
    
    # 2. Deploy native Windows desktop notification toast banner
    toaster = ToastNotifier()
    toaster.show_toast(
        alert_title,
        display_message,
        duration=10,      # Number of seconds the alert banner stays pinned to screen
        threaded=False    # Keeps application execution blocked until manually dismissed
    )
```

---

## Configuration & Local Deployment

### 1. Customization
- **Clone or download** the script file inside your chosen local workspace folder directory.
- **Open `monitor.py`** with any raw text editor to easily customize variables (`EYE_BREAK_INTERVAL`, `CHAIR_BREAK_INTERVAL`, or specific text strings within `MOVEMENT_TASKS`).

### 2. Execution Runpath
To boot up the monitoring engine workspace environment, open your terminal directory and execute:
```bash
python3 monitor.py
```

### 3. Graceful Termination
To halt background loop operations at any point during active workspace production sessions, send a standard keyboard interrupt command sequence: `Ctrl+C`.