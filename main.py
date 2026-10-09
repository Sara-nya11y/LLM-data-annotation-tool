# LLM Training Data Annotation Tool - Pro Level
import json

print("=== LLM Data Annotation Tool (ChatGPT Style) ===")
print("This tool creates training data for AI models\n")

dataset = []

while True:
    print("\n--- New Data Point ---")
    user_prompt = input("Enter User Prompt (or 'q' to save & quit): ")
    if user_prompt.lower() == 'q':
        break

    ai_response = input("Enter Ideal AI Response: ")
    
    print("\nRate the data:")
    print("1. Category: [Helpful, Harmful, Coding, General]")
    print("2. Quality: [Good, Bad, Average]")
    print("3. Language: [English, Telugu, Hinglish]")
    
    category = input("Enter Category: ")
    quality = input("Enter Quality: ")
    language = input("Enter Language: ")

    data_point = {
        "prompt": user_prompt,
        "ideal_response": ai_response,
        "annotation": {
            "category": category,
            "quality": quality,
            "language": language
        }
    }
    dataset.append(data_point)
    print(f"Added! Total: {len(dataset)}")

# Save as JSONL - This is how OpenAI, Meta train AI
with open("llm_training_data.jsonl", "w", encoding="utf-8") as f:
    for data in dataset:
        json.dump(data, f, ensure_ascii=False)
        f.write("\n")

print(f"\nSUCCESS! {len(dataset)} training points created.")
print("File saved: llm_training_data.jsonl")
print("This is the EXACT format used by OpenAI & Meta to train AI!")
