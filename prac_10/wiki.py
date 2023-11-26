import wikipedia

user_prompt = input("Enter Page Title: ")
while user_prompt != "":
    search_result = wikipedia.page(user_prompt, auto_suggest=False)
    print(search_result.title)
    print(search_result.summary)
    print(search_result.url)
    user_prompt = input("Enter Page Title: ")
