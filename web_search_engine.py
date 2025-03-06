import requests

def search_web(query):
    api_key = "AIzaSyCYDnr93uWTNUpmeDB3HOklWD9482NFUVA"  
    search_engine_id = "94d4e5df9917b4235"  
    
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    
    response = requests.get(url)
    data = response.json()
    results = []

    if "items" in data:
        for item in data["items"]:
            results.append((item["title"], item["snippet"]))
    
    return results

def main():
    while True:
        query = input("Enter search query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        results = search_web(query)
        if results:
            print("\nSearch Results:")
            for title, snippet in results:
                print(f"\nTitle: {title}\nSnippet: {snippet}\n")
        else:
            print("No results found.")

if __name__ == "__main__":
    main()
