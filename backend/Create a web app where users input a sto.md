Create a web app where users input a story prompt (e.g., "A dragon in a modern city..."), and a multi-agent system generates a short story continuation (100-200 words). Use a multi-agent framework to divide the generation: e.g., one agent brainstorms ideas, another writes the story, and a third refines it. The app must be runnable locally.
Requirements:
Frontend: Use React to build a single-page app with:
A text input for the prompt.
A "Generate Story" button.
A display area for the generated story.
Basic loading indicator (e.g., spinner) during generation.
Use Axios or fetch to send the prompt to the backend via POST.
Backend: Use FastAPI (Python) to create a server with:
A POST endpoint (e.g., /generate) that receives the prompt.
Integrate a multi-agent tool/framework (e.g., LangChain agents, CrewAI, or AutoGen) to handle the generation:
Agent 1: Generate outline or key plot points based on prompt.
Agent 2: Write the initial story draft.
Agent 3: Edit/refine for coherence and creativity.
Use a generative AI model (e.g., OpenAI GPT via their API, or Hugging Face's free inference) within the agents.
Return the final story as JSON to the frontend.
Handle errors like empty prompts.
Multi-Agent Integration: Choose any open-source multi-agent library (e.g., install via pip if needed, but assume quick setup). Agents should collaborate sequentially or in parallel for the output. Keep it simple—focus on functionality.