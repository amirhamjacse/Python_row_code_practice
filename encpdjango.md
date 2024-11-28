Sure! Here's another simple example using Django to demonstrate **encapsulation**. In this example, we will create a **Student** model that holds the student's grade, and we will provide controlled access to that grade via methods to calculate and update the grade. 

### Example: **Encapsulation in a Student Model**

Let's say we have a **Student** model, and we want to encapsulate the student's grade. The grade will be private, and we will use methods to set and get the grade, as well as ensure that it stays within a valid range (0 to 100).

### Step-by-Step Example:

#### 1. Create the Model (`models.py`)

```python
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    # Private grade attribute (not directly accessible)
    __grade = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def set_grade(self, grade):
        """Setter method to update the student's grade."""
        if 0 <= grade <= 100:
            self.__grade = grade
            self.save()  # Save the updated grade to the database
        else:
            print("Grade must be between 0 and 100.")

    def get_grade(self):
        """Getter method to access the student's grade."""
        return self.__grade

    def __str__(self):
        """String representation of the student."""
        return f"Student {self.name}, Grade: {self.get_grade()}"
```

### **Explanation**:
- The `__grade` attribute is **private** and cannot be accessed directly from outside the class.
- The `set_grade()` method allows you to set the student's grade but ensures the grade is between `0` and `100`. If the grade is outside that range, it prevents updating it.
- The `get_grade()` method provides access to the student's grade, encapsulating the internal state.

#### 2. Create Views to Interact with the Student Model (`views.py`)

```python
# views.py
from django.shortcuts import render
from .models import Student

def student_details(request):
    student = Student.objects.first()  # Get the first student in the database

    return render(request, 'student_details.html', {'student': student})

def update_grade(request):
    student = Student.objects.first()  # Get the first student
    grade = float(request.GET.get('grade', 0))

    # Update the student's grade using the setter method
    student.set_grade(grade)

    return render(request, 'student_details.html', {'student': student})
```

### **Explanation**:
- The `student_details` view retrieves a **Student** object and passes it to the template for rendering.
- The `update_grade` view retrieves a **Student** object, gets the new grade from the request, and uses the `set_grade()` method to update the grade.

#### 3. Create Templates (`student_details.html`)

```html
<!-- student_details.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
</head>
<body>
    <h1>{{ student.name }}'s Grade</h1>
    <p>Current Grade: {{ student.get_grade }}</p>

    <form method="get" action="{% url 'update_grade' %}">
        <label for="grade">Update Grade: </label>
        <input type="text" name="grade" id="grade" required>
        <button type="submit">Update</button>
    </form>
</body>
</html>
```

### **Explanation**:
- The template displays the student’s name and their grade using the `get_grade()` method.
- The form allows the user to input a new grade, which is passed to the `update_grade` view to update the student's grade.

#### 4. Create URLs (`urls.py`)

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_details, name='student_details'),
    path('update_grade/', views.update_grade, name='update_grade'),
]
```

### **Explanation**:
- We define two URL routes: one to display the student details and another to update the student's grade.

### 5. Apply Migrations

Run the following commands to apply the migrations and set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### **Summary**:
- **Encapsulation** is used to protect the `__grade` field from direct access, and we provide controlled access to it using getter (`get_grade()`) and setter (`set_grade()`) methods.
- The **setter method** ensures that the grade is always between 0 and 100, encapsulating the logic for grade validation.
- We then interact with the model through the view and template, ensuring that users can update the grade only through the controlled method, not by modifying the grade directly.

### Benefits of Encapsulation in This Example:
- **Security**: The grade cannot be changed directly from outside the class. The logic for modifying the grade is encapsulated in the `set_grade()` method, which checks if the grade is valid.
- **Flexibility**: If we want to change the way grades are calculated or validated in the future, we only need to update the setter method without affecting the rest of the code.
- **Maintainability**: The model and views remain clean and focused on their responsibilities, with the internal workings of grade modification hidden within the `Student` model.

This is a simple and clear demonstration of **encapsulation** in Django that helps protect data integrity and makes your code more maintainable and secure.