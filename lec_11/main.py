import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_filtered_posts():
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        
        filtered_posts = [
            post for post in posts
            if len(post['title'].split()) <= 6 and post['body'].count('\n') < 3
        ]
        
        for post in filtered_posts:
            print(f"Title: {post['title']}")
            print(f"Body: {post['body'][:100]}...")  # Show only the first 100 characters
            print("-" * 40)
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

def create_post():
    new_post = {
        "title": "New Post Title",
        "body": "This is the content of the new post.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    if response.status_code == 201:
        print("Post created successfully:")
        print(response.json())
    else:
        print(f"Failed to create post. Status code: {response.status_code}")

def update_post(post_id):
    updated_post = {
        "title": "Updated Post Title",
        "body": "Updated content for the post.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    if response.status_code == 200:
        print("Post updated successfully:")
        print(response.json())
    else:
        print(f"Failed to update post. Status code: {response.status_code}")

def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print(f"Post with ID {post_id} deleted successfully.")
    else:
        print(f"Failed to delete post with ID {post_id}. Status code: {response.status_code}")

def main():
    print("Performing GET request with filters:")
    get_filtered_posts()
    
    print("\nPerforming POST request to create a new post:")
    create_post()
    
    print("\nPerforming PUT request to update a post:")
    update_post(post_id=1)
    
    print("\nPerforming DELETE request to delete a post:")
    delete_post(post_id=1)

if __name__ == "__main__":
    main()
