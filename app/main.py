import os

from fastapi import FastAPI
import openai
from dotenv import load_dotenv


API = FastAPI(
    title="AI API",
    description="",
    version="0.0.1",
    docs_url="/",
)
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")


@API.get("/outreach")
async def outreach(your_name: str, job_title: str, company: str, manager_name: str):
    prompt = f"Write a cold outreach letter to {manager_name} at {company} " \
             f"about the {job_title} role from {your_name}."
    result, *_ = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a master cold outreach letter writer."},
            {"role": "user", "content": prompt},
        ],
    ).choices
    return result.get("message").get("content")
