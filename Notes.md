###  What is CI/CD Pipeline ?
CI/CD pipeline Stands for Continuous Integration/Continuos Deployment Pipeline.
It's a series of automated steps that help software developers build , test and deploy their application quickly and reliably.


### CI (Continuous Integration):

Jab developers apne code ko bar-bar ek shared repository (e.g., GitHub) mein daalte hain aur woh code automatically test hota hai.
Iska matlab hai ki code changes ek saath integrate (merge) hote hain, aur errors jaldi detect ho jaate hain.


### CD (Continuous Delivery/Deployment):
# Continuous Delivery: 
Code jab test pass kar leta hai, toh woh automatically ek staging environment (testing ke liye banaya hua system) par ready ho jaata hai.

# Continuous Deployment:
Agar delivery ke baad sab kuch sahi ho, toh code ko automatically live environment (production) mein deploy kar diya jaata hai.



### Pipeline

Is pipeline mein alag-alag steps hote hain jaise:
->Code Build karna
->Tests run karna (Unit tests, Integration tests)
->Deploy karna (staging ya production environment mein)

### Real-Life Example:
Socho tum Flipkart ke developer ho aur tumhe ek naye feature (jaise "Buy Now" button) ko live karna hai.

# Without CI/CD Pipeline: 
Tum manually code ko deploy karoge, testing karoge, aur agar galti hui, toh poori website crash ho sakti hai. Bohot time lagta hai aur galtiyan zyada hoti hain.

# With CI/CD pipeline:
Tum apna code likhte ho, usse GitHub par push karte ho.
-> Pipeline automatically tumhara code build karega, test karega aur agar sab sahi hua, toh staging aur production par deploy kar dega.
-> Agar koi bug hai, toh woh pipeline ke testing stage mein hi detect ho jayega aur deployment ruk jayega.

### File names in the CI/CD Pipeline:
.github/workflows
src/LinkLNS
tests
.gitignore
LICENSE
README.md
init_setup.sh
pyproject.toml
requirements.txt
requirements_dev.txt
setup.cfg
setup.py
template.py
tox.ini



### .github/workflows

# Role: 
ye folder GitHub Actions ke liye hai, jo tumhari CI/CD pipeline ko automate karte hain.
# Kaam kya hai?
Is folder mein tum workflows banate ho (e.g., YAML files) jo yeh decide karte hain ki jab tum code push karte ho ya pull request banate ho, toh kaunsa action automate hoga (e.g., tests chalana, deployment karna, etc.).
Example: Tum push karte hi automatic tests run karwane chahte ho, toh uska workflow .github/workflows folder mein save hota hai.

# --- What is that Pushing and Pulling the code

# Git Push
Git push ka matlab hai aapke local changes ko remote repository mein bhej dena. Jab aap kuch naya code likhte hain aur use commit karte hain, toh woh sirf aapke computer par hota hai. Push karne se woh changes GitHub jaise remote server par chale jaate hain, jisse doosre log bhi unhe dekh aur use kar sakte hain

# Git Pull
Git pull ka matlab hai remote repository se latest changes ko apne local system par le aana. Yeh do cheezon ka combination hai:
git fetch: Remote se new changes download karta hai
git merge: Un changes ko aapke local code mein merge kar deta hai

### src/LinkLNS
# Role: 
Yeh tumhare project ka main source code hota hai.
# Kaam kya hai?
src/YoutubePackage ke andar tum apna core logic aur features ka code likhte ho jo tumhara project perform karega.
Example: Agar tum ek calculator app bana rahe ho, toh src/LinkLNS ke andar tum addition, subtraction, etc. ka code likhoge.





### tests
# Role: 
Yeh folder testing ke liye hai, jahaan tum apne code ko verify karte ho.
# Kaam kya hai?
Is folder mein tum unit tests aur integration tests likhte ho, jo ensure karte hain ki tumhara code sahi kaam kar raha hai ya nahi.
# --- Unit Tests: 
Chhoti-chhoti functionalities ko test karte hain.
# --- Integration Tests: 
Alag-alag modules ko ek saath kaam karte hue test karte hain.
# Example: 
Agar tum addition function banate ho, toh test file mein check karoge ki add(2, 3) ka output 5 aa raha hai ya nahi.



### .gitignore
# Role: 
Git ko batata hai ki kaunse files ya folders ko track nahi karna hai.
# Kaam kya hai?
Kuch files ko version control (Git) mein nahi daala jaata, jaise:
->Temporary files (.pyc, __pycache__)
->API keys ya passwords
->Large log files
# Example: 
Agar tumhari project folder mein temp.log hai, aur tum chahte ho ki woh GitHub par upload na ho, toh uska naam .gitignore file mein daal do.



###  LICENSE
# Role: 
Yeh file tumhare project ka legal agreement define karti hai.
# Kaam kya hai?
Is file mein tum batate ho ki tumhara code kaise use ho sakta hai.
Open-source hoga ya nahi?
Log tumhara code modify kar sakte hain ya nahi?
# Example: 
Agar tum MIT License use karte ho, toh log tumhara code free mein use aur modify kar sakte hain.



### README.md
# Role:
 Yeh tumhare project ka introduction aur documentation hota hai.
# Kaam kya hai?
Is file mein tum project ke baare mein basic details likhte ho:
Project ka purpose kya hai?
Kaise install karein?
Kaise use karein?
# Example: 
Agar tum ek weather app bana rahe ho, toh README file mein tum instructions likhoge jaise:
"Install Python"
"Run app.py to see the weather."


### init_setup.sh
# Role: 
Yeh ek setup script hai jo tumhare project ka initial setup karta hai.
# Kaam kya hai?
Is file ko run karte hi tumhare system par tumhari project ki dependencies install ho jaati hain ya koi basic configurations ho jaati hain.
Example: Agar tumhe Python packages (requirements.txt) install karne hain, toh init_setup.sh mein command likhi hogi:
 --- > pip install -r requirements.txt


### pyproject.toml

# Role: 
Yeh file tumhare Python project ka configuration file hai.

# Kaam kya hai?

Batata hai ki tumhara project kaunse tools aur dependencies use karega.
Yeh build system ke liye zaruri hota hai.
toml ek file format hai jo Python projects ke liye standardized hai.
Example:
Agar tum pytest aur setuptools use karte ho, toh yeh file define karegi:
  -->   [build-system]
        requires = ["setuptools", "wheel"]
        build-backend = "setuptools.build_meta"


### requirements.txt

# Role: 
Yeh file tumhare project ke necessary dependencies (libraries) ki list rakhti hai.

# Kaam kya hai?
Is file mein woh libraries likhi hoti hain jo tumhare project ke chalne ke liye zaruri hain. Jab tum kisi naye system mein project run karoge, yeh file use karke sari dependencies install ho jaayengi.


### Differences Betweeen Requirements.txt and pyproject.toml:



#                                               Dependency Resolution:
                                pyproject.toml: Build time par dependencies resolve hoti hain, jo ki flexible hota hai lekin exact reproducibility guarantee nahi karta.
                                requirements.txt: Exact pinned versions provide karta hai, jo ki CI/CD mein consistency ensure karta hai5.
#                                                Build vs Deployment:
                                pyproject.toml: Package building aur distribution ke liye behtar hai.
                                requirements.txt: Deployment environments aur CI/CD pipelines mein exact environment recreate karne ke liye zyada suitable hai.
#                                               Flexibility vs Stability:
                                pyproject.toml: Development mein zyada flexible hota hai, lekin CI/CD mein variability introduce kar sakta hai.
                                requirements.txt: CI/CD mein stability provide karta hai, kyunki har bar exact same versions install hoti hai.
#                                                Usage in Pipeline:
                                pyproject.toml: Package building ya testing stages mein use ho sakta hai.
                                requirements.txt: Typically environment setup ya dependency installation steps mein use hota hai.
            
            
            
            Conclusion mein, dono files ka apna-apna mahatva hai CI/CD pipeline mein. pyproject.toml project definition aur building ke liye use hota hai, jabki requirements.txt consistent aur reproducible environments ensure karne ke liye istemal hota hai, jo ki CI/CD pipelines mein crucial hota hai




### requirements_dev.txt:


# Role: 
Yeh file development ke time required dependencies ko list karti hai.
# Kaam kya hai?
Yeh un libraries ka list rakhti hai jo sirf development ke liye chahiye hoti hain, production ke liye nahi.
# Example: 
Testing libraries jaise pytest ya mypy ka use tum production mein nahi karte ho, lekin development ke waqt chahiye hote hain.


### setup.cfg
# Role: 
Yeh tumhare Python package ke configuration details rakhta hai.
# Kaam kya hai?
Yeh file tumhare project ke metadata (e.g., name, version, author, etc.) aur installation instructions define karti hai.
Yeh setup.py ke kaam ko simplify karne ke liye use hoti hai.

### setup.py
# Role: 
Yeh file tumhare project ko ek installable package banati hai.
# Kaam kya hai?
Is file ke through tum apne project ko kisi aur system par install kar sakte ho.
Yehi file batati hai ki tumhara code kaise package hoke install hoga.



### template.py
# Role: 
Yeh file ek starting template hai, jo tumhare project mein frequently repeat hone wala code rakhti hai.
# Kaam kya hai?
Tum kisi functionality ke liye ek base template bana ke rakho, jo baar-baar use ho sake.
Isse tumhara kaam faster aur standardized ho jaata hai



### tox.ini
# Role: 
Yeh file testing automation tool tox ka configuration rakhti hai.
# Kaam kya hai?
Alag-alag Python environments (e.g., Python 3.7, 3.8) ke liye tumhare tests automate karne mein help karta hai.
Tum is file mein define karte ho ki kaunse tests run karne hain aur kis environment mein.




### Difference Between setup.cfg and setup.py




#                   setup.cfg	                                                         setup.py
A configuration file for your Python project.	                       A Python script for defining how to package the project.
Written in a declarative format (no Python code).	                   Written in Python code (imperative format).
Stores project metadata like name, version, author, etc.	           Includes logic for packaging and installing the project.
Simplifies the process by separating configuration from code.	       Used for more complex setups where logic or dynamic conditions are needed




### Difference Between template.py vs Other Files




#                       template.py	                                                                 Other Files
A custom Python script that acts as a code template for your project.	       Other files focus on project configuration, dependencies, or automation. 
Contains reusable boilerplate code (e.g., a main() function).	               Deals with the technical structure and dependencies of your project.





### Difference Between tox.ini vs requirements.txt vs requirements_dev.txt



# tox.ini:	
Automates testing across multiple Python environments and dependencies.
# requirements.txt:	
Lists libraries and versions required to run the project.
# requirements_dev.txt:
Lists libraries needed for development purposes (e.g., testing tools).




### Summaray 


                                                                setup.cfg:	Declarative configuration for the project (metadata, package details).
                                                                setup.py:	 Imperative script for packaging and installation (dynamic logic allowed).
                                                                template.py: 	Custom Python script with reusable boilerplate code.
                                                                tox.ini: 	Configuration for running tests across environments.
                                                                requirements.txt:	Lists libraries needed to run the project (runtime dependencies).
                                                                requirements_dev.txt:	Lists libraries needed for development only (e.g., testing tools).
                                         



