from typing import List
from crewai import Agent, Task, Crew, LLM, Process
from crewai.project import CrewBase, agent, task, crew

from crewai_tools import SerperDevTool, ScrapeWebsiteTool, DirectoryReadTool, FileReadTool, FileWriterTool
from pydantic import BaseModel, Field
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

llm= LLM(
    model= 'gemini-2.5-flash-lite',
    temperature= 0.7
)

class output_type(BaseModel):
    content_type: str = Field(..., description= 'The type of content to be created (e.g., blog post, social media post, video)')
    topic: str = Field(..., description="The topic of the content")
    target_audience: str = Field(..., description="The target audience for the content")
    tags: List[str] = Field(..., description="Tags to be used for the content")
    content: str = Field(..., description="The content itself")

@CrewBase
class MarketingAgents():
    '''The marketing crew is responsible for creating and executing marketing strategies, content creation, and managing marketing campaigns.'''
    agents_config= 'config/agents.yaml'
    tasks_config= 'config/tasks.yaml'

    @agent
    def head_of_marketing(self) -> Agent:
        return Agent(
            config= self.agents_config['head_of_marketing'],
            tools= [
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileReadTool(),
                FileWriterTool()
            ],
            reasoning= True,
            inject_date= True,
            allow_delegation= True,
            max_rpm= 3,
            llm= llm
        )
    
    @agent
    def content_creator_social_media(self) -> Agent:
        return Agent(
            config= self.agents_config['content_creator_social_media'],
            tools= [
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileReadTool(),
                FileWriterTool()
            ],
            inject_date= True,
            allow_delegation= True,
            max_rpm= 3,
            max_iter= 15,
            llm= llm
        )
    
    @agent
    def content_writer_blogs(self) -> Agent:
        return Agent(
            config= self.agents_config['content_writer_blogs'],
            tools= [
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts/blogs'),
                FileReadTool(),
                FileWriterTool()
            ],
            inject_date= True,
            allow_delegation= True,
            max_rpm= 3,
            max_iter= 10,
            llm= llm
        )
    
    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config= self.agents_config['seo_specialist'],
            tools= [
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool('resources/drafts'),
                FileReadTool(),
                FileWriterTool()
            ],
            inject_date= True,
            allow_delegation= True,
            max_rpm= 3,
            max_iter= 10,
            llm= llm
        )
    

    @task
    def task1(self) -> Task:
        return Task(
            config= self.tasks_config['market_research'],
            agent= self.head_of_marketing()
        )
    
    @task
    def task2(self) -> Task:
        return Task(
            config= self.tasks_config['prepare_marketing_strategy'],
            agent= self.head_of_marketing()
        )
    
    @task
    def task3(self) -> Task:
        return Task(
            config= self.tasks_config['create_content_calendar'],
            agent= self.content_creator_social_media()
        )
    
    @task
    def task4(self) -> Task:
        return Task(
            config= self.tasks_config['prepare_post_drafts'],
            agent= self.content_creator_social_media(),
            output_json= output_type,
            async_execution= True
        )
    
    @task
    def task5(self) -> Task:
        return Task(
            config= self.tasks_config['prepare_scripts_for_reels'],
            agent= self.content_creator_social_media(),
            output_json= output_type,
            async_execution= True
        )
    
    @task
    def task6(self) -> Task:
        return Task(
            config= self.tasks_config['content_research_for_blogs'],
            agent= self.content_writer_blogs()
        )
    
    @task
    def task7(self) -> Task:
        return Task(
            config= self.tasks_config['draft_blogs'],
            agent= self.content_writer_blogs(),
            output_json= output_type
        )
    
    @task
    def task8(self) -> Task:
        return Task(
            config= self.tasks_config['seo_optimization'],
            agent= self.seo_specialist(),
            output_json= output_type
        )
    

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents= self.agents,
            tasks= self.tasks,
            process= Process.sequential,
            verbose= True,
            planning= True,
            planning_llm= llm,
            max_rpm= 3
        )
    
    
if __name__ == '__main__':
    from datetime import datetime

    inputs = {
        "product_name": "SubSlash AI",
        "target_audience": "Millennials and Gen Z (ages 22-40) who have 'subscription fatigue' and want to save money but hate confrontation.",
        "product_description": "An AI-powered personal finance assistant that scans your bank statements to find forgotten subscriptions (Netflix, Gym, SaaS) and automatically negotiates cancellations or refunds on your behalf. It uses a secure, empathetic AI negotiator to chat with support agents so you don't have to.",
        "budget": "$2,500 initial launch budget",
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }

    marketing_agent = MarketingAgents()
    marketing_agent.crew().kickoff(inputs=inputs)
    print('Marketing crew has been successfully created and run.')