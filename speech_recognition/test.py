
SLACK_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XX-X-X-X- /* <===  */ 
SLACK_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
  Recognize_SLACK(audio, username=IBM_USERNAME, password=IBM_PASSWORD)   
except sr.UnknownValueError:
    print("SLACK Speech to Text could not understand audio")


 def Recognize_SLACK(audio, username, password):
     print("SLACK Speech to Text thinks you said " + username + " " + password)
