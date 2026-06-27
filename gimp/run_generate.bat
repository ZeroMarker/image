@echo off
echo ========================================
echo GIMP 图片生成脚本
echo ========================================
echo.

REM 检查 GIMP 是否安装
where gimp >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到 GIMP 命令
    echo 请确保 GIMP 已安装并添加到系统 PATH
    echo.
    echo 默认安装路径:
    echo   C:\Program Files\GIMP 2\bin
    echo.
    pause
    exit /b 1
)

echo 正在运行图片生成脚本...
echo.

REM 运行 Python-Fu 脚本
gimp -i -b "(python-fu-eval RUN-NONINTERACTIVE 0 \"execfile('D:/image/gimp/create_images.py')\")" -b "(gimp-quit 0)"

echo.
echo ========================================
echo 脚本执行完成！
echo 输出目录: %USERPROFILE%\gimp_output
echo ========================================
echo.

REM 打开输出目录
explorer "%USERPROFILE%\gimp_output"

pause
