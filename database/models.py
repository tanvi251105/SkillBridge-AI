from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class CareerReport:
    id: int
    user_id: int
    career_goal: str
    skills: str
    education: str
    report: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class ResumeReport:
    id: int
    user_id: int
    filename: str
    ats_score: int
    suggestions: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class InterviewResult:
    id: int
    user_id: int
    score: int
    feedback: str
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class QuizResult:
    id: int
    user_id: int
    topic: str
    score: int
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")