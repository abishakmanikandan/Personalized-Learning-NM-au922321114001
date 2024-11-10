import random
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Mock data for students
students = {
    "student_1": {"name": "Alice", "learning_style": "visual", "progress": 0.6, "preferences": ["math", "science"]},
    "student_2": {"name": "Bob", "learning_style": "auditory", "progress": 0.3, "preferences": ["history", "literature"]},
    "student_3": {"name": "Charlie", "learning_style": "kinesthetic", "progress": 0.8, "preferences": ["math", "geography"]},
}

# Mock data for educational content
content = {
    "content_1": {"subject": "math", "learning_style": "visual"},
    "content_2": {"subject": "science", "learning_style": "visual"},
    "content_3": {"subject": "history", "learning_style": "auditory"},
    "content_4": {"subject": "literature", "learning_style": "auditory"},
    "content_5": {"subject": "geography", "learning_style": "kinesthetic"},
}

# Function to calculate content recommendation based on learning style, subject preferences, and progress
def recommend_content(student_id):
    student = students.get(student_id)
    
    if not student:
        return "Student not found!"
    
    # Get student preferences
    preferred_subjects = student["preferences"]
    preferred_style = student["learning_style"]
    
    # Calculate recommendations
    recommendations = []
    for content_id, content_info in content.items():
        subject_match = content_info["subject"] in preferred_subjects
        style_match = content_info["learning_style"] == preferred_style
        
        # Score content based on matches (this is a simplified scoring approach)
        score = int(subject_match) + int(style_match)
        if score > 0:
            recommendations.append((content_id, score))
    
    # Sort recommendations by score
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    # Return the best recommendation
    recommended_content = [content_id for content_id, score in recommendations]
    
    return {
        "student": student["name"],
        "recommended_content": recommended_content
    }

# Example usage
for student_id in students:
    print(recommend_content(student_id))
