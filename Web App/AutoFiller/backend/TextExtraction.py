import itertools
import re
import pytesseract
import os
import nltk

class TextExtraction:
    def __init__(self):
        self.PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
        self.EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

    def ExtractText(self , img) : 
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)
        return text

    def extract_name(self , text):
        #Find names in Block letters
        names = re.findall('[A-Z]+\.? ?[A-Z]+[\n|,| |\.]', text)

        #Find names in capitalized letters  ([A-Z][a-z]+?\.?( ?[A-Z][a-z]+?){0,5} ?[A-Z][a-z]+?[\n| |,]) 
        names_2 = re.findall('([A-Z][a-z]+?\.? ?( ?[A-Z][a-z]*?){0,5}\.? ?[A-Z][a-z]*?[\n| |,|.])', text)
        names_2 = list(itertools.chain(*names_2))

        #list of words to be avoided while parsing
        avoid_words = ['resume','résumé','cv', 'curriculum','marketing', 'curriculum vitae','vitae', 'curriculum vita',
                        'vita', 'name', 'pg', 'india', 'curriculam vitae', 'business development', 'cast', 'coc,','uae',
                        'address', 'email', 'email address', 'sales', 'u.p', 'product development', 'personal statement',
                        'full Name','street address', 'mobile', 'phone', 'number', 'phone number', 'mobile number', 'product',
                        'agarwal', 'inter', 'secondary', 'steels', 'element', 'engineering','system', 'school', 'operating',
                        'acknowledgement', 'assimilated', 'collaborated', 'collaboration','collaborations', 'india', 'isf,',
                        'professional summary', 'professional', 'title', 'job title', 'job' 'technological', 'high', 'college',
                        'top', 'device', 'launch', 'ams', 'crm', 'P Technological', 'project engineer', 'cgpa', 'gpa',
                        'personal profile', 'years', 'lv', 'career', 'career profile','lv', 'curriculum viate', 'civil',
                        'post applied', 'applied', 'post', 'for', 'electrical engineer', 'ps', 'district', 'ilets',
                        'career objective.', 'it', 'carrier objective', 'electrical project handling', 'mig,', 'hvac',
                        'mdu', 'linkedin', 'facebook', 'behance', 'youtube', 'github', 'in', 'portfolio','total experience',
                        'pbd','working','xcx','wwd','mba','dtdc','cf ril', 'fi', 'ef', 'dd', 'project management',
                        'engineer', 'apj', 'course university', 'university', 'ltd.', 'educational', 'n.y.', 's.s.',
                        'information technology', 'uk', 'usa', 'uae','pakistan','china','canada','saudia','arabia',
                        'educational background', 'details', 'personal details', 'clout', 'cloud', 'inditex', 'vy.', 'instrument',
                        'instrument super', 'bca', 'u.p.', 'qa', 'gis', 'gre', 'aicte', 'professional and', 'education background',
                        'tx', 'pvc', 'acadmic qualification', 'apply for merchandiser', 'education background','bechelor',
                        'beardsell pvt.', 'class', 'fi ef', 'uae,', 'of', 'b.s.', 'project', ''
                        'contributed', 'participated', 'participations', 'partnered', 'partnerships', 'volunteer work',
                        'volunteer', 'side activities', 'projects', 'education', 'experience', 'work', 'work experience',
                        'skills', 'interests', 'biography', 'bio', 'about me', 'about', 'info', 'contact', 'contact info',
                        'reference', 'reference will be established upon request', 'certificates', 'additional certificates',
                        'courses', 'student', 'online courses', 'short courses', 'languages', 'internships', 'organizations',
                        'organization', 'matriculation', 'intermediate', 'pre-engineering', 'bachelors', 'masters',
                        'bscs', 'bachelor of science', 'btech', 'btech', 'bachelor of technology', 'bs-cs,', 'sslc',
                        'bse', 'bachelor of commerce', 'bcom', 'b.com', 'information', 'personal information',
                        'info','achievements', 'personal projects', 'personal skills', 'summary', 'courses and certificates:',
                        'profile', 'hobbies & interests', 'hobbies and interests', 'hobbies', 'career objective',
                        'objective', 'other skills', 'academic', 'academics', 'academic qualification', 'references',
                        'personal', 'cnic', 'dob', 'date of birth', 'work history','computer skills', 'referenc',
                        'economics and finance', 'top skills', 'personal email', 'contact no', 'contact no.', 
                        'cnic no', 'cnic no.', 'religion', 'domicile', 'a levels', 'o levels', 'working links',
                        'links', 'working experience', 'awards and achievements', 'awards', 'soft skills', 
                        'volunteer experience', 'conferences and courses', 'conferences', 'educational qualification',
                        'educational qualifications', 'value addition', 'declaration', 'brief employment history',
                        'extra activities', 'extra', 'skills and responsibilities', 'duties and responsibilities',
                        'skills and abilities', 'area of expertise', 'technical skills', 'current address', 
                        'permanent address', 'passport no', 'expiry date', 'career summary', 'email id', 'phone no',
                        'contact no', 'contact no.', 'phone no.', 'education qualification', 'python', 'js6', 'ansys'
                        ]

        #variable to limit iteration
        counter = 0
        #Checks whether an avoid word is present and skips over it
        for element in names:
            if counter==3:
                break
            if not element.lower().replace('\n','').strip() in avoid_words:
                return element
            counter+=1
        
        counter=0
        for element in names_2:
            if counter==4:
                break
            if not element.lower().replace('\n','').strip() in avoid_words:
                return element
            counter+=1
        return ''

    def extract_phone_number(self , resume_text):
        phone = re.findall(self.PHONE_REG, resume_text)
        if phone:
            number = ''.join(phone[0])
    
            if resume_text.find(number) >= 0 and len(number) < 16:
                return number
        return None
    
    
    def extract_emails(self, resume_text):
        return re.findall(self.EMAIL_REG, resume_text)

    def process_emails(self , emailID):
        # Identifying the string slicing for gmail
        if type(emailID) == list:
            emailNum = 0
            for eml in emailID:
                for i in range(len(eml)):
                    if eml[i] == '@':
                        index1 = i
                        break
                for j in range(index1 , len(eml)):
                    if eml[j] == '.':
                        index2 = j
                        break
                if eml[index1 + 1:index2] == 'qmail' or eml[index1 + 1:index2] == 'gqmail':
                    part1 = eml[0:index1 + 1]
                    part2 = eml[index1 + 1 : index2]
                    part3 = eml[index2:len(eml)]
                    eml = part1 + 'gmail' + part3
                    emailID[emailNum] = eml
                    emailNum =  emailNum + 1
        else:
            for i in range(len(emailID)):
                if emailID[i] == '@':
                    index1 = i
                    break
            for j in range(index1 , len(emailID)):
                if emailID[j] == '.':
                    index2 = j
                    break
            part1 = emailID[0:index1 + 1]
            part2 = emailID[index1 + 1 : index2]
            part3 = emailID[index2:len(emailID)]
            emailID = part1 + 'gmail' + part3
        return emailID