def countEmail():
    # This first line is provided for you
    file_name = input("Enter file:")
    if len(file_name) < 1 : file_name = "mbox-short.txt"
    
    email_sender_counts = dict() 

    # Try except for bad input 
    try:
        with open(file_name) as file_handler: # With opens and closes file
            for line in file_handler:         # Loops through lines in file handler
                if line.startswith("From "):  # Finds lines that start with "From "
                    email = line.split()[1] # Gets the second word (sender email address)
                    
                    # Sets it to 1 if it isn't in the dictionary and increments if it is
                    if email not in email_sender_counts:
                        email_sender_counts[email] = 1
                    else:
                        email_sender_counts[email] += 1

    except:
        print(f"Bad file name : {file_name}")
        quit()

    # Get the email with the most emails sent
    max_email = max(email_sender_counts, key=email_sender_counts.get)
    max_sent = email_sender_counts[max_email]

    print(f"{max_email} {max_sent}")
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
