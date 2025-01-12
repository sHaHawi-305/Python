"""
created this program because I understand how challenging it can be to find direction when starting something new.
My goal is to empower others to confidently take the first steps toward their tech dreams.
Whether you're exploring a career in data, web development, or machine learning,
I hope this tool will make your transition easier and more fulfilling.
"""





import os 
import json
import time 
from tqdm import tqdm
from colorama import init, Fore, Style
from InquirerPy import inquirer
from tabulate import tabulate



# to start colorama so we can give colors to the output:
init()

# build User class:

class User:
    def __init__(self, username):
        self.username = username
        self.career_path = None
        self.progress = []


    def save_progress(self):
        with open(f"{self.username}_data.json", "w") as userdata:
            json.dump({"career_path": self.career_path, "progress": self.progress}, userdata)

    
    def load_progress(self):
        if os.path.exists(f"{self.username}_data.json"):
            with open(f"{self.username}_data.json", "r") as userdata:
                data = json.load(userdata)
                self.career_path = data.get("career_path")
                self.progress = data.get("progress") if data.get("progress") is not None else []


# build roadmap class :

class Roadmap:
    # determine what career_paths to include
    def __init__(self):
        self.careers = {
            1 : "Data Analyst",
            2 : "Data Scientist",
            3 : "Data Engineer",
            4 : "Web Developer",
            5 : "DevOps",
            6 : "Cyber-Security",
            7 : "Machine Learning Engineer"
        }

        # breakdown roadmaps for each career_path:
        self.skills = {
            "Data Analyst": {"Excel": ["Basic Functions", "Pivot Tables", "Chart", "Conditional Formating"],
                             "SQL": ["Basic Queries", "Joins", "Subqueries", "CTEs"],
                             "Data Visualization": ["Microsoft Power BI", "Tableau"],
                             "Python": ["Pandas", "Numpy", "Seaborn", "Matpoltlip"]},
                             
            "Data Scientist": {"Mathmatics & Statistics": ["Descriptive Statistics", "Inferential Statistics","Liner algebra", "Calculus", "Probbility"],
                                "Python": ["Pandas", "Numpy", "Seaborn", "Matplotlip", "Machine Learning", "Deep Learning"],
                                "SQL": ["Advanced Queries Databases", "Joins", "CTEs", "Subqueries"],
                                "R": ["Advanced Level"]},
            

            "Data Engineer": {"SQL": ["Data Warehousing", "ETL Proscesses"],
                              "NoSQL": ["MongoDB"],
                               "Python": ["Data Pipeline Development"],
                               "Java or Scala": ["Advanced Level"],
                               "Cloud Services": ["Microsoft Azure", "AWS Services", "Google Cloud"]},


            "Web Developer": {"HTML/CSS": ["Responsive Design", "Accessibility"],
                              "JavaScript": ["DOM Manipulation", "Frameworks like 'React'"],
                              "Version Control": ["Proficiency in Git"],
                              "APIs": ["Experience in RESTful services and API integration"] },


            "DevOps": {"Docker": ["Containerization", "Orchestration"],
                       "CI/CD": ["Continuous Integration", "Continuous Deployment"],
                       "Cloud Services": ["Microsoft Azure", "AWS Services", "Google Cloud"],
                       "Version Control": ["Mastery of Git and GitHub"]},

            "Cyber-Security": {"Networking": ["Fire Walls", "VPNs", "Ethical Hacking", " TCP/IP"],
                               "Security Protocols": ["Encryption", "Authentication", "access control"],
                               "Compliance Standards": ["GDPR", "HIPAA", "PCI-DSS"],
                               "Vulnerability Assessment": ["Nessu OR Metasploit"]},
            
            "Machine Learning Engineer": {"Mathmatics & Statistics": ["Descriptive Statistics", "Inferential Statistics","Liner algebra", "Calculus", "Probbility"],
                                          "Python": ["Model Development", "Data Preprocessing"],
                                          "Libraries": ["TensorFlow", "PyTorch"],
                                          "Big Data Technologies": ["Spark", "Hadoop"]},                        
        }



        # job description & avg salary
        self.job_data = {"Data Analyst": {"Job Description": ["Analyzes data to help businesses make informed decisions. Uses tools like Excel, SQL, and data visualization techniques."],
                                          "Average Salary in USA": ["$70,000 - $90,000","per Year", "this data based on the date 31-12-2024"]},


                        "Data Scientist":{"Job Description": ["Combines statistics, programming, and domain expertise to extract insights from complex data. Works on machine learning models and data-driven solutions."],
                                          "Average Salary in USA":["$100,000 - $130,000","per Year", "this data based on the date 31-12-2024"]},

                        
                        "Data Engineer":{"Job Description": ["Designs and builds systems for collecting, storing, and analyzing data. Focuses on data architecture and ETL (extract, transform, load) processes."],
                                          "Average Salary in USA": ["$90,000 - $120,000","per Year", "this data based on the date 31-12-2024"]},


                        "Web Developer":{"Job Description": ["Creates and maintains websites and web applications. Works with front-end technologies (HTML, CSS, JavaScript) and back-end frameworks"],
                                         "Average Salary in USA": ["$70,000 - $100,000","per Year", "this data based on the date 31-12-2024"]},

                        
                        "DevOps":{"Job Description": ["Bridges the gap between development and operations, focusing on automating processes and improving software delivery."],
                                  "Average Salary in USA": ["90,000 - $120,000","per Year", "this data based on the date 31-12-2024"]},


                        "Cyber-Security":{"Job Description": ["Protects an organization's computer systems and networks from cyber threats. Monitors security and responds to incidents."],
                                          "Average Salary in USA": ["$80,000 - $110,000","per Year", "this data based on the date 31-12-2024"]},

                        
                        "Machine Learning Engineer":{"Job Description": ["Designs and implements machine learning models at scale. Works closely with data scientists to transform models into production-ready systems."],
                                                     "Average Salary in USA": ["$110,000 - $140,000","per Year", "this data based on the date 31-12-2024"]}
        }



        # breakdown resources for each career_path:
        self.resources = {
            "Data Analyst":{"Youtube (English Languge)" : ["AlexTheAnalyst - Data Analysis Bootcamp", "https://www.youtube.com/watch?v=rGx1QNdYzvs&list=PLUaB-1hjhk8FE_XZ87vPPSfHqb6OcM0cF"],
                            "Courses" : ["Google Data Analytics Professional Certificate", "IBM Data Analyst Professional Certificate"],
                            "Books" : ["Advancing Into Analytics: From Excel to Python and R", "R for Data Science: Import, Tidy, Transform, Visualize, and Model Data" ]},

            "Data Scientist":{"Youtube,Courses and Books all in one place" : ["https://github.com/Moataz-Elmesmary/Data-Science-Roadmap"]},

            "Data Engineer" :{"Youtube,Courses and Books all in one place" : ["https://github.com/Moataz-Elmesmary/Data-Science-Roadmap"]},

            "Web Developer" :{"Youtube (Arabic languge)": ["elzero web school"],
                               "Courses": ["The Complete Web Developer Bootcamp on 'Udemy'", "Full-Stack Web Development on 'Coursera'"]},

            "DevOps":{"Courses": ["DevOps Specialization on 'Coursera'", "Docker Mastery on 'Udemy'"],
                      "Books": ["The Phoenix Project 'by Gene Kim'", "Site Reliability Engineering 'by Niall Richard'"]},

            "Cyber-Security":{"Courses": ["Cybersecurity Specialization on 'Coursera'", "Certified Ethical Hacker on 'Udemy'"],
                              "Books": ["The Web Application Hacker's Handbook 'by Dafydd Stuttard'", "Hacking: The Art of Exploitation 'by Jon Erickson'"],
                              "Online Platforms": ["Cybrary for free cybersecurity training", "Hack The Box for practical hacking challenges"]},

            "Machine Learning Engineer":{"Youtube and more": ["https://github.com/Moataz-Elmesmary/Data-Science-Roadmap"],
                                         "Courses": ["Machine Learning by Andrew Ng on 'Coursera'", "Deep Learning Specialization on 'Coursera'"],
                                         "Books": ["Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow 'by Aurélien Géron'", "Deep Learning 'by Ian Goodfellow'"],
                                         "Online Platforms": ["Kaggle for datasets and competitions", " GitHub for open-source machine learning projects"]}                      
        }


    def get_menu(self):
        return [f"{key}. {value}" for key, value in self.careers.items()]
    

    #get_roadmaps_and_resources
    def get_roadmap(self,choice): 
        roadmap_info = {}
        if choice in self.careers:
            roadmap_info["title"] = f"{self.careers[choice]} Roadmap"
            roadmap_info["skills"] = self.skills[self.careers[choice]]
            roadmap_info["resources"] = self.resources[self.careers[choice]]# to show resources with the roadmaps
            roadmap_info["job_data"] = self.job_data[self.careers[choice]]# to show job descriptions
        return roadmap_info
    


    def get_progress(self, progress):
        return [step for career_path, step in progress] if progress else []



def main():
    username = input("Enter your username to create or access your account: ") # to store user name and used in User class
    user = load_user_data(username)


    roadmap = Roadmap()

    while True:

        if user.career_path is None:
            greeting = f"Hello {Fore.CYAN + username + Style.RESET_ALL}, choose career path to see its roadmap"
            print(greeting)

            menu = roadmap.get_menu()

            # make the choices dynamic and active:
            choices = [item.split(". ")[1] for item in menu]
            choice_made = inquirer.select(
                message="Choose your Career path",
                choices=choices
            ).execute()

            user.career_path = choices.index(choice_made) + 1 # (+1) to match the key in career dict
            print(f"You Have Selected: {roadmap.careers[user.career_path]}")

            user.save_progress() #to save the account data after creating an account and selecting a path
            
        else:

            welcome_back = f"Welcome Back {Fore.CYAN + username + Style.RESET_ALL}!"
            print()#to keep space between lines to read with ease
            print(welcome_back)
            print(f"You are continuing in: {Fore.RED + roadmap.careers[user.career_path] + Style.RESET_ALL}")


            progress_steps = roadmap.get_progress(user.progress)
            if progress_steps:
                print()#to keep space between lines to read with ease
                print(Fore.GREEN + f"Your Progress Record is[{', '.join(progress_steps)}]" + Style.RESET_ALL)

            else:
                print()#to keep space between lines to read with ease
                print(Fore.MAGENTA + "Your Progress Is EMPTY!" + Style.RESET_ALL)
            

            print(Fore.GREEN + "Keep Going!" + Style.RESET_ALL)

        roadmap_info = roadmap.get_roadmap(user.career_path)
        print()#to keep space between lines to read with ease

        #to show Jobs_Info:
        display_job_info(roadmap, user.career_path)

        print()
        #show roadmaps breakedown by skills & tasks
        for skill, tasks in roadmap_info["skills"].items():
            print(Fore.CYAN + f". Skill: {skill}, [Tasks]: {', '.join(tasks)}" + Style.RESET_ALL)

        print()

        #show resources breakedown by subject & resource
        print()#to keep space between lines to read with ease
        display_resources(roadmap, user.career_path)
        
        print()


        while True:
            step = input(Fore.YELLOW +"Enter a completed step to update progress (type 'exit' to quit) or (type 'change' to Reselect career path):" + Style.RESET_ALL).strip().casefold()

            # to escape the loop and check if the user want to exit the program
            if step.lower() == "exit":
                print(Fore.MAGENTA + f"Have a nice day {user.username}, program is off" + Style.RESET_ALL)
                return
            
            # give the user the opition to change career_path
            elif step.lower() == "change":
                user.career_path = None # to reset the user career path so he can Reselect again
                user.progress = [] # to empty the user data of old selection 
                user.save_progress() # to save username data with empty progress 
                break

            elif not step:  # to check if the user typed a step not an empty str
                print(Fore.RED + "Progress step can't be EMPTY!, Please Enter VALID step" + Style.RESET_ALL)
                continue
            
            elif step.isnumeric() == True: # to check if the user typed Number instead of Words
                print(Fore.RED + "Step MUST be words, please enter VALID step using words" + Style.RESET_ALL)
                continue

            elif isinstance(step, str) and step: # to check if the user typed Valid step
                user.progress.append((user.career_path, step))
                try:
                    user.save_progress()
                except Exception :
                    print(Fore.RED + "Unable to save progreess" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Step MUST be words, please enter VALID step using words" + Style.RESET_ALL)

            # to show dynamic animation for progress
            for _ in tqdm(range(100), desc="Updating progress", ncols=75):
                time.sleep(0.025)


            print()#to keep space between lines to read with ease
            print(Fore.GREEN + f"Updated Progress For {roadmap.careers[user.career_path]}: {step}" + Style.RESET_ALL)


def load_user_data(username):
    user = User(username)
    user.load_progress()
    return user



def display_job_info(roadmap, career_path):
    roadmap_info = roadmap.get_roadmap(career_path)
    print(Fore.RED + roadmap_info["title"] + Style.RESET_ALL)

    # Prepare the data for job info table
    job_data = []
    job_description = roadmap_info["job_data"]["Job Description"]
    avg_salary = roadmap_info["job_data"]["Average Salary in USA"]
    
    job_data.append(["Job Description", ', '.join(job_description)])
    job_data.append(["Average Salary", ', '.join(avg_salary)])

    headers = ["Job Information", "Details"]
    
    # Print the job information table
    print(tabulate(job_data, headers=headers, tablefmt="fancy_grid"))
    print()  # Space for readability

def display_resources(roadmap, career_path):
    roadmap_info = roadmap.get_roadmap(career_path)
    print(Fore.MAGENTA + "Study Resources For You IF You Don't Know Where to START!" + Style.RESET_ALL)
    
    # Prepare the data for resources table
    resources_data = []
    
    for subjects, resources in roadmap_info["resources"].items():
        resources_data.append([subjects, ', '.join(resources)])
    
    headers = ["Subject", "Resources"]
    
    # Print the resources table
    print(tabulate(resources_data, headers=headers, tablefmt="fancy_grid"))
    print() 

if __name__=="__main__":
    main()
