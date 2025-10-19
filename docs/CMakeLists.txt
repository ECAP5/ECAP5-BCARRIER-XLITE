find_package(Sphinx)

if(Sphinx_FOUND)
  add_sphinx_document(
      documentation
      CONF_FILE "${CMAKE_CURRENT_LIST_DIR}/src/conf.py"
      SKIP_PDF
      "${CMAKE_CURRENT_LIST_DIR}/src/_ext/requirement.py"
      "${CMAKE_CURRENT_LIST_DIR}/src/_static/css/custom.css"
      "${CMAKE_CURRENT_LIST_DIR}/src/_static/mechanical.pdf"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/logo.svg"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/io-pinout.svg"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/io-pinout.csv"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/stackup.png"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/power.png"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/som.png"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/power-ldo.png"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/uart-selector.svg"
      "${CMAKE_CURRENT_LIST_DIR}/src/assets/overview.svg"
      "${CMAKE_CURRENT_LIST_DIR}/src/index.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/index.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/1_introduction.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/2_specification.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/3_system_overview.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/4_power.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/5_soms.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/6_uart.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/7_misc.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/8_mechanical.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/design/9_routing.rst"
      "${CMAKE_CURRENT_LIST_DIR}/src/errata/1.0.rst"
    )
else()
  message(WARNING "No Sphinx found. Documentation target not available.")
endif()
