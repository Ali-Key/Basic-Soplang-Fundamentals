# 🌍 Soplang Data Types Guide

Welcome to the **Soplang Data Types Guide** — a simple and beginner-friendly introduction to the different data types available in **Soplang**, a Somali-first programming language.

This guide covers the most common types you'll use when writing Soplang code, complete with examples and comments in both English and Somali.

---

## 📘 What is Soplang?

**Soplang** is a beginner-focused, easy-to-learn programming language designed for Somali speakers. It uses familiar syntax and Somali keywords to help new programmers learn core programming concepts in their native language.

---

## 🧠 What You'll Learn

In this guide, you'll learn how to:

- Declare variables using `door`, `liis`, `shey`
- Work with strings, numbers, booleans, lists, and dictionaries
- Display values using the built-in `qor()` function
- Combine and display multiple variables
- Understand both dynamic and static typing in Soplang

---

## 🔠 1. Primitive Data Types

### 🧵 String (Xarfo)
Represents a sequence of characters/text.

```soplang
door name = "Ali Omar Abdi"
```

✅ Example: "Ali Omar Abdi"

### 🔢 Integer (Lambaro Dhan)
Whole numbers without decimals.

```soplang
door age = 21
```

✅ Example: 21

### 🔟 Float (Lambaro Dhibco Leh)
Decimal numbers.

```soplang
door height = 5.9
```

✅ Example: 5.9

### ✅ Boolean (Run/Been)
Represents truth values: run (true), been (false)

```soplang
door isStudent = run
```

✅ Example: run or been

---

## 📚 2. Collection Types

### 📋 List (Liis)
An ordered group of values.

```soplang
door grades = [85, 90, 78]
```

✅ Example: [85, 90, 78]

### 🗂️ Dictionary (Sheyga)
A group of key-value pairs.

```soplang
door PersonInfo = {
    "name": "Ahmed",
    "age": 21,
    "isStudent": run
}
```

✅ Example: {"name": "Ahmed", "age": 21}

You can also use the shey keyword:

```soplang
shey PersonInfo = {
    "name": "Ahmed",
    "age": 21,
    "isStudent": run
}
```

---

## 🖨️ 3. Displaying Values with qor()
Use the qor() function to print values.

```soplang
qor("Name: " + name)
qor("Age: " + age)
qor("Height: " + height)
qor("Is Student: " + isStudent)
qor("Grades: " + grades)
qor("Person: " + PersonInfo)
```

---

## 🧾 4. Full Example

```soplang
door name = "Ali Omar Abdi"
door age = 21
door height = 5.9
door isStudent = run
door grades = [85, 90, 78]

shey PersonInfo = {
    "name": "Ali Omar Abdi",
    "age": 21,
    "isStudent": run
}

qor("My name is " + name + ", I am " + age + " years old, and I am a student: " + isStudent)
```

---

## 📝 Summary Table

| Type       | Keyword(s)   | Example                  |
|------------|--------------|--------------------------|
| String     | door         | "Ali Omar Abdi"         |
| Integer    | door, labadaran | 21                   |
| Float      | door, labadaran | 5.9                  |
| Boolean    | door         | run, been               |
| List       | liis, door   | [85, 90, 78]            |
| Dictionary | shey, door   | {"name": "Ali", "age": 21} |

---

## 👨‍💻 Author

Ali Omar Abdi  
📍 Mogadishu, Somalia  
🎓 Computer Applications Student at JUST University  
🔗 LinkedIn  
💻 GitHub  

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 💡 Tip for Beginners

Don't worry if you don't understand everything the first time. Practice writing and reading Soplang code regularly — it gets easier with time!






