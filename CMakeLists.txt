find_package(wxWidgets REQUIRED COMPONENTS core base)
include(${wxWidgets_USE_FILE})
add_executable(app app.cpp)
target_link_libraries(app ${wxWidgets_LIBRARIES})