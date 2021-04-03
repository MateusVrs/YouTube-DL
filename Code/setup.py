from cx_Freeze import setup, Executable
setup(
    name="YouTube - Download",
    version="1.0.3",
    options={"build_exe": {
        'packages': ["tkinter", "time", "pytube"],
        'include_files': ['Images/youtube.png', 'Images/youtube.ico'],
        'include_msvcr': True,
    }},
    executables=[Executable("main.pyw", base='Win32GUI',
                            icon='Images/youtube.ico',
                            target_name='YouTube - Download',
                            shortcutName='Youtube - Download',
                            shortcutDir='DesktopFolder')]
)

# python setup.py bdist_msi
