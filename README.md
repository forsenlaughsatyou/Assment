# Assment
tools used: django restframework
note : started off writing the code in function based views but it throws an error while performing PUT request. couldn't hang on to it as the time is running out.
So  I used class based views and commented out the fbv. I didn't want to use CBV but its kind of last resort. 
used Modelviewset instead of mixins.
I had a hard time following the CBV but used documentation as ref
did not put extra constrains on address qualifications and projects as we have them as primary key, throws an error when creating an employee.
since I used routers it allows Partial updation while we pass emp id as pk in the url.
advatage of using Modelviewsets is that it creates URL_PATTERNS internally for each modelserializer along with built in messages.
