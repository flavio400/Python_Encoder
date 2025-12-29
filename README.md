# Python Encoder


# What is it built for?

It's designed for bug bounties, to help you bypass the WAF (web application firewall) 
by generating different variants of your payload, very useful for XSS (cross site scripting),
CSRF (cross site request forgery), SQLi (SQL injection), and all the attacks that require to inject a payload.



# How does it work?

-> takes the input
-> let's you choose the type of encoding (URL, Double URL, HTML, Unicode, Base64, UTF-7, all in a file.txt, all with permutations in a file.txt)
-> prints the encoded payload or generates the file with different types of encoding



# What are the requirements?

-> python 3.6 or over
-> it uses built-in python libraries, so you don't need to install anything



# How to install and execute?

-> type this in your terminal:
   - git clone https://github.com/flavio400/Python_Encoder.git
   - cd Python_Encoder
   - python encoder.py # there are no arguments to put in, the script will ask you everything
   



