# Foxdot file include Test

message = "Include function loaded"

def include_message(text_01 = message):
    print(text_01)
    return

if __name__ == "__main__":
    include_message("Include function text from include_test loaded")