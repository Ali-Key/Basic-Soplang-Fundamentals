# 🌍 Soplang Basics: Data Types and Operators

Welcome to the **Soplang Basics Guide**! This guide is designed to help beginners learn the fundamentals of **Soplang**, a Somali-first programming language. Soplang uses simple Somali keywords to make programming easy and fun.

---

## 📘 What is Soplang?

**Soplang** is a beginner-friendly programming language created for Somali speakers. It uses Somali keywords to teach programming concepts in a way that feels natural and easy to understand.

---

## 🧠 What You'll Learn

In this guide, you'll learn how to:

- Declare variables using Soplang keywords like `door`, `tiro`, `qoraal`, `labadaran`, `shey`, `liis`, and `waxba`.
- Work with strings, numbers, booleans, lists, and dictionaries.
- Use basic operators like arithmetic, comparison, logical, and assignment operators.
- Display values using the built-in `qor()` function.
- Combine and display multiple variables in a single output.

---

## 🔑 Variable Declaration Keywords

Here’s a quick summary of the keywords used to declare variables in Soplang:

| **Keyword** | **Meaning**               | **Example**                              |
|-------------|---------------------------|------------------------------------------|
| `door`      | Dynamic variable          | `door magac = "Ali Key"`                |
| `tiro`      | Integer (whole number)    | `tiro da = 21`                          |
| `qoraal`    | String (text)             | `qoraal magac = "Ali Omar"`             |
| `labadaran` | Boolean (true/false)      | `labadaran waaRun = run`                |
| `shey`      | Object (key-value pairs)  | `shey personInfo = { "name": "Ali" }`   |
| `liis`      | List (array of values)    | `liis grades = [85, 90, 78]`            |
| `waxba`     | Null (empty value)        | `door a = waxba`                        |

---

## 🔠 Data Types in Soplang

### 🧵 String (Text)
Represents text or characters.

```soplang
qoraal name = "Ali Omar Abdi"
qor(name)  // Outputs: Ali Omar Abdi
```

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
    "name": "Ali Omar Abdi",
    "age": 21,
    "isStudent": run
}
```

✅ Example: {"name": "Ali Omar Abdi", "age": 21}

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

## ➕ Operators in Soplang

Soplang provides a variety of operators for performing operations on values. Here’s a summary of the most commonly used operators:

### 🔢 Arithmetic Operators
Used for mathematical calculations.

| **Operator** | **Description**       | **Example**               |
|--------------|-----------------------|---------------------------|
| `+`          | Addition              | `tiro sum = 5 + 3`        |
| `-`          | Subtraction           | `tiro diff = 10 - 4`      |
| `*`          | Multiplication        | `tiro product = 6 * 7`    |
| `/`          | Division              | `door quotient = 15 / 2`  |
| `%`          | Modulus (remainder)   | `tiro remainder = 10 % 3` |

---

### ⚖️ Comparison Operators
Used to compare values.

| **Operator** | **Description**       | **Example**               |
|--------------|-----------------------|---------------------------|
| `==`         | Equal to              | `labadaran isEqual = 5 == 5` |
| `!=`         | Not equal to          | `labadaran notEqual = 5 != 3` |
| `>`          | Greater than          | `labadaran isGreater = 7 > 4` |
| `<`          | Less than             | `labadaran isLess = 3 < 8` |
| `>=`         | Greater than or equal | `labadaran isGreaterOrEqual = 5 >= 5` |
| `<=`         | Less than or equal    | `labadaran isLessOrEqual = 4 <= 6` |

---

### 🧠 Logical Operators
Used to combine multiple conditions.

| **Operator** | **Description**       | **Example**               |
|--------------|-----------------------|---------------------------|
| `&&`         | Logical AND           | `labadaran result = run && been` |
| `||`         | Logical OR            | `labadaran result = run || been` |
| `!`          | Logical NOT           | `labadaran result = !run` |

---

### 🖋️ Assignment Operators
Used to assign values to variables.

| **Operator** | **Description**       | **Example**               |
|--------------|-----------------------|---------------------------|
| `=`          | Assign                | `tiro x = 10`             |
| `+=`         | Add and assign         | `tiro x += 5` (x = x + 5) |
| `-=`         | Subtract and assign    | `tiro x -= 3` (x = x - 3) |
| `*=`         | Multiply and assign    | `tiro x *= 2` (x = x * 2) |
| `/=`         | Divide and assign      | `door x /= 4` (x = x / 4) |
| `%=`         | Modulus and assign     | `tiro x %= 2` (x = x % 2) |


---

## 📝 Summary Table

| Type       | Keyword(s)   | Example                  |
|------------|--------------|--------------------------|
| String     | qoraal       | "Ali Omar Abdi"         |
| Integer    | tiro         | 21                      |
| Float      | door         | 5.9                     |
| Boolean    | labadaran    | run, been               |
| List       | liis         | [85, 90, 78]            |
| Dictionary | shey         | {"name": "Ali Omar Abdi", "age": 21} |

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






