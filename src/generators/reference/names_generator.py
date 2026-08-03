"""
=========================================================
ShopSphere Analytics
names_generator.py

Generates

first_names_male.csv
first_names_female.csv
last_names.csv
email_domains.csv

=========================================================
"""

import pandas as pd

from config.config import REFERENCE_DATA

"""
=========================================================
Email Domains
=========================================================
"""
EMAIL_DOMAINS = [

    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "icloud.com",
    "proton.me",
    "rediffmail.com",
    "zoho.com",
    "live.com",
    "aol.com",

    "example.com",
    "mail.com",
    "inbox.com",
    "fastmail.com",
    "gmx.com",

    "company.in",
    "tech.in",
    "india.com",
    "student.edu",
    "business.in"

]

"""
=========================================================
Male Names
=========================================================
"""
MALE_NAMES = [
    "Rahul", "Amit", "Rohit", "Prasanta", "Ankit", "Sourav", "Abhishek", "Ajay", "Akash", "Akshay",
    "Vikram", "Manoj", "Kunal", "Ramesh", "Sandeep", "Nikhil", "Deepak", "Arjun", "Varun", "Rajesh",
    "Sunil", "Harsh", "Yash", "Sameer", "Gaurav", "Santosh", "Pankaj", "Hemant", "Shivam", "Lokesh",
    "Anand", "Devendra", "Kartik", "Omkar", "Raghav", "Siddharth", "Vivek", "Chirag", "Naveen", "Ashish",
    "Pradeep", "Ravi", "Suraj", "Mahesh", "Narendra", "Balaji", "Vinod", "Mohan", "Krishna", "Shankar",
    "Aarav", "Vihaan", "Reyansh", "Advait", "Aryan", "Darshan", "Hrithik", "Kabir", "Manan", "Parth",
    "Rudra", "Shivansh", "Tanmay", "Uday", "Viraj", "Yuvraj", "Zubin", "Bhavesh", "Chaitanya", "Dinesh",
    "Eshan", "Farhan", "Girish", "Harshit", "Indrajit", "Jayant", "Keshav", "Lakshya", "Madhav", "Naman",
    "Ojas", "Pranay", "Raghunath", "Saket", "Tushar", "Ujjwal", "Vishal", "Yogesh", "Zeeshan", "Alok",
    "Bharat", "Chetan", "Dilip", "Eklavya", "Feroz", "Gopal", "Hanuman", "Ishaan", "Jagat", "Kiran",
    "Lalit", "Mukul", "Nitin", "Omprakash", "Prakash", "Qasim", "Rajiv", "Suresh", "Tarun", "Umesh",
    "Vimal", "Wasim", "Xavier", "Yatin", "Zahir", "Abhay", "Bhaskar", "Chandan", "Dharma", "Eshwar",
    "Faisal", "Govind", "Harendra", "Irfan", "Jitendra", "Kailash", "Laxman", "Mohanlal", "Nagesh", "Onkar",
    "Prithvi", "Rameshwar", "Shyam", "Trilok", "Uttam", "Vidyut", "Waman", "Yogendra", "Zorawar",
    "Abhinav", "Aditya", "Akhil", "Alokesh", "Amar", "Animesh", "Anirban", "Anirudh", "Anmol", "Anshul",
    "Arvind", "Ashutosh", "Atul", "Avinash", "Ayush", "Basant", "Bhanu", "Bhuvan", "Chiranjeev", "Damodar",
    "Debashish", "Deependra", "Dhananjay", "Dipankar", "Durgesh", "Gautam", "Giridhar", "Harendra", "Hemendra", "Inder",
    "Ishan", "Jagdish", "Jatin", "Jayesh", "Jeevan", "Jitendra", "Kalyan", "Kamlesh", "Kanishk", "Kapil",
    "Kartikeya", "Keshava", "Kiranraj", "Kuldeep", "Lakhan", "Lalitendra", "Laxmikant", "Madhukar", "Mahendra", "Manish",
    "Mayank", "Milind", "Mithun", "Mukesh", "Naresh", "Navin", "Naveendra", "Nikhilesh", "Niranjan", "Nitesh",
    "Omveer", "Padmanabhan", "Parmesh", "Prabhat", "Pradeesh", "Pradyumna", "Prakashan", "Pranav", "Prashant", "Prem",
    "Pushkar", "Raghunandan", "Rajendra", "Rajivraj", "Ramakant", "Rameshwaran", "Ranjan", "Ravindra", "Sachin", "Sagar",
    "Sahil", "Sajjan", "Saketraj", "Samir", "Sandeepan", "Sanjay", "Sanket", "Santoshraj", "Sarvesh", "Satish",
    "Shailendra", "Shantanu", "Sharad", "Shashank", "Shivendra", "Shobhit", "Shravan", "Shyamraj", "Siddhesh", "Somnath",
    "Subhash", "Sudhir", "Sujal", "Sukhdev", "Sumeet", "Sunendra", "Surendra", "Suryakant", "Swapnil", "Tanveer",
    "Tejas", "Trilochan", "Udayraj", "Ujjwalraj", "Umang", "Upendra", "Vaibhav", "Vasant", "Vedant", "Veer",
    "Venkatesh", "Vibhor", "Vidyadhar", "Vignesh", "Vikrant", "Vinay", "Vineet", "Virendra", "Vishesh", "Vishnu",
    "Vishwajeet", "Vivekanand", "Yograj", "Yuvrajraj", "Zubinraj",
    "Abhijit", "Achyut", "Adarsh", "Ajinkya", "Akshat", "Amrit", "Aniket", "Anirudhraj", "Ankitraj", "Ansh",
    "Arnav", "Ashwin", "Atman", "Avik", "Ayushman", "Bhuvanesh", "Chandresh", "Darshanraj", "Debjit", "Dev",
    "Dheeraj", "Dipesh", "Divyansh", "Durga", "Gagan", "Ganesh", "Girishraj", "Harshad", "Hemraj", "Indrajeet",
    "Ishwar", "Jagannath", "Jayanth", "Jeevanraj", "Jignesh", "Kamal", "Kanishka", "Karthik", "Keshavan", "Kiranraj",
    "Krishnendu", "Kulraj", "Lakshmanraj", "Lalitraj", "Laxmikumar", "Madhusudan", "Mahadev", "Manojraj", "Mayur", "Milindraj",
    "Mithilesh", "Mukund", "Nandan", "Naveenraj", "Nikhilraj", "Nirav", "Nirmal", "Niteshraj", "Omkarraj", "Padmanabh",
    "Parag", "Parmeshwar", "Prabhu", "Pradyot", "Prakashraj", "Pranesh", "Prashantraj", "Premraj", "Pushpendra", "Raghavendra",
    "Rajaram", "Rajeev", "Rajkumar", "Ramakrishna", "Rameshraj", "Ranjit", "Ravindraj", "Sachindra", "Sagarraj", "Sahilraj",
    "Sajid", "Saketesh", "Samarth", "Sandeepraj", "Sanjiv", "Sanketraj", "Santoshkumar", "Saroj", "Satyanarayan", "Shailesh",
    "Shantiraj", "Sharadraj", "Shashiraj", "Shivraj", "Shobhan", "Shridhar", "Shyamkumar", "Siddhant", "Somesh", "Subodh",
    "Sudhakar", "Sujit", "Sukumar", "Sumit", "Sunilraj", "Surajraj", "Suryanarayan", "Swapnesh", "Tanay", "Tejraj",
    "Trilokesh", "Udaykumar", "Ujjwalraj", "Umrao", "Upendraraj", "Vaishnav", "Vamshi", "Varadaraj", "Vedraj", "Veeresh",
    "Venkataraj", "Vibhorraj", "Vidyutraj", "Vigneshraj", "Vikramraj", "Vinayraj", "Vineetraj", "Virajraj", "Vishalraj", "Vishnukumar",
    "Vishwesh", "Vivekraj", "Yogeshraj", "Yuvrajkumar", "Zubair",
    "Abhayraj", "Achint", "Adityaraj", "Ajayraj", "Akashraj", "Amol", "Anandraj", "Anil", "Aniraj", "Ankitkumar",
    "Anshuman", "Arindam", "Arun", "Ashok", "Atulraj", "Avinashraj", "Ayushraj", "Baldev", "Bhaskarraj", "Chandanraj",
    "Chaturbhuj", "Damodarraj", "Darshanesh", "Debraj", "Devraj", "Dhanraj", "Dilipraj", "Dipak", "Durairaj", "Ganpat",
    "Gopalraj", "Govindraj", "Harinarayan", "Harshraj", "Hemantraj", "Indraj", "Ishwarraj", "Jagatraj", "Jairaj", "Jitendraraj",
    "Kailashraj", "Kamalraj", "Kanishkaraj", "Karthikraj", "Keshavraj", "Kiranesh", "Krishnaraj", "Kuldeepraj", "Lakshmanesh", "Lalitkumar",
    "Laxmanraj", "Madhavrao", "Maheshraj", "Manik", "Manojkumar", "Mayankraj", "Milindra", "Mithunraj", "Mukeshraj", "Nareshraj",
    "Naveenkumar", "Nikhilkumar", "Niranjanraj", "Niteshkumar", "Omprakashraj", "Padmaraj", "Parmeshraj", "Prabhakar", "Pradeepraj", "Pradyumn",
    "Prakashkumar", "Pranavraj", "Prashantraj", "Premkumar", "Pushpendraraj", "Raghunathraj", "Rajeevkumar", "Rajkumarraj", "Ramakrishnan", "Rameshkumar",
    "Ranjanraj", "Ravindrakumar", "Sachinraj", "Sagaraj", "Sahilraj", "Sajidraj", "Saketkumar", "Samirraj", "Sandeepkumar", "Sanjayraj",
    "Sanketkumar", "Santoshkumarraj", "Sarveshkumar", "Satishraj", "Shailendrakumar", "Shantiraj", "Sharadkumar", "Shashankraj", "Shivkumar", "Shobhitraj",
    "Shravanraj", "Shyamrajkumar", "Siddheshraj", "Somnathraj", "Subhashraj", "Sudhirraj", "Sujalraj", "Sukhdevraj", "Sumeetraj", "Sunilkumar",
    "Surendrakumar", "Suryakumar", "Swapnilraj", "Tanveerraj", "Tejaskumar", "Trilokraj", "Udayrajkumar", "Ujjwalrajkumar", "Umangraj", "Upendrakumar",
    "Vaibhavraj", "Vasantraj", "Vedantraj", "Veerkumar", "Venkateshkumar", "Vibhorrajkumar", "Vidyadharraj", "Vigneshkumar", "Vikramkumar", "Vinaykumar",
    "Vineetkumar", "Virendrakumar", "Visheshraj", "Vishnukumarraj", "Vishwajeetraj", "Vivekanandraj", "Yograjkumar", "Yuvrajkumarraj", "Zubairraj",
    
]


"""
=========================================================
Female Names
=========================================================
"""

FEMALE_NAMES = [
    "Priya", "Sneha", "Pooja", "Neha", "Ananya", "Riya", "Anjali", "Kavita", "Megha", "Shreya",
    "Aarti", "Divya", "Sonal", "Nisha", "Komal", "Swati", "Preeti", "Rashmi", "Bhavna", "Kiran",
    "Manisha", "Sapna", "Payal", "Jyoti", "Tanvi", "Ishita", "Simran", "Kirti", "Madhuri", "Rekha",
    "Sangeeta", "Rajni", "Alka", "Chhavi", "Deepa", "Geeta", "Indira", "Kalpana", "Lata", "Maya",
    "Namrata", "Pallavi", "Ritika", "Suhani", "Trisha", "Vaishnavi", "Vidya", "Yamini", "Zoya", "Ayesha",
    "Farah", "Hina", "Jaya", "Kajal", "Leena", "Monika", "Nandini", "Oviya", "Parul", "Renu",
    "Sita", "Tanuja", "Uma", "Varsha", "Winnie", "Xara", "Yashika", "Zeenat", "Amrita", "Barkha",
    "Charu", "Damini", "Ekta", "Falguni", "Gargi", "Hemlata", "Indu", "Juhi", "Kanika", "Lavanya",
    "Mitali", "Naina", "Ojasvi", "Prerna", "Roshni", "Shalini", "Tanya", "Urvashi", "Vandana", "Yogita",
    "Aakriti", "Bhawna", "Chitra", "Diksha", "Esha", "Garima", "Harsha", "Ipsita", "Jhanvi", "Khushi",
    "Laxmi", "Mona", "Nikita", "Oorja", "Padmini", "Rupali", "Sakshi", "Tara", "Usha", "Vasudha",
    "Anushka", "Bhavika", "Chandni", "Devika", "Elina", "Gitanjali", "Heena", "Ira", "Jasleen", "Kashish",
    "Lekha", "Mansi", "Navya", "Ovi", "Pragya", "Rhea", "Shweta", "Twinkle", "Urmi", "Vibha",
    "Aarohi", "Bhavana", "Chanchal", "Deepali", "Eshita", "Gauri", "Harini", "Ishani", "Jagruti", "Kalpita",
    "Lalita", "Madhavi", "Nirmala", "Oviya", "Padma", "Ragini", "Sanjana", "Tanu", "Ujjwala", "Vasanti",
    "Anitha", "Bina", "Chaya", "Damayanti", "Elina", "Gopika", "Hemangi", "Indira", "Jaya", "Kamini",
    "Leela", "Mala", "Nalini", "Oorja", "Pavitra", "Rupashi", "Sarika", "Triveni", "Uma", "Vidhi",
    "Aditi", "Bhargavi", "Chandrika", "Devanshi", "Esha", "Gayatri", "Hema", "Ira", "Jahnavi", "Kanchan",
    "Laxmi", "Manjari", "Nandita", "Ojasvi", "Pratibha", "Roshni", "Shivani", "Tanushree", "Urmila", "Vibha",
    "Anushree", "Binita", "Chhaya", "Dipti", "Ekisha", "Gitanjali", "Harsha", "Indu", "Juhi", "Kavya",
    "Lopamudra", "Mitali", "Nikita", "Omisha", "Poonam", "Ritika", "Sushma", "Tara", "Usha", "Vaidehi",
    "Amisha", "Barkha", "Charulata", "Darshana", "Evelyn", "Gulnaz", "Hiral", "Ipsita", "Jasmin", "Kiranmayi",
    "Lavanya", "Meenakshi", "Nisha", "Oorvi", "Prerna", "Radhika", "Snehal", "Tanya", "Vandana", "Yamini",
    "Aakanksha", "Bhavini", "Chitra", "Dimple", "Eshwari", "Gargi", "Hemlata", "Ishika", "Jhanvi", "Kajal",
    "Lalima", "Mona", "Navya", "Ovi", "Pallavi", "Reshma", "Shreya", "Twinkle", "Vaishali", "Zoya",
    "Aaradhya", "Bhagyashree", "Chandana", "Devika", "Eshani", "Gopali", "Hina", "Ishitha", "Jasleen", "Kashish",
    "Lekha", "Mansi", "Naina", "Oorja", "Pragya", "Rhea", "Shruti", "Tanvi", "Urvi", "Vasudha",
    "Ananya", "Bhumika", "Chandni", "Diksha", "Elisha", "Gauri", "Heena", "Ira", "Jaya", "Kalyani",
    "Lata", "Madhuri", "Nandini", "Oviya", "Pooja", "Renu", "Sakshi", "Tanuja", "Uma", "Vidya",
    "Amrita", "Bhavna", "Chhavi", "Divya", "Ekta", "Geeta", "Harini", "Indira", "Jyoti", "Kavita",
    "Leena", "Megha", "Neha", "Ojasvi", "Parul", "Rashmi", "Simran", "Trisha", "Urvashi", "Vaishnavi",
    "Aarti", "Binita", "Charu", "Damini", "Esha", "Garima", "Hiral", "Ipshita", "Kiran", "Lavina",
    "Mala", "Nirmala", "Omisha", "Padmini", "Ritika", "Shalini", "Sonal", "Tara", "Usha", "Vibha",
    "Anjali", "Barkha", "Chandrika", "Deepa", "Elina", "Gulnaz", "Hemangi", "Ishita", "Juhi", "Kanika",
    "Lopamudra", "Mitali", "Nikita", "Oorvi", "Pallavi", "Roshni", "Sneha", "Twinkle", "Vandana", "Yogita",
  
    "Aarohi", "Bhavana", "Chanchal", "Deepika", "Eshita", "Gauri", "Harini", "Ishani", "Jagruti", "Kalpita",
    "Lalita", "Madhavi", "Nirmala", "Oviya", "Padma", "Ragini", "Sanjana", "Tanu", "Ujjwala", "Vasanti",
    "Anitha", "Bina", "Chaya", "Damayanti", "Elina", "Gopika", "Hemangi", "Indira", "Jaya", "Kamini",
    "Leela", "Mala", "Nalini", "Oorja", "Pavitra", "Rupashi", "Sarika", "Triveni", "Uma", "Vidhi",
    "Aditi", "Bhargavi", "Chandrika", "Devanshi", "Esha", "Gayatri", "Hema", "Ira", "Jahnavi", "Kanchan",
    "Laxmi", "Manjari", "Nandita", "Ojasvi", "Pratibha", "Roshni", "Shivani", "Tanushree", "Urmila", "Vibha",
    "Anushree", "Binita", "Chhaya", "Dipti", "Ekisha", "Gitanjali", "Harsha", "Indu", "Juhi", "Kavya",
    "Lopamudra", "Mitali", "Nikita", "Omisha", "Poonam", "Ritika", "Sushma", "Tara", "Usha", "Vaidehi",
    "Amisha", "Barkha", "Charulata", "Darshana", "Evelyn", "Gulnaz", "Hiral", "Ipsita", "Jasmin", "Kiranmayi",
    "Lavanya", "Meenakshi", "Nisha", "Oorvi", "Prerna", "Radhika", "Snehal", "Tanya", "Vandana", "Yamini",
    "Aakanksha", "Bhavini", "Chitra", "Dimple", "Eshwari", "Gargi", "Hemlata", "Ishika", "Jhanvi", "Kajal",
    "Lalima", "Mona", "Navya", "Ovi", "Pallavi", "Reshma", "Shreya", "Twinkle", "Vaishali", "Zoya",
    "Aaradhya", "Bhagyashree", "Chandana", "Devika", "Eshani", "Gopali", "Hina", "Ishitha", "Jasleen", "Kashish",
    "Lekha", "Mansi", "Naina", "Oorja", "Pragya", "Rhea", "Shruti", "Tanvi", "Urvi", "Vasudha",
    "Ananya", "Bhumika", "Chandni", "Diksha", "Elisha", "Gauri", "Heena", "Ira", "Jaya", "Kalyani",
    "Lata", "Madhuri", "Nandini", "Oviya", "Pooja", "Renu", "Sakshi", "Tanuja", "Uma", "Vidya",
    "Amrita", "Bhavna", "Chhavi", "Divya", "Ekta", "Geeta", "Harini", "Indira", "Jyoti", "Kavita",
    "Leena", "Megha", "Neha", "Ojasvi", "Parul", "Rashmi", "Simran", "Trisha", "Urvashi", "Vaishnavi",
    "Aarti", "Binita", "Charu", "Damini", "Esha", "Garima", "Hiral", "Ipshita", "Kiran", "Lavina",
    "Mala", "Nirmala", "Omisha", "Padmini", "Ritika", "Shalini", "Sonal", "Tara", "Usha", "Vibha",
    "Anjali", "Barkha", "Chandrika", "Deepa", "Elina", "Gulnaz", "Hemangi", "Ishita", "Juhi", "Kanika",
    "Lopamudra", "Mitali", "Nikita", "Oorvi", "Pallavi", "Roshni", "Sneha", "Twinkle", "Vandana", "Yogita"
 
]

"""
=========================================================
Last Names
=========================================================
"""
LAST_NAMES = [
    "Sharma", "Das", "Deb", "Roy", "Gupta", "Patel", "Singh", "Kumar", "Verma", "Dutta",
    "Banerjee", "Mukherjee", "Chatterjee", "Bhattacharya", "Ghosh", "Sengupta", "Chakraborty", "Bose", "Sen", "Mitra",
    "Saha", "Chowdhury", "Ray", "Majumdar", "Nair", "Menon", "Pillai", "Iyer", "Reddy", "Naidu",
    "Shetty", "Pai", "Shenoy", "Desai", "Joshi", "Kulkarni", "Gadkari", "Bhat", "Hegde", "Kamat",
    "Pandey", "Tripathi", "Mishra", "Tiwari", "Dwivedi", "Chaturvedi", "Upadhyay", "Shukla", "Pathak", "Rastogi",
    "Saxena", "Mathur", "Tyagi", "Nigam", "Srivastava", "Agarwal", "Goel", "Jain", "Khandelwal", "Maheshwari",
    "Mehta", "Kapoor", "Khanna", "Malhotra", "Bhatia", "Arora", "Gill", "Sidhu", "Sandhu", "Dhillon",
    "Brar", "Grewal", "Pannu", "Randhawa", "Mann", "Chahal", "Sekhon", "Bains", "Toor", "Virdee",
    "Ahluwalia", "Sodhi", "Sethi", "Grover", "Anand", "Chopra", "Suri", "Talwar", "Bajaj", "Sawhney",
    "Kohli", "Sachdev", "Luthra", "Monga", "Narang", "Wadhwa", "Bedi", "Sobti", "Tandon", "Vohra",
    "Aggarwal", "Bagchi", "Barua", "Borthakur", "Bhuyan", "Kalita", "Medhi", "Saikia", "Hazarika", "Deka",
    "Phukan", "Rajkhowa", "Bora", "Konwar", "Gogoi", "Chetia", "Borpujari", "Talukdar", "Sarma", "Baruah",
    "Banik", "Pal", "Mondal", "Halder", "Sarkar", "Karmakar", "Dasgupta", "Chakrabarti", "Bhattacharjee", "Choudhury",
    "Barman", "Biswas", "Pramanik", "Adhikari", "Kundu", "Naskar", "Ganguly", "Lodh", "Senapati", "Samanta",
    "Mahato", "Hansda", "Murmu", "Soren", "Tudu", "Kisku", "Munda", "Oraon", "Lakra", "Ekka",
    "Toppo", "Kerketta", "Kujur", "Barla", "Minz", "Dhanwar", "Bhagat", "Pahan", "Beshra", "Bara",
    "Poddar", "Basu", "Datta", "Chanda", "Chakma", "Reang", "Tripura", "Debbarma", "Jamatia", "Koloi",
    "Lal", "Rawat", "Negi", "Bisht", "Kandpal", "Pant", "Joshi", "Bhandari", "Thapa", "Rana",
    "Karki", "Tamang", "Lama", "Sherpa", "Gurung", "Magar", "Chhetri", "Bhujel", "Rai", "Subba",
    "Pradhan", "Chettri", "Maharjan", "Shrestha", "Manandhar", "Tuladhar", "Maskey", "Singhdeo", "Rajput", "Chauhan",
    "Solanki", "Parmar", "Gohil", "Jadeja", "Sisodia", "Tomar", "Bundela", "Bais", "Bhadoria", "Kachhwaha",
    "Pawar", "Shinde", "Deshmukh", "Gaikwad", "Jadhav", "Kadam", "More", "Nikam", "Patil", "Raut",
    "Salunkhe", "Sawant", "Thorat", "Wagh", "Yadav", "Ahir", "Chaudhary", "Jat", "Dahiya", "Sangwan",
    "Malik", "Hooda", "Kadian", "Dalal", "Nain", "Panghal", "Rathi", "Tanwar", "Jakhar", "Beniwal",
    "Balyan", "Dhankar", "Faujdar", "Gulia", "Khatri", "Bansal", "Mittal", "Nagpal", "Rohilla", "Sikka",
    "Bhardwaj", "Kaushik", "Dahiya", "Bhargava", "Chandel", "Thakur", "Rawal", "Solanki", "Raghuwanshi", "Rajvanshi",
    "Singhania", "Oswal", "Porwal", "Lodha", "Bagmar", "Bafna", "Choradia", "Kothari", "Tapadia", "Sarda",
    "Bhansali", "Kedia", "Nahata", "Pansari", "Ranka", "Sanghvi", "Shah", "Vora", "Zaveri", "Modi",
    "Ambani", "Adani", "Birla", "Tata", "Godrej", "Mahindra", "Kirloskar", "Jindal", "Mittal", "Goenka"

    "Acharya", "Acharjee", "Adhikari", "Agnihotri", "Alam", "Ali", "Amarnath", "Amble", "Anand", "Angadi",
    "Annadurai", "Antony", "Aravind", "Arul", "Arya", "Ashraf", "Azad", "Babu", "Baghel", "Bahadur",
    "Bajpai", "Bakshi", "Balakrishnan", "Balasubramanian", "Bali", "Banerjee", "Bangar", "Baral", "Barik", "Barman",
    "Barua", "Basu", "Bedi", "Behera", "Belurkar", "Bendre", "Beniwal", "Bhagat", "Bhalla", "Bhandarkar",
    "Bhandari", "Bharadwaj", "Bhardwaj", "Bhargava", "Bhaskar", "Bhat", "Bhatia", "Bhatnagar", "Bhattacharjee", "Bhattacharya",
    "Bhatti", "Bhavsar", "Bhonsle", "Bhosale", "Bisht", "Biswas", "Biyani", "Bora", "Borpujari", "Bose",
    "Budhwar", "Bulchandani", "Butalia", "Chadha", "Chakrabarti", "Chakraborty", "Chandel", "Chandra", "Chandran", "Chandrashekar",
    "Chaudhari", "Chaudhary", "Chaudhuri", "Chavan", "Chawla", "Chhabra", "Chhibber", "Chopra", "Choudhary", "Choudhury",
    "Chowdhury", "Chugh", "Dalal", "Dalvi", "Damle", "Dandekar", "Daniel", "Dasgupta", "Datta", "Dave",
    "Dayal", "Debbarma", "Debnath", "Deshmukh", "Deshpande", "Devaraj", "Devgan", "Dey", "Dhaliwal", "Dhamija",
    "Dhanraj", "Dhawan", "Dholakia", "Dhruv", "Dhull", "Dhungana", "Dixit", "Dubey", "Duggal", "Dutt",
    "Dwivedi", "Ediga", "Eknath", "Elangovan", "Emmanuel", "Eshwar", "Fadnavis", "Fakir", "Farooq", "Fateh",
    "Fernandes", "Francis", "Gade", "Gajjar", "Gandhi", "Ganesh", "Ganorkar", "Gaonkar", "Garg", "Gavaskar",
    "Gawande", "Gawli", "George", "Ghoshal", "Gokhale", "Gomathi", "Gopal", "Gopalan", "Goswami", "Gowda",
    "Goyal", "Gujar", "Gupta", "Gurung", "Gyawali", "Haider", "Haldar", "Halder", "Hameed", "Hegde",
    "Hemraj", "Hooda", "Hussain", "Ibrahim", "Ilyas", "Indrajeet", "Ingle", "Isaac", "Iyengar", "Iyer",
    "Jadhav", "Jagannath", "Jain", "Jaiswal", "Jani", "Jat", "Jatav", "Jha", "Jhaveri", "Jindal",
    "Joseph", "Joshi", "Kadam", "Kailash", "Kaimal", "Kakade", "Kalita", "Kamble", "Kamra", "Kanchan",
    "Kandpal", "Kannan", "Kansal", "Kant", "Kapadia", "Kapoor", "Kar", "Karan", "Karnik", "Karpe",
    "Karthik", "Karun", "Kasliwal", "Kashyap", "Kathuria", "Katkar", "Katyal", "Kaul", "Kavoor", "Kazi",
    "Keerthi", "Kelkar", "Keni", "Keshri", "Khan", "Khanna", "Kharbanda", "Khatri", "Khedkar", "Kher",
    "Khobragade", "Khot", "Khullar", "Khurana", "Khurasiya", "Kiran", "Kirloskar", "Kishore", "Kohli", "Kolhe",
    "Konda", "Konwar", "Koppikar", "Koranne", "Koshy", "Kotwal", "Koul", "Krishnan", "Kulkarni", "Kumar",
    "Kumawat", "Kumbhar", "Kundra", "Kunwar", "Kurien", "Kurmi", "Kushwaha", "Kutty", "Lad", "Lahiri",
    "Lakra", "Lal", "Lama", "Lanjewar", "Laskar", "Lata", "Lather", "Laxman", "Lodha", "Lokhande",
    "Lonkar", "Lulla", "Madan", "Madhavan", "Mahajan", "Mahanta", "Mahapatra", "Mahato", "Maheshwari", "Malhotra",
    "Malik", "Mallik", "Malviya", "Mandal", "Mani", "Maniar", "Manjhi", "Manohar", "Manral", "Mansingh",
    "Mantri", "Marathe", "Marwah", "Masih", "Mathur", "Matondkar", "Maurya", "Meena", "Mehta", "Menon"
    "Menon", "Merchant", "Meshram", "Mewara", "Mhatre", "Mishra", "Misra", "Mittal", "Modak", "Modi",
    "Mohanty", "Mokashi", "Mondal", "Monga", "Moni", "Moolchandani", "Moorthy", "Mori", "Mote", "Motwani",
    "Mughal", "Mukerjee", "Mukesh", "Mukherjee", "Mullick", "Mundra", "Muni", "Munshi", "Murmu", "Murthy",
    "Mutha", "Nadar", "Nagar", "Nagpal", "Nair", "Naka", "Nakhate", "Nalawade", "Nambiar", "Namdeo",
    "Nanda", "Nanduri", "Nandy", "Nangia", "Naqvi", "Narain", "Narang", "Narayan", "Narayanan", "Narsingh",
    "Natarajan", "Nath", "Nayak", "Nayar", "Nayyar", "Negi", "Nene", "Nerurkar", "Netha", "Newar",
    "Nichani", "Nigam", "Nikam", "Nilakantan", "Nimbalkar", "Niranjan", "Nirmal", "Nisar", "Nithyanand", "Nizam",
    "Ojha", "Omprakash", "Onkar", "Oommen", "Oswal", "Pachauri", "Padmanabhan", "Padukone", "Pagare", "Pai",
    "Pal", "Palanisamy", "Paliwal", "Pallavi", "Panchal", "Pandey", "Pandit", "Panicker", "Panja", "Pankaj",
    "Pansare", "Pant", "Pappu", "Parab", "Parashar", "Parashuram", "Parikh", "Parmar", "Parthasarathy", "Parulekar",
    "Paswan", "Patankar", "Pathak", "Patil", "Patkar", "Patnaik", "Pattnaik", "Paul", "Pawar", "Payal",
    "Pazhani", "Pegu", "Phadke", "Phanse", "Phatak", "Phukan", "Pillai", "Pingale", "Pinto", "Piplani",
    "Pitre", "Poddar", "Pol", "Poonia", "Poojary", "Porwal", "Prabhu", "Pradhan", "Prakash", "Prasad",
    "Prashar", "Pratap", "Prem", "Premchand", "Pujari", "Punia", "Purohit", "Puri", "Qureshi", "Raghavan",
    "Raghuwanshi", "Rai", "Raj", "Raja", "Rajagopal", "Rajamani", "Rajan", "Rajaram", "Rajasekar", "Rajesh",
    "Rajguru", "Rajput", "Raju", "Ramakrishnan", "Raman", "Ramanathan", "Ramesh", "Rana", "Randhawa", "Ranganathan",
    "Ranjan", "Rao", "Rastogi", "Rathi", "Raval", "Ravindra", "Rawal", "Rawat", "Ray", "Raza",
    "Razdan", "Reddy", "Rege", "Rehman", "Rekhi", "Renu", "Reshamwala", "Reuben", "Reza", "Rizvi",
    "Roy", "Roychowdhury", "Sabharwal", "Sachan", "Sachdeva", "Sachin", "Sachwani", "Sadarangani", "Saha", "Sahai",
    "Sahani", "Sahoo", "Sahu", "Sai", "Saikia", "Saini", "Sakhuja", "Salaria", "Salgaonkar", "Saluja",
    "Samanta", "Sampath", "Samson", "Samuel", "Sanghvi", "Sangwan", "Sankaran", "Sankhla", "Sant", "Santosh",
    "Sapkal", "Sapra", "Saraf", "Saran", "Saraswat", "Sarda", "Sarin", "Sarma", "Sarna", "Saroj",
    "Sarraf", "Sastry", "Sathe", "Sathyan", "Satyam", "Satyapal", "Satyavrat", "Sawant", "Sawhney", "Saxena",
    "Sayyed", "Sehgal", "Sekhon", "Selvaraj", "Sen", "Sengupta", "Senthil", "Sequeira", "Seth", "Sethi",
    "Shah", "Shahani", "Shahbaz", "Shahzad", "Shakya", "Shamrao", "Shamsher", "Shankar", "Shanmugam", "Shantaram",
    "Sharan", "Sharma", "Sharoff", "Sheikh", "Shekhar", "Shelar", "Shetty", "Shinde", "Shingade", "Shinghal"


]


"""
=========================================================
LGeneric Save Function
=========================================================
"""

def save_list(data, filename, column_name):

    df = pd.DataFrame({

        column_name: data

    })

    output = REFERENCE_DATA / filename

    df.to_csv(

        output,

        index=False

    )

    print(

        filename,

        len(df)

    )
"""
=========================================================
Generate
=========================================================
"""
def generate_names():

    save_list(

        MALE_NAMES,

        "first_names_male.csv",

        "FirstName"

    )

    save_list(

        FEMALE_NAMES,

        "first_names_female.csv",

        "FirstName"

    )

    save_list(

        LAST_NAMES,

        "last_names.csv",

        "LastName"

    )

    save_list(

        EMAIL_DOMAINS,

        "email_domains.csv",

        "Domain"

    )

    print("Done")
    
"""
=========================================================
Main
=========================================================
"""

if __name__=="__main__":

    generate_names()