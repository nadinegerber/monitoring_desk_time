<img width="1424" height="752" alt="image_806437d1" src="https://github.com/user-attachments/assets/38a7dab2-d88d-4688-93bc-91b8b09a7166" />


### About This Program
# Python Ergonomic Assistant

An automated desktop utility designed to combat Digital Eye Strain and sedentary fatigue using structured break intervals....by being a minimalist, lightweight terminal-based background automation tool engineered to protect developers from digital eye strain and prolonged sedentary behavior. This utility implements a multi-sensory notification system, combining local audio text-to-speech instructions with native visual system desktop dialog prompts.


## Why This Tool is Necessary

Like many developers, I get so locked into coding that I forget to blink or stand up. To fix my own bad habits, I built a lightweight Python script that acts as an ergonomic guardian. It quietly triggers reminders every 20 minutes to rest your eyes and every 45 minutes to stretch. Check out the repository to see the clean code architecture and how you can run it on your own machine!

The Problem: 
Digital Eye Strain drops natural human blinking by 50%, leading to fatigue and reduced developer productivity.

Focusing on digital displays for extended periods leads to **Digital Eye Strain** (Computer Vision Syndrome) and physical fatigue. Because computer screens are made of thousands of tiny, shifting pixels rather than solid ink, they force our eyes to work much harder than a printed page. 


### 👁️ The Science Behind the 20-Minute Eye Break
* **Reduced Blink Rate:** Humans normally blink 15–17 times per minute. When staring at a screen, blinking drops by up to 50% (down to 3–7 times per minute), causing rapid tear evaporation, dryness, and irritation.
* **Incomplete Blinking:** Intense screen focus causes "partial blinks," where the eyelids fail to close completely, leaving the lower half of the eye exposed and dry.
* **Constant Micro-Focusing:** Because pixelated text has soft edges, the ciliary muscles in your eyes must constantly flex and refocus to keep the image sharp, leading to rapid muscle fatigue.
* **Muscular Lock:** Looking at close objects requires your inner eye muscles to contract heavily to pull your eyes inward. A 20-second break looking at something 20 feet away resets and relaxes these locked muscles.

### 🪑 The Science Behind the 45-Minute Desk Break
* **Postural Fatigue:** Sitting static locks your spine, hips, and neck into position, restricting blood flow and causing slouching.
* **Metabolic Slump:** Prolonged sitting slows down your metabolism and reduces your body's ability to regulate blood sugar and break down fats.
* **Circulation Reset:** Standing up every 45 minutes re-engages major muscle groups, triggers healthy blood circulation, and prevents long-term musculoskeletal stiffness.

This program automates the health intervals required to protect your body and vision based on how our biology reacts to screens. It is a lightweight Python background application automating healthy micro-break schedules.

## Program Features
- **Zero-CPU Standby Footprint:** Utilizes operating system kernel-level thread scheduling (`time.sleep`) instead of continuous active polling loops to preserve machine battery lifespan.
- **20-20-20 Rule Enforcement:** Automatically triggers visual and vocal reminders every 20 minutes to reduce eye muscle fatigue.
- **Randomized Ergonomic Assignments:** Keeps wellness breaks unpredictable and engaging by drawing physical stretches randomly from a customizable runtime matrix.
- **Blocking Modal User Interface:** Deploys native system-level alert dialog windows that remain pinned to the foreground until manually dismissed by clicking "OK".

---

## How It Works
The script runs as a continuous, silent background process directly within your workspace terminal. Every minute it checks session runtimes boundaries against configured parameters. When parameters match, it executes audio instructions followed by a blocking interface window.

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

You can easily adjust execution timing parameters and string targets by opening monitor.py in a raw text editor.
  
- **Open `monitor.py`** with any raw text editor to easily customize variables (`EYE_BREAK_INTERVAL`, `CHAIR_BREAK_INTERVAL`, or specific text strings within `MOVEMENT_TASKS`).

Modify EYE_BREAK_INTERVAL or CHAIR_BREAK_INTERVAL constants at the top of the file to change alert windows (measured in minutes).

Update the strings inside the MOVEMENT_TASKS multi-dimensional array to feature your own personalized stretch routines.


### 2. Execution Runpath
To boot up the monitoring engine workspace environment, open your terminal directory and execute:
```bash
python3 monitor.py
```

### 3. Graceful Termination
To halt background loop operations at any point during active workspace production sessions, send a standard keyboard interrupt command sequence: `Ctrl+C`.
