# Llama2Syntax
A script to test a range of 26 different forms of syntax on given Llama 2 based GGML files language models, to find working/optimal prompt syntax.

### OUTPUT:
The Main Display looks like this...
=========================================================================================
                                     Model-Syntax
=========================================================================================


 Defaults:

     TEST_CONTENT = Hello Mr. Llama, nice to see you, care to shoot the breeze?!!
      TEMPERATURE = 0.5
   CONTEXT_LENGTH = 4096


 Enter a CONTEXT_LENGTH or Blank for Default or 'exit' to Quit:

 Enter a TEMPERATURE or Blank for Default or 'exit' to Quit:

 Enter a TEST_CONTENT or Blank for Default or 'exit' to Quit:


 Searching for Json...
 Model Json Found.
 Searching for models...
 Model used: llama2_7b_chat_uncensored.ggmlv3.q2_K
 Context used: 4096


 Initialising, be patient...
llama.cpp: loading model from ./models/llama2_7b_chat_uncensored.ggmlv3.q2_K.bin
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_ctx      = 4096
llama_model_load_internal: ftype      = 10 (mostly Q2_K)
llama_model_load_internal: model size = 7B
llama_model_load_internal: mem required  = 4525.64 MB (+ 1026.00 MB per state)

```
The results are saved to the "./data/output.log", here is a example snippet with results 1-3 of 26... 
```
TEST CONTENT:
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
