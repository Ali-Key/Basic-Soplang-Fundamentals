# 🌍 Soplang Data Types Guide

Welcome to the **Soplang Data Types Guide** — a simple and beginner-friendly introduction to the different data types and variable declaration keywords available in **Soplang**, a Somali-first programming language.

This guide covers the most common types you'll use when writing Soplang code, complete with examples and comments in both English and Somali.

---

## 📘 What is Soplang?

**Soplang** is a beginner-focused, easy-to-learn programming language designed for Somali speakers. It uses familiar syntax and Somali keywords to help new programmers learn core programming concepts in their native language.

---

## 🧠 What You'll Learn

In this guide, you'll learn how to:

- Declare variables using `door`, `tiro`, `qoraal`, `labadaran`, `shey`, `liis`, and `waxba`
- Work with strings, numbers, booleans, lists, and dictionaries
- Display values using the built-in `qor()` function
- Combine and display multiple variables
- Understand both dynamic and static typing in Soplang

---

## 🔑 Variable Declaration Keywords

Soplang provides several keywords for declaring variables, each tailored to specific data types. Here's a summary:

| **Keyword** | **Meaning**               | **English Equivalent** | **Example**                              |
|-------------|---------------------------|-------------------------|------------------------------------------|
| `door`      | Dynamic variable declaration | `var`/`let`            | `door magac = "Ali Key"`               |
| `tiro`      | Integer type              | `int`                  | `tiro da = 21`                           |
| `qoraal`    | String type               | `string`               | `qoraal magac = "Ali Omar"`             |
| `labadaran` | Boolean type              | `bool`                 | `labadaran waaRun = true`                |
| `shey`      | Object type               | `object`               | `shey person = { "name": "Ali Key" }`  |
| `liis`      | List/array type           | `array`                | `liis numbers = [1, 2, 3]`               |
| `waxba`     | Null value                | `null`                 | `door a = waxba`                         |

---

## 🔠 1. Primitive Data Types

### 🧵 String (Xarfo)
Represents a sequence of characters or text.

```soplang
qoraal name = "Ali Omar Abdi"
```

✅ Example: "Ali Omar Abdi"

### 🔢 Integer (Lambaro Dhan)
Whole numbers without decimals.

```soplang
tiro age = 21
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
labadaran isStudent = run
```

✅ Example: run or been

---

## 📚 2. Collection Types

### 📋 List (Liis)
An ordered group of values.

```soplang
liis grades = [85, 90, 78]
```

✅ Example: [85, 90, 78]

### 🗂️ Dictionary (Sheyga)
A group of key-value pairs.

```soplang
shey PersonInfo = {
    "name": "Ahmed",
    "age": 21,
    "isStudent": run
}
```

✅ Example: {"name": "Ahmed", "age": 21}

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
qoraal name = "Ali Omar Abdi"
tiro age = 21
door height = 5.9
labadaran isStudent = run
liis grades = [85, 90, 78]

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
| String     | qoraal       | "Ali Omar Abdi"         |
| Integer    | tiro         | 21                      |
| Float      | door         | 5.9                     |
| Boolean    | labadaran    | run, been               |
| List       | liis         | [85, 90, 78]            |
| Dictionary | shey         | {"name": "Ali", "age": 21} |

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






