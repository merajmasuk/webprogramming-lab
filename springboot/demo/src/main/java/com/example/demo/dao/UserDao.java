package com.example.demo.dao;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Repository;

@Repository
public class UserDao {
    private final static List<UserDetails> APPLICATION_USERS = Arrays.asList(
        new User(
            "merajmasuk@gmail.com",
            "password",
            Collections.singleton(new SimpleGrantedAuthority("ROLE_ADMIN"))
        ),
        new User(
            "meraj.stu2017@juniv.edu",
            "password",
            Collections.singleton(new SimpleGrantedAuthority("ROLE_ADMIN"))
        )
    );

    public UserDetails finduserByEmail(String email) {
        return APPLICATION_USERS
                    .stream()
                    .filter(u -> u.getUsername().equals(email))
                    .findFirst()
                    .orElseThrow(() -> new UsernameNotFoundException("User not found"));
    }

}
