#                   Enhanced Q&A Chatbot With deepseek-r1:1.5b, Gemma3:1b, Gemma3:4b

 It uses 'Ollama' class of langchain community to generate response to the user query. 
 The user can select the Ollama model from the sidebar and adjust the response parameters
 like temperature and max tokens. The user can ask any question and get the response from 
 the chatbot. The response is generated using the 'generate_response' function which takes
 the user query, Ollama model, temperature, and max tokens as input and returns the response. 
 The response is displayed on the screen. If the user has not entered any question, it
 displays a message to enter the question. The chatbot deepseek-r1:1.5b, uses Gemma3:1b and
 Gemma3:4b models to generate the response to the user query. 
