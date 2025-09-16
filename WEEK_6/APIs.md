# APIs (Application Programming Interfaces)

## 🔹 What is an API?
An **API** is like a **messenger** between two software programs.  
It defines how different software components should **talk to each other**.

👉 Example in real life:  
- You (the user) want food.  
- The **kitchen** (server) prepares it.  
- The **waiter (API)** takes your order, tells the kitchen, and brings food back.  

So, an API is the **middleman** that helps two systems communicate.

---

## 🔹 Types of APIs
1. **Web APIs**  
   - Allow apps to talk to each other over the internet.  
   - Example: Weather API (you ask for today’s weather, it gives back temperature and forecast).  

2. **Library/API in Programming**  
   - A set of functions you can use in your code.  
   - Example: Python’s `math` module is an API that lets you use `sqrt()` or `sin()` without writing the logic.

---

## 🔹 How APIs Work (Web Example)
1. **You send a request** → e.g., ask for user data from GitHub.  
2. **API processes it** → Talks to the database or service.  
3. **API sends a response** → You get JSON or data back.  

👉 **Request Example (HTTP):**  
```
GET https://api.github.com/users/octocat
```

👉 **Response Example (JSON):**
```json
{
  "login": "octocat",
  "id": 1,
  "public_repos": 8
}
```

---

## 🔹 Why APIs are Important
- Reuse features without building from scratch.  
- Make apps **communicate** (e.g., Google Maps API in Ola/Uber).  
- Provide **security** (you don’t directly access databases).  

---

✅ **In short:**  
An **API is a bridge that lets two software applications talk to each other.**
