@echo off
rem --- THIS IS THE MAGIC LINE ---
cd /d "%~dp0"
rem --- IT FORCES THE SCRIPT TO WORK IN ITS OWN DIRECTORY ---

SETLOCAL EnableDelayedExpansion

rem --- Define File Type Mappings ---
set "image_types=.jpg .jpeg .png .gif .bmp .webp"
set "video_types=.mp4 .mov .avi .mkv .webm"
rem --- Add more types as needed, e.g., set "audio_types=.mp3 .wav" ---

rem For each file in the current folder
for %%f in (".\*") do (
    rem Get the file extension
    set "ext=%%~xf"
    
    rem Check if it's a file and not our script
    if defined ext if /i "%%~nxF" neq "%~nx0" (
        
        set "target_folder="

        rem Check if the extension is in our image list
        for %%t in (%image_types%) do (
            if /i "!ext!"=="%%t" set "target_folder=Images"
        )

        rem Check if the extension is in our video list
        for %%t in (%video_types%) do (
            if /i "!ext!"=="%%t" set "target_folder=Videos"
        )
        
        rem --- Add more checks for other types here ---

        rem If no specific mapping was found, use the extension name (without the dot)
        if not defined target_folder (
            set "target_folder=!ext:~1!"
        )

        rem If a target folder was determined...
        if defined target_folder (
            rem Check if the target folder exists, if not, create it
            if not exist "!target_folder!" mkdir "!target_folder!"
            
            rem Move the file
            echo Moving "%%~nxF" to "!target_folder!\"
            move "%%f" "!target_folder!\"
        )
    )
)

echo.
echo Sorting complete!
pause