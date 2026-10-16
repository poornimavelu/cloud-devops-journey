def configure_port():
    service_port = 8080
    print("Port configured inside function:", service_port)
    return service_port
result=configure_port()
print("Port outside function:",result)


##################################\

error_counter = 0
def record_error():
    global error_counter
    error_counter+=1
record_error()
record_error()
record_error()

print(record_error())


error_counter = 0

def record_error():
    global error_counter
    error_counter += 1

record_error()
record_error()
record_error()

print(error_counter)

###################################


    