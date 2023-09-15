# syntax.py

# Imports
from llama_cpp import Llama
import os

# Globals
llm = None
MODEL_PATH = "./models/llama2_7b_chat_uncensored.ggmlv3.q8_0.bin"  # Replace with your actual model path
CONTEXT_LENGTH = 4096
OUTPUT_LOG_PATH = "./data/output.log"
INPUT_LOG_PATH = "./data/input.log"
TEMPERATURE = 0.5

# Initialize the model
def initialize_model():
    global llm
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
        {"name": "Method 1", "prompt": "### Instruction: Given the recent events of 'the conversation started', integrate the following: Human said, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama replied, 'I come here sometimes for peace.' Summarize this in up to one-paragraph."},
        {"name": "Method 2", "prompt": "### Instruction: In light of the recent events, 'the conversation started', Human expressed, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama responded, 'I come here sometimes for peace.' Provide a three-sentence summary."},
        {"name": "Method 3", "prompt": "### Instruction: With the backdrop of 'the conversation started', Human communicated, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama answered, 'I come here sometimes for peace.' Condense this into up to one-paragraph."},
        {"name": "Method 4", "prompt": "### Instruction: Considering the recent events, 'the conversation started', Human uttered, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama stated, 'I come here sometimes for peace.' Sum it up in up to one-paragraph."},
        {"name": "Method 5", "prompt": "### Instruction: Reflecting on 'the conversation started', Human mentioned, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama declared, 'I come here sometimes for peace.' Create a three-sentence summary."},
        {"name": "Method 6", "prompt": "### Instruction: In the context of 'the conversation started', Human questioned, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama affirmed, 'I come here sometimes for peace.' Summarize succinctly in up to one-paragraph."},
        {"name": "Method 7", "prompt": "### Instruction: Against the backdrop of 'the conversation started', Human inquired, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama confirmed, 'I come here sometimes for peace.' Provide a brief three-sentence summary."},
        {"name": "Method 8", "prompt": "### Instruction: Given 'the conversation started', Human spoke, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama acknowledged, 'I come here sometimes for peace.' Condense these interactions into up to one-paragraph."},
        {"name": "Method 9", "prompt": "### Instruction: In reference to 'the conversation started', Human articulated, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama replied, 'I come here sometimes for peace.' Summarize in up to one-paragraph."},
        {"name": "Method 10", "prompt": "### Instruction: With respect to 'the conversation started', Human conveyed, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama responded, 'I come here sometimes for peace.' Provide a three-sentence encapsulation."},
        {"name": "Method 11", "prompt": "### Instruction: Given the recent events, 'the conversation started', summarize in up to one-paragraph only the answer: Human said, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama replied, 'I come here sometimes for peace.'"},
        {"name": "Method 12", "prompt": "### Instruction: In light of 'the conversation started', provide a three-sentence summary, answer only: Human expressed, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama responded, 'I come here sometimes for peace.'"},
        {"name": "Method 13", "prompt": "### Instruction: With the backdrop of 'the conversation started', condense into up to one-paragraph, answer only: Human communicated, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama answered, 'I come here sometimes for peace.'"},
        {"name": "Method 14", "prompt": "### Instruction: Considering the recent events, 'the conversation started', sum it up in up to one-paragraph, answer only: Human uttered, 'hello there! i am glad to meet you here in the middle of nowhere. do you come here often?!' and Wise-Llama stated, 'I come here sometimes for peace.'"}
    ]

    
    # Clear the output and input logs
    with open(OUTPUT_LOG_PATH, 'w') as f:
        f.write("Output Log:\n\n")
    with open(INPUT_LOG_PATH, 'w') as f:
        f.write("Input Prompts Log:\n\n")

    # Loop through each method to get responses
    for method in methods:
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
    initialize_model()
    test_prompt_formats()
