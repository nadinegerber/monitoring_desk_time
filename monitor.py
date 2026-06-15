import os
import time
import random

# =====================================================================
# --- USER CONFIGURATION PANEL ---
# Feel free to adjust these intervals (in minutes) to suit your workflow.
# =====================================================================
EYE_BREAK_INTERVAL = 20
CHAIR_BREAK_INTERVAL = 45

# --- SYSTEM LANGUAGE PROFILE CONFIGURATION ---
# Change this string variable to match any voice installed on your system.
# On macOS, examples include "Thomas" (French), "Alex" (English), etc.
SYSTEM_VOICE = "Alex"

# --- RANDOMIZED MOVEMENT PHRASES ---
# Pair your custom spoken phrases with their visual popup box text descriptions.
# Format: ("Audio Spoken Phrase", "Visual Pop-up Screen Text")
MOVEMENT_TASKS = [
    ("Please stand up and stretch your arms toward the ceiling.", "Stand up and stretch your arms toward the ceiling!"),
    ("Time to go drink a glass of water.", "Go drink a glass of water."),
    ("Please do ten gentle torso twists.", "Do 10 gentle torso twists."),
    ("Walk to the window and look outside for a bit.", "Walk to the window and look outside."),
    ("Roll your shoulders backward five times.", "Roll your shoulders backward 5 times."),
    ("Perform five bodyweight squats to get blood flowing.", "Do 5 bodyweight squats.")
]

def trigger_alert(display_message, speech_text, alert_title):
    """
    Handles the multi-sensory fallback alerting mechanism.
    First triggers local text-to-speech engine, then deploys a blocking system dialog.
    NOTE: This implementation uses native macOS command utilities ('say' and 'osascript').
    """
    # 1. Audio Notification via Terminal Text-to-Speech Engine
    # Adjust speech rate (-r) or system voice (-v) to customize performance
    os.system(f'say -r 170 -v {SYSTEM_VOICE} "{speech_text}"')
    
    # 2. Visual Blocking Notification (Native macOS System Dialog Box)
    escaped_message = display_message.replace('"', '\\"')
    command = f'display dialog "{escaped_message}" with title "{alert_title}" buttons {{"OK"}} default button "OK" with icon caution'
    os.system(f"osascript -e '{command}'")

def main():
    # Print the terminal interface layout on application initialization
    print("==================================================")
    print("         CHRONO-HEALTH & FOCUS MONITOR             ")
    print("==================================================")
    print(f"[*] Eye Strain Rule: Active every {EYE_BREAK_INTERVAL} minutes.")
    print(f"[*] Physical Movement: Active every {CHAIR_BREAK_INTERVAL} minutes.")
    print("[*] Status: Running silently in background...")
    print("[*] To STOP tracking, press Ctrl+C or close this window.")
    print("==================================================")
    
    # Initialize session tracking variable runtime counter
    elapsed_time = 0
    
    try:
        while True:
            # Thread sleep execution for 60 seconds (utilizes 0% CPU overhead while waiting)
            time.sleep(60)
            elapsed_time += 1
            
            print(f" -> Session runtime: {elapsed_time} min")
            
            # --- EYE STRAIN CHECK ---
            if elapsed_time % EYE_BREAK_INTERVAL == 0:
                print("\n[!] Triggering Eye Break Alert...")
                audio_phrase = "Attention. Look at something far away for twenty seconds."
                box_message = "20-20-20 Rule:\nLook at something 20 feet away for at least 20 seconds to relax your eye muscles."
                
                trigger_alert(box_message, audio_phrase, "Eye Strain Break!")
                print("[+] Eye break dismissed. Resuming timer.\n")
                
            # --- CHAIR MOVEMENT CHECK ---
            if elapsed_time % CHAIR_BREAK_INTERVAL == 0:
                print("\n[!] Triggering Physical Movement Alert...")
                # Fetch a randomized movement task tuple from the configuration list
                audio_instruction, visual_instruction = random.choice(MOVEMENT_TASKS)
                
                box_message = f"Time to get out of your chair!\n\nYour assignment:\n{visual_instruction}"
                
                trigger_alert(box_message, audio_instruction, "Get Up & Move!")
                print("[+] Movement break dismissed. Resuming timer.\n")

    except KeyboardInterrupt:
        # Catch termination shortcut command (Ctrl+C) for an elegant closure layout
        print("\n==================================================")
        print("     MONITOR TERMINATED BY USER. STAY HEALTHY!     ")
        print("==================================================\n")

if __name__ == "__main__":
    main()