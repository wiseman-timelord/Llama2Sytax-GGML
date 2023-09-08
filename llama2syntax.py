from llama_cpp import Llama
import os
import glob
import readline
import multiprocessing

# Globals
llm = None
TEST_CONTENT_LARGE = "Your name is Mr. Llama, your role is Chatbot to Human. You are at half-way up a mountain, where you and Human are present, and Human has just stated, Hello I though I'd go up the mountain for a while, fancy meeting you here, how are you doing today?, to you. Your task is, in one sentence, to respond to Humans's statement, in a method that are in context with, your emotional state being Indifferent, as well as the recent events are that, The conversation Started."
TEST_CONTENT_DEFAULT_SMALL = "Hello Mr. Llama, nice to see you, care to shoot the breeze?!"
TEMPERATURE_DEFAULT = 0.5
CONTEXT_LENGTH = 4096
OUTPUT_LOG_PATH = "./data/output.log"
INPUT_LOG_PATH = "./data/input.log"
TEST_CONTENT = None  # Initialize as None
TEMPERATURE = None  # Initialize as None
MODEL_PATH = None  # Initialize as None
CORES_DEFAULT = int(multiprocessing.cpu_count() * 0.75)  # 3/4 of total cores
CORES = None  # Initialize as None

# Main Display Function
def main_display():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 89)
    print("                                     Llama2Syntax")
    print("=" * 89)
    print("\n\n                                      Defaults:")
    print(f"\n TEST_CONTENT_LARGE = {TEST_CONTENT_LARGE}")
    print(f"\n TEST_CONTENT_DEFAULT_SMALL = {TEST_CONTENT_DEFAULT_SMALL}")
    print(f"\n      TEMPERATURE = {TEMPERATURE_DEFAULT}")
    print(f"   CONTEXT_LENGTH = {CONTEXT_LENGTH}")
    print(f"            CORES = {CORES_DEFAULT}\n")

# User input for TEST_CONTENT, TEMPERATURE, CONTEXT_LENGTH, and CORES
def get_user_configurations():
    global TEST_CONTENT, TEMPERATURE, CONTEXT_LENGTH, CORES

    # Helper function to get user input
    def get_input(prompt, default, type_cast):
        while True:
            print(f"\n{prompt} or 'exit' to Quit:")
            value = input().strip()
            if value.lower() == 'exit':
                exit()
            elif value == '':
                return default
            else:
                try:
                    return type_cast(value)
                except ValueError:
                    print(f"Invalid input. Please enter a {type_cast.__name__}.")

    prompt_size = get_input(" Type your message or \"large\"/Blank for Large/Small Default", TEST_CONTENT_DEFAULT_SMALL, str).lower()
    if prompt_size == 'large':
        TEST_CONTENT = TEST_CONTENT_LARGE
    else:
        TEST_CONTENT = prompt_size

    TEMPERATURE = get_input("Enter a TEMPERATURE", TEMPERATURE_DEFAULT, float)
    CONTEXT_LENGTH = get_input("Enter a CONTEXT_LENGTH", CONTEXT_LENGTH, int)
    CORES = get_input("Enter number of cores to use", CORES_DEFAULT, int)


# Search for config.json and .bin models
def search_json_and_models():
    global MODEL_PATH

    # Helper function to exit if file not found
    def check_file_existence(path, error_message):
        if not os.path.exists(path):
            print(error_message)
            choice = input("Would you like to try again? (y/n): ")
            if choice.lower() == 'n':
                exit()
            return False
        return True

    # Search for config.json
    print("\n\n Searching for Json...")
    while not check_file_existence('./models/config.json', "config.json not present in ./models!"):
        pass
    print(" Model Json Found.")
    # Search for .bin models
    print(" Searching for models...")
    bin_files = glob.glob('./models/*.bin')
    if len(bin_files) == 0:
        print(" No .bin models in models folder!")
        exit()
    elif len(bin_files) == 1:
        MODEL_PATH = bin_files[0]
    else:
        print(" Multiple .bin models found. Please select one:")
        for i, file in enumerate(bin_files):
            print(f" {i+1}. {file}")
        choice = int(input(" Enter the number of your choice: "))
        MODEL_PATH = bin_files[choice - 1]

    model_name = os.path.basename(MODEL_PATH).replace('.bin', '')
    print(f" Model used: {model_name}")
    print(f" Context used: {CONTEXT_LENGTH}")



# Initialize the model
def initialize_model():
    global llm
    print(f"\n Initialising, be patient...")
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=CONTEXT_LENGTH,
        embedding=True,
        n_threads=20,
    )

# Function to test different prompt formats
def test_prompt_formats():
    responses = {}
    
    # Define methods in a list of dictionaries
    methods = [
        {"name": "Method 1", "prompt": f"[INST] <<SYS>>\n<</SYS>>\n{TEST_CONTENT}[/INST]"},
        {"name": "Method 2", "prompt": f"[INST] <<SYS>>\n{TEST_CONTENT}\n<</SYS>>\n[/INST]"},
        {"name": "Method 3", "prompt": f"[INST] <<SYS>> <</SYS>> {TEST_CONTENT} [/INST]"},
        {"name": "Method 4", "prompt": f"[INST] {TEST_CONTENT} [/INST]"},
        {"name": "Method 5", "prompt": f"<<SYS>> {TEST_CONTENT} <</SYS>>"},
        {"name": "Method 6", "prompt": f"### Instruction: {TEST_CONTENT}\n### Response:"},
        {"name": "Method 7", "prompt": f"### Instruction:\n{TEST_CONTENT}\n### Response:"},
        {"name": "Method 8", "prompt": f"### Instruction:\n{TEST_CONTENT}\n\n### Response:"},
        {"name": "Method 9", "prompt": f"### Instruction:\n{TEST_CONTENT}"},
        {"name": "Method 10", "prompt": f"### Instruction: {TEST_CONTENT}"},
        {"name": "Method 11", "prompt": f"### Human: {TEST_CONTENT}\n### Assistant:"},
        {"name": "Method 12", "prompt": f"### Human:\n{TEST_CONTENT}\n### Assistant:"},
        {"name": "Method 13", "prompt": f"### Human:\n{TEST_CONTENT}\n\n### Assistant:"},
        {"name": "Method 14", "prompt": f"### Human:\n{TEST_CONTENT}"},
        {"name": "Method 15", "prompt": f"### Human: {TEST_CONTENT}"},
        {"name": "Method 16", "prompt": f"### System: {TEST_CONTENT}\n### Response:"},
        {"name": "Method 17", "prompt": f"### System:\n{TEST_CONTENT}\n### Response:"},
        {"name": "Method 18", "prompt": f"### System:\n{TEST_CONTENT}"},
        {"name": "Method 19", "prompt": f"### System: {TEST_CONTENT}"},
        {"name": "Method 20", "prompt": f"### User: {TEST_CONTENT}\n### Response:"},
        {"name": "Method 21", "prompt": f"### User:\n{TEST_CONTENT}\n### Response:"},
        {"name": "Method 22", "prompt": f"### User:\n{TEST_CONTENT}\n\n### Response:"},
        {"name": "Method 23", "prompt": f"### User:\n{TEST_CONTENT}"},
        {"name": "Method 24", "prompt": f"### User: {TEST_CONTENT}"},
        {"name": "Method 25", "prompt": f"Q: {TEST_CONTENT}"},
        {"name": "Method 26", "prompt": f"Q: {TEST_CONTENT}\nA:"}
    ]
    
    # Clear the output and input logs
    with open(OUTPUT_LOG_PATH, 'w') as f:
        f.write(f"TEST CONTENT:\n\"{TEST_CONTENT}\"\n\n")
    with open(INPUT_LOG_PATH, 'w') as f:
        f.write("Input Prompts Log:\n\n")

    # Loop through each method to get responses
    for method in methods:
        # Log the prompt to the input log
        with open(INPUT_LOG_PATH, 'a') as f:
            f.write(f"{method['name']} Prompt: {method['prompt']}\n\n")
        
        # Log the complete input just before sending it to the model
        with open(INPUT_LOG_PATH, 'a') as f:
            f.write(f"Complete Input for {method['name']}: {method['prompt']}\n\n")
        
        # Get the model's response
        response = llm(method['prompt'], temperature=TEMPERATURE)["choices"][0]["text"].strip()
        responses[method['name']] = response

    # Log all responses to the output log
    with open(OUTPUT_LOG_PATH, 'a') as f:
        for method_name, response in responses.items():
            f.write(f"RESULT {method_name}\n")
            f.write("------------------------\n")
            f.write(f"Result:\n{response}\n\n")

if __name__ == "__main__":
    main_display()
    get_user_configurations()
    search_json_and_models()
    initialize_model()
    test_prompt_formats()