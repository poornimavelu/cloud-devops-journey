total_requests = 500
failed_requests = 0

try:
    error_rate = total_requests / failed_requests
    print(f"Error rate: {error_rate}")
except ZeroDivisionError:
    print("Cannot calculate rate: failed requests is zero")

########################################################################

def parse_and_divide(input_string):
 try:
    num = int(input_string)
    result = 100 / num
    print(f"Result is: {result}")
 except ValueError:
   print ("Error: Input must be a valid integer")
 except ZeroDivisionError:
   print ("Error: Cannot divide by zero")
parse_and_divide("25")
parse_and_divide("0")
parse_and_divide("cluster-a")

def parse_and_divide(input_string):
    try:
        num = int(input_string)
        result = 100 / num
        print(f"Result is: {result}")
    except ValueError:
        print("Error: Input must be a valid integer")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

parse_and_divide("25")
parse_and_divide("0")
parse_and_divide("cluster-a")

######################################################################

print("Opening connection to database...")
try:
     "timeout" + 404
except TypeError:
     print("Caught error: Incompatible types in query")
finally:
     print("Closing database connection.")
   




    

    