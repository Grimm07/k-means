cmake_minimum_required(VERSION 3.21)
project(Project)

set(CMAKE_CXX_STANDARD 14)

link_libraries(sqlite3)
include_directories(Code/C/include)
add_executable(Project
        Code/C/src/km.c
        Code/C/src/main.c
        )
