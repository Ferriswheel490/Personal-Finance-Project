#Cecily's Helpers
import trace
import sys
def debug():
    def trace_calls(frame,event,argument):
        func=frame.f_code.co_name
        ignore=['__init__','_shutdown','ident','_stop','daemon','_maintain_shutdown_locks','<listcomp>']
        if func in ignore or func[0]=='_' or func[0]=='<':
            pass
        else:
            if event == 'call': #when function is called
                #f_code: the file
                #co_name: the function
                #f_code.co_name: function name
                print(f'Calling function: {frame.f_code.co_name}')

            elif event == 'line': #when a new line of code happens
                #lineno: line number
                print(f'    Executing line {frame.f_lineno} in {frame.f_code.co_name}')

            elif event == 'return': #When we return stuff
                print(f'    {frame.f_code.co_name} returned {argument}')

            elif event == 'exception': #Triggered when there is an exception
                print(f'        Exeption in {frame.f_code.co_name}: {argument}')

        return trace_calls
    sys.settrace(trace_calls)