# -*- coding: utf-8 -*-
"""Assignment #2: Strings

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qiyr2sqhg5ArIlZqJ5GVfKIY9lIy4TCc

**This is the username/ password user defined function. CALL FUNCTION = "generate_student_info'**
****
- It is referenced in main, condition 's'.
- while loop to re-execute function
- "if else' to handle exeptions

NOTE: RUN ALL USER DEFINED FUNCTION SNIPS BEFORE YOU RUN MAIN
"""

# This is the user defined function for password and username generator
def generate_student_info():

  #this is a while statement so the user can generate another user/ password without exiting
  while True:

   first_name_str = input(str("Enter the student's first name: \n"))
   #this is for the username str
   user_first_str = first_name_str[0]
   #this is for the password str
   pass_first_str = first_name_str[0:2]

   last_name_str = input(str("\n\n Enter the student's last name: \n"))
   user_last_str = last_name_str[0:6]

   no_middle_name = input("\n\n Does the student have a middle name? ('y/n')\n")

   # This is to check if the student does not have a middle name/will also make the username
   if no_middle_name == 'y':
     middle_name_str = input(str("\n\n Enter the student's middle name: \n"))
     user_middle_str = middle_name_str[0]
     pass_middle_str = middle_name_str[0::2]

  #innitialize to empty so you dont need two user functions and to prevent "index out of range"
   elif no_middle_name == 'n':
     user_middle_str = ""
     pass_middle_str = ""

   phone_num_str = input(str("\n\n Enter the student's parent's phone number: \n"))
   # now reverse phone number to make it easier to get last 4 digits
   reverse_phone_str = phone_num_str[::-1]
   # forward reverse
   pass_phone_str = reverse_phone_str[0:4]

   #now make username and password
   student_username = (user_last_str + user_first_str + user_middle_str)
   student_password = (pass_first_str + pass_middle_str + pass_phone_str)

   # add border
   print("----------------------------------------------")
   print("Username:", student_username)
   print("Password:", student_password)
   print("----------------------------------------------")

   # If the user wants to generate another username/password without returning to main
   run_again_student = input("\n\n would you like to generate another username and password?: ('y/n')\n")
   if run_again_student != 'y':
    break

"""**This is pig latin user defined function. CALL FUNCTION = 'pig_latin_generator'**
*****
- It is referenced in main, condition 'p'.
- uses while loop to re-execute function or return to main
- 'if else' to handle exceptions
- contains list of vowels to check exceptions in lenth of user input string
"""

# user defined function for pig latin generator
def pig_latin_generator():

    # While the user wants to run this function
    while True:

        # Defining the vowels to check if they are the first letter of the word
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        english_word_str = input(str("Enter the english word: \n"))

        # if the first letter of english word is a vowel...
        if english_word_str[0] in vowel_letters:
          # then check the next letter which would be index 1 - the length of word
            pig_latin_str = (english_word_str[1:] + "ay")

            # if the length of word is greater than a and the second letter is also a vowel...
            # need to verify length of string is > 1 or else it won't execute apparently
            if len(english_word_str) > 1 and english_word_str[1] in vowel_letters:
              pig_latin_str = (english_word_str[2:] + "ay")

        # if the first letter is NOT a vowel...
        else:
          pig_latin_str = (english_word_str[1:] + english_word_str[0] + "ay")

        # print pig latin word + border

        print("----------------------------------------------")
        print("The word in pig latin is:", pig_latin_str)
        print("----------------------------------------------")

        # User can run function again without exiting to main
        pig_latin_again = input("\n\n Would you like to generate another pig latin word? ('y/n'): \n")
        if pig_latin_again != 'y':
         break

"""**This is MAIN.**
** **
- Utilizes user-defined functions to make it easier to combine both programs into 1.
- It will call from the user defined functions to execute programs of user's choice
- while loop to re-execute program choice
- if else staements to execute program user defined functions per user input
"""

# main will call from other functions to execute
while True:
  program_choice= input("Which program would you like to run? ('s' for student user/password generator, 'p' for pig latin, 'e' to exit program.  \n")

  if program_choice == 's':
   generate_student_info()
  if program_choice == 'p':
    pig_latin_generator()
  elif program_choice =='e':
    break

  run_program_again = input("\n\n Would you like to run the program again? ('y/n'): \n")
  if run_program_again != 'y':
    break