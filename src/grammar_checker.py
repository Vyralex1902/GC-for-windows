import keyboard
import pyperclip
import time
import language_tool_python

tool = language_tool_python.LanguageTool(
    "en-US"
)  # I choose American English, you can make it a global var.


def check_and_replace_text():  # Takes effect on any selected text
    """
    This function copies the currently selected text,
    checks its grammar, and replaces it with the corrected text.
    """
    # Simulate "Ctrl+C" to copy selected text.
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.5)  # Small delay to allow the clipboard to update

    original_text = pyperclip.paste()

    if not original_text:
        print("No text found in clipboard.")
        return

    # Get corrected text using LanguageTool
    corrected_text = tool.correct(original_text)

    if corrected_text and corrected_text != original_text:
        pyperclip.copy(corrected_text)
        # Simulate "Ctrl+V" to paste the corrected text.
        keyboard.press_and_release("ctrl+v")
        print("Text replaced with corrected version.")
    else:
        print("No corrections needed.")


def main():
    print(
        "Grammar Checker running. Press Ctrl+Alt+G to check and correct selected text."
    )
    keyboard.add_hotkey("ctrl+alt+g", check_and_replace_text)
    # Keep the script running until the user presses Esc.
    keyboard.wait("esc")


if __name__ == "__main__":
    main()
