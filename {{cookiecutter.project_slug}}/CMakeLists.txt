cmake_minimum_required(VERSION 3.14)

project({{ cookiecutter.project_slug }} VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

{% if cookiecutter.use_spdlog == 'y' -%}
find_package(spdlog REQUIRED)
{% endif -%}
{% if cookiecutter.use_opencv == 'y' -%}
find_package(OpenCV REQUIRED)
{% endif -%}
{% if cookiecutter.use_ntcore == 'y' -%}
find_package(ntcore REQUIRED)
find_package(Threads REQUIRED)
{% endif -%}
{% if cookiecutter.use_tbb == 'y' -%}
find_package(TBB REQUIRED)
{% endif %}
add_subdirectory(src)
