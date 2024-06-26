LinkedIn Live Learning S.W.A.F
Enhancing User Outcomes through Interactive Learning and AI Connectivity
Project Team: Shaun, Faatiha, Wysdom, Abraham
Overview
LinkedIn Learning is a powerful tool that allows millions of individuals to access high-quality content for personal learning at affordable prices. However, there are areas for improvement:

Assessment Improvement: Multiple choice questions don’t actively test content to proficiency and need enhancements.
Integration and Accreditation: LinkedIn Learning is not widely integrated into university systems and is not a major player in accreditation, representing a significant market opportunity.
What is LinkedIn Live Learning?
An interactive video learning platform that utilizes user input and AI feedback to enhance learning outcomes. Key features include:

Interactive Video Sessions: Engaging learning sessions with real-time feedback.
Personalized Feedback: Tailored to the user's responses for more effective learning.
Impactful Learning: Users earn certifications recognized by employers and universities.
Open-Ended Questions: Real-world experience in computer science environments.
Project Components
Back-End
Language & Framework: Python and Flask
AI Integration: OpenAI API for generating and handling interactive content.
Connectivity: Seamless integration with front-end components.
Front-End
Technologies: HTML, CSS, Bootstrap
User Interface: Rebuilt LinkedIn Learning UI including sign-in interface and profile interaction.
Video Content: Structured video sessions broken into digestible pieces with periodic checks for understanding.
Impact
Transitioning LinkedIn Learning from a focus on personal development to employment certifications and university accreditation. Our solution addresses the following:

Education Access: Less than 30% of community college students completed a computer programming or computer science course due to lack of proper instruction or access to courses.
Enhanced Learning: Switching to open-ended, interview-style questions prepares candidates for real-world job skills.
Recruiter Benefits: Recruiters can see relevant accreditations, ensuring candidates are job-ready.
Partnerships
We aim to create a credible platform that is worth users’ time, allowing LinkedIn to scale and impact learning effectively.






# Code Evaluation Learning System

This project implements a code evaluation learning system using OpenAI's GPT-3.5-turbo model. The system allows users to submit code for evaluation, receive feedback, and watch instructional and hint videos. If the submitted code passes the evaluation, the user proceeds to the next learning set.

### Instructions

1. **Replace placeholders**: Make sure to replace `YOUR_API_KEY` with your actual OpenAI API key and provide the path to your UML class diagram image.
2. **Add the README**: Save this content in a file named `README.md` and add it to your GitHub repository.

This `README.md` file provides a comprehensive overview of your project, including setup instructions, usage, and detailed descriptions of the classes and methods.

## Features

- User registration and progress tracking
- Submission of code for evaluation
- Integration with OpenAI's GPT-3.5-turbo model for code evaluation
- Display of instructional and hint videos
- Feedback on code submissions
- Hard-coded correct code for comparison

## Classes

### User

Represents a user in the system.

**Attributes:**
- `user_id: str`
- `user_name: str`
- `progress: int`

**Methods:**
- `__init__(user_id: str, user_name: str)`
- `watch_video(video: Video) -> None`
- `submit_code(submission: CodeSubmission) -> None`
- `proceed_to_next_set() -> None`

### Video

Represents a video in the system.

**Attributes:**
- `video_id: str`
- `video_type: str`
- `video_url: str`

**Methods:**
- `__init__(video_id: str, video_type: str, video_url: str)`
- `play() -> None`

### CodeSubmission

Represents a code submission for evaluation.

**Attributes:**
- `submission_id: str`
- `code: str`
- `instructions: str`
- `model: LLMModel`
- `evaluation_result: dict`

**Methods:**
- `__init__(submission_id: str, code: str, instructions: str, model: LLMModel)`
- `submit() -> None`
- `evaluate_code() -> None`

### LLMModel

Represents the language model used for code evaluation.

**Attributes:**
- `model_id: str`
- `api_key: str`

**Methods:**
- `__init__(model_id: str)`
- `evaluate(code: str, instructions: str, hint_stage: bool=True) -> dict`
- `is_correct_code(submitted_code: str, correct_code: str) -> bool`
- `extract_score(feedback: str) -> int`
- `get_concise_feedback(feedback: str) -> str`

### LearningSystem

Manages the overall learning system.

**Attributes:**
- `system_id: str`
- `optimal_video_url: str`
- `hint_videos_url: list`

**Methods:**
- `__init__(system_id: str)`
- `provide_feedback(submission: CodeSubmission) -> None`
- `provide_optimal_solution_video() -> None`
- `provide_hint_videos_in_stages(submission: CodeSubmission) -> None`
- `set_optimal_video_url(url: str) -> None`
- `set_hint_videos_url(urls: list) -> None`

## Main Script

The main script reads command-line arguments, sets up the user, video, and learning system, and manages the flow of the learning process.

**Usage:**

```bash
python main.py <userID> <userName> <codeSubmissionFile> <instructionsFile> <instructionalVideoURL> <optimalVideoURL> <hintVideo1URL> <hintVideo2URL> <hintVideo3URL>
