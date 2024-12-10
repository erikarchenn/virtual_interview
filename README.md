# virtual_interview
<!-- INTRODUCTION -->
## Introduction
For our CS 366 final project, we developed an AI chatbot to understand the effects of gender presentation in these voice interfaces (VUI's) and how they impact participant performance in mock job interviews. To utilize the AI interviewer as a practice tool, you must click on the microphone icon in the interface to begin conversing, and clicking once more to finish up what you have to say. You must introduce yourself initially as "Alex," a gender-neutral persona to prevent any gender bias. 

## Running this Interface on your Device
To utilize this interface, you must download the code in this repository (works regardless of the device OS) and run the code on your IDE of choice (ex. VS Code).
You must download all three files: `app.py` , `requirements.txt` , and `utils.py` . All 3 are necessary to run the code successfully on your device.

## Installation
Below you will find instructions on how to fire up the virtual mock interview.
1. To preface, the male voice is named "onyx" where the female voice is named "nova," this is critical information if you choose to utilize this interface to practice interviewing.
   This can be changed in line 35 of `utils.py` as shown in this line:
   ```sh
   voice="nova",
   ```
2. If you decide to keep or change the voice, it is totally up to you! You must run `utils.py` first to initialize all starting data and information. Furthermore, you can now run `app.py` to fire up the program.
   
3. Initially, you will see this when you first run it in the terminal:
```sh
 streamlit run /Users/erikachen/Downloads/CS366/app.py [ARGUMENTS]
2024-12-10 17:46:30.052 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Session state does not function when running a script without `streamlit run`
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.053 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-12-10 17:46:30.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
```
Once you see this, copy and paste the arguments as shown above on your screen with your information into the terminal and run it. The program should fire up on your browser.

4. To begin the interview, you must click on the microphone (be sure that it has been enabled) to introduce yourself to the virtual interviewer. Please click on the microphone to stop talking and allow the program to process what has been said. The interviewer will respond and you can begin your virtual interview as questions follow. There are 7 questions that will be asked in the interview.

5. As you progress, the interviewer will provide feedback and respond to what you have said, and bid you farewell as you complete the interview. 
