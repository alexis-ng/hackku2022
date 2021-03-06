#  CalledIn
*CalledIn is a job matching program meant to connect employers and job seekers in areas without internet & or access to job boards like LinkedIn, Glassdoor, etc*
## About the Project
#### Applicant Side
- Has an automated voice calling system through Twilio
- Take in the voice data and transcribe it
- Matches the skills of the applicant to job posts from corporates
- Sends an SMS/Voice call message with information about the Job opportunities
  
#### Employer Side
- Collaborate with companies to create a job database (through Twilio)
- Matches skills of an applicant pool with job postings


## Built With

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9-blue"></a>  <a href="https://firebase.google.com/"><img src="https://img.shields.io/badge/Firebase-Database-yellow"></a>  <a href="https://nodejs.org/en/"><img src="https://img.shields.io/badge/Node.js-17.8-green"></a>  <a href="https://www.twilio.com/"><img src="https://img.shields.io/badge/Twilio-red"></a>  <a href="https://mapsplatform.google.com/"><img src="https://img.shields.io/badge/Google_Maps-API-darkgreen"></a>

## Installation & Configuration
### Prerequisites
- Have a public hosting site available
- Create a Google [Firebase](Firebase.google.com) account
- Create a [Twilio](twilio.com) account
- Download the following libraries:
```zsh
pip install nltk

pip install firebase-admin

pip install speechRecognition
```
### Twilio hosted on AWS Server
Twillio was used to create an automated calling system that interacts with the job applicants and the companies/job listings. The backend server is hosted on AWS.

### Firestore Database 
Firestore is a real-time NoSQL Database that stores job applicants and listings. It queries based on age, proximity to the job, and qualifications. 

## Usage
To use CalledIn, much of the installation & configuration requirements must be followed in order to use. 
| Configuring Call Fields|
|---------------|
|Create your calling information in [job_seeker.py](https://github.com/alexis-ng/hackku2022/blob/main/job_seeker.py), [job_listing.py](https://github.com/alexis-ng/hackku2022/blob/main/job_listing.py), and [src/database.py](https://github.com/alexis-ng/hackku2022/blob/main/src/database.py). Make sure the fieldnames(member variables) match!|

```python
class JobListing: #employer
    def __init__(self, phone_number) -> None:
        self._phone_number = phone_number
        self._name = ""
        self._min_age = 0
        self._zipcode = 0
        self._keywords = []
        self._description = ""
        self._links = []
class Job_Seeker: #applicant
    def __init__(self, phone_number):
        self._phone_number = phone_number
        self._name = ""
        self._age = 0
        self._zipcode = 0
        self._distance = 0
        self._keywords = []
        self._description = ""
        self._links = {}
```
|Creating Keywords|
|------------------|
|Check out [extract_keywords.py](https://github.com/alexis-ng/hackku2022/blob/main/extract_keywords.py) to set your own configurations. Extract_Keywords uses [nltk](https://www.nltk.org/) toolkit to analyze the transcribed data |


## Authors
Alexis Ng - [@alexis-ng](https://github.com/alexis-ng/) <br>
Bhavik Goplani - [bhavik-goplani](https://github.com/bhavik-goplani)<br>
Suhaan Syed - [SuhaanSyed](https://github.com/SuhaanSyed)<br>
Vinayak Jha - [realVinayak](https://github.com/realVinayak) <br>
