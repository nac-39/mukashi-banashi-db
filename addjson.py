import json

def main():
    with open("./stories.json", "r",encoding="utf-8") as f:
        question_json = json.loads(f.read())
        print(len(question_json))
        while True:
            new_title = input("title: ")
            new_content = input("content: ")
            if not(new_title) or not(new_content):
                break
            question_json.append({
                "title": new_title,
                "content": new_content
            })

    with open("./stories.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(question_json, indent=2, ensure_ascii=False))
    
if __name__ == "__main__":
    main()