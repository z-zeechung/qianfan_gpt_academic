#include <windows.h>
#include <fstream>
#include <unistd.h>
#include <process.h>
#include <cstdio>

/* The 'main' function of Win32 GUI programs: this is where execution starts */
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
	chdir(".\\src\\gpt_academic");
	//system("..\\python\\python.exe windows_run.py");
	
	
	STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory(&si, sizeof(STARTUPINFO));
    si.cb = sizeof(STARTUPINFO);
    ZeroMemory(&pi, sizeof(PROCESS_INFORMATION));
    
	LPSTR commandLine = "..\\python\\python.exe windows_run.py";
	CreateProcess(NULL, commandLine, NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi);
	
	
	
	/*HANDLE hFile = CreateFile("output.log", GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
	
	si.hStdError = hFile;
	si.hStdOutput = hFile;
	
	CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    CloseHandle(hFile);*/
}
