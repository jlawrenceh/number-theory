def Infinite():
    print("=================================")
    print("         INFINITE NUMBERS")
    print("=================================")
    print("The set of natural numbers is infinite.")
    
def ClosurePropertyAdd():
    print("=================================")
    print("   CLOSURE PROPERTY ADDITION")
    print("=================================")
    
    print("Natural addition is closed.")
    print("Formula: x + y is an element of Natural Numbers")
    
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x, ' + ', y, ' is an element of Natural Numbers' )

def ClosurePropertyMulti():
    print("===================================")
    print("   CLOSURE PROPERTY MULTIPLICATION")
    print("===================================")
    
    print("Natural multiplication is closed.")
    print("Formula: x * y is an element of Natural Numbers")
    
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x, ' * ', y, ' is an element of Natural Numbers' )
    
def AssociativePropertyAdd():
    print("=================================")
    print(" ASSOCIATIVE PROPERTY ADDITION")
    print("=================================")
    
    print("Natural number addition is associative.")
    print("Formula: x + ( y + z) = ( x + y ) + z")
    
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    print(x, ' + (', y, '+ ', z, ') = (' , x, " + ", y, ") + ", z)

def AssociativePropertyMulti():
    print("=====================================")
    print(" ASSOCIATIVE PROPERTY MULTIPLICATION")
    print("=====================================")
    
    print("Natural number multiplication is associative.")
    print("Formula: (x * y) * z = x * (y * z)")
    
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    print('(', x, '*', y, ') *', z, '=', x, '* (', y, '*', z, ')')


def CommutativePropertyAdd():
    print("=================================")
    print(" COMMUTATIVE PROPERTY ADDITION")
    print("=================================")
    
    print("Natural number addition is commutative.")
    print("Formula: m + n = n + m")
    
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    print(m , ' + ' , n , " = ", n, " + ", m)

def CommutativePropertyMulti():
    print("=====================================")
    print(" COMMUTATIVE PROPERTY MULTIPLICATION")
    print("=====================================")
    
    print("Natural number multiplication is commutative.")
    print("Formula: x * y = y * x")
    
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x , ' * ' , y , " = ", y, " * ", x)


def IdentityPropertyAdd():
    print("=================================")
    print(" IDENTITY PROPERTY ADDITION")
    print("=================================")
    
    print("Natural number addition is identity.")
    print("Formula: m + 0 = m")
    
    m = int(input("Enter m: "))
    print(m , ' + ' , 0 , " = ", m)

def IdentityPropertyMulti():
    print("==================================")
    print(" IDENTITY PROPERTY MULTIPLICATION")
    print("==================================")
    
    print("Natural number multiplication is identity.")
    print("Formula: n * 1 = n = 1 * n")
    
    n = int(input("Enter n: "))
    print(n, '*',1, '=', n, '=', 1, '*', n )


def DistributiveProperty():
    print("=================================")
    print(" DISTRIBUTIVE PROPERTY")
    print("=================================")
    
    print("Natural number multiplication distributes over addition.")
    print("Formula: (x + y)* z = (x * z) + (y * z)")
    
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    print('(', x, '+', y, ')*', z, '= (', x, '*', z, ') + (', y, '*', z, ')')


def BasicProperties():
    print("[1] Infinite Numbers")
    print("[2] Closure Property (Addition)")
    print("[3] Closure Property (Multiplication)")
    print("[4] Associative Property (Addition)")
    print("[5] Associative Property (Multiplication)")
    print("[6] Commutative Property (Addition)")
    print("[7] Commutative Property (Multiplication)")
    print("[8] Identity Property (Addition)")
    print("[9] Identity Property (Multiplication)")
    print("[10] Distributive Property")
    
    #BasicProperties()
    option = int(input("Choose: "))
    
    while option != 0:
        if option == 1:
            Infinite()
        elif option == 2:
            ClosurePropertyAdd()
        elif option == 3:
            ClosurePropertyMulti()
        elif option == 4:
            AssociativePropertyAdd()
        elif option == 5:
            AssociativePropertyMulti()
        elif option == 6:
            CommutativePropertyAdd()
        elif option == 7:
            CommutativePropertyMulti()
        elif option == 8:
            IdentityPropertyAdd()
        elif option == 9:
            IdentityPropertyMulti()
        elif option == 10:
            DistributiveProperty()


        else:
            print("No existing property. Please try again.")
        
        print()
        option = int(input("Choose again or EXIT: "))
    
    menu()

def SuccessorOp(m,n):
    print(f"= {m} + {n}")

    if n > 0:
        print(f"= {m} + S({n-1})")
        print(f"= S({m}) + {n-1}")
        return SuccessorOp(m+1, n-1)
    else:
        return m

def menu():
    print("=================================")
    print("               MENU")
    print("=================================")
    print("[1] Basic Properties of Natural Numbers")
    print("[2] The Successor Operation")
    print("[3] The Well Ordering Property")
    print("[4] Exit")


menu()
choice = int(input("Enter choice: "))

while choice != 4:
    if choice == 1:
        print("=================================")
        print("         BASIC PROPERTIES")
        print("=================================")
        BasicProperties()
    elif choice == 2:
        print("=================================")
        print("       Successor Operation")
        print("=================================")
        m = int(input("Enter the value of m: "))
        n = int(input("Enter the value of n: "))
        ans = SuccessorOp(m,n)
        print(f"= {ans}")
    elif choice == 3:
        print("=================================")
        print("   The Well Ordering Property")
        print("=================================")
    else:
        print("Invalid choice. Try again.")
    
    print()
    choice = int(input("Enter choice: "))
    
print("Thank you.")
