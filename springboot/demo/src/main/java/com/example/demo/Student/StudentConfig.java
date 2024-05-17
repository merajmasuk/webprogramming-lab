package com.example.demo.Student;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class StudentConfig {
    @Bean
    CommandLineRunner commandLineRunner(StudentRepository repository) {
        return args -> {
            Student meraj = new Student(
                "Meraj al Maksud",
                "merajmasuk@gmail.com",
                LocalDate.of(1997, Month.DECEMBER, 17),
                27
            );

            Student alex = new Student(
                "Alex",
                "alex@gmail.com",
                LocalDate.of(2004, Month.JANUARY, 5),
                21
            );

            repository.saveAll(
                List.of(meraj, alex)
            );
        };
    }
}
