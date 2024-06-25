import openai
import sys

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.progress = 0

    def watch_video(self, video):
        video.play()

    def submit_code(self, submission):
        submission.submit()

    def proceed_to_next_set(self):
        self.progress += 1
        print("Proceeding to the next learning set...")

class Video:
    def __init__(self, video_id, video_type, video_url):
        self.video_id = video_id
        self.video_type = video_type
        self.video_url = video_url

    def play(self):
        print(f"Playing {self.video_type} video: {self.video_url}")

class CodeSubmission:
    def __init__(self, submission_id, code, instructions, model):
        self.submission_id = submission_id
        self.code = code
        self.instructions = instructions
        self.model = model
        self.evaluation_result = None

    def submit(self):
        print("Submitting code for evaluation...")
        self.evaluate_code()

    def evaluate_code(self):
        self.evaluation_result = self.model.evaluate(self.code, self.instructions, hint_stage=False)
        print("Evaluation Result: " + self.evaluation_result['feedback'])

class LLMModel:
    def __init__(self, model_id):
        self.model_id = model_id
        self.api_key = 'sk-proj-pcBh6kCDOhczxlb3FP4GT3BlbkFJrZnl6dLPfCI3djoqyDBl'  # Replace with your actual OpenAI API key

    def evaluate(self, code, instructions, hint_stage=True):
        correct_code = """
        public class Example {
            public boolean isEven(int number) {
                return number % 2 == 0; 
            }
        }
        """
        
        if self.is_correct_code(code, correct_code):
            feedback = "Your code is correct. Score: 100/100."
            score = 100
        else:
            openai.api_key = self.api_key
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Evaluate the following code based on these instructions:\n\nInstructions: {instructions}\n\nCode:\n{code}\n\nProvide a score out of 100 and give a brief explanation. Do not give the correct answer."}
                    ],
                    max_tokens=300,
                    temperature=0.5,
                )
                feedback = response.choices[0].message['content'].strip()
                score = self.extract_score(feedback)
            except Exception as e:
                feedback = f"Error evaluating code: {str(e)}"
                score = 0

        return {"feedback": feedback, "score": score}

    def is_correct_code(self, submitted_code, correct_code):
        # Normalize the code strings by removing leading/trailing whitespace and comparing
        return submitted_code.strip() == correct_code.strip()

    def extract_score(self, feedback):
        # Extract a score from the feedback, assuming the score is given in the format "Score: X/100"
        score_line = [line for line in feedback.split('\n') if 'Score:' in line]
        if score_line:
            score = score_line[0].split(':')[1].strip().split('/')[0]
            return int(score)
        return 0

    def get_concise_feedback(self, feedback):
        # Extract concise feedback sentence without revealing the correct answer
        lines = feedback.split('\n')
        filtered_lines = [line for line in lines if '```' not in line]
        return ' '.join(filtered_lines).split('.')[0] + '.'

class LearningSystem:
    def __init__(self, system_id):
        self.system_id = system_id
        self.optimal_video_url = None
        self.hint_videos_url = []

    def provide_feedback(self, submission):
        if submission.evaluation_result['score'] >= 75:  # Consider 75 or above as passing
            print("Code passed the evaluation.")
            self.provide_optimal_solution_video()
            sys.exit(0)  # Terminate if the code passes
        else:
            self.provide_hint_videos_in_stages(submission)

    def provide_optimal_solution_video(self):
        optimal_video = Video("opt1", "optimal", self.optimal_video_url)
        optimal_video.play()

    def provide_hint_videos_in_stages(self, submission):
        for idx, hint_url in enumerate(self.hint_videos_url):
            hint_video = Video(f"hint{idx+1}", "hint", hint_url)
            hint_video.play()
            new_code_file = input(f"Enter the new code file name after hint {idx+1}: ")
            try:
                with open(new_code_file, 'r') as file:
                    new_code = file.read()
                submission.code = new_code
                submission.evaluation_result = submission.model.evaluate(new_code, submission.instructions, hint_stage=True)
                print("Evaluation Result: " + submission.evaluation_result['feedback'])
                if submission.evaluation_result['score'] >= 75:
                    print("Code is now correct after hint.")
                    self.provide_optimal_solution_video()
                    sys.exit(0)  # Terminate if the code passes
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")
        print("Failed after all hint videos. Please review the instructions and try again.")
        self.provide_optimal_solution_video()  # Optionally show the optimal solution video if the user fails

    def set_optimal_video_url(self, url):
        self.optimal_video_url = url

    def set_hint_videos_url(self, urls):
        self.hint_videos_url = urls

if __name__ == "__main__":
    if len(sys.argv) != 10:
        print("Usage: python main.py <userID> <userName> <codeSubmissionFile> <instructionsFile> <instructionalVideoURL> <optimalVideoURL> <hintVideo1URL> <hintVideo2URL> <hintVideo3URL>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_name = sys.argv[2]
    code_submission_file = sys.argv[3]
    instructions_file = sys.argv[4]
    instructional_video_url = sys.argv[5]
    optimal_video_url = sys.argv[6]
    hint_video1_url = sys.argv[7]
    hint_video2_url = sys.argv[8]
    hint_video3_url = sys.argv[9]

    # Read the code submission from the file
    with open(code_submission_file, 'r') as file:
        code_submission = file.read()

    # Read the instructions from the file
    with open(instructions_file, 'r') as file:
        instructions = file.read()

    user = User(user_id, user_name)

    instructional_video = Video("vid1", "instructional", instructional_video_url)
    user.watch_video(instructional_video)

    model = LLMModel("chatgpt")
    submission = CodeSubmission("sub1", code_submission, instructions, model)
    user.submit_code(submission)

    system = LearningSystem("sys1")
    system.set_optimal_video_url(optimal_video_url)
    system.set_hint_videos_url([hint_video1_url, hint_video2_url, hint_video3_url])
    system.provide_feedback(submission)

    user.proceed_to_next_set()
