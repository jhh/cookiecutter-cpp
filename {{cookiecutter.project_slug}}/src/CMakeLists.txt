
add_executable({{ cookiecutter.project_slug }}-app
    main.cpp
)

target_link_libraries({{ cookiecutter.project_slug }}-app
    PRIVATE
    ntcore
    ${OpenCV_LIBS}
    ${TBB_IMPORTED_TARGETS}
)
