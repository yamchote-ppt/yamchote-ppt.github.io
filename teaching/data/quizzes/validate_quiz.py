#!/usr/bin/env python3
"""
Quiz JSON Validator
Validates quiz JSON files for common errors before deployment
"""

import json
import sys
from pathlib import Path

def validate_quiz_file(filepath):
    """Validate a quiz JSON file"""
    errors = []
    warnings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"❌ Invalid JSON syntax: {e}"], []
    except Exception as e:
        return [f"❌ Error reading file: {e}"], []
    
    # Check required top-level fields
    required_fields = ['id', 'courseCode', 'title', 'duration', 'questions']
    for field in required_fields:
        if field not in data:
            errors.append(f"❌ Missing required field: '{field}'")
    
    # Validate duration
    if 'duration' in data:
        if not isinstance(data['duration'], int) or data['duration'] <= 0:
            errors.append(f"❌ duration must be a positive integer, got: {data['duration']}")
    
    # Validate questions
    if 'questions' in data:
        if not isinstance(data['questions'], list):
            errors.append("❌ 'questions' must be an array")
        elif len(data['questions']) == 0:
            warnings.append("⚠️  No questions found in quiz")
        else:
            question_ids = set()
            for i, q in enumerate(data['questions'], 1):
                # Check required question fields
                q_required = ['id', 'question', 'type', 'points']
                for field in q_required:
                    if field not in q:
                        errors.append(f"❌ Question {i}: Missing '{field}'")
                
                # Check duplicate IDs
                if 'id' in q:
                    if q['id'] in question_ids:
                        errors.append(f"❌ Question {i}: Duplicate ID '{q['id']}'")
                    question_ids.add(q['id'])
                
                # Validate question type
                if 'type' in q:
                    if q['type'] not in ['multiple-choice', 'text']:
                        errors.append(f"❌ Question {i}: Invalid type '{q['type']}', must be 'multiple-choice' or 'text'")
                    
                    # Type-specific validation
                    if q['type'] == 'multiple-choice':
                        if 'options' not in q:
                            errors.append(f"❌ Question {i}: Missing 'options' for multiple-choice")
                        elif not isinstance(q['options'], list):
                            errors.append(f"❌ Question {i}: 'options' must be an array")
                        elif len(q['options']) < 2:
                            errors.append(f"❌ Question {i}: Must have at least 2 options")
                        
                        if 'correctAnswer' in q:
                            if not isinstance(q['correctAnswer'], int):
                                errors.append(f"❌ Question {i}: correctAnswer must be integer for multiple-choice")
                            elif 'options' in q and isinstance(q['options'], list):
                                if q['correctAnswer'] < 0 or q['correctAnswer'] >= len(q['options']):
                                    errors.append(f"❌ Question {i}: correctAnswer {q['correctAnswer']} out of range (0-{len(q['options'])-1})")
                        else:
                            errors.append(f"❌ Question {i}: Missing 'correctAnswer'")
                    
                    elif q['type'] == 'text':
                        if 'correctAnswer' not in q:
                            warnings.append(f"⚠️  Question {i}: No reference answer provided for text question")
                
                # Validate points
                if 'points' in q:
                    if not isinstance(q['points'], (int, float)) or q['points'] <= 0:
                        errors.append(f"❌ Question {i}: points must be positive number, got: {q['points']}")
    
    # Check for template placeholders
    if 'id' in data and data['id'] == 'CHANGE_ME':
        warnings.append("⚠️  Quiz ID still set to 'CHANGE_ME'")
    if 'courseCode' in data and data['courseCode'] == 'CHANGE_ME':
        warnings.append("⚠️  Course code still set to 'CHANGE_ME'")
    
    # Check for comment fields (should be removed)
    comment_fields = [k for k in data.keys() if k.startswith('_')]
    if comment_fields:
        warnings.append(f"⚠️  Found comment fields (should be removed): {', '.join(comment_fields)}")
    
    return errors, warnings


def validate_config_file(filepath):
    """Validate quiz-config.json file"""
    errors = []
    warnings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"❌ Invalid JSON syntax: {e}"], []
    except Exception as e:
        return [f"❌ Error reading file: {e}"], []
    
    # Check top-level structure
    if 'courses' not in data:
        errors.append("❌ Missing 'courses' field")
        return errors, warnings
    
    if not isinstance(data['courses'], dict):
        errors.append("❌ 'courses' must be an object")
        return errors, warnings
    
    # Validate each course
    for course_code, course_data in data['courses'].items():
        if not isinstance(course_data, dict):
            errors.append(f"❌ Course {course_code}: Must be an object")
            continue
        
        # Check required course fields
        if 'quizzes' not in course_data:
            errors.append(f"❌ Course {course_code}: Missing 'quizzes' array")
            continue
        
        if not isinstance(course_data['quizzes'], list):
            errors.append(f"❌ Course {course_code}: 'quizzes' must be an array")
            continue
        
        # Validate each quiz entry
        quiz_ids = set()
        for i, quiz in enumerate(course_data['quizzes'], 1):
            if not isinstance(quiz, dict):
                errors.append(f"❌ Course {course_code}, Quiz {i}: Must be an object")
                continue
            
            # Check required fields
            for field in ['id', 'file', 'displayName', 'enabled']:
                if field not in quiz:
                    errors.append(f"❌ Course {course_code}, Quiz {i}: Missing '{field}'")
            
            # Check duplicate IDs
            if 'id' in quiz:
                if quiz['id'] in quiz_ids:
                    errors.append(f"❌ Course {course_code}: Duplicate quiz ID '{quiz['id']}'")
                quiz_ids.add(quiz['id'])
            
            # Check file exists
            if 'file' in quiz:
                quiz_path = Path(filepath).parent / quiz['file']
                if not quiz_path.exists():
                    errors.append(f"❌ Course {course_code}, Quiz {i}: File not found: {quiz['file']}")
            
            # Check enabled field
            if 'enabled' in quiz and not isinstance(quiz['enabled'], bool):
                errors.append(f"❌ Course {course_code}, Quiz {i}: 'enabled' must be boolean (true/false)")
    
    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_quiz.py <quiz-file.json>")
        print("   or: python validate_quiz.py quiz-config.json")
        print("   or: python validate_quiz.py --all")
        sys.exit(1)
    
    if sys.argv[1] == '--all':
        # Validate all quiz files in directory
        quiz_dir = Path(__file__).parent
        all_valid = True
        
        # Validate config
        config_file = quiz_dir / 'quiz-config.json'
        if config_file.exists():
            print(f"\n{'='*60}")
            print(f"Validating: quiz-config.json")
            print('='*60)
            errors, warnings = validate_config_file(config_file)
            
            if errors:
                all_valid = False
                print("\n❌ ERRORS:")
                for error in errors:
                    print(f"  {error}")
            
            if warnings:
                print("\n⚠️  WARNINGS:")
                for warning in warnings:
                    print(f"  {warning}")
            
            if not errors and not warnings:
                print("✅ No issues found!")
        
        # Validate all quiz JSON files
        for quiz_file in quiz_dir.glob('*-*.json'):
            if quiz_file.name == 'quiz-config.json':
                continue
            
            print(f"\n{'='*60}")
            print(f"Validating: {quiz_file.name}")
            print('='*60)
            
            errors, warnings = validate_quiz_file(quiz_file)
            
            if errors:
                all_valid = False
                print("\n❌ ERRORS:")
                for error in errors:
                    print(f"  {error}")
            
            if warnings:
                print("\n⚠️  WARNINGS:")
                for warning in warnings:
                    print(f"  {warning}")
            
            if not errors and not warnings:
                print("✅ No issues found!")
        
        print("\n" + "="*60)
        if all_valid:
            print("✅ All quiz files are valid!")
        else:
            print("❌ Some files have errors. Please fix them before deploying.")
        print("="*60)
        
        sys.exit(0 if all_valid else 1)
    
    filepath = Path(sys.argv[1])
    
    if not filepath.exists():
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    
    print(f"Validating: {filepath.name}")
    print("="*60)
    
    if filepath.name == 'quiz-config.json':
        errors, warnings = validate_config_file(filepath)
    else:
        errors, warnings = validate_quiz_file(filepath)
    
    if errors:
        print("\n❌ ERRORS:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("✅ No issues found! Quiz file is valid.")
    
    print("="*60)
    
    sys.exit(0 if not errors else 1)


if __name__ == '__main__':
    main()
