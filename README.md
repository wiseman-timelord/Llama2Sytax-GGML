# Llama2Syntax
A script to test a range of 26 different forms of syntax on given Llama 2 based GGML files language models, to find working/optimal prompt syntax.

### OUTPUT:
The example snippet with results 1-3 in "./data/output.log"... 
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
