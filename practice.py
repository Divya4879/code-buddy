import os
import google.generativeai as genai
import markdown 


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story set in a college.")
# print(response.text)


model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(
#     "Tell me a story about a connection at first sight.",
#     generation_config=genai.types.GenerationConfig(
#         # Only one candidate for now.
#         candidate_count=1,
#         stop_sequences=["x"],
#         max_output_tokens=100,
#         temperature=0.3,
#     ),
# )


response = model.generate_content(" You're  a personal gym trainer with over 10 yrs of experience. You've helped many celebrities achieve their weight loss.Give me a general workout plan for 7 days for a normal person with just the list of exercises and their sets and reps to be performed that a person who wants to tone up should do.All exercises should be bodyweight only. This student is an beginner-intermediate level in workout.",
    generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=["x"],
        max_output_tokens=1000,
        temperature=0,
    ),
)

print(response.text)



# print(response.text)

# response = model.generate_content(
#     'Write a fluff story  in about 100 words.',
#     generation_config = genai.GenerationConfig(
#         max_output_tokens=1000,
#         temperature=0.1,
#     )
# )
# print(response.text)

# model=genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   system_instruction="You have been a world-renowned author with over 2 decades of experience."
#   )

# response = model.generate_content(
#     'Write a angst story  in about 400 words.',
#     generation_config = genai.GenerationConfig(
#         max_output_tokens=1000,
#         temperature=0.1,
#     )
# )
# print(response.text)


# Upload the file and print a confirmation.
# sample_file = genai.upload_file(path="jetpack.jpg",
#                              display_name="Jetpack drawing")

# # # print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")



# # # Choose a Gemini model.
# # model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# # # Prompt the model with text and the previously uploaded image.
# # response = model.generate_content([sample_file, "Describe how this product might be manufactured."])
 
# # # response = ">" + response.text
# # # print(markdown.markdown(response))

# # print(response.text)

# import PIL.Image

# sample_file_2 = PIL.Image.open('coder.jpg')
# sample_file_3 = PIL.Image.open('cute.jpg')

# # Choose a Gemini model.
# model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# prompt = "Write a short powerful and beautiful story about the people in second and third images"

# response = model.generate_content([prompt, sample_file, sample_file_2, sample_file_3])

# print(response.text)



# model = genai.GenerativeModel("gemini-1.5-flash")
# chat = model.start_chat(
#     history=[
#         {"role": "user", "parts": "Hello, I have 2 dogs in my house."},
#         {"role": "model", "parts": "Great to meet you. What would you like to know?"},
#     ]
# )

# response = chat.send_message("How many paws are in my house?")
# print(response.text)