from google import genai

client = genai.Client(api_key="AIzaSyCx5z2QN8f4POg3M2-iEYZEgSokWwcI448")

def main():
    try:
        models = client.models.list()

        print("\n✅ AVAILABLE MODELS:\n")

        for m in models:
            print(m.name)

    except Exception as e:
        print("\n❌ ERROR OCCURRED:\n")
        print(e)

if __name__ == "__main__":
    main()