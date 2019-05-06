
add_executable({{ cookiecutter.project_slug }}-app
    main.cpp
)

target_link_libraries({{ cookiecutter.project_slug }}-app
    PRIVATE
{% if cookiecutter.use_spdlog == 'y' -%}
spdlog::spdlog
{% endif -%}
{% if cookiecutter.use_opencv == 'y' -%}
${OpenCV_LIBS}
{% endif -%}
{% if cookiecutter.use_ntcore == 'y' -%}
ntcore
Threads::Threads
{% endif -%}
{% if cookiecutter.use_tbb == 'y' -%}
${TBB_IMPORTED_TARGETS}
{% endif -%}
)
