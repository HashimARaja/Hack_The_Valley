import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCOlj8ioX6ddt1ofOgOhldPMHIccLz_3OQ")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

x = "Machine Learning"
p = "USA"

response = model.generate_content("for the following career path: " + x +"\nProvide a concise Education path and goals for this career path and include a varity of "+p+ " University programs to choose from and beginning, middle and end stage jobs")

print(response.text)
