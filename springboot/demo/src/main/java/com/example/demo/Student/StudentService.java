package com.example.demo.Student;

import java.time.LocalDate;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jakarta.transaction.Transactional;

@Service
public class StudentService {

    private final StudentRepository studentRepository;

    @Autowired
    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }
    
    public List<Student> hello() {
        return studentRepository.findAll();
    }

    public void addNewStudent(Student student) {
        Optional<Student> studentOptional = studentRepository.findStudentByEmail(student.getEmail());
        if (studentOptional.isPresent()) {
            throw new IllegalStateException("Email taken");
        }
        studentRepository.save(student);
    }

    public void deleteStudent(Long studentId) {
        if (!studentRepository.existsById(studentId)) {
            throw new IllegalStateException("Student with id " + studentId + " does not exist");
        }
        studentRepository.deleteById(studentId);
    }

    @Transactional
    public void updateStudent(Long studentId, String name, String email, LocalDate dob) {
        // Optional<Student> studentOptional = studentRepository.findStudentById(studentId);
        // if (!studentOptional.isPresent()) {
        //     throw new IllegalStateException("Student with id " + studentId + " does not exist");
        // }
        Student student = studentRepository.findStudentById(studentId)
                .orElseThrow(() -> new IllegalStateException(
                        "Student with id " + studentId + " does not exist"));
        
        if (name != null
                && name.length() > 0
                && !Objects.equals(student.getName(), name)) {
            student.setName(name);
        }

        if (email != null
                && email.length() > 0
                && !Objects.equals(student.getEmail(), email)) {
            
            Optional<Student> studentOptional = studentRepository.findStudentByEmail(email);
            if (studentOptional.isPresent()) {
                throw new IllegalStateException("Email taken");
            }
            student.setEmail(email);
        }

        if (dob != null) {
            student.setDob(dob);
        }
        // studentRepository.update(student);
    }
}
