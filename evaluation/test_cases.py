test_cases = [

# EMAIL TESTS

{"text": "Contact me at abc@gmail.com",
"expected": "Contact me at ab***********"},

{"text": "Send mail to john.doe@company.org",
"expected": "Send mail to jo******************"},

{"text": "My email is testuser123@yahoo.com",
"expected": "My email is te*******************"},

{"text": "Reach support at helpdesk@service.com",
"expected": "Reach support at he*******************"},

{"text": "Write to admin@website.net",
"expected": "Write to ad***************"},

{"text": "Email contact: sample.mail@domain.co",
"expected": "Email contact: sa*******************"},


# PHONE TESTS

{"text": "Call me at 9876543210",
"expected": "Call me at 98********"},

{"text": "Emergency contact 9123456789",
"expected": "Emergency contact 91********"},

{"text": "My number is 9876501234",
"expected": "My number is 98********"},

{"text": "Office phone 9345678912",
"expected": "Office phone 93********"},

{"text": "Dial 9876000001 for help",
"expected": "Dial 98******** for help"},


# CARD NUMBER TESTS

{"text": "Card number 1234 5678 9012 3456",
"expected": "Card number [BLOCKED]"},

{"text": "Payment card 4321 8765 1111 2222",
"expected": "Payment card [BLOCKED]"},

{"text": "Use card 1111 2222 3333 4444 for payment",
"expected": "Use card [BLOCKED] for payment"},


# ADDRESS TESTS

{"text": "Meet me at Flat 502 MG Road",
"expected": "Meet me at ********"},

{"text": "My house is Apartment 12 Park Avenue",
"expected": "My house is ********"},

{"text": "Office located at Building 9 Tech Park",
"expected": "Office located at ********"},

{"text": "Send courier to House 45 Green Colony",
"expected": "Send courier to ********"},


# OFFENSIVE WORD REPLACEMENTS

{"text": "You are stupid",
"expected": "You are unwise"},

{"text": "That idea is dumb",
"expected": "That idea is uninformed"},

{"text": "Stop talking nonsense",
"expected": "Stop talking incorrect"},

{"text": "He is a fool",
"expected": "He is a misguided"},


# ABUSIVE LANGUAGE

{"text": "You idiot",
"expected": "You person"},

{"text": "He behaves like a moron",
"expected": "He behaves like a individual"},

{"text": "That jerk ruined the work",
"expected": "That rude person ruined the work"},

{"text": "I hate you",
"expected": "I dislike you"},


# NORMAL TEXT (NEGATIVE TESTS)

{"text": "The weather is nice today",
"expected": "The weather is nice today"},

{"text": "Machine learning is fascinating",
"expected": "Machine learning is fascinating"},

{"text": "Data governance is important",
"expected": "Data governance is important"},


# MIXED CASES

{"text": "Contact john.doe@company.org or call 9876543210",
"expected": "Contact jo****************** or call 98********"},

{"text": "Send details to admin@site.com and visit Flat 502 MG Road",
"expected": "Send details to ad************* and visit ********"},

{"text": "My card 1234 5678 9012 3456 was stolen",
"expected": "My card [BLOCKED] was stolen"},

{"text": "You idiot, stop this nonsense",
"expected": "You person, stop this incorrect"},


# PARAGRAPH TESTS (REALISTIC)

{
"text": "Hi, my name is John. Contact me at john.doe@gmail.com or call 9876543210. I live at Flat 502 MG Road.",
"expected": "Hi, my name is John. Contact me at jo***************** or call 98********. I live at ********."
},

{
"text": "Customer reported that his card 1234 5678 9012 3456 was compromised. Please email support@bank.com immediately.",
"expected": "Customer reported that his card [BLOCKED] was compromised. Please email su***************** immediately."
},

{
"text": "You idiot, that was a stupid idea. Please contact admin@portal.com.",
"expected": "You person, that was a unwise idea. Please contact ad****************."
},

{
"text": "Reach our office at Building 9 Tech Park or phone 9345678912.",
"expected": "Reach our office at ******** or phone 93********."
},

{
"text": "Hello team, the meeting will happen tomorrow at our office in Apartment 12 Park Avenue.",
"expected": "Hello team, the meeting will happen tomorrow at our office in ********."
},
  

# More cases

{
"text": "Contact me at abc@gmail.com",
"expected": "Contact me at ab***********"
},

{
"text": "Send report to john.doe@company.org",
"expected": "Send report to jo******************"
},

{
"text": "Call me at 9876543210",
"expected": "Call me at 98********"
},

{
"text": "Emergency number +91 9876543210",
"expected": "Emergency number +91 98********"
},

{
"text": "Card number 1234 5678 9012 3456",
"expected": "Card number [BLOCKED]"
},

{
"text": "You are stupid",
"expected": "You are unwise"
},

{
"text": "He is an idiot",
"expected": "He is an person"
},

{
"text": "The weather is pleasant today",
"expected": "The weather is pleasant today"
},


# MULTIPLE EMAILS

{
"text": "Send emails to alice@gmail.com and bob@yahoo.com",
"expected": "Send emails to al************* and bo*************"
},

{
"text": "Our contacts are admin@site.com, help@site.com",
"expected": "Our contacts are ad*************, he************"
},

{
"text": "Please notify support@portal.com and manager@portal.com",
"expected": "Please notify su**************** and ma*****************"
},


# MULTIPLE PHONES

{
"text": "Call 9876543210 or 9123456789",
"expected": "Call 98******** or 91********"
},

{
"text": "Emergency numbers 9876543210, 9345678912",
"expected": "Emergency numbers 98********, 93********"
},

{
"text": "Contact 9876000001 or 9876000002 for details",
"expected": "Contact 98******** or 98******** for details"
},


# EMAIL + PHONE MIX

{
"text": "Contact john@gmail.com or phone 9876543210",
"expected": "Contact jo************* or phone 98********"
},

{
"text": "Email support@service.com and call 9345678912",
"expected": "Email su******************* and call 93********"
},


# MULTIPLE CARD NUMBERS

{
"text": "Cards 1234 5678 9012 3456 and 4321 8765 1111 2222 were used",
"expected": "Cards [BLOCKED] and [BLOCKED] were used"
},

{
"text": "Payment with 1111 2222 3333 4444 failed",
"expected": "Payment with [BLOCKED] failed"
},


# ADDRESS VARIATIONS

{
"text": "Meet at House 12 Green Colony tomorrow",
"expected": "Meet at ******** tomorrow"
},

{
"text": "Office shifted to Apartment 4 Lake View Road",
"expected": "Office shifted to ********"
},

{
"text": "Courier delivered to Building 3 Sunrise Park",
"expected": "Courier delivered to ********"
},


# OFFENSIVE LANGUAGE MIX

{
"text": "That stupid plan was nonsense",
"expected": "That unwise plan was incorrect"
},

{
"text": "Stop behaving like a fool",
"expected": "Stop behaving like a misguided"
},

{
"text": "Your argument is dumb nonsense",
"expected": "Your argument is uninformed incorrect"
},


# ABUSIVE LANGUAGE MIX

{
"text": "You jerk stop that",
"expected": "You rude person stop that"
},

{
"text": "That moron broke the device",
"expected": "That individual broke the device"
},

{
"text": "Why are you such an idiot",
"expected": "Why are you such an person"
},


# MIXED ABUSE + EMAIL

{
"text": "You idiot email admin@site.com",
"expected": "You person email ad*************"
},

{
"text": "That stupid guy sent mail to helpdesk@portal.com",
"expected": "That unwise guy sent mail to he********************"
},


# EMAIL + ADDRESS

{
"text": "Send documents to manager@company.com at Flat 502 MG Road",
"expected": "Send documents to ma****************** at ********"
},


# PHONE + ADDRESS

{
"text": "Visit House 12 Green Colony or call 9876543210",
"expected": "Visit ******** or call 98********"
},


# LONG SENTENCES

{
"text": "If you need help contact support@company.com or call 9345678912 immediately",
"expected": "If you need help contact su******************** or call 93******** immediately"
},

{
"text": "My card 1234 5678 9012 3456 was used fraudulently please block it",
"expected": "My card [BLOCKED] was used fraudulently please block it"
},


# PARAGRAPH TESTS

{
"text": "Hello team, please send reports to admin@office.com. For urgent matters call 9876543210.",
"expected": "Hello team, please send reports to ad**************. For urgent matters call 98********."
},

{
"text": "Customer complained that card 1111 2222 3333 4444 was charged. Contact customer at 9345678912.",
"expected": "Customer complained that card [BLOCKED] was charged. Contact customer at 93********."
},

{
"text": "You idiot this nonsense idea failed again. Please contact manager@company.com.",
"expected": "You person this incorrect idea failed again. Please contact ma*******************."
},

{
"text": "Office moved from Apartment 12 Park Avenue to Building 9 Tech Park.",
"expected": "Office moved from ******** to ********."
},


# NEGATIVE TESTS

{
"text": "Artificial intelligence is transforming industries",
"expected": "Artificial intelligence is transforming industries"
},

{
"text": "We will meet tomorrow morning",
"expected": "We will meet tomorrow morning"
},

{
"text": "Python is widely used in data science",
"expected": "Python is widely used in data science"
},

{
"text": "Email me at hello@gmail.com",
"expected": "Email me at he*************"
},

{
"text": "My email is user123@yahoo.com",
"expected": "My email is us***************"
},

{
"text": "Reach me through contact@company.com",
"expected": "Reach me through co*******************"
},

{
"text": "Write to info@portal.com",
"expected": "Write to in**************"
},


# ---------------- EASY PHONE CASES ----------------

{
"text": "My phone number is 9876500000",
"expected": "My phone number is 98********"
},

{
"text": "Call 9123400000 tomorrow",
"expected": "Call 91******** tomorrow"
},

{
"text": "Emergency number 9345600000",
"expected": "Emergency number 93********"
},

{
"text": "Contact via 9876001111",
"expected": "Contact via 98********"
},

{
"text": "Dial 9876000002 for support",
"expected": "Dial 98******** for support"
},

{
"text": "Reach us at 9876000003",
"expected": "Reach us at 98********"
},

{
"text": "Our helpline is 9876000004",
"expected": "Our helpline is 98********"
},

{   
"text": "Customer care number is 9876000005",
"expected": "Customer care number is 98********"
},

{
"text": "For assistance call 9876000006",
"expected": "For assistance call 98********"
},

{
"text": "Report issues to 9876000007",
"expected": "Report issues to 98********"
},

{
"text": "Contact support at 9876000008",
"expected": "Contact support at 98********"
},

{
"text": "For inquiries call 9876000009",
"expected": "For inquiries call 98********"
},

{
"text": "Our emergency number is 9876000010",
"expected": "Our emergency number is 98********"
},



# ---------------- EASY OFFENSIVE WORD CASES ----------------

{
"text": "That idea is stupid",
"expected": "That idea is unwise"
},

{
"text": "Your logic is dumb",
"expected": "Your logic is uninformed"
},

{
"text": "Stop this nonsense now",
"expected": "Stop this incorrect now"
},

{
"text": "You are a fool",
"expected": "You are a misguided" 
},

{
"text": "He is an idiot",
"expected": "He is an person"
},

{
"text": "That jerk is annoying",
"expected": "That rude person is annoying"
},

# ---------------- EASY ABUSIVE CASES ----------------

{
"text": "You idiot",
"expected": "You person"
},

{
"text": "He is a moron",
"expected": "He is a individual"
},

{
"text": "That jerk caused trouble",
"expected": "That rude person caused trouble"
},

{"text": "I hate you",
"expected": "I dislike you"
},

{
"text": "You fool",
"expected": "You misguided"
},

{
"text": "Stop behaving like a jerk",
"expected": "Stop behaving like a rude person"
},

{
"text": "That moron broke the device",
"expected": "That individual broke the device"
},


# ---------------- ADDRESS CASES ----------------

{
"text": "Meet at Flat 10 Lake Road",
"expected": "Meet at ********"
},

{
"text": "The office is in House 9 Park Avenue",
"expected": "The office is in ********"
},

{
"text": "Courier sent to Apartment 3 Green Colony",
"expected": "Courier sent to ********"
},


# ---------------- CARD CASES ----------------

{
"text": "Use card 1234 5678 9012 3456",
"expected": "Use card [BLOCKED]"
},

{
"text": "Transaction done with 4321 8765 1111 2222",
"expected": "Transaction done with [BLOCKED]"
},


# ---------------- MIXED PII CASES ----------------

{
"text": "Email admin@site.com or call 9876500000",
"expected": "Email ad************* or call 98********"
},

{
"text": "Reach manager@office.com at 9345600000",
"expected": "Reach ma***************** at 93********"
},

{
"text": "My card 1234 5678 9012 3456 was used contact bank@help.com",
"expected": "My card [BLOCKED] was used contact ba**************"
},


# ---------------- ABUSE + EMAIL ----------------

{
"text": "You idiot email support@company.com",
"expected": "You person email su********************"
},

{
"text": "That stupid guy mailed admin@portal.com",
"expected": "That unwise guy mailed ad****************"
},


# ---------------- PARAGRAPH CASES ----------------

{
"text": "Hello team, please contact support@company.com for assistance.",
"expected": "Hello team, please contact su******************** for assistance."
},

{
"text": "Customer reported card 1111 2222 3333 4444 stolen.",
"expected": "Customer reported card [BLOCKED] stolen."
},

{
"text": "If you need help call 9876500000 immediately.",
"expected": "If you need help call 98******** immediately."
},


# ---------------- NORMAL TEXT (NEGATIVE) ----------------

{
"text": "Artificial intelligence improves productivity",
"expected": "Artificial intelligence improves productivity"
},

{
"text": "Data science helps organizations make decisions",
"expected": "Data science helps organizations make decisions"
},

{
"text": "Software engineering requires problem solving",
"expected": "Software engineering requires problem solving"
},


#More test cases



# -------- EMAIL TESTS --------

{
"text": "Contact me at ab@gmail.com",
"expected": "Contact me at ab***********"
},

{
"text": "Send mail to cd@yahoo.com",
"expected": "Send mail to cd***********"
},

{
"text": "My email is ef@company.com",
"expected": "My email is ef************"
},

{
"text": "Reach us at gh@service.org",
"expected": "Reach us at gh*************"
},

{
"text": "Please email xy@gmail.com",
"expected": "Please email xy***********"
},

{
"text": "Contact uv@yahoo.com",
"expected": "Contact uv***********"
},

{
"text": "Mail can be sent to kl@company.com",
"expected": "Mail can be sent to kl************"
},

{
"text": "Support email mn@service.org",
"expected": "Support email mn*************"
},

# -------- PHONE TESTS --------

{
"text": "Call 9876543210",
"expected": "Call 98********"
},

{
"text": "Phone number 9123456789",
"expected": "Phone number 91********"
},

{
"text": "Dial 9345678912",
"expected": "Dial 93********"
},

{
"text": "Contact 9876500000",
"expected": "Contact 98********"
},
{
"text": "My contact is 9876501234",
"expected": "My contact is 98********"
},

{
"text": "Reach me at 9123401234",
"expected": "Reach me at 91********"
},

{
"text": "Helpline 9345612345",
"expected": "Helpline 93********"
},

{
"text": "Call number 9876001111",
"expected": "Call number 98********"
},

# -------- CARD NUMBER TESTS --------

{
"text": "Card 1234 5678 9012 3456",
"expected": "Card [BLOCKED]"
},

{
"text": "Payment using 1111 2222 3333 4444",
"expected": "Payment using [BLOCKED]"
},


# -------- OFFENSIVE WORD TESTS --------

{
"text": "That was stupid",
"expected": "That was unwise"
},

{
"text": "This idea is dumb",
"expected": "This idea is uninformed"
},

{
"text": "Stop this nonsense",
"expected": "Stop this incorrect"
},

{
"text": "He is a fool",
"expected": "He is a misguided"
},

{
"text": "That comment was stupid",
"expected": "That comment was unwise"
},

{
"text": "Your answer is dumb",
"expected": "Your answer is uninformed"
},

{
"text": "This explanation is nonsense",
"expected": "This explanation is incorrect"
},

{
"text": "He behaved like a fool",
"expected": "He behaved like a misguided"
},

# -------- ABUSIVE LANGUAGE TESTS --------

{
"text": "You idiot",
"expected": "You person"
},

{
"text": "He is a moron",
"expected": "He is a individual"
},

{
"text": "That jerk broke it",
"expected": "That rude person broke it"
},

{
"text": "I hate you",
"expected": "I dislike you"
},

{
    "text": "I am a fool",
    "expected": "I am a misguided"
},

{
    "text": "He is a jerk",
    "expected": "He is a rude person"
},

{
"text": "Stop acting like an idiot",
"expected": "Stop acting like an person"
},

{
"text": "That guy is a moron",
"expected": "That guy is a individual"
},

{
"text": "The rude jerk shouted",
"expected": "The rude rude person shouted"
},

{
"text": "Why do you hate you",
"expected": "Why do you dislike you"
},
# -------- NORMAL TEXT TESTS --------

{
"text": "Machine learning is interesting",
"expected": "Machine learning is interesting"
},

{
"text": "Data governance is important",
"expected": "Data governance is important"
},

{
"text": "Software development needs practice",
"expected": "Software development needs practice"
},

{
"text": "Artificial intelligence is evolving",
"expected": "Artificial intelligence is evolving"
},

# Address Specific Cases

# Missing street keywords

{
"text": "Meet me at 502 MG",
"expected": "Meet me at ********"
},

{
"text": "My home is 45 Green Area",
"expected": "My home is ********"
},

{
"text": "Office located at 78 Business District",
"expected": "Office located at ********"
},


# Number after street

{
"text": "Meet at MG Road 502",
"expected": "Meet at ********"
},

{
"text": "Office is on Park Avenue 10",
"expected": "Office is on ********"
},


# Lowercase words (regex expects capital)

{
"text": "visit flat 502 mg road",
"expected": "visit ********"
},

{
"text": "my house is apartment 12 park avenue",
"expected": "my house is ********"
},


# Extra punctuation

{
"text": "Meet me at Flat-502 MG Road",
"expected": "Meet me at ********"
},

{
"text": "Office at House#45 Green Colony",
"expected": "Office at ********"
},


# Different address styles

{
"text": "Come to 5th floor Orion Mall",
"expected": "Come to ********"
},

{
"text": "Meet at Lulu Mall Kochi",
"expected": "Meet at ********"
},

{
"text": "Office is inside Infopark Kochi",
"expected": "Office is inside ********"
},


# Indian style addresses

{
"text": "House near temple road",
"expected": "House near ********"
},

{
"text": "Opposite City Hospital MG Road",
"expected": "Opposite ********"
},

{
"text": "Behind Central Mall Park Street",
"expected": "Behind ********"
},


# Multi-line / complex structure

{
"text": "Flat 502 Tower B Sunrise Residency",
"expected": "********"
},

{
"text": "Block C Sector 12 Green Colony",
"expected": "********"
},


# Short addresses

{
"text": "Come to Park Avenue",
"expected": "Come to ********"
},

{
"text": "Meet at MG Road",
"expected": "Meet at ********"
},


# With commas

{
"text": "Flat 502, Sunrise Residency",
"expected": "********"
}



]