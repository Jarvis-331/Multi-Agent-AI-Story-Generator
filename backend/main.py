from fastapi import FastAPI, HTTPException
from .schemas import StoryRequest, StoryResponse
from .crew import run_story_crew

app = FastAPI(title="Multi-Agent Story Generator")

@app.post("/generate", response_model=StoryResponse)
def generate_story(request: StoryRequest):

    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    try:
        story = run_story_crew(request.prompt)
        return StoryResponse(story=story)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
