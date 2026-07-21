def get_response(user):

    if user == "hello":
        return "👋 Hello! Welcome."

    elif user == "hi":
        return "😊 Hi! How are you?"

    elif user == "how are you":
        return "😄 I am fine."

    elif user == "ai":
        return "🧠 AI stands for Artificial Intelligence."

    elif user == "python":
        return "🐍 Python is a powerful programming language."

    elif user == "github":
        return "💻 GitHub is used to host projects."

    elif user == "linkedin":
        return "🌐 LinkedIn is a professional networking platform."

    elif user == "help":
        return "Commands: hello, hi, ai, python, github, linkedin, date, time, exit"

    elif user == "exit":
        return "exit"

    else:
        return "❌ Sorry! I don't understand."