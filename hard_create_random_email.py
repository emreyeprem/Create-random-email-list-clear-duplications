import json
import random
import string
# domains = [ "hotmail.com", "gmail.com", "aol.com", "masn.com" , "apple.com", "yahoo.com"]
# letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t"]
#
# def get_one_random_domain(domains):
#         return domains[random.randint( 0, len(domains)-1)]
#
#
# def get_one_random_name(letters):
#     email_name = ""
#     for i in range(7):
#         email_name = email_name + letters[random.randint(0,11)]
#     return email_name
#
#
# def generate_random_emails():
#
#     for i in range(0,10):
#          one_name = str(get_one_random_name(letters))
#          one_domain = str(get_one_random_domain(domains))
#          print(one_name  + "@" + one_domain)
#
# def main():
#     generate_random_emails()
#-------------------import alphabet--&
final_list = []
email_list = []
for i in range(0,8):
    for j in range(3,8):
        email_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(j))

        domains = ["hotmail.com", "gmail.com", "aol.com", "msn.com" , "apple.com", "yahoo.com"]
        chosen_domain = random.choice(domains)
        #print(chosen_domain)
        email_list.append(email_name + '@' + chosen_domain)
# print(email_list)
for i in range(3,9):
    doubles = [email_list[i] for _ in range(1)]
    email_list.append(doubles[0])

#print(email_list)
for x in email_list:
    if x not in final_list:
        final_list.append(x)
print(len(email_list))
print(len(final_list))

#-------------------------json--file-----------------

with open('clear_duplication.json', 'w') as email_file:
    json.dump(final_list, email_file)
