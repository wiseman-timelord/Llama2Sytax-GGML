# Llama2Syntax-GGML
Status: Working.
* The Llama2Syntax is a Python application designed to test 26 prompt formats with the Llama language model. It allows users to customize the test content, temperature, and context length for the model. The application log the model's responses, that can then be referenced against the inputs used in the input log, to find the optimal prompt(s) for your model, thus providing a comprehensive understanding of how the model interprets and responds to each. It's an essential tool for developers and researchers who are working with the Llama 2 model and want to understand its behavior better, especially for example, when a model card is missing details.
* This script may also be used as a dropin tool for my other program "Llama2Robot", and uses the same, model folders and log files, however, if you do this, then watch out you do not over-write the,  "requirements.txt" and "Win Install.bat", files.  

## Features
1. **User Customization:** Allows users to input or modify configurations like `TEST_CONTENT`, `TEMPERATURE`, and `CONTEXT_LENGTH`.
2. **Model Initialization:** Initializes the Llama model with the given configurations.
3. **Prompt Testing:** Tests various prompt formats to see how the model responds to each.
4. **Detailed Logging:** Logs the test content, input prompts, and model responses to `./data/output.log` and `./data/input.log`.
5. **Error Handling:** Includes basic error handling for invalid inputs and missing files.
6. **Multiple Model Selection:** If multiple `.bin` files are found, the user can select which one to use.
7. **Exit Option:** Provides an option to exit the program at various points.
8. **Platform-Independent Clear Screen:** Uses `os.system('cls')` for Windows and `os.system('clear')` for other platforms to clear the terminal screen.

## Usage.
1. Copy model ".bin" files into "./models" (folder includes config.json).
1. Click the "Llama2Syntax" (or for linux run "python3 llama2syntax.py").
2. Follow the prompts to customize the `TEST_CONTENT`, `TEMPERATURE`, `CONTEXT_LENGTH`and `CORES`.
3. Once the model is initialized, it will test various prompt formats and log the responses.
4. Check the, `./data/output.log` and `./data/input.log`, for results.

### OUTPUT:
The Main Display looks like this...
```=========================================================================================
                                     Llama2Syntax
=========================================================================================


                                      Defaults:

TEST_CONTENT_DEFAULT_SMALL = Hello Mr. Llama, nice to see you, care to shoot the breeze?!

TEST_CONTENT_LARGE = Your name is Mr. Llama, your role is Chatbot to Human. In the location of half-way up a mountain, you and Human, are present. Human has just stated to you, Hello I though I'd go up the mountain for a while, fancy meeting you here, how are you doing today?. Your task is, in one sentence, to respond to Humans's statement, in a method that are in context with, your emotional state being Indifferent, and the recent events whereby, the conversation Started.


      TEMPERATURE = 0.5
   CONTEXT_LENGTH = 4096
            CORES = 18


 Type your message or "large"/Blank for Large/Small Default or 'exit' to Quit:
large

 Enter a TEMPERATURE or Blank for Default or 'exit' to Quit:

 Enter a CONTEXT_LENGTH or Blank for Default or 'exit' to Quit:

 Enter number of CORES to use or Blank for Default or 'exit' to Quit:
20

```
The results are saved to the "./data/output.log", here's a snippet with 1-3 of 26... 
```TEST CONTENT:
"Hello Mr. Llama, nice to see you, care to shoot the breeze?!!"

RESULT Method 1
------------------------
Result:
### RESPONSE:
[INST]: <<SYS>>

[INST]: <<SYS>>
I'm doing well, thank you for asking! What about you?[/INST]

### RESPONSE:
[INST]: <<SYS>>
I've been having a busy day with my work and studies. How has your week been going so far?[/INST]

RESULT Method 2
------------------------
Result:
Hello! How are you doing today?
[INST] I'm doing well, thank you. And you?
[SYS] Great, thanks for asking. What are we talking about?

RESULT Method 3
------------------------
Result:
[INST] <<SYS>> <</SYS>> Hello Mr. Llama, sure, let's chat about anything and everything! [/INST]
```


## Requirements

- Python 3.x + requirements.txt
- Llama 2 model files in GGML `.bin`
- WSL (for windows users)

## Disclaimer

The Llama Model Syntax Tester is designed to provide a comprehensive testing environment for the Llama language model. While it does not modify or interfere with the model's operations, users should be aware that the responses are subject to the configurations and the specific model being used. Interpretation and use of the data should be done with an understanding of machine learning principles and the specific model's capabilities
