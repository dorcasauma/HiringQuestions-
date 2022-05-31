import re
from googletrans import Translator

def google_translator():
    return Translator()

def api(word):
    error_message = ''
    try:
        if not word  or len(word) == 0:
            error_message = "String is empty or invalid"
        elif not re.search('[a-zA-Z]', word):
            error_message = "String invalid characters"
            
        if error_message != '':
            return {
                "message": error_message,
                "success": False,
                "input_string": word
            }
       
        detector = google_translator()
        return_data = list()
        language_list = []
        for item in word.split(' '):
            detect_result = detector.detect(item)
            print(detect_result)
            return_data.append(
                {
                    "input_string": item,
                    "short_form": detect_result[0],
                    "long_form": detect_result[1]
                }
            )
            language_list.append(detect_result[0])

        return {
            "data": return_data,
            "success": True,
            "input_string": word,
            "same_language": len(set(language_list)) == 1
        }
    except Exception as e:
        print(e)
        return {
            "message": "String is empty or invalid",
            "success": False,
        }

if __name__ == "__main__":
    print(api("hello world"))